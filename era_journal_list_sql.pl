#!/usr/bin/perl

use strict;

my $file = $ARGV[0];
my $prefix = $ARGV[1] or '';
my $sql_flavour = $ARGV[2] or '';

if ($prefix) {
  $prefix = $prefix . '_';
}

open F, $file;

my $line;
my $count = 0;

my $eraid;
my $title;
my @issns;
my @disciplines;
my $md;
# <journalRank> is 2010 only
my $rank;
# <foreignTitle> is 2012 only
my $foreign_title;

sub set_verbose
{
  my $flag = shift;
  # This is needed for Oracle's sqlplus
  if ($sql_flavour eq 'oracle') {
    print "set scan $flag\n";
    print "set echo $flag\n";
    print "set termout $flag\n";
    print "set feedback $flag\n";
  }
}

sub print_era_journal
{
  my $eraid = shift;
  my $title = shift;
  my $issns = @_;

  $title =~ s/'/''/g;
  $title =~ s/&amp;/&/g;

  $foreign_title =~ s/'/''/g;
  $foreign_title =~ s/&amp;/&/g;

  if ($rank eq 'Not ranked') {
    $rank = 0
  }

  my $i;

  if ($rank) {
    print "insert into ${prefix}journal (eraid, title, rank) values ($eraid, '$title', '$rank');\n";
  } else {
    print "insert into ${prefix}journal (eraid, title) values ($eraid, '$title');\n";
  }

  $i = 0;
  foreach (@issns) {
    $i ++;
    print "insert into ${prefix}journal_issn (eraid, issn, column_id) values ($eraid, '$_', $i);\n";
  }

  $i = 0;
  foreach (@disciplines) {
    $_ = $_.'00';
    $_ = $_.'00' if length($_)==4;

    $i ++;
    print "insert into ${prefix}journal_for (eraid, discipline, column_id) values ($eraid, '$_', $i);\n";
  }

  print "update ${prefix}journal set multidisciplinary_ind = 'Y' where eraid = $eraid;\n" if ($md);
  print "update ${prefix}journal set foreign_title = '$foreign_title' where eraid = $eraid;\n" if ($foreign_title);
}

set_verbose("off");

while ($line = <F>) {
  if ($line =~ /eraIdentifier>(\d+)</) {
    if ($eraid) {
      print_era_journal($eraid, $title, @issns);
      $count++;
      if ($count % 5000 == 0) {
        set_verbose("on");

        print("select count(*) from ${prefix}journal;\n");

        set_verbose("off");
      }
    }
    $eraid = $1;
    $title = '';
    @issns = ();
    @disciplines = ();
    $md = 0;
    $foreign_title = '';
    $rank = 0;
  }
  elsif ($line =~ /title>([^<]+)</) {
    $title = $1;
  }
  elsif ($line =~ /<foreignTitle>([^<]+)</) {
    $foreign_title = $1;
  }
  elsif ($line =~ /<journalRank>([^<]+)</) {
    $rank = $1;
  }
  elsif ($line =~ /<issn issnCode="(.+)"\/>/) {
    push @issns, $1;
  }
  elsif ($line =~ /<fieldOfResearch forCode="([0-9]+)" /) {
    push @disciplines, $1;
  }
  elsif ($line =~ /<fieldOfResearch forCode="MD" /) {
    $md = 1;
  }
}

if ($eraid) {
  print_era_journal($eraid, $title, @issns);
}

set_verbose("on");

print("select count(*) from ${prefix}journal;\n");

if ($sql_flavour eq 'oracle') {
  print "commit;\n";
  print "exit\n";
}
