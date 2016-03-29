<?xml version="1.0" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
<rankedJournalListImport>
	<rankedJournalList>
		<xsl:apply-templates select="//item"/>
	</rankedJournalList>
</rankedJournalListImport>
</xsl:template>

<xsl:template match="item">
	<rankedJournal>
		<eraIdentifier><xsl:value-of select="ERAID"/></eraIdentifier>
		<title><xsl:value-of select="Title"/></title>
		<xsl:if test="Foreign_Title != ''">
		<foreignTitle><xsl:value-of select="Foreign_Title"/></foreignTitle>
		</xsl:if>
		<fieldsOfResearch>
			<xsl:if test="FoR_1 != ''">
			<fieldOfResearch forCode="{FoR_1}" forName="{FoR_1_Name}"/>
			</xsl:if>
			<xsl:if test="FoR_2 != ''">
			<fieldOfResearch forCode="{FoR_2}" forName="{FoR_2_Name}"/>
			</xsl:if>
			<xsl:if test="FoR_3 != ''">
			<fieldOfResearch forCode="{FoR_3}" forName="{FoR_3_Name}"/>
			</xsl:if>
		</fieldsOfResearch>
		<issns>
			<xsl:if test="ISSN_1 != ''">
			<issn issnCode="{ISSN_1}"/>
			</xsl:if>
			<xsl:if test="ISSN_2 != ''">
			<issn issnCode="{ISSN_2}"/>
			</xsl:if>
			<xsl:if test="ISSN_3 != ''">
			<issn issnCode="{ISSN_3}"/>
			</xsl:if>
			<xsl:if test="ISSN_4 != ''">
			<issn issnCode="{ISSN_4}"/>
			</xsl:if>
			<xsl:if test="ISSN_5 != ''">
			<issn issnCode="{ISSN_5}"/>
			</xsl:if>
			<xsl:if test="ISSN_6 != ''">
			<issn issnCode="{ISSN_6}"/>
			</xsl:if>
			<xsl:if test="ISSN_7 != ''">
			<issn issnCode="{ISSN_7}"/>
			</xsl:if>
		</issns>
	</rankedJournal>
</xsl:template>

</xsl:stylesheet>
