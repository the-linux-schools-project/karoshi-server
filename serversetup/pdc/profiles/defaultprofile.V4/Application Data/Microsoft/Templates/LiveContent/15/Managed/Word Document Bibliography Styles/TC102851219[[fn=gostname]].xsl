<?xml version="1.0" encoding="utf-8"?>





<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt"	xmlns:b="http://schemas.openxmlformats.org/officeDocument/2006/bibliography" xmlns:t="http://www.microsoft.com/temp">
	<xsl:output method="html" encoding="us-ascii"/>


	
	<xsl:template match="*" mode="outputHtml2">
			<xsl:apply-templates mode="outputHtml"/>		
	</xsl:template>

	<xsl:template name="StringFormatDot">
		<xsl:param name="format" />
		<xsl:param name="parameters" />

    <xsl:variable name="prop_EndChars">
      <xsl:call-template name="templ_prop_EndChars"/>
    </xsl:variable>

    <xsl:choose>
			<xsl:when test="$format = ''"></xsl:when>
			<xsl:when test="substring($format, 1, 2) = '%%'">
				<xsl:text>%</xsl:text>
				<xsl:call-template name="StringFormatDot">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="parameters" select="$parameters" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=2">
					<xsl:call-template name="templ_prop_Dot"/>
				</xsl:if>
			</xsl:when>
			<xsl:when test="substring($format, 1, 1) = '%'">
				<xsl:variable name="pos" select="substring($format, 2, 1)" />
				<xsl:apply-templates select="msxsl:node-set($parameters)/t:params/t:param[position() = $pos]" mode="outputHtml2"/>
				<xsl:call-template name="StringFormatDot">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="parameters" select="$parameters" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=2">
					<xsl:variable name="temp2">
						<xsl:call-template name="handleSpaces">
							<xsl:with-param name="field" select="msxsl:node-set($parameters)/t:params/t:param[position() = $pos]"/>
						</xsl:call-template>
					</xsl:variable>				
					<xsl:variable name="lastChar">
						<xsl:value-of select="substring($temp2, string-length($temp2))"/>
					</xsl:variable>
					<xsl:if test="not(contains($prop_EndChars, $lastChar))">
						<xsl:call-template name="templ_prop_Dot"/>
					</xsl:if>
				</xsl:if>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($format, 1, 1)" />
				<xsl:call-template name="StringFormatDot">
					<xsl:with-param name="format" select="substring($format, 2)" />
					<xsl:with-param name="parameters" select="$parameters" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=1">
					<xsl:if test="not(contains($prop_EndChars, $format))">
						<xsl:call-template name="templ_prop_Dot"/>
					</xsl:if>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>	

	<xsl:template name="StringFormat">
		<xsl:param name="format" />
		<xsl:param name="parameters" />
		<xsl:choose>
			<xsl:when test="$format = ''"></xsl:when>
			<xsl:when test="substring($format, 1, 2) = '%%'">
				<xsl:text>%</xsl:text>
				<xsl:call-template name="StringFormat">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="parameters" select="$parameters" />
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="substring($format, 1, 1) = '%'">
				<xsl:variable name="pos" select="substring($format, 2, 1)" />
				<xsl:apply-templates select="msxsl:node-set($parameters)/t:params/t:param[position() = $pos]" mode="outputHtml2"/>
				<xsl:call-template name="StringFormat">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="parameters" select="$parameters" />
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($format, 1, 1)" />
				<xsl:call-template name="StringFormat">
					<xsl:with-param name="format" select="substring($format, 2)" />
					<xsl:with-param name="parameters" select="$parameters" />
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>




  <xsl:template name="localLCID">
    <xsl:param name="LCID"/>

    <xsl:variable name="_LCID1">
      <xsl:choose>
        <xsl:when test="$LCID!='0' and $LCID!=''">
          <xsl:value-of select="$LCID"/>
        </xsl:when>
        <xsl:when test="/b:Citation">
          <xsl:value-of select="/*/b:Locals/b:DefaultLCID"/>
        </xsl:when>
        <xsl:when test="b:LCID">
          <xsl:value-of select="b:LCID"/>
        </xsl:when>
        <xsl:when test="../b:LCID">
          <xsl:value-of select="../b:LCID"/>
        </xsl:when>
        <xsl:when test="../../b:LCID">
          <xsl:value-of select="../../b:LCID"/>
        </xsl:when>
        <xsl:when test="../../../b:LCID">
          <xsl:value-of select="../../../b:LCID"/>
        </xsl:when>
        <xsl:when test="../../../../b:LCID">
          <xsl:value-of select="../../../../b:LCID"/>
        </xsl:when>
        <xsl:when test="../../../../b:LCID">
          <xsl:value-of select="../../../../b:LCID"/>
        </xsl:when>
        <xsl:when test="../../../../../b:LCID">
          <xsl:value-of select="../../../../../b:LCID"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="/*/b:Locals/b:DefaultLCID"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:choose>
      <xsl:when test="$_LCID1!='0' and string-length($_LCID1)>0">
        <xsl:value-of select="$_LCID1"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="/*/b:Locals/b:DefaultLCID"/>
      </xsl:otherwise>
    </xsl:choose>

  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationLong_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationLong/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationLong_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationLong/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationLong_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationLong/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationLong_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationLong/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationShort_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationShort/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationShort_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationShort/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationShort_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationShort/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_CitationShort_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:CitationShort/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationLong_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationLong/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationLong_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationLong/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationLong_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationLong/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationLong_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationLong/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationShort_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationShort/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationShort_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationShort/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationShort_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationShort/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_CitationShort_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:CitationShort/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationLong_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationLong/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationLong_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationLong/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationLong_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationLong/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationLong_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationLong/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationShort_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationShort/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationShort_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationShort/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationShort_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationShort/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_CitationShort_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:CitationShort/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationLong_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationLong/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationLong_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationLong/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationLong_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationLong/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationLong_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationLong/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationShort_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationShort/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationShort_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationShort/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationShort_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationShort/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_CitationShort_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:CitationShort/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationLong_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationLong/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationLong_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationLong/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationLong_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationLong/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationLong_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationLong/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationShort_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationShort/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationShort_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationShort/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationShort_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationShort/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_CitationShort_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:CitationShort/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_str_OnlineCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:OnlineCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_OnlineUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:OnlineUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_FiledCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:FiledCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PatentFiledCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PatentFiledCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InNameCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InNameCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_WithUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:WithUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VersionShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VersionShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InterviewCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InterviewCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InterviewWithCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InterviewWithCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InterviewByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InterviewByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_AndUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:AndUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_AndOthersUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:AndOthersUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_MotionPictureCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:MotionPictureCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PatentCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PatentCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditionShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditionShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditionUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditionUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_RetrievedFromCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:RetrievedFromCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_RetrievedCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:RetrievedCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_FromCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:FromCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_FromUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:FromUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_NoDateShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:NoDateShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_NumberShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:NumberShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_NumberShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:NumberShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PatentNumberShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PatentNumberShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PagesCountinousShort" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PagesCountinousShort"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PageShort" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PageShort"/>
  </xsl:template>

  
  <xsl:template name="templ_str_SineNomineShort" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:SineNomineShort"/>
  </xsl:template>

  
  <xsl:template name="templ_str_SineLocoShort" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:SineLocoShort"/>
  </xsl:template>

  
  <xsl:template name="templ_str_SineLocoSineNomineShort" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:SineLocoSineNomineShort"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumeOfShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumeOfShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumesOfShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumesOfShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumeShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumeShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumeShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumeShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumesShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumesShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumesShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumesShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_VolumeCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:VolumeCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_AuthorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:AuthorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_BookAuthorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:BookAuthorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ArtistShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ArtistShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_WriterCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:WriterCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_WritersCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:WritersCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_WriterShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:WriterShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductedByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductedByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductedByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductedByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductorCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductorCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductorsCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductorsCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductorShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductorShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductorsShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductorsShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ConductorsShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ConductorsShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CounselShortUnCapIso" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CounselShortUnCapIso"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CounselShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CounselShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectedByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectedByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectedByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectedByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectorCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectorCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectorsCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectorsCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectorShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectorShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectorsShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectorsShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_DirectorsShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:DirectorsShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditedByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditedByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditedByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditedByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditorCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditorCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditorsCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditorsCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditorShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditorShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditorsShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditorsShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_EditorsShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:EditorsShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_IntervieweeShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:IntervieweeShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InterviewerCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InterviewerCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InterviewersCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InterviewersCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_InventorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InventorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformedByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformedByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformedByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformedByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformerCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformerCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformersCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformersCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformerShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformerShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformerShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformerShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformersShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformersShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_PerformersShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:PerformersShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducedByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducedByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducedByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducedByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducerCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducerCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducersCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducersCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProductionCompanyShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProductionCompanyShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducerShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducerShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducersShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducersShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ProducerShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ProducerShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatedByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatedByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatedByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatedByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatorCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatorCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatorsCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatorsCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatorShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatorShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatorShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatorShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatorsShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatorsShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_TranslatorsShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:TranslatorsShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ComposerCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ComposerCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ComposersCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ComposersCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ComposerShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ComposerShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ComposersShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ComposersShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_ComposerShortUnCapIso" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:ComposerShortUnCapIso"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompiledByCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompiledByCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompiledByUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompiledByUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilerCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilerCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilersCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilersCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilerShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilerShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilerShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilerShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilersShortCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilersShortCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilersShortUnCap" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilersShortUnCap"/>
  </xsl:template>

  
  <xsl:template name="templ_str_CompilerShortUnCapIso" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:CompilerShortUnCapIso"/>
  </xsl:template>


  

  
  <xsl:template name="templ_prop_Culture" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/@Culture"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Direction" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Properties/b:Direction"/>
  </xsl:template>


  

  
  <xsl:template name="templ_prop_EndChars" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:EndChars"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_NormalizeSpace" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:text>no</xsl:text>
    
  </xsl:template>

  
  <xsl:template name="templ_prop_Space" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:Space"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_NonBreakingSpace" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:NonBreakingSpace"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ListSeparator" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:ListSeparator"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Dot" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:Dot"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_DotInitial" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:DotInitial"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_GroupSeparator" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:GroupSeparator"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_EnumSeparator" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:EnumSeparator"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Equal" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:Equal"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Enum" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:Enum"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_OpenQuote" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:OpenQuote"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_CloseQuote" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:CloseQuote"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_OpenBracket" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:OpenBracket"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_CloseBracket" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:CloseBracket"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_FromToDash" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:FromToDash"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_OpenLink" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:OpenLink"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_CloseLink" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:CloseLink"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_AuthorsSeparator" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:AuthorsSeparator"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_NoAndBeforeLastAuthor" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:NoAndBeforeLastAuthor"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SimpleAuthor_F" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:SimpleAuthor/b:F"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SimpleAuthor_M" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:SimpleAuthor/b:M"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SimpleAuthor_L" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:SimpleAuthor/b:L"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SimpleDate_D" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:SimpleDate/b:D"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SimpleDate_M" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:SimpleDate/b:M"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SimpleDate_Y" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:SimpleDate/b:Y"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_SameAuthor" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:SameAuthor"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_MainAuthor_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:MainAuthor/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_MainAuthor_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:MainAuthor/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_MainAuthor_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:MainAuthor/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_MainAuthor_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:MainAuthor/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_OtherAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:OtherAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_OtherAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:OtherAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_OtherAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:OtherAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_OtherAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:OtherAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_SecondaryAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:SecondaryAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_SecondaryAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:SecondaryAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_SecondaryAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:SecondaryAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_SecondaryAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:SecondaryAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_Date_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:Date/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_Date_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:Date/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_Date_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:Date/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_MLA_Date_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:MLA/b:Date/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_MainAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:MainAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_MainAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:MainAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_MainAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:MainAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_MainAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:MainAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_SecondaryAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_SecondaryAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_SecondaryAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_SecondaryAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_BeforeLastAuthor" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:BeforeLastAuthor"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_GeneralOpen" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:GeneralOpen"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_GeneralClose" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:GeneralClose"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_SecondaryOpen" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryOpen"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_SecondaryClose" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryClose"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Hyphens" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:Hyphens"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_Date_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:Date/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_Date_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:Date/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_Date_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:Date/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_Date_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:Date/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateAccessed_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateAccessed/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateAccessed_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateAccessed/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateAccessed_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateAccessed/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateAccessed_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateAccessed/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateCourt_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateCourt/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateCourt_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateCourt/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateCourt_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateCourt/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_APA_DateCourt_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:DateCourt/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_SameAuthor" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:SameAuthor"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_MainAuthor_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:MainAuthor/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_MainAuthor_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:MainAuthor/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_MainAuthor_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:MainAuthor/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_MainAuthor_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:MainAuthor/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_OtherAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:OtherAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_OtherAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:OtherAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_OtherAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:OtherAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_OtherAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:OtherAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_SecondaryAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:SecondaryAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_SecondaryAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:SecondaryAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_SecondaryAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:SecondaryAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_SecondaryAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:SecondaryAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_Date_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:Date/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_Date_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:Date/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_Date_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:Date/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Chicago_Date_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Chicago/b:Date/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_MainAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:MainAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_MainAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:MainAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_MainAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:MainAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_MainAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:MainAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_SecondaryAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:SecondaryAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_SecondaryAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:SecondaryAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_SecondaryAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:SecondaryAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_SecondaryAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:SecondaryAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_SameAuthor" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:SameAuthor"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_GeneralOpen" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:GeneralOpen"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_GeneralClose" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:GeneralClose"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_Date_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:Date/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_Date_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:Date/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_Date_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:Date/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_Date_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:Date/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_DateAccessed_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:DateAccessed/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_DateAccessed_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:DateAccessed/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_DateAccessed_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:DateAccessed/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_ISO690_DateAccessed_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:ISO690/b:DateAccessed/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Authors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Authors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Authors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Authors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Authors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Authors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Authors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Authors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Date_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Date/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Date_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Date/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Date_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Date/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_Date_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:Date/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_GeneralOpen" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:GeneralOpen"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_GeneralClose" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:GeneralClose"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_OneSlash" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:OneSlash"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_Gost_TwoSlash" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Gost/b:TwoSlash"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_MainAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:MainAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_MainAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:MainAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_MainAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:MainAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_MainAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:MainAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_SecondaryAuthors_FML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:SecondaryAuthors/b:FML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_SecondaryAuthors_FM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:SecondaryAuthors/b:FM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_SecondaryAuthors_ML" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:SecondaryAuthors/b:ML"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_SecondaryAuthors_FL" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:SecondaryAuthors/b:FL"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_SameAuthor" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:SameAuthor"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_GeneralOpen" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:GeneralOpen"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_GeneralClose" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:GeneralClose"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_Date_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:Date/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_Date_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:Date/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_Date_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:Date/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_Date_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:Date/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_DateAccessed_DMY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:DateAccessed/b:DMY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_DateAccessed_DM" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:DateAccessed/b:DM"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_DateAccessed_MY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:DateAccessed/b:MY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_SIST_DateAccessed_DY" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SIST/b:DateAccessed/b:DY"/>
  </xsl:template>

  
  <xsl:template name="templ_prop_NoCommaBeforeAnd" >
    <xsl:param name="LCID" />
    <xsl:variable name="_LCID">
      <xsl:call-template name="localLCID">
        <xsl:with-param name="LCID" select="$LCID"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:NoCommaBeforeAnd"/>
  </xsl:template>

  
  <xsl:variable name="constGost_CitationOpen">
	<xsl:call-template name="templ_prop_OpenBracket" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationClose">
	<xsl:call-template name="templ_prop_CloseBracket" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationNamePartsSeparator">
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationNameAndOther">
	<xsl:call-template name="templ_prop_Space" />
	<xsl:call-template name="templ_str_AndOthersUnCap"/>
 	
