#!/bin/sh

WGET=`which wget`
UNZIP=`which unzip`
BUNZIP2=`which bunzip2`
BZIP2=`which bzip2`

echo WGET=$WGET
echo UNZIP=$UNZIP
echo BZIP2=$BZIP2

CACHE_DIR=.cache/era_xml

if [ -f $CACHE_DIR/ERA2010_journal_title_list.xml.bz2 -a -f $CACHE_DIR/ERA2012_journal_title_list.xml.bz2 ]; then
  cp $CACHE_DIR/* .
  $BUNZIP2 *.xml.bz2
  exit 0
fi

# Download files and extract contents

mkdir downloads
cd downloads

$WGET http://content.webarchive.nla.gov.au/gov/wayback/20120317002747/http://www.arc.gov.au/zip/ERA2010_tech_pack.zip

mkdir ERA2010_tech_pack
cd ERA2010_tech_pack
$UNZIP ../ERA2010_tech_pack.zip
cd ..

# The 2012 tech pack can be obtained from here, and it contains the journal list in XSLX format
# wget http://content.webarchive.nla.gov.au/gov/wayback/20140212022156/http://www.arc.gov.au//zip/ERA-SEER2012-tech-pack.zip
# 
# mkdir ERA2012_tech_pack
# cd ERA2012_tech_pack
# unzip ../ERA-SEER2012-tech-pack.zip
# cd ..

# However we can download only the journal list
$WGET http://content.webarchive.nla.gov.au/gov/wayback/20140212052430/http://www.arc.gov.au/xls/era12/ERA2012JournalList.xlsx

# We could extract the xlsx, and extract the data that way
# mkdir ERA2012_journal_list
# cd ERA2012_journal_list
# unzip ../ERA2012JournalList.xlsx
# cd ..

# Leave the downloads directory
cd ..

# Extract ERA 2012 journal list and convert it to XML
python -c "import pyexcel, pyexcel.ext.text, pyexcel.ext.xlsx; sheet = pyexcel.sheets.NominableSheet(pyexcel.get_sheet(file_name='downloads/ERA2012JournalList.xlsx'), name_columns_by_row=0); pyexcel.save_as(array=sheet, dest_file_name='downloads/ERA2012JournalList.json')"

python -c "import json, dicttoxml; data = json.load(open('downloads/ERA2012JournalList.json')); f = open('downloads/ERA2012JournalList.messy-xml', 'wb'); f.write(dicttoxml.dicttoxml(data, attr_type=False, custom_root='JournalList')); f.close()"

# Post-process the dicttoxml XML into the ERA 2010 journal list XML format
lxmlproc --output downloads/ERA2012JournalList.xml  era_journal_list_tidy.xsl downloads/ERA2012JournalList.messy-xml

# Copy both files into the output directory
mkdir -p $CACHE_DIR/
cp downloads/ERA2010_tech_pack/code-table/XML-Format/ERA2010_journal_title_list.xml $CACHE_DIR
cp downloads/ERA2012JournalList.xml $CACHE_DIR/ERA2012_journal_title_list.xml

cp $CACHE_DIR/* .

$BZIP2 $CACHE_DIR/*
