<?xml version="1.0" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>

<!-- Identity template : copy all text nodes, elements and attributes -->
<xsl:template match="@*|node()">
    <xsl:copy>
        <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
</xsl:template>

<xsl:template match="fieldOfResearch[@forCode = preceding-sibling::fieldOfResearch/@forCode]"/>

<xsl:template match="title[contains(text(), '&#10;')]">
    <title><xsl:value-of select="translate(text(),'&#10;', ' ')"/></title>
</xsl:template>

</xsl:stylesheet>