</xsl:variable>
<xsl:variable name="constGost_CitationAuthorYearSeparator">
	<xsl:call-template name="templ_prop_ListSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationAuthorOrYearVolumeSeparator">
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationVolumeFooter">
	<xsl:call-template name="templ_prop_Enum" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationPageHeader">
	<xsl:call-template name="templ_prop_Space" />
	<xsl:call-template name="templ_str_PageShort"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationVolumeHeader">
	<xsl:call-template name="templ_prop_ListSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationVolumeStringVolumeSeparator">
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CitationAuthorSeparator">
	<xsl:call-template name="templ_prop_GroupSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_SourceTypeOpen">
	<xsl:call-template name="templ_prop_Space" />
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
 	
</xsl:variable>
<xsl:variable name="constGost_SourceTypeClose">
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
 	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesOpen">
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
 	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesClose">
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
 	
</xsl:variable>
<xsl:variable name="constGost_TitleHeader">
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_TitlePrefixTitleSeparator">
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_NamePartsSeparator">
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_PersonSeparator">
	<xsl:call-template name="templ_prop_ListSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_PersonAndOther">
	<xsl:call-template name="templ_prop_Space" />
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	<xsl:call-template name="templ_str_AndOthersUnCap"/>
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
 	
</xsl:variable>
<xsl:variable name="constGost_SemiColonSeparatedItemsSeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_GroupSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesSeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_GroupSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_Gost_OneSlash" />
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CollectionNameHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_Gost_TwoSlash" />
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_SecondaryResponsibilitiesHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_Gost_OneSlash" />
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_SecondaryResponsibilitiesSeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_Gost_OneSlash" />
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_SineLoco">
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	<xsl:call-template name="templ_str_SineLocoShort"/>
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
 	
</xsl:variable>
<xsl:variable name="constGost_SineNomine">
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	<xsl:call-template name="templ_str_SineNomineShort"/>
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
 	
</xsl:variable>
<xsl:variable name="constGost_HyphenSectionHeader">
	<xsl:call-template name="templ_prop_Dot" />
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_FromToDash" />
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_HyphenSectionSeparator">
	<xsl:call-template name="templ_prop_ListSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_ColonElementSeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>

<xsl:variable name="constGost_ShortTitleHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_Equal" />
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_SoundRecordingMediumHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_ElectronicSourceMediumHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_PatentNumberHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_PatentTypeHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_CaseNumberHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_AbbreviatedCaseNumberHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_ReportTypeHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_EnumSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_PublisherProductionCompanySeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_GroupSeparator" />
 	
</xsl:variable>
<xsl:variable name="constGost_TheaterCitySeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_GroupSeparator" />
 	
</xsl:variable>


<xsl:variable name="constGost_AuthorHeader">
	<xsl:call-template name="templ_str_AuthorShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_TranslatorHeader">
	<xsl:call-template name="templ_str_TranslatorShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CompilerHeader">
	<xsl:call-template name="templ_str_CompilerShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_ComposerHeader">
	<xsl:call-template name="templ_str_ComposerShortUnCapIso"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_ArtistHeader">
	<xsl:call-template name="templ_str_ArtistShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_ConductorHeader">
	<xsl:call-template name="templ_str_ConductorShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_PerformerHeader">
	<xsl:call-template name="templ_str_PerformerShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_WriterHeader">
	<xsl:call-template name="templ_str_WriterShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_DirectorHeader">
	<xsl:call-template name="templ_str_DirectorShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_ProducerNameHeader">
	<xsl:call-template name="templ_str_ProducerShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_CounselHeader">
	<xsl:call-template name="templ_str_CounselShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_BookAuthorHeader">
	<xsl:call-template name="templ_str_BookAuthorShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>
<xsl:variable name="constGost_IntervieweeHeader">
	<xsl:call-template name="templ_str_IntervieweeShortUnCap"/>
	<xsl:call-template name="templ_prop_Space" />
 	
</xsl:variable>

	




	
	<xsl:template match="/">



		<xsl:choose>

			
			
			<xsl:when test="b:Version">
				<xsl:text>2006.5.07</xsl:text>
			</xsl:when>

			<xsl:when test="b:XslVersion">
				<xsl:text>2003</xsl:text>
			</xsl:when>

      <xsl:when test="b:StyleNameLocalized">
        <xsl:choose>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1033'">
            <xsl:text>GOST - Name Sort</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1025'">
            <xsl:text>Gost - فرز الأسماء</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1037'">
            <xsl:text>GOST - שמות</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1041'">
            <xsl:text>GOST: 名前順</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2052'">
            <xsl:text>GOST - 名称排序</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1028'">
            <xsl:text>Gost - 姓名排序</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1042'">
            <xsl:text>GOST - 이름 정렬</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1036'">
            <xsl:text>Gost - Tri par nom</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1040'">
            <xsl:text>GOST - Ordinamento per nome</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='3082'">
            <xsl:text>GOST - Orden de nombre</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1043'">
            <xsl:text>Gost - Namen sorteren</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1031'">
            <xsl:text>Gost - Namenssortierung</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1046'">
            <xsl:text>Gost - Classificação por Nome</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1049'">
            <xsl:text>ГОСТ — сортировка по именам</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1035'">
            <xsl:text>GOST - nimilajittelu</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1032'">
            <xsl:text>Gost - Ταξινόμηση ονόματος</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1081'">
            <xsl:text>Gost - नाम वर्गीकरण</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1054'">
            <xsl:text>Gost - เรียงลำดับตามชื่อ</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1057'">
            <xsl:text>Gost - Pengurutan Nama</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1086'">
            <xsl:text>Gost - Isihan Nama</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1066'">
            <xsl:text>Gost - Sắp xếp Tên</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1053'">
            <xsl:text>Gost – Namnsortering</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1069'">
            <xsl:text>GOST - Izen-ordena</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1027'">
            <xsl:text>Gost (per nom)</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1030'">
            <xsl:text>GOST - Sorteret efter navn</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1110'">
            <xsl:text>GOST - por nome</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1044'">
            <xsl:text>Gost - sortert etter navn</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1061'">
            <xsl:text>GOST – nime järgi sortimine</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1062'">
            <xsl:text>Gost - pēc vārda</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1063'">
            <xsl:text>Gost – rūšiavimas pagal vardą</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1045'">
            <xsl:text>GOST — sortowanie według nazw</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2070'">
            <xsl:text>GOST - Ordenação de Nomes</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1029'">
            <xsl:text>GOST – řazení podle jména</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1055'">
            <xsl:text>Gost - Ad Sırası</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1038'">
            <xsl:text>GOSZT — Név szerinti rendezés</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1048'">
            <xsl:text>Gost - Sortare după nume</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1058'">
            <xsl:text>ГОСТ – сортування за іменами</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1026'">
            <xsl:text>Gost –  сортиране по име</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1050'">
            <xsl:text>GOST - sortirani nazivi</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1087'">
            <xsl:text>Ресей Федерациясының техникалық басқару мен метрология жөніндегі федералды агенттігі</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2074'">
            <xsl:text>Gost - Name Sort</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='3098'">
            <xsl:text>Gost - Name Sort</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1051'">
            <xsl:text>Gost – Zoradenie názvov</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1060'">
            <xsl:text>GOST – razvrščanje imen</xsl:text>
          </xsl:when>
        </xsl:choose>
      </xsl:when>
			
			<xsl:when test="b:GetImportantFields">
				<b:ImportantFields>
					<xsl:choose>
						<xsl:when test="b:GetImportantFields/b:SourceType='Book'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='BookSection'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Author/b:BookAuthor/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:BookTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='JournalArticle'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Issue</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='ArticleInAPeriodical'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:PeriodicalTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Edition</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Issue</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='ConferenceProceedings'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ConferenceName</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Report'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='SoundRecording'">
							<b:ImportantField><xsl:text>b:Author/b:Artist/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:AlbumTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ProductionCompany</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Medium</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Performance'">
							<b:ImportantField><xsl:text>b:Author/b:Writer/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ProductionCompany</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Theater</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Art'">
							<b:ImportantField><xsl:text>b:Author/b:Artist/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Institution</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='DocumentFromInternetSite'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:InternetSiteTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ProductionCompany</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Month</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Day</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:YearAccessed</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:MonthAccessed</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:DayAccessed</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:URL</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Version</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='InternetSite'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:InternetSiteTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ProductionCompany</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Month</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Day</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:YearAccessed</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:MonthAccessed</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:DayAccessed</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:URL</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Version</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Film'">
							<b:ImportantField><xsl:text>b:Author/b:Director/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ProductionCompany</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Interview'">
							<b:ImportantField><xsl:text>b:Author/b:Interviewee/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:BroadcastTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Month</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Day</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Broadcaster</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Station</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Patent'">
							<b:ImportantField><xsl:text>b:Author/b:Inventor/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Month</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Day</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:CountryRegion</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='ElectronicSource'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:ProductionCompany</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Medium</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Case'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Court</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Misc'">
							<b:ImportantField><xsl:text>b:Author/b:Author/b:NameList</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Title</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:PublicationTitle</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Year</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:City</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Publisher</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Volume</xsl:text></b:ImportantField>
							<b:ImportantField><xsl:text>b:Issue</xsl:text></b:ImportantField>
						</xsl:when>

					</xsl:choose>
				</b:ImportantFields>
			</xsl:when>
			
			
			<xsl:when test="b:Citation">

				<xsl:variable name="ListPopulatedWithMain">
						<xsl:call-template name="populateMain">
							<xsl:with-param name="Type">b:Citation</xsl:with-param>
						</xsl:call-template>
				</xsl:variable>

			
			
				<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">
					<head>
					</head>
					<body>
			            <xsl:variable name="LCID">
			              <xsl:choose>
			                <xsl:when test="b:LCID='0' or b:LCID='' or not(b:LCID)">
			                  <xsl:value-of select="/*/b:Locals/b:DefaultLCID"/>
			                </xsl:when>
			                <xsl:otherwise>
			                  <xsl:value-of select="b:LCID"/>
			                </xsl:otherwise>
			              </xsl:choose>
			            </xsl:variable>

			            <xsl:element name="p">

						<xsl:attribute name="lang">
							<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$LCID]/@Culture"/>
						</xsl:attribute>

						<xsl:attribute name="dir">
							<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$LCID]/b:Properties/b:Direction"/>
						</xsl:attribute>

						<xsl:variable name="type">
							<xsl:value-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:SourceType"/>
						</xsl:variable>

						<xsl:variable name="title0">
							<xsl:choose>
								<xsl:when test="string-length(msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:ShortTitle)>0">
									<xsl:value-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:ShortTitle" />
								</xsl:when>

								<xsl:otherwise>
									<xsl:value-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Title" />
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>

						<xsl:variable name="year0">
							<xsl:value-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Year" />
						</xsl:variable>						

						<xsl:variable name="authorMain">
							<xsl:copy-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Author/b:Main"/>
						</xsl:variable>

						<xsl:variable name="author0">
							<xsl:choose>
								<xsl:when test="string-length(msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Author/b:Main/b:Corporate) > 0">
									<xsl:value-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Author/b:Main/b:Corporate" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:variable name="cAuthors">
										<xsl:value-of select="count(msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Author/b:Main/b:NameList/b:Person)" />
									</xsl:variable>
									<xsl:for-each select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Author/b:Main/b:NameList/b:Person">
										<xsl:choose>
											<xsl:when test="position() >= 2">
											</xsl:when>
											<xsl:when test="position() = 1">
												<xsl:call-template name="formatNameCore">
													<xsl:with-param name="FML">
														<xsl:call-template name="templ_prop_Gost_CitationShort_FML"/>
													</xsl:with-param>
													<xsl:with-param name="FM">
														<xsl:call-template name="templ_prop_Gost_CitationShort_FM"/>
													</xsl:with-param>
													<xsl:with-param name="ML">
														<xsl:call-template name="templ_prop_Gost_CitationShort_ML"/>
													</xsl:with-param>
													<xsl:with-param name="FL">
														<xsl:call-template name="templ_prop_Gost_CitationShort_FL"/>
													</xsl:with-param>
													<xsl:with-param name="upperLast">no</xsl:with-param>
													<xsl:with-param name="withDot">no</xsl:with-param>
												</xsl:call-template>
											</xsl:when>
										</xsl:choose>
									</xsl:for-each>
									<xsl:if test = "$cAuthors > 1">
                    <xsl:variable name="noCommaBeforeAnd">
                      <xsl:call-template name="templ_prop_NoCommaBeforeAnd" />
                    </xsl:variable>
                    <xsl:choose>
                      <xsl:when test="$noCommaBeforeAnd != 'yes'">
                        <xsl:call-template name="templ_prop_AuthorsSeparator"/>
                      </xsl:when>
                      <xsl:otherwise>
                        <xsl:call-template name="templ_prop_Space"/>
                      </xsl:otherwise>
                    </xsl:choose>
                    <xsl:call-template name="templ_str_AndOthersUnCap"/>
									</xsl:if>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>
						
						<xsl:variable name="title">
							<xsl:choose>
								<xsl:when test="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:NoTitle">
								</xsl:when>
								
								<xsl:otherwise>
									<xsl:value-of select="$title0" />
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>

						<xsl:variable name="year">
							<xsl:choose>
								<xsl:when test="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:NoYear">
								</xsl:when>
								
								<xsl:otherwise>
									<xsl:value-of select="$year0" />
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>						

						<xsl:variable name="author">
							<xsl:choose>
								<xsl:when test="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:NoAuthor">
								</xsl:when>
								<xsl:otherwise>
									<xsl:value-of select="$author0" />
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>

					    <xsl:variable name="prop_APA_Hyphens">
					      <xsl:call-template name="templ_prop_Hyphens"/>
					    </xsl:variable>

						<xsl:variable name="volume" select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Volume"/>

						<xsl:variable name="volVolume">
							<xsl:if test="string-length($volume) > 0">
								<xsl:call-template name="StringFormat">
									<xsl:with-param name="format">
									  <xsl:choose>
										<xsl:when test="not(string-length($volume)=string-length(translate($volume, ',', '')))">
										  <xsl:call-template name="templ_str_VolumesShortUnCap"/>
										</xsl:when>
										<xsl:when test="string-length($volume)=string-length(translate($volume, $prop_APA_Hyphens, ''))">
										  <xsl:call-template name="templ_str_VolumeShortUnCap"/>
										</xsl:when>
										<xsl:otherwise>
										  <xsl:call-template name="templ_str_VolumesShortUnCap"/>
										</xsl:otherwise>
									  </xsl:choose>
									</xsl:with-param>
									<xsl:with-param name="parameters">
										<t:params>
											<t:param>
												<xsl:value-of select="$volume"/>
											</t:param>
										</t:params>
									</xsl:with-param>
								</xsl:call-template>
							</xsl:if>
						</xsl:variable>


						<xsl:variable name="pages" select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Pages"/>

		                <xsl:variable name="ppPages">
		                  <xsl:if test="string-length($pages)>0">
		                    <xsl:choose>
		                      <xsl:when test="not(string-length($pages)=string-length(translate($pages, ',', '')))">
		                        <xsl:call-template name="templ_str_PagesCountinousShort"/>
		                      </xsl:when>
		                      <xsl:when test="string-length($pages)=string-length(translate($pages, $prop_APA_Hyphens, ''))">
		                        <xsl:call-template name="templ_str_PageShort"/>
		                      </xsl:when>
		                      <xsl:otherwise>
		                        <xsl:call-template name="templ_str_PagesCountinousShort"/>
		                      </xsl:otherwise>
		                    </xsl:choose>
		                    <xsl:call-template name="templ_prop_Space"/>
		                    <xsl:value-of select="$pages"/>
		                  </xsl:if>
		                </xsl:variable>

						<xsl:variable name="displayAuthor">
							<xsl:value-of select="$author" />
						</xsl:variable>

						<xsl:variable name="displayTitle">
						</xsl:variable>

						
						<xsl:if test="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:FirstAuthor">
							<xsl:call-template name="templ_prop_OpenBracket"/>
						</xsl:if>
					
						<xsl:if test="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:PagePrefix">
							<xsl:value-of select="/b:Citation/b:PagePrefix"/>
						</xsl:if>

						<xsl:value-of select="$displayAuthor" />

						<xsl:if test="string-length($displayTitle) > 0">
							<xsl:if test="string-length($displayAuthor) > 0">
								<xsl:call-template name="templ_prop_ListSeparator"/>
							</xsl:if>
							<xsl:value-of select="$displayTitle"/>
						</xsl:if>

						<xsl:if test="string-length($year) > 0">
							<xsl:if test="string-length($displayAuthor) > 0 or string-length($displayTitle) > 0">
								<xsl:call-template name="templ_prop_ListSeparator"/>
							</xsl:if>	
							<xsl:value-of select="$year"/>
						</xsl:if>

						<xsl:if test="string-length($author0) = 0 and string-length($year0) = 0">
							<xsl:value-of select="msxsl:node-set($ListPopulatedWithMain)/b:Citation/b:Source/b:Tag"/>
						</xsl:if>

						<xsl:if test="string-length($volume) > 0 or string-length($pages) > 0">
							<xsl:if test="string-length($displayAuthor) > 0 or string-length($displayTitle) > 0 or string-length($year) > 0">
								<xsl:call-template name="templ_prop_Space"/>
							</xsl:if>			

							<xsl:choose>
								<xsl:when test="string-length($volume) > 0 and string-length($pages) > 0">
									<xsl:value-of select="$volume"/>
				                    <xsl:call-template name="templ_prop_Enum"/>
				                    <xsl:value-of select="$pages"/>
				                </xsl:when>
								<xsl:when test="string-length($volVolume) > 0">
									<xsl:value-of select="$volVolume"/>
				                </xsl:when>
								<xsl:when test="string-length($ppPages) > 0">
									<xsl:value-of select="$ppPages"/>
				                </xsl:when>
							</xsl:choose>
						</xsl:if>

						<xsl:if test="/b:Citation/b:PageSuffix">
							<xsl:value-of select="/b:Citation/b:PageSuffix"/>
						</xsl:if>
						
						<xsl:if test="/b:Citation/b:LastAuthor">
							<xsl:call-template name="templ_prop_CloseBracket"/>
						</xsl:if>
						<xsl:if test="not(/b:Citation/b:LastAuthor)">
							<xsl:call-template name="templ_prop_GroupSeparator"/>
						</xsl:if>
					

						</xsl:element>
					</body>
				</html>
			</xsl:when>

			<xsl:when test="b:Bibliography">
				<html xmlns:o="urn:schemas-microsoft-com:office:office"
						xmlns:w="urn:schemas-microsoft-com:office:word"
						xmlns="http://www.w3.org/TR/REC-html40">
					<head>
						
						<style>
							p.MsoBibliography, li.MsoBibliography, div.MsoBibliography
						</style>
					</head>

					<body>

						
						
						<xsl:variable name="ListPopulatedWithMain">
							<xsl:call-template name="populateMain">
								<xsl:with-param name="Type">b:Bibliography</xsl:with-param>
							</xsl:call-template>
						</xsl:variable>

						
						
						<xsl:variable name="SortedList">
							<xsl:call-template name="sortedList">
								<xsl:with-param name="sourceRoot">
									<xsl:copy-of select="$ListPopulatedWithMain"/>
								</xsl:with-param>
								
							</xsl:call-template>
						</xsl:variable>

						
						<xsl:for-each select="msxsl:node-set($SortedList)/b:Bibliography/b:Source">
							<xsl:element name="p">
				                <xsl:variable name="LCID">
				                  <xsl:choose>
				                    <xsl:when test="b:LCID='0' or b:LCID='' or not(b:LCID)">
				                      <xsl:value-of select="/*/b:Locals/b:DefaultLCID"/>
				                    </xsl:when>
				                    <xsl:otherwise>
				                      <xsl:value-of select="b:LCID"/>
				                    </xsl:otherwise>
				                  </xsl:choose>
				                </xsl:variable>
								<xsl:attribute name="lang">
									<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$LCID]/@Culture"/>
								</xsl:attribute>
				                <xsl:attribute name="dir">
									<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$LCID]/b:Properties/b:Direction"/>
								</xsl:attribute>
								<xsl:attribute name="class">
									<xsl:value-of select="'MsoBibliography'"/>
								</xsl:attribute>
								
							

								
								<xsl:variable name="prevBook">
									<xsl:value-of select="position()-1"/>
								</xsl:variable>

								<xsl:variable name="cMaxAllow">
									<xsl:call-template name="maxAuthor"/>
								</xsl:variable>


								
								<xsl:variable name ="NonEmptySectionsCount">
									<xsl:call-template name ="getNonEmptySectionsCount"/>
								</xsl:variable>

								
								<xsl:variable name ="SectionsCount">
									<xsl:call-template name="getSectionsCount"/>
								</xsl:variable>

								
								<xsl:variable name ="AllPersonsCount">
									<xsl:call-template name="getAllPersonsCount"/>
								</xsl:variable>

								
								<xsl:variable name ="EtAlSectionsCount">
									<xsl:call-template name="getEtAlSectionsCount"/>
								</xsl:variable>

								
								<xsl:variable name="MainAuthors">
									<xsl:call-template name="formatMainAuthor"/>
								</xsl:variable>

								
								<xsl:variable name="Authors">
									<xsl:if test="b:Author/b:Main != b:Author/b:Author ">
										<xsl:call-template name="formatAuthor"/>
									</xsl:if>
								</xsl:variable>

								
								<xsl:variable name="Editors">
									<xsl:if test="b:Author/b:Main != b:Author/b:Editor">
										<xsl:call-template name="formatEditor"/>
									</xsl:if>
								</xsl:variable>

								
								<xsl:variable name="Translators">
									<xsl:if test="b:Author/b:Main != b:Author/b:Translator">
										<xsl:call-template name="formatTranslator"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name = "Artists">
									<xsl:if test="b:Author/b:Main != b:Author/b:Artist">
										<xsl:call-template name="formatArtist"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name = "Composers">
									<xsl:if test="b:Author/b:Main != b:Author/b:Composer">
										<xsl:call-template name="formatComposer"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="Conductors">
									<xsl:if test="b:Author/b:Main != b:Author/b:Conductor">
										<xsl:call-template name="formatConductor"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name="Performers">
									<xsl:if test="b:Author/b:Main != b:Author/b:Performer">
										<xsl:call-template name="formatPerformer"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name="Writers">
									<xsl:if test="b:Author/b:Main != b:Author/b:Writer">
										<xsl:call-template name="formatWriter"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="Directors">
									<xsl:if test="b:Author/b:Main != b:Author/b:Director">
										<xsl:call-template name="formatDirector"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="ProducerNames">
									<xsl:if test="b:Author/b:Main != b:Author/b:ProducerName">
										<xsl:call-template name ="formatProducerName"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="Interviewees">
									<xsl:if test="b:Author/b:Main != b:Author/b:Interviewee">
										<xsl:call-template name="formatInterviewee"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="Compilers">
									<xsl:if test="b:Author/b:Main != b:Author/b:Compiler">
										<xsl:call-template name ="formatCompiler"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="Inventors">
									<xsl:if test="b:Author/b:Main != b:Author/b:Inventor">
										<xsl:call-template name="formatInventor"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name="Reporters">
									<xsl:if test="string-length(b:Reporter)">
										<xsl:value-of select ="b:Reporter"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name="Counsels">
									<xsl:if test="b:Author/b:Main != b:Author/b:Counsel">
										<xsl:call-template name="formatCounsel"/>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="BookMainAuthors">
									<xsl:if test="b:Author/b:Main != b:Author/b:BookAuthor">
										<xsl:if test="string-length(b:Author/b:BookAuthor/b:NameList/b:Person/b:Last)>0">
											
											
											<xsl:call-template name="templ_str_BookAuthorShortUnCap"/>
											<xsl:call-template name="templ_prop_Space" />
											<xsl:for-each select="b:Author/b:BookAuthor">
												<xsl:call-template name="formatPersons"/>
											</xsl:for-each>
										</xsl:if>
									</xsl:if>
								</xsl:variable>

							    <xsl:variable name="prop_APA_Hyphens2">
							      <xsl:call-template name="templ_prop_Hyphens"/>
							    </xsl:variable>

								<xsl:variable name="volume" select="b:Volume"/>

								<xsl:variable name="volVolume">
									<xsl:if test="string-length($volume) > 0">
										<xsl:call-template name="StringFormat">
											<xsl:with-param name="format">
											  <xsl:choose>
												<xsl:when test="not(string-length($volume)=string-length(translate($volume, ',', '')))">
												  <xsl:call-template name="templ_str_VolumesShortCap"/>
												</xsl:when>
												<xsl:when test="string-length($volume)=string-length(translate($volume, $prop_APA_Hyphens2, ''))">
												  <xsl:call-template name="templ_str_VolumeShortCap"/>
												</xsl:when>
												<xsl:otherwise>
												  <xsl:call-template name="templ_str_VolumesShortCap"/>
												</xsl:otherwise>
											  </xsl:choose>
											</xsl:with-param>
											<xsl:with-param name="parameters">
												<t:params>
													<t:param>
														<xsl:value-of select="$volume"/>
													</t:param>
												</t:params>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:if>
								</xsl:variable>

								<xsl:variable name ="CityPublisherYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="b:City"/>
												<xsl:with-param name ="Publisher" select="b:Publisher"/>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement" select ="b:Year"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="VolumeNumberVolumesHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatColonElement">
												<xsl:with-param name ="FirstParam" select ="b:Edition"/>
												<xsl:with-param name ="SecondParam" select ="$volVolume"/>
												<xsl:with-param name ="ThirdParam" select ="b:NumberVolumes"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name="pages" select="b:Pages"/>

							    <xsl:variable name="prop_APA_Hyphens">
							      <xsl:call-template name="templ_prop_Hyphens"/>
							    </xsl:variable>

								<xsl:variable name ="Pages">
				                  <xsl:if test="string-length($pages)>0">
				                    <xsl:choose>
				                      <xsl:when test="not(string-length($pages)=string-length(translate($pages, ',', '')))">
				                        <xsl:call-template name="templ_str_PagesCountinousShort"/>
				                      </xsl:when>
				                      <xsl:when test="string-length($pages)=string-length(translate($pages, $prop_APA_Hyphens, ''))">
				                        <xsl:call-template name="templ_str_PageShort"/>
				                      </xsl:when>
				                      <xsl:otherwise>
				                        <xsl:call-template name="templ_str_PagesCountinousShort"/>
				                      </xsl:otherwise>
				                    </xsl:choose>
				                    <xsl:call-template name="templ_prop_Space"/>
				                    <xsl:value-of select="$pages"/>
				                  </xsl:if>
								</xsl:variable>
								
								<xsl:variable name ="EditionVolumeNumberVolumesPagesHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatColonElement">
												<xsl:with-param name ="FirstParam" select ="b:Edition"/>
												<xsl:with-param name ="SecondParam" select ="$volVolume"/>
												<xsl:with-param name ="ThirdParam" select ="b:NumberVolumes"/>
												<xsl:with-param name ="FourthParam" select ="$Pages"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CityPublisherDateMonthYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="b:City"/>
												<xsl:with-param name ="Publisher" select="b:Publisher"/>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"/>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CityBroadcasterStationPublisherDateMonthYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="b:City"/>
												<xsl:with-param name ="Publisher">
													<xsl:value-of select="b:Broadcaster"/>
													<xsl:if test="string-length(b:Broadcaster)>0 and (string-length(b:Station)>0 or string-length(b:Publisher)>0)">
                            <xsl:call-template name="templ_prop_NonBreakingSpace"/>
                            <xsl:call-template name="templ_prop_GroupSeparator"/>													
													</xsl:if>
													<xsl:value-of select="b:Station"/>
													<xsl:if test="string-length(b:Station)>0 and string-length(b:Publisher)>0">
                            <xsl:call-template name="templ_prop_NonBreakingSpace"/>
                            <xsl:call-template name="templ_prop_GroupSeparator"/>													
													</xsl:if>
													<xsl:value-of select="b:Publisher"/>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"/>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="IssueVolumeHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatColonElement">
												<xsl:with-param name ="FirstParam" select ="b:Issue"/>
												<xsl:with-param name ="SecondParam" select ="$volVolume"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="PagesHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="$Pages"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="InstitutionHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="b:Institution"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="EditionHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="b:Edition"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="VolumeHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="$volVolume"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CityInstitutionHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="b:City"/>
												<xsl:with-param name ="Publisher" select="b:Institution"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CityPublisherHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="b:City"/>
												<xsl:with-param name ="Publisher" select="b:Publisher"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CityProductionCompanyYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="b:City"/>
												<xsl:with-param name ="Publisher" select="b:ProductionCompany"/>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement" select ="b:Year"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="TheaterCityProductionCompanyDateMonthYearHyphenSection">
									
									<xsl:variable name ='TheaterCity'>
										<xsl:value-of select ='b:Theater'/>
										<xsl:if test ='string-length(b:Theater)>0 and string-length(b:City)>0'>
											
											
											
											
											
											<xsl:value-of select="$constGost_TheaterCitySeparator"/>
										</xsl:if>
										<xsl:value-of select ='b:City'/>
									</xsl:variable>

									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select="$TheaterCity"/>
												<xsl:with-param name ="Publisher" select="b:ProductionCompany"/>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"/>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="ProductionCompanyDateMonthYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="b:ProductionCompany"/>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"/>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="URLHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="b:URL"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="VersionHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="b:Version"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="DateMonthYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatDateMonthYear"/>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="SLProductionCompanyDistributorYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location">
													
													
												</xsl:with-param>
												
												<xsl:with-param name ="Publisher" select ="b:ProductionCompany"/>
												<xsl:with-param name ="Distributor" select="b:Distributor"/>
												<xsl:with-param name ="noSL">yes</xsl:with-param>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement" select ="b:Year"/>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CountryRegionDateMonthYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement" select ="b:CountryRegion"/>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"></xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="CityPublisherProductionCompanyDateMonthYearHyphenSection">
									
									<xsl:variable name ='PublisherProductionCompany'>
										<xsl:value-of select ='b:Publisher'/>
										<xsl:if test ='string-length(b:Publisher)>0 and string-length(b:ProductionCompany)>0'>
											
											
											
											
											
											<xsl:value-of select="$constGost_PublisherProductionCompanySeparator"/>
										</xsl:if>
										<xsl:value-of select ='b:ProductionCompany'/>
									</xsl:variable>

									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select ="b:City"/>
												<xsl:with-param name ="Publisher" select ="$PublisherProductionCompany"/>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"></xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>


								<xsl:variable name ="CityCourtDateMonthYearHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatLocationElement">
												<xsl:with-param name ="Location" select ="b:City"/>
												<xsl:with-param name ="Publisher" select ="b:Court"/>
											</xsl:call-template>
										</xsl:with-param>
										<xsl:with-param name ="SecondElement">
											<xsl:call-template name ="formatDateMonthYear"></xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="DateMonthYearAccessedHyphenSection">
									<xsl:call-template name ="formatHyphenSection">
										<xsl:with-param name ="FirstElement">
											<xsl:call-template name ="formatDateMonthYearAccessed" />
										</xsl:with-param>
									</xsl:call-template>
								</xsl:variable>

								<xsl:variable name ="MainSectionsCount">
									<xsl:choose>
										<xsl:when test ="count(b:Author/b:Main/b:NameList/b:Person) >0 or string-length(b:Author/b:Main/b:Corporate)>0">
											<xsl:value-of select="1"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="0"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:variable>
								

								<xsl:variable name = "srcText">



								<b>
									<xsl:value-of select="$MainAuthors"/>
									
								</b>

								
								<xsl:call-template name="templ_prop_Space" />
								
								

								<xsl:if test="string-length(b:TitlePrefix) > 0">
									<xsl:value-of select="b:TitlePrefix"/>
									
									
								</xsl:if>
								<xsl:value-of select="b:Title"/>

								
								
								<xsl:variable name ="SourceType">
									<xsl:value-of select="b:SourceType"/>
								</xsl:variable>

								<xsl:choose>
									<xsl:when test="string-length($SourceType)=0">
									</xsl:when>
									<xsl:when test="b:SourceType='InternetSite' or b:SourceType='DocumentFromInternetSite'">
										<xsl:value-of select="$constGost_SourceTypeOpen"/>
										<xsl:call-template name="templ_str_OnlineCap"/>
										<xsl:value-of select="$constGost_SourceTypeClose"/>
									</xsl:when>
									<xsl:when test="b:SourceType='Misc' or b:SourceType='ElectronicSource' or b:SourceType='Film'">
										<xsl:if test="string-length(b:Medium) > 0">
											<xsl:value-of select="$constGost_SourceTypeOpen"/>
											<xsl:value-of select="b:Medium"/>
											<xsl:value-of select="$constGost_SourceTypeClose"/>
										</xsl:if>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="$constGost_SourceTypeOpen"/>
										<xsl:value-of select="/b:Bibliography/b:Locals/b:Local[@LCID=$LCID]/b:SourceNames/*[local-name()=$SourceType]"/>
										<xsl:value-of select="$constGost_SourceTypeClose"/>
									</xsl:otherwise>
								</xsl:choose>
								
								
								

                <xsl:if test = "b:SourceType='ElectronicSource' and string-length(b:PublicationTitle) >0">
                  
                  
                  
                  <xsl:value-of select="$constGost_ShortTitleHeader"/>
                  <xsl:value-of select="b:PublicationTitle" />
                </xsl:if>

								<xsl:if test = "b:SourceType='Case' and string-length(b:Reporter) >0">
									<xsl:value-of select="$constGost_ShortTitleHeader"/>
									<xsl:value-of select="b:Reporter" />
								</xsl:if>

                
								<xsl:if test = "string-length(b:ShortTitle) >0">
									
									
									
									<xsl:value-of select="$constGost_ShortTitleHeader"/>
									<xsl:value-of select="b:ShortTitle" />
								</xsl:if>

								
								<xsl:if test ="b:SourceType='Book'">
                 					<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Book_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>
									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$Editors"/>
										<xsl:with-param name ='SecondElement' select ='$Translators'/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherYearHyphenSection"/>
									<xsl:value-of select ="$EditionVolumeNumberVolumesPagesHyphenSection"/>
								</xsl:if>
								

								
								<xsl:if test ="b:SourceType='BookSection'">
									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_BookSection_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="CollectionName" select ="b:BookTitle"/>
										<xsl:with-param name ="FirstElement" select ="$BookMainAuthors"/>
										<xsl:with-param name ='SecondElement' select ='$Editors'/>
										<xsl:with-param name ='ThirdElement' select ='$Translators'/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherYearHyphenSection"/>
									<xsl:value-of select ="$VolumeNumberVolumesHyphenSection"/>
								</xsl:if>

								<xsl:if test ="b:SourceType='JournalArticle'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_JournalArticle_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="CollectionName" select ="b:JournalName"/>
										<xsl:with-param name ="FirstElement" select ="$Editors"/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$IssueVolumeHyphenSection"/>
									<xsl:value-of select ="$PagesHyphenSection"/>
								</xsl:if>


								<xsl:if test ="b:SourceType='ArticleInAPeriodical'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_ArticleInAPeriodical_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="CollectionName" select ="b:PeriodicalTitle"/>
										<xsl:with-param name ="FirstElement" select ="$Editors"/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$EditionHyphenSection"/>
									<xsl:value-of select ="$IssueVolumeHyphenSection"/>
									<xsl:value-of select ="$PagesHyphenSection"/>
								</xsl:if>


								<xsl:if test="b:SourceType='ConferenceProceedings'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_ConferenceProceedings_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="CollectionName" select ="b:ConferenceName"/>
										<xsl:with-param name ="FirstElement" select ="$Editors"/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherYearHyphenSection"/>
									<xsl:value-of select ="$VolumeHyphenSection"/>
									<xsl:value-of select ="$PagesHyphenSection"/>
								</xsl:if>


								<xsl:if test="b:SourceType='Report'">

									<xsl:if test="string-length(b:ThesisType)>0">
										
										
										
										
										
										<xsl:value-of select="$constGost_ReportTypeHeader"/>
										<xsl:value-of select="b:ThesisType"/>
									</xsl:if>

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Report_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:variable name = "DepartmentAndInstitution">
										<xsl:call-template name ="format_SemiColonSeparated_Items">
											<xsl:with-param name ="Item1" select ="b:Department"/>
											<xsl:with-param name ="Item2" select ="b:Institution"/>
										</xsl:call-template>
									</xsl:variable>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$DepartmentAndInstitution"/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherYearHyphenSection"/>
									<xsl:value-of select ="$PagesHyphenSection"/>
								</xsl:if>


								<xsl:if test="b:SourceType='SoundRecording'">

									<xsl:if test="string-length(b:Medium)>0">
										
										
										
										
										
										<xsl:value-of select="$constGost_SoundRecordingMediumHeader"/>
										<xsl:value-of select="b:Medium"/>
									</xsl:if>

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$Artists"/>
										<xsl:with-param name ="SecondElement" select ="$Composers"/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_SoundRecording_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="CollectionName" select ="b:AlbumTitle"/>
										<xsl:with-param name ="FirstElement" select ="$Conductors"/>
										<xsl:with-param name ='SecondElement' select ='$Performers'/>
										<xsl:with-param name ='ThirdElement' select ='$ProducerNames'/>
									</xsl:call-template>

									<xsl:value-of select ="$CityProductionCompanyYearHyphenSection"/>
								</xsl:if>


								<xsl:if test ="b:SourceType='Performance'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$Writers"/>
										<xsl:with-param name ="SecondElement" select ="$Performers"/>
										<xsl:with-param name ="ThirdElement" select ="$Directors"/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Performance_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$ProducerNames"/>
									</xsl:call-template>

									<xsl:value-of select ="$TheaterCityProductionCompanyDateMonthYearHyphenSection"/>
								</xsl:if>

								<xsl:if test="b:SourceType='Art'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$Artists"/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Art_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:value-of select ="$CityInstitutionHyphenSection"/>
								</xsl:if>

								<xsl:if test="b:SourceType='DocumentFromInternetSite'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_DocumentFromInternetSite_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ='formatSecondaryResponsibilities'>
										<xsl:with-param name ='CollectionName' select ='b:InternetSiteTitle'/>
										<xsl:with-param name ='FirstElement' select ='$Editors'/>
										<xsl:with-param name ='SecondElement' select ='$ProducerNames'/>
									</xsl:call-template>
									<xsl:value-of select ="$ProductionCompanyDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$VersionHyphenSection"/>
									<xsl:value-of select ="$DateMonthYearAccessedHyphenSection"/>
									<xsl:value-of select ="$URLHyphenSection"/>
								</xsl:if>

								<xsl:if test ="b:SourceType = 'InternetSite'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_InternetSite_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ='formatSecondaryResponsibilities'>
										<xsl:with-param name ='CollectionName' select ='b:InternetSiteTitle'/>
										<xsl:with-param name ="FirstElement" select ="$Editors"/>
										<xsl:with-param name ='SecondElement' select ='$ProducerNames'/>
									</xsl:call-template>

									<xsl:value-of select ="$ProductionCompanyDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$DateMonthYearAccessedHyphenSection"/>
									<xsl:value-of select ="$URLHyphenSection"/>
								</xsl:if>




								<xsl:if test ="b:SourceType='Film'">

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$Writers"/>
										<xsl:with-param name ="SecondElement" select ="$Performers"/>
										<xsl:with-param name ="ThirdElement" select ="$Directors"></xsl:with-param>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Film_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$ProducerNames"/>
									</xsl:call-template>

									<xsl:value-of select ="$SLProductionCompanyDistributorYearHyphenSection"/>
								</xsl:if>




								
								<xsl:if test ="b:SourceType='Interview'">
                  <xsl:call-template name ="formatSecondaryResponsibilities">
                    <xsl:with-param name ="FirstElement" select ="$Interviewees"/>
                    <xsl:with-param name ="SecondElement" select ="$Compilers"/>
										<xsl:with-param name ="ThirdElement" select ="$Editors"/>
										<xsl:with-param name ="FourthElement" select ="$Translators"/>
									</xsl:call-template>

									<xsl:value-of select="$CityBroadcasterStationPublisherDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$PagesHyphenSection"/>
								</xsl:if>

								<xsl:if test ="b:SourceType='Patent'">
									<xsl:if test ="string-length(b:PatentNumber) >0">
										
										
										
										
										
										<xsl:value-of select="$constGost_PatentNumberHeader"/>
										<xsl:value-of select ="b:PatentNumber"/>
									</xsl:if>
									<xsl:if test ="string-length(b:Type) >0">
										
										
										
										
										
										<xsl:value-of select="$constGost_PatentTypeHeader"/>
										<xsl:value-of select ="b:Type"/>
									</xsl:if>

									<xsl:call-template name ="formatPrimaryResponsibilities">
										<xsl:with-param name ='FirstElement' select ='$Inventors'/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Patent_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>
									
									<xsl:call-template name ="formatSecondaryResponsibilities">
										<xsl:with-param name ="FirstElement" select ="$Editors"/>
										<xsl:with-param name ="SecondElement" select ="$Translators"/>
									</xsl:call-template>

									<xsl:value-of select ="$CountryRegionDateMonthYearHyphenSection"/>
								</xsl:if>

								<xsl:if test ="b:SourceType='ElectronicSource'">
									<xsl:call-template name ='formatPrimaryResponsibilities'>
										<xsl:with-param name ='FirstElement' select ='$Authors'/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_ElectronicSource_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ='formatSecondaryResponsibilities'>
                    <xsl:with-param name ='FirstElement' select ='$Editors'/>
                    <xsl:with-param name ='SecondElement' select ='$ProducerNames'/>
                    <xsl:with-param name ='ThirdElement' select ='$Translators'/>
                  </xsl:call-template>

									<xsl:value-of select="$CityPublisherProductionCompanyDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$EditionHyphenSection"/>
									<xsl:value-of select ="$VolumeHyphenSection"/>
								</xsl:if>

								<xsl:if test="b:SourceType='Case'">
									<xsl:if test ="string-length(b:CaseNumber) >0">
										
										
										
										
										
										<xsl:value-of select="$constGost_CaseNumberHeader"/>
										<xsl:value-of select ="b:CaseNumber"/>
									</xsl:if>

									<xsl:if test ="string-length(b:AbbreviatedCaseNumber) >0">
										
										
										
										
										
										<xsl:value-of select="$constGost_AbbreviatedCaseNumberHeader"/>
										<xsl:value-of select ="b:AbbreviatedCaseNumber"/>
									</xsl:if>

									<xsl:call-template name ='formatPrimaryResponsibilities'>
										<xsl:with-param name ='FirstElement' select ='$Authors'/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Case_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ='formatSecondaryResponsibilities'>
										<xsl:with-param name ='FirstElement' select ='$Counsels'/>
									</xsl:call-template>

									<xsl:value-of select ="$CityCourtDateMonthYearHyphenSection"/>
								</xsl:if>


								<xsl:if test="b:SourceType='Misc'">

									<xsl:call-template name ='formatPrimaryResponsibilities'>
										<xsl:with-param name ='FirstElement' select ='$Authors'/>
										<xsl:with-param name ="NonEmptyPrimSectionsCount">
											<xsl:call-template name ="getNonEmpty_Misc_PrimSectionsCount"/>
										</xsl:with-param>
										<xsl:with-param name ="MainSectionsCount" select ="$MainSectionsCount"/>
									</xsl:call-template>

									<xsl:call-template name ='formatSecondaryResponsibilities'>
										<xsl:with-param name ='CollectionName' select ='b:PublicationTitle'/>
										<xsl:with-param name ='FirstElement' select ='$Compilers'/>
										<xsl:with-param name ="SecondElement" select ="$Editors"/>
										<xsl:with-param name ='ThirdElement' select ='$Translators'/>
									</xsl:call-template>

									<xsl:value-of select ="$CityPublisherDateMonthYearHyphenSection"/>
									<xsl:value-of select ="$EditionHyphenSection"/>
									<xsl:value-of select ="$VolumeHyphenSection"/>
									<xsl:value-of select ="$PagesHyphenSection"/>
								</xsl:if>


								
								<xsl:call-template name ="formatHyphenSection">
									<xsl:with-param name ="FirstElement" select ="b:Comments"/>
								</xsl:call-template>

								<xsl:call-template name ="formatHyphenSection">
									<xsl:with-param name ="FirstElement" select ="b:StandardNumber"/>
								</xsl:call-template>

								</xsl:variable>

								<xsl:if test = "string-length(normalize-space($srcText)) > 0">
									<xsl:copy-of select = "$srcText" />
									<xsl:call-template name="templ_prop_Dot"/>
								</xsl:if>

							</xsl:element>
						</xsl:for-each>
					</body>
				</html>
			</xsl:when>
		</xsl:choose>
	</xsl:template>


	
	
	
	
	<xsl:template name="MainContributors">
		<xsl:param name="SourceRoot"/>
		<xsl:choose>
			<xsl:when test="./b:SourceType='Book'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Translator)>0">Translator</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='BookSection'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='JournalArticle'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='ArticleInAPeriodical'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='ConferenceProceedings'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Report'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='SoundRecording'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Artist)>0">Artist</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Performer)>0">Performer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Composer)>0">Composer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Conductor)>0">Conductor</xsl:when>
					<xsl:when test="string-length(./b:Author/b:ProducerName)>0">ProducerName</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Performance'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Writer)>0">Writer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Director)>0">Director</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Performer)>0">Performer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:ProducerName)>0">ProducerName</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Art'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Artist)>0">Artist</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='DocumentFromInternetSite'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='InternetSite'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Film'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Director)>0">Director</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Writer)>0">Writer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Performer)>0">Performer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:ProducerName)>0">ProducerName</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Interview'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Interviewee)>0">Interviewee</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Patent'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Inventor)>0">Inventor</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='ElectronicSource'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
					<xsl:when test="string-length(./b:Author/b:ProducerName)>0">ProducerName</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Translator)>0">Translator</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Case'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Counsel)>0">Counsel</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Misc'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Compiler)>0">Compiler</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Translator)>0">Translator</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	
	<xsl:template name="sortedList">
		<xsl:param name="sourceRoot"/>
		
		<xsl:apply-templates select="msxsl:node-set($sourceRoot)/*">
			<xsl:sort select="b:SortingString" />
		</xsl:apply-templates>
		
	</xsl:template>

	
	<xsl:template match="*">
		<xsl:element name="{name()}" namespace="{namespace-uri()}">
			
			<xsl:for-each select="@*">
				<xsl:attribute name="{name()}" namespace="{namespace-uri()}">
					
					<xsl:value-of select="." />
				</xsl:attribute>
			</xsl:for-each>
			<xsl:apply-templates>
				<xsl:sort select="b:SortingString" />
			</xsl:apply-templates>
		</xsl:element>
	</xsl:template>

	
	<xsl:template match="text()">
		<xsl:value-of select="." />
	</xsl:template>

	<xsl:template name="maxAuthor">
		<xsl:choose>
			<xsl:when test="count(b:NameList/b:Person) > _MaxAuthor">
				<xsl:value-of select="_MaxAuthor"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="count(b:NameList/b:Person)"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	
	<xsl:template name="formatLastFirst">
		<xsl:call-template name="formatNameCore">
			<xsl:with-param name="FML"><xsl:call-template name="templ_prop_Gost_Authors_FML"/></xsl:with-param>
			<xsl:with-param name="FM"><xsl:call-template name="templ_prop_Gost_Authors_FM"/></xsl:with-param>
			<xsl:with-param name="ML"><xsl:call-template name="templ_prop_Gost_Authors_ML"/></xsl:with-param>
			<xsl:with-param name="FL"><xsl:call-template name="templ_prop_Gost_Authors_FL"/></xsl:with-param>
			<xsl:with-param name="upperLast">no</xsl:with-param>
			<xsl:with-param name="withDot">no</xsl:with-param>
		</xsl:call-template>
	</xsl:template>

	
	
	
	<xsl:template name="formatPersonSeparator">
		<xsl:variable name="cMaxAuthor">
			<xsl:value-of select="count(../b:Person)"/>
		</xsl:variable>

<xsl:variable name="constGost_PersonSeparator">
	<xsl:call-template name="templ_prop_ListSeparator" />
	
</xsl:variable>
<xsl:variable name="constGost_PersonAndOther">
	<xsl:call-template name="templ_prop_Space" />
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	<xsl:call-template name="templ_str_AndOthersUnCap"/>
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
	
</xsl:variable>


		<xsl:variable name="cMaxAllow">
			
			<xsl:choose>
				<xsl:when test="$cMaxAuthor > ../b:_MaxAuthor and ../b:_MaxAuthor > 0">
					<xsl:value-of select="../b:_MaxAuthor"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$cMaxAuthor"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test="$cMaxAuthor > 3">
				
				
				<xsl:value-of select="$constGost_PersonAndOther"/>
			</xsl:when>
			<xsl:when test="$cMaxAllow - 1 > position()">
				
				
				<xsl:value-of select="$constGost_PersonSeparator"/>
			</xsl:when>
			<xsl:when test="position() = $cMaxAuthor - 1">
				<xsl:variable name="noAndBeforeLastAuthor">
			        <xsl:call-template name="templ_prop_NoAndBeforeLastAuthor"/>
				</xsl:variable>

		        <xsl:if test="$noAndBeforeLastAuthor != 'yes'">
					<xsl:call-template name="templ_prop_Space"/>
			        <xsl:call-template name="templ_str_AndUnCap"/>
			        <xsl:call-template name="templ_prop_Space"/>
			    </xsl:if>
		        <xsl:if test="$noAndBeforeLastAuthor = 'yes'">
			        <xsl:call-template name="templ_prop_AuthorsSeparator"/>
		        </xsl:if>
				
				
			</xsl:when>
		</xsl:choose>
	</xsl:template>


	<xsl:template name="formatPersons">
		<xsl:variable name="cMaxAllow">
			<xsl:call-template name="maxAuthor"/>
		</xsl:variable>

		<xsl:variable name ="cIsEtAl">
			
			<xsl:choose>
				<xsl:when test ="count(b:NameList/b:Person[4]) >0">
					<xsl:value-of select="1"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select = "0"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>

		<xsl:variable name="cEtAlPosition">
			
			<xsl:value-of select ="1"/>
		</xsl:variable>

		<xsl:if test="string-length(b:Corporate)=0">
			<xsl:for-each select="b:NameList/b:Person">
				<xsl:variable name="cMaxAuthor">
					<xsl:value-of select="count(../b:NameList/b:Person)"/>
				</xsl:variable>

				
				
				<xsl:if test="($cIsEtAl = '0' and $cMaxAllow >= position()) or ($cIsEtAl = '1' and not (position()>$cEtAlPosition)) ">
					<xsl:call-template name="formatLastFirst"/>
					<xsl:call-template name="formatPersonSeparator"/>
				</xsl:if>
			</xsl:for-each>
		</xsl:if>
		<xsl:if test="string-length(b:Corporate)>0">
			  <xsl:value-of select="b:Corporate"/>
		</xsl:if>
	</xsl:template>

	
	<xsl:template name="formatMainAuthor">
		<xsl:if test="string-length(b:Author/b:Main/b:Corporate)=0">
			<xsl:if test ="count(b:Author/b:Main/b:NameList/b:Person) >0">
				<xsl:for-each select="b:Author/b:Main">
					<xsl:call-template name="formatPersons"/>
				</xsl:for-each>
			</xsl:if>
		</xsl:if>
		<xsl:if test="string-length(b:Author/b:Main/b:Corporate)>0">
			  <xsl:value-of select="b:Author/b:Main/b:Corporate"/>
		</xsl:if>
	</xsl:template>

	
	<xsl:template name="formatAuthor">
		<xsl:if test="string-length(b:Author/b:Main/b:Corporate)=0">
			<xsl:if test ="count(b:Author/b:Author/b:NameList/b:Person) >0">
				<xsl:call-template name="templ_str_AuthorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
				<xsl:for-each select="b:Author/b:Author">
					<xsl:call-template name="formatPersons"/>
				</xsl:for-each>
			</xsl:if>
		</xsl:if>
		<xsl:if test="string-length(b:Author/b:Main/b:Corporate)>0">
			  <xsl:call-template name="templ_str_AuthorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			  <xsl:value-of select="b:Author/b:Main/b:Corporate"/>
		</xsl:if>
	</xsl:template>

	
	<xsl:template name="formatEditor">
		<xsl:if test="string-length(b:Author/b:Editor/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_EditorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Editor">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	
	<xsl:template name="formatTranslator">
		<xsl:if test="string-length(b:Author/b:Translator/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_TranslatorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Translator">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	
	<xsl:template name="formatArtist">
		<xsl:if test="string-length(b:Author/b:Artist/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_ArtistShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Artist">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name="formatWriter">
		<xsl:if test="string-length(b:Author/b:Writer/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_WriterShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Writer">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name="formatPerformer">
		<xsl:if test="string-length(b:Author/b:Performer/b:Corporate)=0">
			<xsl:if test="string-length(b:Author/b:Performer/b:NameList/b:Person/b:Last) > 0">
				<xsl:call-template name="templ_str_PerformerShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
				<xsl:for-each select="b:Author/b:Performer">
					<xsl:call-template name="formatPersons"/>
				</xsl:for-each>
			</xsl:if>
		</xsl:if>
		<xsl:if test="string-length(b:Author/b:Performer/b:Corporate)>0">
			<xsl:call-template name="templ_str_PerformerShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:value-of select="b:Author/b:Performer/b:Corporate"/>
		</xsl:if>		
	</xsl:template>


	<xsl:template name="formatDirector">
		<xsl:if test="string-length(b:Author/b:Director/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_DirectorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Director">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>



	<xsl:template name="formatInterviewee">
		<xsl:if test="string-length(b:Author/b:Interviewee/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_IntervieweeShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Interviewee">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name="formatProducerName">
	
		<xsl:variable name="constGost_ProducerNameHeader">
			<xsl:call-template name="templ_str_ProducerShortUnCap"/><xsl:call-template name="templ_prop_Space"/>			
		</xsl:variable>
	
		<xsl:if test="string-length(b:Author/b:ProducerName/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_ProducerShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:ProducerName">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>


	<xsl:template name="formatConductor">
		<xsl:if test="string-length(b:Author/b:Conductor/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_ConductorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Conductor">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name="formatComposer">
		<xsl:if test="string-length(b:Author/b:Composer/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_ComposerShortUnCapIso"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Composer">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>



	<xsl:template name="formatCompiler">
		<xsl:if test="string-length(b:Author/b:Compiler/b:NameList/b:Person/b:Last) > 0">
			<xsl:call-template name="templ_str_CompilerShortUnCapIso"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Compiler">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="formatCounsel">
		<xsl:if test="string-length(b:Author/b:Counsel/b:NameList/b:Person/b:Last)>0">
			<xsl:call-template name="templ_str_CounselShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Counsel">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="formatInventor">
		<xsl:if test="string-length(b:Author/b:Inventor/b:NameList/b:Person/b:Last)>0">
			<xsl:call-template name="templ_str_InventorShortUnCap"/><xsl:call-template name="templ_prop_Space"/>
			<xsl:for-each select="b:Author/b:Inventor">
				<xsl:call-template name="formatPersons"/>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="getEtAlSectionsCount">
		<xsl:value-of select="count(b:Author/*/b:NameList/b:Person[4])"/>
		
	</xsl:template>

	<xsl:template name ="getAllPersonsCount">
		<xsl:value-of select="count(b:Author/*/b:NameList/b:Person)"/>
		
	</xsl:template>

	<xsl:template name ="getSectionsCount">
		<xsl:value-of select="count(b:Author/*)"/>
		
	</xsl:template>

	<xsl:template name ="getNonEmptySectionsCount">
		<xsl:value-of select="count(b:Author/*/b:NameList/b:Person[1])"/>
		
	</xsl:template>

	<xsl:template name ="getNonEmpty_Book_PrimSectionsCount">
		<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate )"/>
		
	</xsl:template>

	<xsl:template name ="getNonEmpty_BookSection_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_JournalArticle_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_ArticleInAPeriodical_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate)"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_ConferenceProceedings_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Report_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_SoundRecording_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Composer/b:NameList/b:Person[1] | b:Author/b:Artist/b:NameList/b:Person[1] )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Performance_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Writer/b:NameList/b:Person[1] | b:Author/b:Performer/b:NameList/b:Person[1] | b:Author/b:Performer/b:Corporate | b:Author/b:Director/b:NameList/b:Person[1] )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Art_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Artist/b:NameList/b:Person[1] )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_DocumentFromInternetSite_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_InternetSite_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Film_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Writer/b:NameList/b:Person[1] | b:Author/b:Performer/b:NameList/b:Person[1] | b:Author/b:Performer/b:Corporate | b:Author/b:Director/b:NameList/b:Person[1] )"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Interview_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Interviewee/b:NameList/b:Person[1])"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Patent_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Inventor/b:NameList/b:Person[1])"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_ElectronicSource_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate)"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Case_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate)"/>
	</xsl:template>

	<xsl:template name ="getNonEmpty_Misc_PrimSectionsCount">
		<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person[1] | b:Author/b:Author/b:Corporate)"/>
	</xsl:template>

	
	<xsl:template name="populateMain">
		<xsl:param name="Type"/>
		
		<xsl:element name="{$Type}">
			
			<xsl:for-each select="/*[$Type]/b:Source">
				
				<xsl:variable name="MostImportantAuthorLocalName">
					
					<xsl:call-template name="MainContributors"/>
				</xsl:variable>
				<xsl:element name="{'b:Source'}">
					
	        <b:SortingString>

	          	<xsl:variable name = "author0">
				  <xsl:for-each select="./b:Author/*[local-name()=$MostImportantAuthorLocalName]">
				    <xsl:call-template name="formatPersons"/>
				  </xsl:for-each>
				</xsl:variable>

	          	<xsl:variable name = "author">
		    		<xsl:choose>
						<xsl:when test="string-length(./b:Author/*[local-name()=$MostImportantAuthorLocalName]/b:Corporate) > 0">
				            <xsl:value-of select="./b:Author/*[local-name()=$MostImportantAuthorLocalName]/b:Corporate"/>
				        </xsl:when>
						<xsl:when test="string-length($author0) > 0">
				            <xsl:value-of select="$author0"/>
				        </xsl:when>
		    		</xsl:choose>
		    	</xsl:variable>

				<xsl:if test="string-length($author) > 0">
		            <xsl:text>&#32;</xsl:text>
		            <xsl:value-of select="$author"/>
		        </xsl:if>
	        
	            <xsl:if test="string-length(b:Title) > 0">
					<xsl:text>&#32;</xsl:text>
					<xsl:value-of select="b:Title"/>
				</xsl:if>
			</b:SortingString>
			
          <xsl:if test="$Type='b:Citation'">
            
            <b:Title>
              
              <xsl:if test="string-length(b:Title)>0">
                <xsl:value-of select="b:Title"/>
              </xsl:if>
              
              <xsl:if test="string-length(b:Title)=0">
                <xsl:choose>
                  <xsl:when test="b:SourceType='Book' or
                                  b:SourceType='JournalArticle' or
                                  b:SourceType='ConferenceProceedings' or
                                  b:SourceType='Report' or
                                  b:SourceType='Performance' or
                                  b:SourceType='Film' or
                                  b:SourceType='Patent' or
                                  b:SourceType='Case'">

                    <xsl:value-of select="b:ShortTitle"/>
                  </xsl:when>

                  <xsl:when test="b:SourceType='BookSection'">
                    <xsl:variable name="shortTitle" select="b:ShortTitle"/>
                    <xsl:variable name="bookTitle" select="b:BookTitle"/>

                    <xsl:choose>
                      <xsl:when test="string-length($shortTitle)>0">
                        <xsl:value-of select="$shortTitle"/>
                      </xsl:when>
                      <xsl:when test="string-length($bookTitle)>0">
                        <xsl:value-of select="$bookTitle"/>
                      </xsl:when>
                    </xsl:choose>

                  </xsl:when>

                  <xsl:when test="b:SourceType='ArticleInAPeriodical'">
                    <xsl:variable name="shortTitle" select="b:ShortTitle"/>
                    <xsl:variable name="periodicalTitle" select="b:PeriodicalTitle"/>

                    <xsl:choose>
                      <xsl:when test="string-length($shortTitle)>0">
                        <xsl:value-of select="$shortTitle"/>
                      </xsl:when>
                      <xsl:when test="string-length($periodicalTitle)>0">
                        <xsl:value-of select="$periodicalTitle"/>
                      </xsl:when>
                    </xsl:choose>
                  </xsl:when>

                  <xsl:when test="b:SourceType='InternetSite' or
                                  b:SourceType='DocumentFromInternetSite'">
                    <xsl:variable name="shortTitle" select="b:ShortTitle"/>
                    <xsl:variable name="internetSiteTitle" select="b:InternetSiteTitle"/>

                    <xsl:choose>
                      <xsl:when test="string-length($shortTitle)>0">
                        <xsl:value-of select="$shortTitle"/>
                      </xsl:when>
                      <xsl:when test="string-length($internetSiteTitle)>0">
                        <xsl:value-of select="$internetSiteTitle"/>
                      </xsl:when>
                    </xsl:choose>
                  </xsl:when>

                  <xsl:when test="b:SourceType='ElectronicSource' or
                                  b:SourceType='Art' or
                                  b:SourceType='Misc'">
                    <xsl:variable name="shortTitle" select="b:ShortTitle"/>
                    <xsl:variable name="publicationTitle" select="b:PublicationTitle"/>

                    <xsl:choose>
                      <xsl:when test="string-length($shortTitle)>0">
                        <xsl:value-of select="$shortTitle"/>
                      </xsl:when>
                      <xsl:when test="string-length($publicationTitle)>0">
                        <xsl:value-of select="$publicationTitle"/>
                      </xsl:when>
                    </xsl:choose>
                  </xsl:when>

                  <xsl:when test="b:SourceType='SoundRecording'">
                    <xsl:variable name="shortTitle" select="b:ShortTitle"/>
                    <xsl:variable name="albumTitle" select="b:AlbumTitle"/>

                    <xsl:choose>
                      <xsl:when test="string-length($shortTitle)>0">
                        <xsl:value-of select="$shortTitle"/>
                      </xsl:when>
                      <xsl:when test="string-length($albumTitle)>0">
                        <xsl:value-of select="$albumTitle"/>
                      </xsl:when>
                    </xsl:choose>
                  </xsl:when>

                  <xsl:when test="b:SourceType='Interview'">
                    <xsl:variable name="shortTitle" select="b:ShortTitle"/>
                    
                    <xsl:variable name="broadcastTitle" select="b:BroadcastTitle"/>
                    

                    <xsl:choose>
                      <xsl:when test="string-length($shortTitle)>0">
                        <xsl:value-of select="$shortTitle"/>
                      </xsl:when>
                      
                      <xsl:when test="string-length($broadcastTitle)>0">
                        <xsl:value-of select="$broadcastTitle"/>
                      </xsl:when>
                      
                    </xsl:choose>
                  </xsl:when>

                </xsl:choose>
              </xsl:if>
            </b:Title>
          </xsl:if>
          <b:Author>
						
						<b:Main>
							<xsl:if test="string-length(./b:Author/*[local-name()=$MostImportantAuthorLocalName]/b:Corporate)=0">
								<b:NameList>
									<xsl:for-each select="./b:Author/*[local-name()=$MostImportantAuthorLocalName]/b:NameList/b:Person">
										<b:Person>
											
											<b:Last>
												<xsl:value-of select="./b:Last"/>
											</b:Last>
											<b:First>
												<xsl:value-of select="./b:First"/>
											</b:First>
											<b:Middle>
												<xsl:value-of select="./b:Middle"/>
											</b:Middle>
										</b:Person>
									</xsl:for-each>
								</b:NameList>
							</xsl:if>
							<xsl:if test="string-length(./b:Author/*[local-name()=$MostImportantAuthorLocalName]/b:Corporate)>0">
								<b:Corporate>
								  <xsl:value-of select="./b:Author/*[local-name()=$MostImportantAuthorLocalName]/b:Corporate"/>
								</b:Corporate>
							</xsl:if>
						</b:Main>
						<xsl:for-each select="./b:Author/*">
							
							<xsl:if test="name()!='b:Main'">
								<xsl:element name="{name()}" namespace="{namespace-uri()}">
									<xsl:call-template name="copyNameNodes"/>
									
								</xsl:element>
							</xsl:if>
						</xsl:for-each>
					</b:Author>
					<xsl:for-each select="*">
						
            <xsl:if test="name()!='b:Author' and not(name()='b:Title' and $Type='b:Citation')">
              <xsl:element name="{name()}" namespace="{namespace-uri()}">
								<xsl:call-template name="copyNodes"/>
								
							</xsl:element>
						</xsl:if>
					</xsl:for-each>
				</xsl:element>
			</xsl:for-each>
			<xsl:for-each select="/*[$Type]/*">
				
				<xsl:if test="local-name()!='Source'">
					<xsl:call-template name="copyTrees"/>
				</xsl:if>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>

	
	<xsl:template name="copyNameNodes">
		<xsl:if test="string-length(b:Corporate)=0">
			<b:NameList>
				<xsl:for-each select="b:NameList/b:Person">
					
					<b:Person>
						
						<xsl:if test="string-length(./b:Last)>0">
							
							<b:Last>
								<xsl:value-of select="./b:Last"/>
							</b:Last>
						</xsl:if>
						<xsl:if test="string-length(./b:First)>0">
							<b:First>
								<xsl:value-of select="./b:First"/>
							</b:First>
						</xsl:if>
						<xsl:if test="string-length(./b:Middle)>0">
							<b:Middle>
								<xsl:value-of select="./b:Middle"/>
							</b:Middle>
						</xsl:if>
					</b:Person>
				</xsl:for-each>
			</b:NameList>
		</xsl:if>
		<xsl:if test="string-length(b:Corporate)>0">
			<b:Corporate>
			  <xsl:value-of select="b:Corporate"/>
			</b:Corporate>
		</xsl:if>
	</xsl:template>

	
	<xsl:template name="copyNodes">
		<xsl:value-of select="."/>
	</xsl:template>

	
	<xsl:template name="copyTrees">
		<xsl:copy-of select ='.'/>
	</xsl:template>

	<xsl:template name ="formatColonElement">
		<xsl:param name ="FirstParam"></xsl:param>
		<xsl:param name ="SecondParam"></xsl:param>
		<xsl:param name ="ThirdParam"></xsl:param>
		<xsl:param name ="FourthParam"></xsl:param>

		<xsl:variable name="constGost_ColonElementSeparator">
			<xsl:call-template name="templ_prop_NonBreakingSpace" />
			<xsl:call-template name="templ_prop_EnumSeparator" />
			
		</xsl:variable>

		<xsl:value-of select ="$FirstParam"/>
		<xsl:if test ="string-length($FirstParam)>0 and (string-length($SecondParam)>0 or string-length($ThirdParam)>0 or string-length($FourthParam)>0)">
			<xsl:value-of select="$constGost_ColonElementSeparator"/>
		</xsl:if>
		<xsl:value-of select ="$SecondParam"/>
		<xsl:if test ="string-length($SecondParam)>0 and (string-length($ThirdParam)>0 or string-length($FourthParam)>0)">
			<xsl:value-of select="$constGost_ColonElementSeparator"/>
		</xsl:if>
		<xsl:value-of select ="$ThirdParam"/>
		<xsl:if test ="string-length($ThirdParam)>0 and string-length($FourthParam)>0">
			<xsl:value-of select="$constGost_ColonElementSeparator"/>
		</xsl:if>
		<xsl:value-of select ="$FourthParam"/>
	</xsl:template>

	<xsl:template name ="formatLocationElement">
		
		<xsl:param name="noSL"/>
		<xsl:param name="Location"/>
		<xsl:param name ="Publisher"/>
		<xsl:param name ="Distributor"/>
		
<xsl:variable name="constGost_SineNomine">
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	<xsl:call-template name="templ_str_SineNomineShort"/>
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
	
</xsl:variable>
<xsl:variable name="constGost_SineLoco">
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	<xsl:call-template name="templ_str_SineLocoShort"/>
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
	
</xsl:variable>
		
		
		<xsl:choose>
			<xsl:when test ="string-length($Location)=0 and string-length($Publisher)=0">
				
				<xsl:variable name ="LocationColonElement">
					<xsl:call-template name ="formatColonElement">
						<xsl:with-param name ="FirstParam"/>
						<xsl:with-param name ="SecondParam"/>
						<xsl:with-param name ="ThirdParam" select ="b:Distributor"/>
					</xsl:call-template>
				</xsl:variable>

				<xsl:value-of select ="$LocationColonElement"/>
			</xsl:when>
			<xsl:when test ="string-length($Location)>0 or string-length($Publisher)>0">

				<xsl:variable name ="ColonElementFirstParam">
					<xsl:choose>
						<xsl:when test ="$noSL='yes'"></xsl:when>
						
						<xsl:when test ="string-length($Location)=0">
							
							
							
							
							
							
							
							<xsl:value-of select="$constGost_SineLoco"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select ="$Location"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:variable>

				<xsl:variable name ="ColonElementSecondParam">
					<xsl:choose>
						
						<xsl:when test ="string-length($Publisher)=0">
							
							
							
							
							
							
							
							<xsl:value-of select="$constGost_SineNomine"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select ="$Publisher"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:variable>

				<xsl:variable name ="ColonElementThirdParam">
					<xsl:value-of select ="$Distributor"/>
				</xsl:variable>

				<xsl:variable name ="LocationColonElement">
					<xsl:call-template name ="formatColonElement">
						<xsl:with-param name ="FirstParam" select ="$ColonElementFirstParam"/>
						<xsl:with-param name ="SecondParam" select ="$ColonElementSecondParam"/>
						<xsl:with-param name ="ThirdParam" select ="$ColonElementThirdParam"/>
					</xsl:call-template>
				</xsl:variable>

				<xsl:value-of select ="$LocationColonElement"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="formatHyphenSection">
		<xsl:param name="FirstElement"/>
		<xsl:param name="SecondElement"/>
		
<xsl:variable name="constGost_HyphenSectionHeader">
	<xsl:call-template name="templ_prop_Dot" />
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_FromToDash" />
	<xsl:call-template name="templ_prop_Space" />
	
</xsl:variable>
<xsl:variable name="constGost_HyphenSectionSeparator">
	<xsl:call-template name="templ_prop_ListSeparator" />
	
</xsl:variable>
<xsl:variable name="constGost_HyphenSectionPartsSeparator">
	<xsl:call-template name="templ_prop_ListSeparator" />
	
</xsl:variable>
		
		
		<xsl:if test="not (string-length($FirstElement)=0 and string-length($SecondElement)=0)">
			
			
			
			
			
			<xsl:value-of select="$constGost_HyphenSectionHeader"/>
			<xsl:if test="string-length($FirstElement)>0">
				<xsl:value-of select ="$FirstElement"/>
			</xsl:if>
			<xsl:if test="string-length($SecondElement)>0">
				<xsl:if test ="string-length($FirstElement)>0">
					
					
					
					<xsl:value-of select="$constGost_HyphenSectionPartsSeparator"/>
				</xsl:if>
				<xsl:value-of select ="$SecondElement"/>
			</xsl:if>
		</xsl:if>
	</xsl:template>

	<xsl:template name="formatDateMonthYear">
		<xsl:param name="appendSpace"/>
		<xsl:call-template name="formatDateCore">
			<xsl:with-param name="day">
				<xsl:call-template name="handleSpaces">
					<xsl:with-param name="field" select="b:Day"/>
				</xsl:call-template>
			</xsl:with-param>
			<xsl:with-param name="month">
				<xsl:call-template name="handleSpaces">
					<xsl:with-param name="field" select="b:Month"/>
				</xsl:call-template>
			</xsl:with-param>
			<xsl:with-param name="year">
				<xsl:call-template name="handleSpaces">
					<xsl:with-param name="field" select="b:Year"/>
				</xsl:call-template>
			</xsl:with-param>
			
			<xsl:with-param name="DMY"><xsl:call-template name="templ_prop_Gost_Date_DMY"/></xsl:with-param>
			<xsl:with-param name="DM"><xsl:call-template name="templ_prop_Gost_Date_DM"/></xsl:with-param>
			<xsl:with-param name="MY"><xsl:call-template name="templ_prop_Gost_Date_MY"/></xsl:with-param>
			<xsl:with-param name="DY"><xsl:call-template name="templ_prop_Gost_Date_DY"/></xsl:with-param>
		</xsl:call-template>
	</xsl:template>


	<xsl:template name="formatDateMonthYearAccessed">
		<xsl:param name="appendSpace"/>
		<xsl:call-template name="formatDateCore">
			<xsl:with-param name="day">
				<xsl:call-template name="handleSpaces">
					<xsl:with-param name="field" select="b:DayAccessed"/>
				</xsl:call-template>
			</xsl:with-param>
			<xsl:with-param name="month">
				<xsl:call-template name="handleSpaces">
					<xsl:with-param name="field" select="b:MonthAccessed"/>
				</xsl:call-template>
			</xsl:with-param>
			<xsl:with-param name="year">
				<xsl:call-template name="handleSpaces">
					<xsl:with-param name="field" select="b:YearAccessed"/>
				</xsl:call-template>
			</xsl:with-param>
			
			<xsl:with-param name="DMY"><xsl:call-template name="templ_prop_Gost_Date_DMY"/></xsl:with-param>
			<xsl:with-param name="DM"><xsl:call-template name="templ_prop_Gost_Date_DM"/></xsl:with-param>
			<xsl:with-param name="MY"><xsl:call-template name="templ_prop_Gost_Date_MY"/></xsl:with-param>
			<xsl:with-param name="DY"><xsl:call-template name="templ_prop_Gost_Date_DY"/></xsl:with-param>
		</xsl:call-template>
	</xsl:template>


	<xsl:template name ="formatPrimaryResponsibilities">
		<xsl:param name ="FirstElement"></xsl:param>
		<xsl:param name ="SecondElement"></xsl:param>
		<xsl:param name ="ThirdElement"></xsl:param>
		<xsl:param name ="NonEmptyPrimSectionsCount">2</xsl:param>
		<xsl:param name ="MainSectionsCount">0</xsl:param>

<xsl:variable name="constGost_PrimaryResponsibilitiesOpen">
	<xsl:call-template name="templ_prop_Gost_GeneralOpen" />
	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesClose">
	<xsl:call-template name="templ_prop_Gost_GeneralClose" />
	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesSeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_GroupSeparator" />
	
</xsl:variable>
<xsl:variable name="constGost_PrimaryResponsibilitiesHeader">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_Gost_OneSlash" />
	<xsl:call-template name="templ_prop_Space" />
	
</xsl:variable>


		<xsl:if test ="$NonEmptyPrimSectionsCount - $MainSectionsCount>0">
			
			
			
			
			
			
			<xsl:value-of select="$constGost_PrimaryResponsibilitiesHeader"/>
		</xsl:if>

		
		<xsl:if test ="$NonEmptyPrimSectionsCount - $MainSectionsCount >2">
			
			
			<xsl:value-of select="$constGost_PrimaryResponsibilitiesOpen"/>
		</xsl:if>

		
		<xsl:if test ='string-length($FirstElement)>0'>
			<xsl:value-of select = "$FirstElement"/>
		</xsl:if>


		
		<xsl:if test ="not ($FirstElement ='') and $NonEmptyPrimSectionsCount  - $MainSectionsCount > 1">
			
			
			
			
			
			<xsl:value-of select="$constGost_PrimaryResponsibilitiesSeparator"/>
		</xsl:if>

		
		<xsl:if test ='string-length($SecondElement)>0'>
			<xsl:value-of select = "$SecondElement"/>
		</xsl:if>

		
		<xsl:if test ="($FirstElement ='' and $NonEmptyPrimSectionsCount - $MainSectionsCount >1) or ($NonEmptyPrimSectionsCount - $MainSectionsCount  > 2)">
			
			
			
			
			
			<xsl:value-of select="$constGost_PrimaryResponsibilitiesSeparator"/>
		</xsl:if>

		
		<xsl:if test ='string-length($ThirdElement)>0'>
			<xsl:value-of select = "$ThirdElement"/>
		</xsl:if>

		
		<xsl:if test ="$NonEmptyPrimSectionsCount - $MainSectionsCount >2">
			
			
			<xsl:value-of select="$constGost_PrimaryResponsibilitiesClose"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="format_SemiColonSeparated_Items">
		<xsl:param name="Item1"></xsl:param>
		<xsl:param name="Item2"></xsl:param>
		<xsl:param name="Item3"></xsl:param>

<xsl:variable name="constGost_SemiColonSeparatedItemsSeparator">
	<xsl:call-template name="templ_prop_NonBreakingSpace" />
	<xsl:call-template name="templ_prop_GroupSeparator" />
	
</xsl:variable>


		<xsl:value-of select ="$Item1"/>
		<xsl:if test ="string-length($Item1)>0 and (string-length($Item2)>0 or string-length($Item3) >0)">
			
			
			
			<xsl:value-of select="$constGost_SemiColonSeparatedItemsSeparator"/>
		</xsl:if>
		<xsl:value-of select ="$Item2"/>
		<xsl:if test ="string-length($Item2)>0 and string-length($Item3) >0">
			
			
			
			<xsl:value-of select="$constGost_SemiColonSeparatedItemsSeparator"/>
		</xsl:if>
		<xsl:value-of select ="$Item3"/>
	</xsl:template>

	<xsl:template name ="formatSecondaryResponsibilities">
		<xsl:param name ="CollectionName"></xsl:param>
		<xsl:param name ="FirstElement"></xsl:param>
		<xsl:param name ="SecondElement"></xsl:param>
		<xsl:param name ="ThirdElement"></xsl:param>
    <xsl:param name ="FourthElement"></xsl:param>

    <xsl:if test ="string-length($CollectionName)>0 or string-length($FirstElement)>0 or string-length($SecondElement)>0 or string-length($ThirdElement)>0 or string-length($FourthElement)>0">
			<xsl:choose>
				<xsl:when test ="string-length($CollectionName)>0">
					
					
					
					
					
					<xsl:value-of select="$constGost_CollectionNameHeader"/>
					<xsl:value-of select ="$CollectionName"/>
				</xsl:when>
				<xsl:otherwise>
					
					
					
					
					
					<xsl:value-of select="$constGost_SecondaryResponsibilitiesHeader"/>
				</xsl:otherwise>
			</xsl:choose>

			<xsl:if test ="string-length($CollectionName)>0 and string-length($FirstElement)>0">
				
				
				
				<xsl:value-of select="$constGost_SecondaryResponsibilitiesSeparator"/>
			</xsl:if>
			<xsl:value-of select ="$FirstElement"/>
			<xsl:if test ="(string-length($CollectionName)>0 or string-length($FirstElement)>0) and string-length($SecondElement)>0 ">
				
				
				
				<xsl:value-of select="$constGost_SecondaryResponsibilitiesSeparator"/>
			</xsl:if>
			<xsl:value-of select ="$SecondElement"/>
			<xsl:if test ="(string-length($CollectionName)>0 or string-length($FirstElement)>0 or string-length($SecondElement)>0) and string-length($ThirdElement)>0 ">
				
				
				
				<xsl:value-of select="$constGost_SecondaryResponsibilitiesSeparator"/>
			</xsl:if>
			<xsl:value-of select ="$ThirdElement"/>
      <xsl:if test ="(string-length($CollectionName)>0 or string-length($FirstElement)>0 or string-length($SecondElement)>0 or string-length($ThirdElement)>0) and string-length($FourthElement)>0 ">
        
        
        
        <xsl:value-of select="$constGost_SecondaryResponsibilitiesSeparator"/>
      </xsl:if>
      <xsl:value-of select ="$FourthElement"/>
    </xsl:if>



	</xsl:template>

	<xsl:template name="handleSpaces">
		<xsl:param name="field"/>

    <xsl:variable name="prop_NormalizeSpace">
      <xsl:call-template name="templ_prop_NormalizeSpace"/>
    </xsl:variable>

    <xsl:choose>
			<xsl:when test="$prop_NormalizeSpace='yes'">
				<xsl:value-of select="normalize-space($field)"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$field"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	
	<xsl:template name="need_Dot">
		<xsl:param name="field"/>
		
		<xsl:variable name="temp">
			<xsl:call-template name="handleSpaces">
				<xsl:with-param name="field" select="$field"/>
			</xsl:call-template>
		</xsl:variable>

		<xsl:variable name="lastChar">
			<xsl:value-of select="substring($temp, string-length($temp))"/>
		</xsl:variable>

    <xsl:variable name="prop_EndChars">
      <xsl:call-template name="templ_prop_EndChars"/>
    </xsl:variable>


    <xsl:choose>
			<xsl:when test="string-length($temp) = 0">
			</xsl:when>
			<xsl:when test="contains($prop_EndChars, $lastChar)">
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name="templ_prop_Dot"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	
	


	<xsl:template name="formatNameCore">
		<xsl:param name="FML"/>
		<xsl:param name="FM"/>
		<xsl:param name="ML"/>
		<xsl:param name="FL"/>
		<xsl:param name="upperLast"/>
		<xsl:param name="withDot"/>

		<xsl:variable name="first">
			<xsl:call-template name="handleSpaces">
				<xsl:with-param name="field" select="b:First"/>
			</xsl:call-template>
		</xsl:variable>

		<xsl:variable name="middle">
			<xsl:call-template name="handleSpaces">
				<xsl:with-param name="field" select="b:Middle"/>
			</xsl:call-template>
		</xsl:variable>

		<xsl:variable name="last">
			<xsl:call-template name="handleSpaces">
				<xsl:with-param name="field" select="b:Last"/>
			</xsl:call-template>
		</xsl:variable>
		
		<xsl:variable name="format">
			<xsl:choose>
				<xsl:when test="string-length($first) = 0 and string-length($middle) = 0 and string-length($last) = 0 ">
				</xsl:when>
				<xsl:when test="string-length($first) = 0 and string-length($middle) = 0 and string-length($last) != 0 ">
					<xsl:call-template name="templ_prop_SimpleAuthor_L" />
				</xsl:when>
				<xsl:when test="string-length($first) = 0 and string-length($middle) != 0 and string-length($last) = 0 ">
          <xsl:call-template name="templ_prop_SimpleAuthor_M" />
				</xsl:when>
				<xsl:when test="string-length($first) = 0 and string-length($middle) != 0 and string-length($last) != 0 ">
					<xsl:value-of select="$ML"/>
				</xsl:when>
				<xsl:when test="string-length($first) != 0 and string-length($middle) = 0 and string-length($last) = 0 ">
					<xsl:call-template name="templ_prop_SimpleAuthor_F" />
				</xsl:when>
				<xsl:when test="string-length($first) != 0 and string-length($middle) = 0 and string-length($last) != 0 ">
					<xsl:value-of select="$FL"/>
				</xsl:when>
				<xsl:when test="string-length($first) != 0 and string-length($middle) != 0 and string-length($last) = 0 ">
					<xsl:value-of select="$FM"/>
				</xsl:when>
				<xsl:when test="string-length($first) != 0 and string-length($middle) != 0 and string-length($last) != 0 ">
					<xsl:value-of select="$FML"/>
				</xsl:when>
			</xsl:choose>
		</xsl:variable>
		
		<xsl:call-template name="StringFormatName">
			<xsl:with-param name="format" select="$format"/>
			<xsl:with-param name="upperLast" select="$upperLast"/>
			<xsl:with-param name="withDot" select="$withDot"/>
		</xsl:call-template>
		
	</xsl:template>

	<xsl:template name="formatDateCorePrivate">
		<xsl:param name="DMY"/>
		<xsl:param name="DM"/>
		<xsl:param name="MY"/>
		<xsl:param name="DY"/>

		<xsl:param name="day"/>
		<xsl:param name="month"/>
		<xsl:param name="year"/>
		
		<xsl:param name="withDot"/>
		
		<xsl:variable name="format">
			<xsl:choose>
				<xsl:when test="string-length($day) = 0 and string-length($month) = 0 and string-length($year) = 0 ">
				</xsl:when>
				<xsl:when test="string-length($day) = 0 and string-length($month) = 0 and string-length($year) != 0 ">
					<xsl:call-template name="templ_prop_SimpleDate_Y" />
				</xsl:when>
				<xsl:when test="string-length($day) = 0 and string-length($month) != 0 and string-length($year) = 0 ">
				</xsl:when>
				<xsl:when test="string-length($day) = 0 and string-length($month) != 0 and string-length($year) != 0 ">
					<xsl:value-of select="$MY"/>
				</xsl:when>
				<xsl:when test="string-length($day) != 0 and string-length($month) = 0 and string-length($year) = 0 ">
					<xsl:call-template name="templ_prop_SimpleDate_Y" />
				</xsl:when>
				<xsl:when test="string-length($day) != 0 and string-length($month) = 0 and string-length($year) != 0 ">
					<xsl:call-template name="templ_prop_SimpleDate_Y" />
				</xsl:when>
				<xsl:when test="string-length($day) != 0 and string-length($month) != 0 and string-length($year) = 0 ">
				</xsl:when>
				<xsl:when test="string-length($day) != 0 and string-length($month) != 0 and string-length($year) != 0 ">
					<xsl:value-of select="$DMY"/>
				</xsl:when>
			</xsl:choose>
		</xsl:variable>
		
		<xsl:call-template name="StringFormatDate">
			<xsl:with-param name="format" select="$format"/>

			<xsl:with-param name="day" select="$day"/>
			<xsl:with-param name="month" select="$month"/>
			<xsl:with-param name="year" select="$year"/>

			<xsl:with-param name="withDot" select="$withDot"/>
		</xsl:call-template>
		
	</xsl:template>

	<xsl:template name="StringFormatName">
		<xsl:param name="format" />
		<xsl:param name="withDot" />
		<xsl:param name="upperLast"/>

    <xsl:variable name="prop_EndChars">
      <xsl:call-template name="templ_prop_EndChars"/>
    </xsl:variable>

    <xsl:choose>
			<xsl:when test="$format = ''"></xsl:when>
			<xsl:when test="substring($format, 1, 2) = '%%'">
				<xsl:text>%</xsl:text>
				<xsl:call-template name="StringFormatName">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="withDot" select="$withDot" />
					<xsl:with-param name="upperLast" select="$upperLast" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=2 and withDot = 'yes' and not(contains($prop_EndChars, '%'))">
					<xsl:call-template name="templ_prop_Dot"/>
				</xsl:if>
			</xsl:when>
			<xsl:when test="substring($format, 1, 1) = '%'">
				<xsl:variable name="what" select="substring($format, 2, 1)" />
				
				<xsl:choose>
					<xsl:when test="(what = 'l' or what = 'L') and upperLast = 'yes'">
						<span style='text-transform: uppercase;'>
							<xsl:call-template name="formatNameOneItem">
								<xsl:with-param name="format" select="$what"/>
							</xsl:call-template>
						</span>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name="formatNameOneItem">
							<xsl:with-param name="format" select="$what"/>
						</xsl:call-template>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:call-template name="StringFormatName">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="withDot" select="$withDot" />
					<xsl:with-param name="upperLast" select="$upperLast" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=2 and withDot='yes'">
					<xsl:variable name="temp2">
						<xsl:call-template name="handleSpaces">
							<xsl:with-param name="field">
								<xsl:call-template name="formatNameOneItem">
									<xsl:with-param name="format" select="$what"/>
								</xsl:call-template>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:variable>				
					<xsl:variable name="lastChar">
						<xsl:value-of select="substring($temp2, string-length($temp2))"/>
					</xsl:variable>
					<xsl:if test="not(contains($prop_EndChars, $lastChar))">
						<xsl:call-template name="templ_prop_Dot"/>
					</xsl:if>
				</xsl:if>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($format, 1, 1)" />
				<xsl:call-template name="StringFormatName">
					<xsl:with-param name="format" select="substring($format, 2)" />
					<xsl:with-param name="withDot" select="$withDot" />
					<xsl:with-param name="upperLast" select="$upperLast" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=1">
					<xsl:if test="withDot = 'yes' and not(contains($prop_EndChars, $format))">
						<xsl:call-template name="templ_prop_Dot"/>
					</xsl:if>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>	

	<xsl:template name="StringFormatDate">
		<xsl:param name="format" />
		
		<xsl:param name="day"/>
		<xsl:param name="month"/>
		<xsl:param name="year"/>		
		
		<xsl:param name="withDot" />

    <xsl:variable name="prop_EndChars">
      <xsl:call-template name="templ_prop_EndChars"/>
    </xsl:variable>

    <xsl:choose>
			<xsl:when test="$format = ''"></xsl:when>
			<xsl:when test="substring($format, 1, 2) = '%%'">
				<xsl:text>%</xsl:text>
				<xsl:call-template name="StringFormatDate">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="day" select="$day"/>
					<xsl:with-param name="month" select="$month"/>
					<xsl:with-param name="year" select="$year"/>
					<xsl:with-param name="withDot" select="$withDot" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=2 and withDot = 'yes' and not(contains($prop_EndChars, '%'))">
					<xsl:call-template name="templ_prop_Dot"/>
				</xsl:if>
			</xsl:when>
			<xsl:when test="substring($format, 1, 1) = '%'">
				<xsl:variable name="what" select="substring($format, 2, 1)" />
				<xsl:choose>
					<xsl:when test="$what = 'D'">
						<xsl:value-of select="$day"/>
					</xsl:when>
					<xsl:when test="$what = 'M'">
						<xsl:value-of select="$month"/>
					</xsl:when>
					<xsl:when test="$what = 'Y'">
						<xsl:value-of select="$year"/>
					</xsl:when>
				</xsl:choose>
				<xsl:call-template name="StringFormatDate">
					<xsl:with-param name="format" select="substring($format, 3)" />
					<xsl:with-param name="day" select="$day"/>
					<xsl:with-param name="month" select="$month"/>
					<xsl:with-param name="year" select="$year"/>
					<xsl:with-param name="withDot" select="$withDot" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=2 and withDot='yes'">
					<xsl:variable name="temp2">
						<xsl:call-template name="handleSpaces">
							<xsl:with-param name="field">
								<xsl:call-template name="formatNameOneItem">
									<xsl:with-param name="format" select="$what"/>
								</xsl:call-template>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:variable>				
					<xsl:variable name="lastChar">
						<xsl:value-of select="substring($temp2, string-length($temp2))"/>
					</xsl:variable>
					<xsl:if test="not(contains($prop_EndChars, $lastChar))">
						<xsl:call-template name="templ_prop_Dot"/>
					</xsl:if>
				</xsl:if>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($format, 1, 1)" />
				<xsl:call-template name="StringFormatDate">
					<xsl:with-param name="format" select="substring($format, 2)" />
					<xsl:with-param name="day" select="$day"/>
					<xsl:with-param name="month" select="$month"/>
					<xsl:with-param name="year" select="$year"/>
					<xsl:with-param name="withDot" select="$withDot" />
				</xsl:call-template>
				<xsl:if test="string-length($format)=1">
					<xsl:if test="withDot = 'yes' and not(contains($prop_EndChars, $format))">
						<xsl:call-template name="templ_prop_Dot"/>
					</xsl:if>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>	
	<xsl:template name="formatDateCore">
		<xsl:param name="day"/>
		<xsl:param name="month"/>
		<xsl:param name="year"/>
		<xsl:param name="displayND"/>
		
		<xsl:param name="DMY"/>
		<xsl:param name="DM"/>
		<xsl:param name="MY"/>
		<xsl:param name="DY"/>
	
		<xsl:choose>
			<xsl:when test="string-length($year)=0">
				<xsl:if test="$displayND = 'yes'">
					<xsl:call-template name="templ_str_NoDateShortUnCap"/>
				</xsl:if>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name="formatDateCorePrivate">
					<xsl:with-param name="day" select="$day"/>
					<xsl:with-param name="month" select="$month"/>
					<xsl:with-param name="year" select="$year"/>
					
					<xsl:with-param name="DMY" select="$DMY"/>
					<xsl:with-param name="DM" select="$DM"/>
					<xsl:with-param name="MY" select="$MY"/>
					<xsl:with-param name="DY" select="$DY"/>
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
	
	</xsl:template>

	<xsl:template name="formatNameOneItem">
		<xsl:param name="format"/>

		<xsl:choose>
			<xsl:when test="$format = 'F'">
				<xsl:value-of select="b:First"/>
			</xsl:when>
			<xsl:when test="$format = 'L'">
				<xsl:value-of select="b:Last"/>
			</xsl:when>
			<xsl:when test="$format = 'M'">
				<xsl:value-of select="b:Middle"/>
			</xsl:when>
			<xsl:when test="$format = 'f'">
				<xsl:call-template name="formatNameInitial">
					<xsl:with-param name="name" select="b:First"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$format = 'm'">
				<xsl:call-template name="formatNameInitial">
					<xsl:with-param name="name" select="b:Middle"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:when test="$format = 'l'">
				<xsl:call-template name="formatNameInitial">
					<xsl:with-param name="name" select="b:Last"/>
				</xsl:call-template>
			</xsl:when>
		</xsl:choose>

	</xsl:template>

	<xsl:template name="formatNameInitial">
		<xsl:param name="name"/>
		<xsl:variable name="temp">
			<xsl:call-template name="handleSpaces">
				<xsl:with-param name="field" select="$name"/>
			</xsl:call-template>
		</xsl:variable>

    <xsl:variable name="prop_APA_Hyphens">
      <xsl:call-template name="templ_prop_Hyphens"/>
    </xsl:variable>

    <xsl:if test="string-length($temp)>0">

			<xsl:variable name="tempWithoutSpaces">
				<xsl:value-of select="translate($temp, '&#32;&#160;', '')"/>
			</xsl:variable>

			<xsl:if test="not(contains($prop_APA_Hyphens, substring($tempWithoutSpaces, 1, 1)))">
				<xsl:value-of select="substring($tempWithoutSpaces, 1, 1)"/>
				<xsl:call-template name="templ_prop_DotInitial"/>
			</xsl:if>

			<xsl:call-template name="handleHyphens">
				<xsl:with-param name="name" select="$tempWithoutSpaces"/>
			</xsl:call-template>
		</xsl:if>
	</xsl:template>

	<xsl:template name="handleHyphens">
		<xsl:param name="name"/>

    <xsl:variable name="prop_APA_Hyphens">
      <xsl:call-template name="templ_prop_Hyphens"/>
    </xsl:variable>

    <xsl:if test="string-length($name)>=2">
			<xsl:choose>
				<xsl:when test="contains($prop_APA_Hyphens, substring($name, 1, 1))">
					<xsl:value-of select="substring($name, 1, 2)"/>
					<xsl:call-template name="templ_prop_DotInitial"/>
					
					<xsl:call-template name="handleHyphens">
						<xsl:with-param name="name" select="substring($name, 3)"/>
					</xsl:call-template>
				</xsl:when>
				
				<xsl:otherwise>
					<xsl:call-template name="handleHyphens">
						<xsl:with-param name="name" select="substring($name, 2)"/>
					</xsl:call-template>
				</xsl:otherwise>
			</xsl:choose>
			
		</xsl:if>

	</xsl:template>

	
</xsl:stylesheet>

