<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt"
				xmlns:b="http://schemas.openxmlformats.org/officeDocument/2006/bibliography" xmlns:t="http://www.microsoft.com/temp">

	<xsl:output method="html" encoding="us-ascii"/>

	<xsl:template match="/">
		<xsl:call-template name="Start"/>
	</xsl:template>

	<xsl:template name="Start">
		<xsl:choose>
			<xsl:when test="b:Version">
				<xsl:text>2010.2.02</xsl:text>
			</xsl:when>

			<xsl:when test="b:XslVersion">
				<xsl:text>2008</xsl:text>
			</xsl:when>

      <xsl:when test="b:StyleNameLocalized">
        <xsl:choose>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1033'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1025'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1037'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1041'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2052'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1028'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1042'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1036'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1040'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='3082'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1043'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1031'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1046'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1049'">
            <xsl:text>Harvard — Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1035'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1032'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1081'">
            <xsl:text>हार्वर्ड - एंग्लिया</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1054'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1057'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1086'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1066'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1053'">
            <xsl:text>Harvard – Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1069'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1027'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1030'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1110'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1044'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1061'">
            <xsl:text>Harvard ‒ Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1062'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1063'">
            <xsl:text>Harvardas – Anglija</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1045'">
            <xsl:text>Harvard — Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2070'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1029'">
            <xsl:text>Harvard – Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1055'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1038'">
            <xsl:text>Harvard — Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1048'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1058'">
            <xsl:text>Гарвард – Англія</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1026'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1050'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1087'">
            <xsl:text>Гарвард-Англия мәнері</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2074'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='3098'">
            <xsl:text>Harvard - Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1051'">
            <xsl:text>Harvard – Anglia</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1060'">
            <xsl:text>Harvardski način citiranja</xsl:text>
          </xsl:when>
        </xsl:choose>
      </xsl:when>
      
			<xsl:when test="b:category">
				<xsl:text>From Office Online</xsl:text>
			</xsl:when>
			<xsl:when test="b:GetImportantFields">
				<b:ImportantFields>
					<xsl:choose>
						<xsl:when test="b:GetImportantFields/b:SourceType='Book'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Publisher</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Edition</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='BookSection'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Publisher</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Author/b:Editor/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:BookTitle</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Pages</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='JournalArticle'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:JournalName</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Volume</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Issue</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Pages</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='ArticleInAPeriodical'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:PeriodicalTitle</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Month</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Day</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Pages</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='ConferenceProceedings'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Publisher</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Report'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Publisher</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='SoundRecording'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Composer/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:ProductionCompany</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Performance'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Writer/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:ProductionCompany</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Art'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Artist/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Institution</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='DocumentFromInternetSite'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Month</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Day</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:URL</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:YearAccessed</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:MonthAccessed</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:DayAccessed</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='InternetSite'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:URL</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:YearAccessed</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:MonthAccessed</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:DayAccessed</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Film'">
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Author/b:Director/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:CountryRegion</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:ProductionCompany</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Interview'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Interviewee/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Month</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Day</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Patent'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Inventor/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:PatentNumber</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:CountryRegion</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='ElectronicSource'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Publisher</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Case'">
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Reporter</xsl:text>
							</b:ImportantField>
						</xsl:when>

						<xsl:when test="b:GetImportantFields/b:SourceType='Misc'">
							<b:ImportantField>
								<xsl:text>b:Author/b:Author/b:NameList</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Year</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Title</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:City</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Publisher</xsl:text>
							</b:ImportantField>
						</xsl:when>
					</xsl:choose>
				</b:ImportantFields>
			</xsl:when>
			<xsl:when test="b:Bibliography">
				<xsl:call-template name="Bibliography"/>
			</xsl:when>
			<xsl:when test="b:Citation">
				<xsl:call-template name="Citation"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="Entry">
		<xsl:call-template name="Start"/>
	</xsl:template>



	<xsl:template match="*">
		<xsl:element name="{name()}" namespace="{namespace-uri()}">
			<xsl:for-each select="@*">
				<xsl:attribute name="{name()}" namespace="{namespace-uri()}">
					<xsl:value-of select="."/>
				</xsl:attribute>
			</xsl:for-each>
			<xsl:apply-templates>
				<xsl:sort select="b:SortingString" />
			</xsl:apply-templates>
		</xsl:element>
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

	<xsl:template name ="templ_str_UnCapEditorsShort">
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:UnCapEditorsShort"/>
	</xsl:template>

	<xsl:template name="templ_str_Film" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SourceNames/b:Film"/>
	</xsl:template>

	<xsl:template name="templ_str_AccessedCap" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:AccessedCap"/>
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

	<xsl:template name="templ_str_OnAlbumTitleCap" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:OnAlbumTitleCap"/>
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

	<xsl:template name="templ_str_ArtCap" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SourceNames/b:Art"/>
	</xsl:template>

	<xsl:template name="templ_str_SoundRecordingCap" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:SourceNames/b:SoundRecording"/>
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

	<xsl:template name="templ_prop_SecondaryOpen" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryOpen"/>
	</xsl:template>

	<xsl:template name="templ_prop_SecondaryClose" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:SecondaryClose"/>
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

	<xsl:template name="templ_prop_NoItalics" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:NoItalics"/>
	</xsl:template>

	<xsl:template name="templ_prop_TitleOpen" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:TitleOpen"/>
	</xsl:template>

	<xsl:template name="templ_prop_TitleClose" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:General/b:TitleClose"/>
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

	<xsl:template name="templ_prop_BeforeLastAuthor" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:APA/b:BeforeLastAuthor"/>
	</xsl:template>

	<xsl:template name="FindReplaceString">
		<xsl:param name="originalString"/>
		<xsl:param name="stringToBeReplaced"/>
		<xsl:param name="stringReplacement"/>
		<xsl:choose>
			<xsl:when test="contains($originalString,$stringToBeReplaced)">
				<xsl:value-of select="concat(substring-before($originalString,$stringToBeReplaced),$stringReplacement)"/>
				<xsl:call-template name="FindReplaceString">
					<xsl:with-param name="originalString" select="substring-after($originalString,$stringToBeReplaced)"/>
					<xsl:with-param name="stringToBeReplaced" select="$stringToBeReplaced"/>
					<xsl:with-param name="stringReplacement" select="$stringReplacement"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$originalString"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="DisplayPageOrPages">
		<xsl:param name ="pages"/>
		<xsl:choose>
			<xsl:when test="contains($pages, '-')">
				<xsl:value-of select="concat('pp. ', $pages)"/>
			</xsl:when>
			<xsl:when test="contains($pages, ',')">
				<xsl:value-of select="concat('pp. ', $pages)"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="concat('p. ', $pages)"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibAddParagraphAttributes">
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
	</xsl:template>

	<xsl:template name ="BibDisplayStrOnline">
		<xsl:variable name="cURL">
			<xsl:value-of select="count(b:URL)"/>
		</xsl:variable>
		<xsl:variable name="cYearAccessed">
			<xsl:value-of select="count(b:YearAccessed)"/>
		</xsl:variable>
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_OnlineCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:choose>
			<xsl:when test="$cURL!=0 or $cYearAccessed!=0">
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayStrFilm">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_Film"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayStrArt">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_ArtCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>

	</xsl:template>

	<xsl:template name ="BibDisplayStrSoundRecording">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_SoundRecordingCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:choose>
			<xsl:when test="$cProductionCompany=0">
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayStrInterview">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_InterviewCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayDirector">
		<xsl:variable name="cDirector">
			<xsl:value-of select="count(b:Author/b:Director/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name ="directorName">
			<xsl:choose>
				<xsl:when test="$cDirector = 1">
					<xsl:variable name ="cDirectorFirstName">
						<xsl:value-of select ="count(b:Author/b:Director/b:NameList/b:Person/b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cDirectorLastName">
						<xsl:value-of select ="count(b:Author/b:Director/b:NameList/b:Person/b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cDirectorMiddleName">
						<xsl:value-of select ="count(b:Author/b:Director/b:NameList/b:Person/b:Middle)"/>
					</xsl:variable>

					<xsl:choose>
						<xsl:when test="$cDirectorFirstName=1">
							<xsl:value-of select="b:Author/b:Director/b:NameList/b:Person/b:First"/>
							<xsl:choose>
								<xsl:when test ="$cDirectorLastName=1 or $cDirectorMiddleName=1">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cDirectorLastName=0 and $cDirectorMiddleName=0">
									<xsl:call-template name ="templ_prop_Dot"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cDirectorMiddleName=1">
							<xsl:value-of select="b:Author/b:Director/b:NameList/b:Person/b:Middle"/>
							<xsl:choose>
								<xsl:when test ="$cDirectorLastName=1">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_Dot"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cDirectorLastName=1">
							<xsl:value-of select="b:Author/b:Director/b:NameList/b:Person/b:Last"/>
							<xsl:call-template name ="templ_prop_Dot"/>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:when>
					</xsl:choose>
				</xsl:when>

				<xsl:when test ="$cDirector>1">
					<xsl:for-each select="b:Author/b:Director/b:NameList/b:Person">
						<xsl:variable name ="cDirectorFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cDirectorLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cDirectorMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>

						<xsl:choose>
							<xsl:when test="$cDirectorFirstName=1">
								<xsl:value-of select="b:First"/>
								<xsl:choose>
									<xsl:when test ="$cDirectorLastName=1 or $cDirectorMiddleName=1">
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:when test ="$cDirectorLastName=0 and $cDirectorMiddleName=0">
										<xsl:choose>
											<xsl:when test="position()!=$cDirector">
												<xsl:call-template name ="templ_prop_ListSeparator"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name ="templ_prop_Dot"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>

						<xsl:choose>
							<xsl:when test="$cDirectorMiddleName=1">
								<xsl:value-of select="b:Middle"/>
								<xsl:choose>
									<xsl:when test ="$cDirectorLastName=1">
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:choose>
											<xsl:when test="position()!=$cDirector">
												<xsl:call-template name ="templ_prop_ListSeparator"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name ="templ_prop_Dot"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>

						<xsl:choose>
							<xsl:when test="$cDirectorLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:choose>
									<xsl:when test="position()!=$cDirector">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Dot"/>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
				</xsl:when>
			</xsl:choose>
		</xsl:variable>

		<xsl:variable name="directedBy">
			<xsl:call-template name ="templ_str_DirectedByCap"/>
		</xsl:variable>

		<xsl:if test="$directorName!=''">
			<xsl:call-template name ="FindReplaceString">
				<xsl:with-param name="originalString" select="$directedBy"/>
				<xsl:with-param name="stringToBeReplaced" select="'%1'"/>
				<xsl:with-param name="stringReplacement" select="$directorName"/>
			</xsl:call-template>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayCountryRegionPatent">
		<xsl:variable name="cCountryRegion">
			<xsl:value-of select="count(b:CountryRegion)"/>
		</xsl:variable>
		<xsl:variable name="cpatentNumber">
			<xsl:value-of select="count(b:PatentNumber)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCountryRegion!=0">
				<xsl:value-of select="b:CountryRegion"/>
				<xsl:choose>
					<xsl:when test="$cpatentNumber!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayPatentNumber">
		<xsl:variable name="cpatentNumber">
			<xsl:value-of select="count(b:PatentNumber)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cpatentNumber!=0">
				<xsl:variable name="directedBy">
					<xsl:call-template name="templ_str_PatentNumberShortCap"/>
				</xsl:variable>
				<xsl:call-template name ="FindReplaceString">
					<xsl:with-param name="originalString" select="$directedBy"/>
					<xsl:with-param name="stringToBeReplaced" select="'%1'"/>
					<xsl:with-param name="stringReplacement" select="b:PatentNumber"/>
				</xsl:call-template>
				<xsl:call-template name = "templ_prop_Dot"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>


	<xsl:template name ="BibDisplayCountryRegion">
		<xsl:variable name="cCountryRegion">
			<xsl:value-of select="count(b:CountryRegion)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCountryRegion!=0">
				<xsl:value-of select="b:CountryRegion"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:call-template name ="templ_prop_EnumSeparator"/>
	</xsl:template>

	<xsl:template name ="BibDisplayReporter">
		<xsl:variable name="cReporter">
			<xsl:value-of select="count(b:Reporter)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cReporter!=0">
				<xsl:value-of select="b:Reporter"/>
				<xsl:call-template name = "templ_prop_Dot"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompanySRec">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:call-template name ="templ_prop_OpenBracket"/>
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:call-template name ="templ_prop_CloseBracket"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompanyPerformance">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
			</xsl:otherwise>
		</xsl:choose>

		<xsl:call-template name ="templ_prop_EnumSeparator"/>

		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineNomineShort"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompany">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineNomineShort"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayEditor">
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cAuthor">
			<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCorpAuthor">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:if test ="$cAuthor>0 or $cCorpAuthor>0">
			<xsl:choose>
				<xsl:when test="$cEditor = 1">
					<xsl:variable name ="cEditorFirstName">
						<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person/b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cEditorLastName">
						<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person/b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cEditorMiddleName">
						<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person/b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cEditorFirstName=1">
							<xsl:call-template name="splitAuthorSpace">
								<xsl:with-param name ="first">
									<xsl:call-template name="right-trim">
										<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:First"/>
									</xsl:call-template>
								</xsl:with-param>
							</xsl:call-template>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cEditorMiddleName=1">
							<xsl:call-template name="splitAuthorSpace">
								<xsl:with-param name ="first">
									<xsl:call-template name="right-trim">
										<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:Middle"/>
									</xsl:call-template>
								</xsl:with-param>
							</xsl:call-template>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cEditorLastName=1">
							<xsl:value-of select="b:Author/b:Editor/b:NameList/b:Person/b:Last"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
					</xsl:choose>

					<xsl:call-template name ="templ_str_EditorShortUnCap"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:when test="$cEditor>1 and 5>$cEditor">
					<xsl:for-each select="b:Author/b:Editor/b:NameList/b:Person">
						<xsl:variable name ="cEditorFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cEditorLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cEditorMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>

						<xsl:choose>
							<xsl:when test="$cEditorFirstName=1">
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:choose>
									<xsl:when test ="$cEditorMiddleName=0 and $cEditorLastName=0 and $cEditor>1 and (position()+1)=$cEditor">
										<xsl:call-template name ="templ_prop_Space"/>
										<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:when test ="$cEditorMiddleName=0 and $cEditorLastName=0">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cEditorMiddleName=1">
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:choose>
									<xsl:when test ="$cEditorLastName=0 and $cEditor>1 and (position()+1)=$cEditor">
										<xsl:call-template name ="templ_prop_Space"/>
										<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:when test ="$cEditorLastName=0">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cEditorLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:choose>
									<xsl:when test ="$cEditor>1 and (position()+1)=$cEditor">
										<xsl:call-template name ="templ_prop_Space"/>
										<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:call-template name ="templ_str_UnCapEditorsShort"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:for-each select="b:Author/b:Editor/b:NameList/b:Person">
						<xsl:if test="position()=1">
							<xsl:variable name ="cEditorFirstName">
								<xsl:value-of select ="count(b:First)"/>
							</xsl:variable>
							<xsl:variable name ="cEditorLastName">
								<xsl:value-of select ="count(b:Last)"/>
							</xsl:variable>
							<xsl:variable name ="cEditorMiddleName">
								<xsl:value-of select ="count(b:Middle)"/>
							</xsl:variable>
							<xsl:choose>
								<xsl:when test="$cEditorFirstName=1">
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test="$cEditorMiddleName=1">
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test="$cEditorLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
							</xsl:choose>
							<xsl:call-template name ="templ_str_AndOthersUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_UnCapEditorsShort"/>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:if>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayEditorNL">
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="$cEditor = 1">
				<xsl:variable name ="cEditorFirstName">
					<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person/b:First)"/>
				</xsl:variable>
				<xsl:variable name ="cEditorLastName">
					<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person/b:Last)"/>
				</xsl:variable>
				<xsl:variable name ="cEditorMiddleName">
					<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person/b:Middle)"/>
				</xsl:variable>
				<xsl:choose>
					<xsl:when test="$cEditorLastName=1">
						<xsl:value-of select="b:Author/b:Editor/b:NameList/b:Person/b:Last"/>
						<xsl:choose>
							<xsl:when test ="$cEditorMiddleName=1 or $cEditorFirstName=1">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cEditorFirstName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Editor/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test ="$cEditorMiddleName=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:when test ="$cEditorMiddleName!=0">
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cEditorMiddleName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Editor/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
				</xsl:choose>
				<xsl:call-template name ="templ_str_EditorShortUnCap"/>
			</xsl:when>
			<xsl:when test="$cEditor>1 and 5>$cEditor">
				<xsl:for-each select="b:Author/b:Editor/b:NameList/b:Person">
					<xsl:variable name ="cEditorFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cEditorLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cEditorMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cEditorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test ="$cEditorMiddleName=0 and $cEditorLastName=0 and $cEditor>1 and (position()+1)=$cEditor">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cEditorFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cEditorMiddleName=0 and $cEditor>1 and (position()+1)=$cEditor">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cEditorMiddleName=0">
									<xsl:choose>
										<xsl:when test="position()!=$cEditor">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cEditorMiddleName=1">
							<xsl:choose>
								<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cEditor>1 and (position()+1)=$cEditor">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="position()!=$cEditor">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:call-template name ="templ_str_UnCapEditorsShort"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="b:Author/b:Editor/b:NameList/b:Person">
					<xsl:if test="position()=1">
						<xsl:variable name ="cEditorFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cEditorLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cEditorMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>

						<xsl:choose>
							<xsl:when test="$cEditorLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>

						<xsl:choose>
							<xsl:when test="$cEditorFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>

						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cEditorMiddleName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>

						<xsl:call-template name ="templ_str_AndOthersUnCap"/>
						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:call-template name ="templ_str_UnCapEditorsShort"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayAuthorSoundRec">
		<xsl:variable name="cComposer">
			<xsl:value-of select="count(b:Author/b:Composer/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cConductor">
			<xsl:value-of select="count(b:Author/b:Conductor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cPerformer">
			<xsl:value-of select="count(b:Author/b:Performer/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Performer/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="$cComposer!=0">
				<xsl:choose>
					<xsl:when test ="$cComposer=0">
						<xsl:choose>
							<xsl:when test="$cCorporateAuthors=0">
								<xsl:value-of select="'Anon., '"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="b:Author/b:Performer/b:Corporate"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:when test="$cComposer>0 and 5>$cComposer">
						<xsl:for-each select="b:Author/b:Composer/b:NameList/b:Person">
							<xsl:variable name ="cComposerFirstName">
								<xsl:value-of select ="count(b:First)"/>
							</xsl:variable>
							<xsl:variable name ="cComposerLastName">
								<xsl:value-of select ="count(b:Last)"/>
							</xsl:variable>
							<xsl:variable name ="cComposerMiddleName">
								<xsl:value-of select ="count(b:Middle)"/>
							</xsl:variable>
							<xsl:choose>
								<xsl:when test="$cComposerLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:choose>
										<xsl:when test ="$cComposerFirstName=0 and $cComposerMiddleName=0 and $cComposer>1 and (position()+1)=$cComposer">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test="$cComposerFirstName=1">
									<xsl:choose>
										<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
											<xsl:call-template name="HandleSPaceHypenInAuthor">
												<xsl:with-param name="author">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:First"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name="splitAuthorSpace">
												<xsl:with-param name ="first">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:First"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:choose>
										<xsl:when test ="$cComposerMiddleName=0 and $cComposer>1 and (position()+1)=$cComposer">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:when test ="$cComposerMiddleName=0">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:when test ="$cComposerMiddleName!=0">
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test="$cComposerMiddleName=1">
									<xsl:choose>
										<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
											<xsl:call-template name="HandleSPaceHypenInAuthor">
												<xsl:with-param name="author">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:Middle"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name="splitAuthorSpace">
												<xsl:with-param name ="first">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:Middle"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:otherwise>
									</xsl:choose>

									<xsl:choose>
										<xsl:when test ="$cComposer>1 and (position()+1)=$cComposer">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>
						</xsl:for-each>
					</xsl:when>
					<xsl:otherwise>
						<xsl:for-each select="b:Author/b:Composer/b:NameList/b:Person">
							<xsl:if test="position()=1">
								<xsl:variable name ="cComposerFirstName">
									<xsl:value-of select ="count(b:First)"/>
								</xsl:variable>
								<xsl:variable name ="cComposerLastName">
									<xsl:value-of select ="count(b:Last)"/>
								</xsl:variable>
								<xsl:variable name ="cComposerMiddleName">
									<xsl:value-of select ="count(b:Middle)"/>
								</xsl:variable>
								<xsl:choose>
									<xsl:when test="$cComposerLastName=1">
										<xsl:value-of select="b:Last"/>
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
								</xsl:choose>
								<xsl:choose>
									<xsl:when test="$cComposerFirstName=1">
										<xsl:choose>
											<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
												<xsl:call-template name="HandleSPaceHypenInAuthor">
													<xsl:with-param name="author">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:First"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name="splitAuthorSpace">
													<xsl:with-param name ="first">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:First"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
								<xsl:choose>
									<xsl:when test="$cComposerMiddleName=1">
										<xsl:choose>
											<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
												<xsl:call-template name="HandleSPaceHypenInAuthor">
													<xsl:with-param name="author">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:Middle"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name="splitAuthorSpace">
													<xsl:with-param name ="first">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:Middle"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
								<xsl:call-template name ="templ_str_AndOthersUnCap"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:for-each>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$cConductor!=0">
				<xsl:choose>
					<xsl:when test ="$cConductor=0">
						<xsl:choose>
							<xsl:when test="$cCorporateAuthors=0">
								<xsl:value-of select="'Anon., '"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="b:Author/b:Performer/b:Corporate"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:when test="$cConductor>0 and 5>$cConductor">
						<xsl:for-each select="b:Author/b:Conductor/b:NameList/b:Person">
							<xsl:variable name ="cConductorFirstName">
								<xsl:value-of select ="count(b:First)"/>
							</xsl:variable>
							<xsl:variable name ="cConductorLastName">
								<xsl:value-of select ="count(b:Last)"/>
							</xsl:variable>
							<xsl:variable name ="cConductorMiddleName">
								<xsl:value-of select ="count(b:Middle)"/>
							</xsl:variable>
							<xsl:choose>
								<xsl:when test="$cConductorLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:choose>
										<xsl:when test ="$cConductorFirstName=0 and $cConductorMiddleName=0 and $cConductor>1 and (position()+1)=$cConductor">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test="$cConductorFirstName=1">
									<xsl:choose>
										<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
											<xsl:call-template name="HandleSPaceHypenInAuthor">
												<xsl:with-param name="author">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:First"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name="splitAuthorSpace">
												<xsl:with-param name ="first">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:First"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:choose>
										<xsl:when test ="$cConductorMiddleName=0 and $cConductor>1 and (position()+1)=$cConductor">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:when test ="$cConductorMiddleName=0">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:when test ="$cConductorMiddleName!=0">
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test="$cConductorMiddleName=1">
									<xsl:choose>
										<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
											<xsl:call-template name="HandleSPaceHypenInAuthor">
												<xsl:with-param name="author">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:Middle"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name="splitAuthorSpace">
												<xsl:with-param name ="first">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:Middle"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:choose>
										<xsl:when test ="$cConductor>1 and (position()+1)=$cConductor">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>
						</xsl:for-each>
					</xsl:when>
					<xsl:otherwise>
						<xsl:for-each select="b:Author/b:Conductor/b:NameList/b:Person">
							<xsl:if test="position()=1">
								<xsl:variable name ="cConductorFirstName">
									<xsl:value-of select ="count(b:First)"/>
								</xsl:variable>
								<xsl:variable name ="cConductorLastName">
									<xsl:value-of select ="count(b:Last)"/>
								</xsl:variable>
								<xsl:variable name ="cConductorMiddleName">
									<xsl:value-of select ="count(b:Middle)"/>
								</xsl:variable>
								<xsl:choose>
									<xsl:when test="$cConductorLastName=1">
										<xsl:value-of select="b:Last"/>
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
								</xsl:choose>
								<xsl:choose>
									<xsl:when test="$cConductorFirstName=1">
										<xsl:choose>
											<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
												<xsl:call-template name="HandleSPaceHypenInAuthor">
													<xsl:with-param name="author">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:First"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name="splitAuthorSpace">
													<xsl:with-param name ="first">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:First"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
								<xsl:choose>
									<xsl:when test="$cConductorMiddleName=1">
										<xsl:choose>
											<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
												<xsl:call-template name="HandleSPaceHypenInAuthor">
													<xsl:with-param name="author">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:Middle"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name="splitAuthorSpace">
													<xsl:with-param name ="first">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:Middle"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
								<xsl:call-template name ="templ_str_AndOthersUnCap"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:for-each>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$cPerformer!=0">
				<xsl:choose>
					<xsl:when test ="$cPerformer=0">
						<xsl:choose>
							<xsl:when test="$cCorporateAuthors=0">
								<xsl:value-of select="'Anon., '"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="b:Author/b:Performer/b:Corporate"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:when test="$cPerformer>0 and 5>$cPerformer">
						<xsl:for-each select="b:Author/b:Performer/b:NameList/b:Person">
							<xsl:variable name ="cPerformerFirstName">
								<xsl:value-of select ="count(b:First)"/>
							</xsl:variable>
							<xsl:variable name ="cPerformerLastName">
								<xsl:value-of select ="count(b:Last)"/>
							</xsl:variable>
							<xsl:variable name ="cPerformerMiddleName">
								<xsl:value-of select ="count(b:Middle)"/>
							</xsl:variable>
							<xsl:choose>
								<xsl:when test="$cPerformerLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:choose>
										<xsl:when test ="$cPerformerFirstName=0 and $cPerformerMiddleName=0 and $cPerformer>1 and (position()+1)=$cPerformer">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test="$cPerformerFirstName=1">
									<xsl:choose>
										<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
											<xsl:call-template name="HandleSPaceHypenInAuthor">
												<xsl:with-param name="author">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:First"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name="splitAuthorSpace">
												<xsl:with-param name ="first">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:First"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:choose>
										<xsl:when test ="$cPerformerMiddleName=0 and $cPerformer>1 and (position()+1)=$cPerformer">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:when test ="$cPerformerMiddleName=0">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:when test ="$cPerformerMiddleName!=0">
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test="$cPerformerMiddleName=1">
									<xsl:choose>
										<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
											<xsl:call-template name="HandleSPaceHypenInAuthor">
												<xsl:with-param name="author">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:Middle"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name="splitAuthorSpace">
												<xsl:with-param name ="first">
													<xsl:call-template name="right-trim">
														<xsl:with-param name ="s" select="b:Middle"/>
													</xsl:call-template>
												</xsl:with-param>
											</xsl:call-template>
										</xsl:otherwise>
									</xsl:choose>

									<xsl:choose>
										<xsl:when test ="$cPerformer>1 and (position()+1)=$cPerformer">
											<xsl:call-template name ="templ_prop_Space"/>
											<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
											<xsl:call-template name ="templ_prop_Space"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
							</xsl:choose>
						</xsl:for-each>
					</xsl:when>
					<xsl:otherwise>
						<xsl:for-each select="b:Author/b:Performer/b:NameList/b:Person">
							<xsl:if test="position()=1">
								<xsl:variable name ="cPerformerFirstName">
									<xsl:value-of select ="count(b:First)"/>
								</xsl:variable>
								<xsl:variable name ="cPerformerLastName">
									<xsl:value-of select ="count(b:Last)"/>
								</xsl:variable>
								<xsl:variable name ="cPerformerMiddleName">
									<xsl:value-of select ="count(b:Middle)"/>
								</xsl:variable>
								<xsl:choose>
									<xsl:when test="$cPerformerLastName=1">
										<xsl:value-of select="b:Last"/>
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
								</xsl:choose>
								<xsl:choose>
									<xsl:when test="$cPerformerFirstName=1">
										<xsl:choose>
											<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
												<xsl:call-template name="HandleSPaceHypenInAuthor">
													<xsl:with-param name="author">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:First"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name="splitAuthorSpace">
													<xsl:with-param name ="first">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:First"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
								<xsl:choose>
									<xsl:when test="$cPerformerMiddleName=1">
										<xsl:choose>
											<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
												<xsl:call-template name="HandleSPaceHypenInAuthor">
													<xsl:with-param name="autho">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:Middle"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:call-template name="splitAuthorSpace">
													<xsl:with-param name ="first">
														<xsl:call-template name="right-trim">
															<xsl:with-param name ="s" select="b:Middle"/>
														</xsl:call-template>
													</xsl:with-param>
												</xsl:call-template>
												<xsl:call-template name ="templ_prop_Space"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
								<xsl:call-template name ="templ_str_AndOthersUnCap"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:for-each>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors=0">
						<xsl:value-of select="'Anon., '"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Author/b:Performer/b:Corporate"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthorPatent">
		<xsl:variable name ="cInventors">
			<xsl:value-of select ="count(b:Author/b:Inventor/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cInventors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors=0">
						<xsl:value-of select="'Anon., '"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$cInventors>0 and 5>$cInventors">
				<xsl:for-each select="b:Author/b:Inventor/b:NameList/b:Person">
					<xsl:variable name ="cInventorFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cInventorLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cInventorMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cInventorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test ="$cInventorFirstName=0 and $cInventorMiddleName=0 and $cInventors>1 and (position()+1)=$cInventors">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cInventorFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cInventorMiddleName=0 and $cInventors>1 and (position()+1)=$cInventors">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cInventorMiddleName=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:when test ="$cInventorMiddleName!=0">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cInventorMiddleName=1">
							<xsl:choose>
								<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test ="$cInventors>1 and (position()+1)=$cInventors">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="b:Author/b:Inventor/b:NameList/b:Person">
					<xsl:if test="position()=1">
						<xsl:variable name ="cInventorFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cInventorLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cInventorMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>
						<xsl:choose>
							<xsl:when test="$cInventorLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cInventorFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cInventorMiddleName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:call-template name ="templ_str_AndOthersUnCap"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthorPerformance">
		<xsl:variable name ="cWriters">
			<xsl:value-of select ="count(b:Author/b:Writer/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cWriters=0">
				<xsl:value-of select="'Anon., '"/>
			</xsl:when>
			<xsl:when test="$cWriters>0 and 5>$cWriters">
				<xsl:for-each select="b:Author/b:Writer/b:NameList/b:Person">
					<xsl:variable name ="cWriterFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cWriterLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cWriterMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cWriterLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test ="$cWriterFirstName=0 and $cWriterMiddleName=0 and $cWriters>1 and (position()+1)=$cWriters">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cWriterFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cWriterMiddleName=0 and $cWriters>1 and (position()+1)=$cWriters">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cWriterMiddleName=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:when test ="$cWriterMiddleName!=0">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cWriterMiddleName=1">
							<xsl:choose>
								<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test ="$cWriters>1 and (position()+1)=$cWriters">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="b:Author/b:Writer/b:NameList/b:Person">
					<xsl:if test="position()=1">
						<xsl:variable name ="cWriterFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cWriterLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cWriterMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>
						<xsl:choose>
							<xsl:when test="$cWriterLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cWriterFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cWriterMiddleName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:call-template name ="templ_str_AndOthersUnCap"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthorInterview">
		<xsl:variable name ="cInterviewees">
			<xsl:value-of select ="count(b:Author/b:Interviewee/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cInterviewees=0">
				<xsl:value-of select="'Anon., '"/>
			</xsl:when>
			<xsl:when test="$cInterviewees>0 and 5>$cInterviewees">
				<xsl:for-each select="b:Author/b:Interviewee/b:NameList/b:Person">
					<xsl:variable name ="cIntervieweeFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cIntervieweeLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cIntervieweeMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cIntervieweeLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test ="$cIntervieweeFirstName=0 and $cIntervieweeMiddleName=0 and $cInterviewees>1 and (position()+1)=$cInterviewees">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cIntervieweeFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cIntervieweeMiddleName=0 and $cInterviewees>1 and (position()+1)=$cInterviewees">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cIntervieweeMiddleName=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:when test ="$cIntervieweeMiddleName!=0">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cIntervieweeMiddleName=1">
							<xsl:choose>
								<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test ="$cInterviewees>1 and (position()+1)=$cInterviewees">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="b:Author/b:Interviewee/b:NameList/b:Person">
					<xsl:if test="position()=1">
						<xsl:variable name ="cIntervieweeFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cIntervieweeLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cIntervieweeMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>
						<xsl:choose>
							<xsl:when test="$cIntervieweeLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cIntervieweeFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cIntervieweeMiddleName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:call-template name ="templ_str_AndOthersUnCap"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="splitAuthorSpace">
		<xsl:param name ="first"/>
		<xsl:param name ="end"/>
		<xsl:choose>
			<xsl:when test="contains($first, '&#32;')">
				<xsl:value-of select="substring(substring-before($first, '&#32;'),1,1)" />
				<xsl:call-template name ="templ_prop_Dot"/>
				<xsl:call-template name ="templ_prop_Space"/>
				<xsl:variable name ="result">
					<xsl:call-template name ="left-trim">
						<xsl:with-param name ="s" select="substring-after($first,'&#32;')"/>
					</xsl:call-template>
				</xsl:variable>
				<xsl:call-template name="splitAuthorSpace">
					<xsl:with-param name="first" select="$result" />
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($first,1,1)"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>


	<xsl:template name="BibDisplayArtist">
		<xsl:variable name ="cArtists">
			<xsl:value-of select ="count(b:Author/b:Artist/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cArtists=0">
				<xsl:value-of select="'Anon., '"/>
			</xsl:when>
			<xsl:when test="$cArtists>0 and 5>$cArtists">
				<xsl:for-each select="b:Author/b:Artist/b:NameList/b:Person">
					<xsl:variable name ="cArtistFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cArtistLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cArtistMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cArtistLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test ="$cArtistFirstName=0 and $cArtistMiddleName=0 and $cArtists>1 and (position()+1)=$cArtists">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cArtistFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cArtistMiddleName=0 and $cArtists>1 and (position()+1)=$cArtists">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cArtistMiddleName=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:when test ="$cArtistMiddleName!=0">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cArtistMiddleName=1">
							<xsl:choose>
								<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test ="$cArtists>1 and (position()+1)=$cArtists">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="b:Author/b:Artist/b:NameList/b:Person">
					<xsl:if test="position()=1">
						<xsl:variable name ="cArtistFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cArtistLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cArtistMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>
						<xsl:choose>
							<xsl:when test="$cArtistLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cArtistFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cArtistMiddleName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:call-template name ="templ_str_AndOthersUnCap"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthor">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors=0">
						<xsl:choose>
							<xsl:when test ="$cEditor=0 or $DisplayEditorIfAuthorUnavailale!='true'">
								<xsl:value-of select="'Anon., '"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="BibDisplayEditorNL"/>
								<xsl:call-template name="templ_prop_ListSeparator"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$cAuthors>0 and 5>$cAuthors">
				<xsl:for-each select="b:Author/b:Author/b:NameList/b:Person">
					<xsl:variable name ="cAuthorFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cAuthorLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cAuthorMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test ="$cAuthorFirstName=0 and $cAuthorMiddleName=0 and $cAuthors>1 and (position()+1)=$cAuthors">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<xsl:choose>
						<xsl:when test="$cAuthorFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:choose>
								<xsl:when test ="$cAuthorMiddleName=0 and $cAuthors>1 and (position()+1)=$cAuthors">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:when test ="$cAuthorMiddleName=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:when test ="$cAuthorMiddleName!=0">
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cAuthorMiddleName=1">
							<xsl:choose>
								<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="splitAuthorSpace">
										<xsl:with-param name ="first">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:Middle"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>

							<xsl:choose>
								<xsl:when test ="$cAuthors>1 and (position()+1)=$cAuthors">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_BeforeLastAuthor"/>
									<xsl:call-template name ="templ_prop_Space"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="b:Author/b:Author/b:NameList/b:Person">
					<xsl:if test="position()=1">
						<xsl:variable name ="cAuthorFirstName">
							<xsl:value-of select ="count(b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cAuthorLastName">
							<xsl:value-of select ="count(b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cAuthorMiddleName">
							<xsl:value-of select ="count(b:Middle)"/>
						</xsl:variable>
						<xsl:choose>
							<xsl:when test="$cAuthorLastName=1">
								<xsl:value-of select="b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cAuthorFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="$cAuthorMiddleName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>
						<xsl:call-template name ="templ_str_AndOthersUnCap"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:if>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="HandleHypenInAuthor">
		<xsl:param name="authour"/>
		<xsl:param name="RetVal"/>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:if test="not(starts-with($authour,$prop_APA_FromToDash)) and $RetVal=''">
			<xsl:value-of select="substring($authour,1,1)"/>
			<xsl:call-template name ="templ_prop_Dot"/>
		</xsl:if>
		<xsl:choose>
			<xsl:when test="contains($authour,$prop_APA_FromToDash)">
				<xsl:call-template name="HandleHypenInAuthor">
					<xsl:with-param name="authour" select="substring-after($authour,$prop_APA_FromToDash)"/>
					<xsl:with-param name="RetVal">
						<xsl:value-of select="$RetVal"/>
						<xsl:value-of select="$prop_APA_FromToDash"/>
						<xsl:value-of select="substring(substring-after($authour,$prop_APA_FromToDash),1,1)"/>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$RetVal"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="HandleSPaceHypenInAuthor">
		<xsl:param name ="author"/>
		<xsl:choose>
			<xsl:when test="contains($author,'&#32;')">
				<xsl:call-template name ="HandleHypenInAuthor">
					<xsl:with-param name ="authour">
						<xsl:value-of select ="substring-before($author,'&#32;')"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:call-template name ="templ_prop_Space"/>
				<xsl:variable name ="result">
					<xsl:call-template name ="left-trim">
						<xsl:with-param name ="s" select="substring-after($author,'&#32;')"/>
					</xsl:call-template>
				</xsl:variable>
				<xsl:call-template name ="HandleSPaceHypenInAuthor">
					<xsl:with-param name="author">
						<xsl:value-of select ="$result"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="HandleHypenInAuthor">
					<xsl:with-param name ="authour">
						<xsl:value-of select ="$author"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayDayMonthYear">
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cDay!=0">
				<xsl:choose>
					<xsl:when test ="$cMonth!=0">
						<xsl:choose>
							<xsl:when test ="$cYear!=0">
								<xsl:call-template name ="templ_prop_OpenBracket"/>
								<xsl:value-of select="b:Day"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Month"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_CloseBracket"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test ="$cYear!=0">
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:choose>
					<xsl:when test ="$cYear!=0">
						<xsl:choose>
							<xsl:when test ="$cMonth!=0">
								<xsl:call-template name ="templ_prop_OpenBracket"/>
								<xsl:value-of select="b:Month"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_CloseBracket"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayDayMonth">
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:if test ="$cMonth!=0">
			<xsl:if test ="$cDay!=0">
				<xsl:value-of select="b:Day"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:if>
			<xsl:value-of select="b:Month"/>
			<xsl:call-template name ="templ_prop_ListSeparator"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayDayMonthArtInPeriod">
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:if test ="$cMonth!=0">
			<xsl:if test ="$cDay!=0">
				<xsl:value-of select="b:Day"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:if>
			<xsl:value-of select="b:Month"/>
			<xsl:call-template name ="templ_prop_ListSeparator"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayVolumeIssue">
		<xsl:variable name ="cPeriodicalTitle">
			<xsl:value-of select="count(b:PeriodicalTitle)"/>
		</xsl:variable>
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>

		<xsl:if test ="$cPeriodicalTitle!=0">
			<i>
				<xsl:value-of select="b:PeriodicalTitle"/>
			</i>
			<xsl:choose>
				<xsl:when test="$cMonth!=0 or $cVolume!=0 or $cIssue!=0 or $cPages!=0">
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name = "templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:call-template name ="templ_prop_Space"/>

		</xsl:if>

		<xsl:if test ="$cMonth!=0">
			<xsl:if test ="$cDay!=0">
				<xsl:value-of select="b:Day"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:if>
			<xsl:value-of select="b:Month"/>
			<xsl:choose>
				<xsl:when test="$cVolume!=0 or $cIssue!=0 or $cPages!=0">
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name = "templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>

		<xsl:variable name="str_VolumeCap">
			<xsl:call-template name="templ_str_VolumeCap"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cVolume!=0">
				<xsl:choose>
					<xsl:when test ="$cIssue=0">
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="$str_VolumeCap"/>
							<xsl:with-param name="stringToBeReplaced" select="'%1'"/>
							<xsl:with-param name="stringReplacement" select="b:Volume"/>
						</xsl:call-template>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Volume"/>
						<xsl:call-template name ="templ_prop_OpenBracket"/>
						<xsl:value-of select="b:Issue"/>
						<xsl:call-template name ="templ_prop_CloseBracket"/>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:if test ="$cIssue!=0">
					<xsl:value-of select="'Issue'"/>
					<xsl:call-template name ="templ_prop_Space"/>
					<xsl:value-of select="b:Issue"/>
					<xsl:choose>
						<xsl:when test="$cPages!=0">
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name = "templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayVolumeIssueJA">
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test="$cMonth!=0">
				<xsl:choose>
					<xsl:when test ="$cDay!=0">
						<xsl:value-of select="b:Day"/>
						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:value-of select="b:Month"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Month"/>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="($cVolume!=0 or $cIssue!=0) and $cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>

		<xsl:variable name="str_VolumeCap">
			<xsl:call-template name="templ_str_VolumeCap"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cVolume!=0">
				<xsl:choose>
					<xsl:when test ="$cIssue=0">
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="$str_VolumeCap"/>
							<xsl:with-param name="stringToBeReplaced" select="'%1'"/>
							<xsl:with-param name="stringReplacement" select="b:Volume"/>
						</xsl:call-template>
					</xsl:when>
					<xsl:when test ="$cIssue!=0">
						<xsl:value-of select="b:Volume"/>
						<xsl:call-template name ="templ_prop_OpenBracket"/>
						<xsl:value-of select="b:Issue"/>
						<xsl:call-template name ="templ_prop_CloseBracket"/>
					</xsl:when>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:if test ="$cIssue!=0">
					<xsl:value-of select="'Issue'"/>
					<xsl:call-template name ="templ_prop_Space"/>
					<xsl:value-of select="b:Issue"/>
					<xsl:choose>
						<xsl:when test="$cPages!=0">
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name = "templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayYear">
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cYear=1">
				<xsl:value-of select = "b:Year"/>
				<xsl:call-template name = "templ_prop_Dot"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:call-template name="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="BibDisplayYearCase">
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cReporter">
			<xsl:value-of select="count(b:Reporter)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cYear=1">
				<xsl:call-template name ="templ_prop_OpenBracket"/>
				<xsl:value-of select = "b:Year"/>
				<xsl:call-template name ="templ_prop_CloseBracket"/>
				<xsl:if test="$cReporter=0">
					<xsl:call-template name = "templ_prop_Dot"/>
				</xsl:if>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_prop_OpenBracket"/>
				<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
				<xsl:call-template name ="templ_prop_CloseBracket"/>
				<xsl:if test="$cReporter=0">
					<xsl:call-template name = "templ_prop_Dot"/>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:call-template name="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="BibDisplayInstitutionArt">
		<xsl:variable name="cInstitution">
			<xsl:value-of select="count(b:Institution)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cInstitution!=0">
				<xsl:call-template name ="templ_prop_Space"/>
				<xsl:call-template name ="templ_prop_OpenBracket"/>
				<xsl:value-of select = "b:Institution"/>
				<xsl:call-template name ="templ_prop_CloseBracket"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayTitle">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:call-template name ="templ_prop_Dot"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayTitleInt">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:value-of select="b:Title"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayTitleES">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:value-of select="b:Title"/>
			<xsl:call-template name ="templ_prop_ListSeparator"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayTitleCase">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:value-of select="b:Title"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayTitleBC">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:value-of select="b:Title"/>
			<xsl:call-template name ="templ_prop_Dot"/>
			<xsl:if test ="$cAuthors!=0">
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:if>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayJournalName">
		<xsl:variable name ="cJournalName">
			<xsl:value-of select="count(b:JournalName)"/>
		</xsl:variable>
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>

		<xsl:if test ="$cJournalName!=0">
			<xsl:value-of select="b:JournalName"/>
			<xsl:choose>
				<xsl:when test="$cMonth!=0 or $cPages!=0 or $cVolume!=0 or $cIssue!=0">
					<xsl:call-template name ="templ_prop_ListSeparator"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayPeriodicalTitle">
		<xsl:variable name ="cPeriodicalTitle">
			<xsl:value-of select="count(b:PeriodicalTitle)"/>
		</xsl:variable>
		<xsl:if test ="$cPeriodicalTitle!=0">
			<xsl:value-of select="b:PeriodicalTitle"/>
			<xsl:call-template name ="templ_prop_ListSeparator"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayBookTitle">
		<xsl:variable name="cBookTitle">
			<xsl:value-of select="count(b:BookTitle)"/>
		</xsl:variable>
		<xsl:if test ="$cBookTitle!=0">
			<xsl:value-of select="b:BookTitle"/>
			<xsl:call-template name ="templ_prop_Dot"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayCity">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cState">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0 and $cState!=0">
				<xsl:value-of select="b:City"/>
				<xsl:call-template name ="templ_prop_OpenBracket"/>
				<xsl:value-of select="b:StateProvince"/>
				<xsl:call-template name="templ_prop_CloseBracket"/>
			</xsl:when>
			<xsl:when test ="$cCity!=0 or $cState!=0">
				<xsl:choose>
					<xsl:when test="$cCity!=0">
						<xsl:value-of select="b:City"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:StateProvince"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:choose>
			<xsl:when test ="$cCity!=0 or $cState!=0">
				<xsl:call-template name ="templ_prop_EnumSeparator"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_prop_Enum"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayPages">
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="pages">
			<xsl:value-of select="b:Pages"/>
		</xsl:variable>
		<xsl:if test ="$cPages!=0">
			<xsl:call-template name ="DisplayPageOrPages">
				<xsl:with-param name="pages" select ="$pages"/>
			</xsl:call-template>
			<xsl:call-template name ="templ_prop_Dot"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayConfCity">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
				<xsl:call-template name ="templ_prop_Dot"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayCityReport">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:call-template name="templ_prop_EnumSeparator"/>
	</xsl:template>

	<xsl:template name="BibDisplayConfCityConfProc">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
				<xsl:call-template name ="templ_prop_ListSeparator"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineLocoShort"/>
				<xsl:call-template name ="templ_prop_ListSeparator"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayConfPublisher">
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cPublisher!=0">
				<xsl:value-of select="b:Publisher"/>
				<xsl:choose>
					<xsl:when test ="$cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineNomineShort"/>
				<xsl:choose>
					<xsl:when test ="$cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
				</xsl:choose>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayPublisher">
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cPublisher!=0">
				<xsl:value-of select="b:Publisher"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineNomineShort"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayPublisherBC">
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cPublisher!=0">
				<xsl:value-of select="b:Publisher"/>
				<xsl:choose>
					<xsl:when test ="$cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:call-template name ="templ_str_SineNomineShort"/>
				<xsl:choose>
					<xsl:when test ="$cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
				</xsl:choose>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayEdition">
		<xsl:variable name="cEdition">
			<xsl:value-of select="count(b:Edition)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cEdition!=0">
				<xsl:value-of select="b:Edition"/>
				<xsl:call-template name ="templ_prop_Space"/>
				<xsl:call-template name ="templ_str_EditorShortUnCap"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAccessedDates">
		<xsl:variable name="cYearAccessed">
			<xsl:value-of select="count(b:YearAccessed)"/>
		</xsl:variable>
		<xsl:variable name="cMonthAccessed">
			<xsl:value-of select="count(b:MonthAccessed)"/>
		</xsl:variable>
		<xsl:variable name="cDayAccessed">
			<xsl:value-of select="count(b:DayAccessed)"/>
		</xsl:variable>

		<xsl:if test ="$cYearAccessed!=0">
			<br>
				<xsl:variable name ="str_AccessedCap">
					<xsl:call-template name ="templ_str_AccessedCap"/>
				</xsl:variable>
				<xsl:variable name ="prop_Space">
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:variable>
				<xsl:choose>
					<xsl:when test="$cDayAccessed!=0">
						<xsl:choose>
							<xsl:when test="$cMonthAccessed!=0">
								<xsl:if test ="$cYearAccessed!=0">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_SecondaryOpen"/>
									<xsl:call-template name ="FindReplaceString">
										<xsl:with-param name="originalString" select="string($str_AccessedCap)"/>
										<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
										<xsl:with-param name="stringReplacement" select="$prop_Space"/>
									</xsl:call-template>
									<xsl:value-of select="b:DayAccessed"/>
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:value-of select="b:MonthAccessed"/>
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:value-of select="b:YearAccessed"/>
									<xsl:call-template name ="templ_prop_SecondaryClose"/>
									<xsl:call-template name ="templ_prop_Dot"/>
								</xsl:if>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:call-template name ="templ_prop_SecondaryOpen"/>
								<xsl:call-template name ="FindReplaceString">
									<xsl:with-param name="originalString" select="string($str_AccessedCap)"/>
									<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
									<xsl:with-param name="stringReplacement" select="$prop_Space"/>
								</xsl:call-template>
								<xsl:value-of select="b:YearAccessed"/>
								<xsl:call-template name ="templ_prop_SecondaryClose"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="$cMonthAccessed!=0">
								<xsl:if test="$cYearAccessed!=0">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_prop_SecondaryOpen"/>
									<xsl:call-template name ="FindReplaceString">
										<xsl:with-param name="originalString" select="string($str_AccessedCap)"/>
										<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
										<xsl:with-param name="stringReplacement" select="$prop_Space"/>
									</xsl:call-template>
									<xsl:value-of select="b:MonthAccessed"/>
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:value-of select="b:YearAccessed"/>
									<xsl:call-template name ="templ_prop_SecondaryClose"/>
									<xsl:call-template name ="templ_prop_Dot"/>
								</xsl:if>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:call-template name ="templ_prop_SecondaryOpen"/>
								<xsl:call-template name ="FindReplaceString">
									<xsl:with-param name="originalString" select="string($str_AccessedCap)"/>
									<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
									<xsl:with-param name="stringReplacement" select="$prop_Space"/>
								</xsl:call-template>
								<xsl:value-of select="b:YearAccessed"/>
								<xsl:call-template name ="templ_prop_SecondaryClose"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</br>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayURL">
		<xsl:variable name="cURL">
			<xsl:value-of select="count(b:URL)"/>
		</xsl:variable>
		<xsl:if test ="$cURL!=0">
			<br>
				<xsl:text>Available at:</xsl:text>
				<xsl:call-template name ="templ_prop_Space"/>
				<u>
					<xsl:value-of select="b:URL"/>
				</u>
			</br>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="ProceedBibliography">
		<xsl:param name="sList"/>
		<xsl:for-each select="msxsl:node-set($sList)/b:Bibliography/b:Source">
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

			<xsl:variable name="cAuthors" >
				<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person)" />
			</xsl:variable>
			<xsl:variable name="cCorporateAuthors">
				<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
			</xsl:variable>
			<xsl:variable name="cEditor">
				<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
			</xsl:variable>
			<xsl:variable name="cCity">
				<xsl:value-of select="count(b:City)"/>
			</xsl:variable>
			<xsl:variable name="cPublisher">
				<xsl:value-of select="count(b:Publisher)"/>
			</xsl:variable>
			<xsl:variable name="cYear">
				<xsl:value-of select="count(b:Year)"/>
			</xsl:variable>
			<xsl:variable name="cYearAccessed">
				<xsl:value-of select="count(b:YearAccessed)"/>
			</xsl:variable>
			<xsl:variable name="cURL">
				<xsl:value-of select="count(b:URL)"/>
			</xsl:variable>

			<xsl:variable name="SourceType">
				<xsl:value-of select="b:SourceType"/>
			</xsl:variable>

			<xsl:choose>
				<xsl:when test="$SourceType = 'Book'">
					<xsl:element name="p">
						<xsl:call-template name = "BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor">
							<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
						</xsl:call-template>
						<xsl:call-template name = "BibDisplayYear"/>
						<i>
							<xsl:call-template name = "BibDisplayTitle"/>
						</i>
						<xsl:call-template name = "BibDisplayEdition"/>
						<xsl:call-template name = "BibDisplayCity"/>
						<xsl:call-template name = "BibDisplayPublisher"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'BookSection'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor">
							<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
						</xsl:call-template>
						<xsl:call-template name = "BibDisplayYear"/>
						<xsl:call-template name = "BibDisplayTitleBC"/>

						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:variable name="str_InNameCap">
							<xsl:call-template name="templ_str_InNameCap"/>
						</xsl:variable>
						<xsl:variable name="prop_EnumSeaparator">
							<xsl:call-template name="templ_prop_EnumSeparator"/>
						</xsl:variable>
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="string($str_InNameCap)"/>
							<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
							<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
						</xsl:call-template>
						<xsl:if test = "$cEditor!=0">
							<xsl:call-template name ="BibDisplayEditor"/>
							<xsl:if test = "$cAuthors!=0">
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:if>
						</xsl:if>
						<i>
							<xsl:call-template name ="BibDisplayBookTitle"/>
						</i>
						<xsl:call-template name = "BibDisplayEdition"/>
						<xsl:call-template name = "BibDisplayCity"/>
						<xsl:call-template name = "BibDisplayPublisherBC"/>
						<xsl:call-template name ="BibDisplayPages"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'InternetSite'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor"/>
						<xsl:call-template name = "BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayStrOnline"/>
						<xsl:call-template name ="BibDisplayURL"/>
						<xsl:call-template name ="BibDisplayAccessedDates"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'DocumentFromInternetSite'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor"/>
						<xsl:call-template name = "BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayStrOnline"/>
						<xsl:call-template name ="BibDisplayURL"/>
						<xsl:call-template name ="BibDisplayAccessedDates"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'JournalArticle'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor">
							<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
						</xsl:call-template>
						<xsl:call-template name = "BibDisplayYear"/>
						<xsl:call-template name = "BibDisplayTitle"/>
						<i>
							<xsl:call-template name ="BibDisplayJournalName"/>
						</i>
						<xsl:call-template name ="BibDisplayVolumeIssueJA"/>
						<xsl:call-template name ="BibDisplayPages"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'ArticleInAPeriodical'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor">
							<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
						</xsl:call-template>
						<xsl:call-template name = "BibDisplayYear"/>
						<xsl:call-template name = "BibDisplayTitle"/>
						<xsl:call-template name ="BibDisplayVolumeIssue"/>
						<xsl:call-template name ="BibDisplayPages"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'ConferenceProceedings'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor">
							<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
						</xsl:call-template>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayConfCityConfProc"/>
						<xsl:call-template name ="BibDisplayConfPublisher"/>
						<xsl:call-template name ="BibDisplayPages"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Report'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitleES"/>
						</i>
						<xsl:call-template name ="BibDisplayCityReport"/>
						<xsl:call-template name ="BibDisplayPublisher"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Art'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayArtist"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayStrArt"/>
						<xsl:call-template name ="BibDisplayInstitutionArt"/>
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'SoundRecording'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthorSoundRec"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayStrSoundRecording"/>
						<xsl:call-template name ="BibDisplayProductionCompanySRec"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Performance'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthorPerformance"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayProductionCompanyPerformance"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Interview'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthorInterview"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitleInt"/>
						</i>
						<xsl:call-template name="BibDisplayStrInterview"/>
						<xsl:call-template name ="BibDisplayDayMonthYear"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'ElectronicSource'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitleES"/>
						</i>
						<xsl:call-template name ="BibDisplayCityReport"/>
						<xsl:call-template name ="BibDisplayConfPublisher"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Patent'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthorPatent"/>
						<xsl:call-template name ="BibDisplayYear"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayCountryRegionPatent"/>
						<xsl:call-template name ="BibDisplayPatentNumber"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Film'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<i>
							<xsl:call-template name ="BibDisplayTitle"/>
						</i>
						<xsl:call-template name ="BibDisplayYear"/>
						<xsl:call-template name ="BibDisplayStrFilm"/>
						<xsl:call-template name ="BibDisplayDirector"/>
						<xsl:call-template name ="BibDisplayCountryRegion"/>
						<xsl:call-template name ="BibDisplayProductionCompany"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Case'">
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
						<i>
							<xsl:call-template name ="BibDisplayTitleCase"/>
						</i>
						<xsl:call-template name ="BibDisplayYearCase"/>
						<xsl:call-template name ="BibDisplayReporter"/>
					</xsl:element>
				</xsl:when>
				<xsl:when test="$SourceType = 'Misc'">
					<xsl:element name="p">
						<xsl:call-template name = "BibAddParagraphAttributes"/>
						<xsl:call-template name = "BibDisplayAuthor">
							<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
						</xsl:call-template>
						<xsl:call-template name = "BibDisplayYear"/>
						<i>
							<xsl:call-template name = "BibDisplayTitle"/>
						</i>
						<xsl:call-template name = "BibDisplayEdition"/>
						<xsl:call-template name = "BibDisplayCity"/>
						<xsl:call-template name = "BibDisplayPublisher"/>
					</xsl:element>
				</xsl:when>
				<xsl:otherwise>
					<xsl:element name="p">
						<xsl:call-template name ="BibAddParagraphAttributes"/>
					</xsl:element>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:for-each>
	</xsl:template>

	<xsl:template name="Bibliography">
		<html xmlns="http://www.w3.org/TR/REC-html40">
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

				<xsl:variable name="sList">
					<xsl:call-template name="sortedList">
						<xsl:with-param name="sourceRoot">
							<xsl:copy-of select="$ListPopulatedWithMain"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:variable>

				<xsl:call-template name="ProceedBibliography">
					<xsl:with-param name="sList" select="$sList"/>
				</xsl:call-template>
			</body>
		</html>
	</xsl:template>

	<xsl:template name="sortedList">
		<xsl:param name="sourceRoot"/>
		<xsl:apply-templates select="msxsl:node-set($sourceRoot)/*">
			<xsl:sort select="b:SortingString" />
		</xsl:apply-templates>
	</xsl:template>

	<xsl:template name="Citation">
		<xsl:for-each select="b:Citation">
			<xsl:variable name="SourceType">
				<xsl:value-of select="b:Source/b:SourceType"/>
			</xsl:variable>
			<xsl:choose>
				<xsl:when test="$SourceType = 'Book' or 
                $SourceType = 'BookSection' or
                $SourceType = 'InternetSite' or
                $SourceType = 'JournalArticle' or
                $SourceType = 'ArticleInAPeriodical' or
			    $SourceType = 'Misc' or
			    $SourceType = 'ElectronicSource' or
			    $SourceType = 'Report' or
				$SourceType = 'DocumentFromInternetSite' or
			    $SourceType = 'Art' or
			    $SourceType = 'SoundRecording' or
				$SourceType = 'Performance' or
				$SourceType = 'Interview' or
				$SourceType = 'Patent' or
                $SourceType = 'ConferenceProceedings' ">
					<html xmlns="http://www.w3.org/TR/REC-html40">
						<body>
							<xsl:variable name="cAuthors">
								<xsl:call-template name="MainContributors">
									<xsl:with-param name="returnType" select="'Count'"/>
								</xsl:call-template>
							</xsl:variable>

							<xsl:variable name="cCorporateAuthors">
								<xsl:value-of select="count(b:Source/b:Author/b:Author/b:Corporate)" />
							</xsl:variable>
							<xsl:variable name="cYear">
								<xsl:value-of select="count(b:Source/b:Year)" />
							</xsl:variable>
							<xsl:variable name ="cNoAuthor">
								<xsl:value-of select="count(b:NoAuthor)" />
							</xsl:variable>
							<xsl:variable name ="cNoTitle">
								<xsl:value-of select="count(b:NoTitle)" />
							</xsl:variable>
							<xsl:variable name ="cNoYear">
								<xsl:value-of select="count(b:NoYear)" />
							</xsl:variable>
							<xsl:variable name ="cPages">
								<xsl:value-of select="count(b:Pages)" />
							</xsl:variable>
							<xsl:variable name ="year">
								<xsl:choose>
									<xsl:when test ="$cYear=1">
										<xsl:value-of select = "b:Source/b:Year"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>
							<xsl:variable name ="author">
								<xsl:choose>
									<xsl:when test ="$cAuthors='' or $cAuthors=0">
										<xsl:choose>
											<xsl:when test="$cCorporateAuthors!=0">
												<xsl:value-of select="b:Source/b:Author/b:Author/b:Corporate"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="'Anon.'"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="MainContributors">
											<xsl:with-param name="returnType" select="Name"/>
											<xsl:with-param name="countAuthors" select="$cAuthors"/>
										</xsl:call-template>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>

							<xsl:variable name ="initValueOfPages">
								<xsl:value-of select="b:Pages"/>
							</xsl:variable>

							<xsl:variable name ="pages">
								<xsl:choose>
									<xsl:when test="contains($initValueOfPages, '-')">
										<xsl:value-of select="concat('pp. ', $initValueOfPages)"/>
									</xsl:when>
									<xsl:when test="contains($initValueOfPages, ',')">
										<xsl:value-of select="concat('pp. ', $initValueOfPages)"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="concat('p. ', $initValueOfPages)"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>

							<xsl:variable name="prop_APA_Hyphens">
								<xsl:call-template name="templ_prop_Hyphens"/>
							</xsl:variable>

							<xsl:variable name="volume" select="b:Volume"/>

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


							<xsl:if test="b:FirstAuthor">
								<xsl:call-template name ="templ_prop_OpenBracket"/>
							</xsl:if>

							<xsl:if test="b:PagePrefix">
								<xsl:value-of select="b:PagePrefix"/>
							</xsl:if>

							<xsl:variable name ="volpagesInfo">
								<xsl:call-template name="VolumePages">
									<xsl:with-param name ="displayTitle" select="$author"/>
									<xsl:with-param name ="year" select="$year"/>
									<xsl:with-param name ="volume" select="$volume"/>
									<xsl:with-param name ="volVolume" select="$volVolume"/>
									<xsl:with-param name ="pPages" select="$pages"/>
									<xsl:with-param name ="pages" select="$initValueOfPages"/>
								</xsl:call-template>
							</xsl:variable>

							<xsl:if test="$cNoAuthor=0">
								<xsl:value-of select="$author"/>
								<xsl:if test ="$cNoYear=0 or $volpagesInfo!=''">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:if>
							</xsl:if>

							<xsl:if test ="$cNoYear=0">
								<xsl:value-of select="$year"/>
								<xsl:if test ="$volpagesInfo!=''">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:if>
							</xsl:if>

							<xsl:if test ="$volpagesInfo!=''">
								<xsl:value-of select="$volpagesInfo"/>
							</xsl:if>

							<xsl:if test="b:PageSuffix">
								<xsl:value-of select="b:PageSuffix"/>
							</xsl:if>

							<xsl:if test="b:LastAuthor">
								<xsl:call-template name="templ_prop_CloseBracket"/>
							</xsl:if>
							<xsl:if test="not(b:LastAuthor)">
								<xsl:call-template name="templ_prop_GroupSeparator"/>
							</xsl:if>

						</body>
					</html>
				</xsl:when>

				<xsl:when test="$SourceType = 'Case' or $SourceType = 'Film'">
					<html xmlns="http://www.w3.org/TR/REC-html40">
						<body>
							<xsl:variable name="Title">
								<xsl:value-of select="b:Source/b:Title" />
							</xsl:variable>

							<xsl:variable name="cCorporateAuthors">
								<xsl:value-of select="count(b:Source/b:Author/b:Author/b:Corporate)" />
							</xsl:variable>
							<xsl:variable name="cYear">
								<xsl:value-of select="count(b:Source/b:Year)" />
							</xsl:variable>
							<xsl:variable name ="cNoAuthor">
								<xsl:value-of select="count(b:NoAuthor)" />
							</xsl:variable>
							<xsl:variable name ="cNoTitle">
								<xsl:value-of select="count(b:NoTitle)" />
							</xsl:variable>
							<xsl:variable name ="cNoYear">
								<xsl:value-of select="count(b:NoYear)" />
							</xsl:variable>
							<xsl:variable name ="cPages">
								<xsl:value-of select="count(b:Pages)" />
							</xsl:variable>
							<xsl:variable name ="cTitle">
								<xsl:value-of select="count(b:Source/b:Title)" />
							</xsl:variable>
							<xsl:variable name ="year">
								<xsl:choose>
									<xsl:when test ="$cYear=1">
										<xsl:value-of select = "b:Source/b:Year"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_str_NoDateShortUnCap"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>

							<xsl:variable name="prop_APA_Hyphens">
								<xsl:call-template name="templ_prop_Hyphens"/>
							</xsl:variable>

							<xsl:variable name="volume" select="b:Volume"/>

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

							<xsl:variable name ="initValueOfPages">
								<xsl:value-of select="b:Pages"/>
							</xsl:variable>

							<xsl:variable name ="pages">
								<xsl:choose>
									<xsl:when test="contains($initValueOfPages, '-')">
										<xsl:value-of select="concat('pp. ', $initValueOfPages)"/>
									</xsl:when>
									<xsl:when test="contains($initValueOfPages, ',')">
										<xsl:value-of select="concat('pp. ', $initValueOfPages)"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="concat('p. ', $initValueOfPages)"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>

							<xsl:if test="b:FirstAuthor">
								<xsl:call-template name ="templ_prop_OpenBracket"/>
							</xsl:if>

							<xsl:if test="b:PagePrefix">
								<xsl:value-of select="b:PagePrefix"/>
							</xsl:if>

							<xsl:variable name ="volpagesInfo">
								<xsl:call-template name="VolumePages">
									<xsl:with-param name ="displayTitle" select="$Title"/>
									<xsl:with-param name ="year" select="$year"/>
									<xsl:with-param name ="volume" select="$volume"/>
									<xsl:with-param name ="volVolume" select="$volVolume"/>
									<xsl:with-param name ="pPages" select="$pages"/>
									<xsl:with-param name ="pages" select="$initValueOfPages"/>
								</xsl:call-template>
							</xsl:variable>

							<xsl:if test="$cTitle=1">
								<xsl:if test="$cNoTitle=0">
									<xsl:value-of select="$Title"/>
									<xsl:if test ="$cNoYear=0 or $volpagesInfo!=''">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:if>
								</xsl:if>
							</xsl:if>

							<xsl:if test ="$cNoYear=0">
								<xsl:value-of select="$year"/>
								<xsl:if test ="$volpagesInfo!=''">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:if>
							</xsl:if>

							<xsl:if test ="$volpagesInfo!=''">
								<xsl:value-of select="$volpagesInfo"/>
							</xsl:if>

							<xsl:if test="b:PageSuffix">
								<xsl:value-of select="b:PageSuffix"/>
							</xsl:if>

							<xsl:if test="b:LastAuthor">
								<xsl:call-template name="templ_prop_CloseBracket"/>
							</xsl:if>

							<xsl:if test="not(b:LastAuthor)">
								<xsl:call-template name="templ_prop_GroupSeparator"/>
							</xsl:if>

						</body>
					</html>
				</xsl:when>

				<xsl:otherwise>
					<html xmlns="http://www.w3.org/TR/REC-html40">
						<body>
							<xsl:variable name="cTag">
								<xsl:value-of select="count(b:Source/b:Tag)"/>
							</xsl:variable>
							<xsl:choose>
								<xsl:when test ="$cTag!=0">
									<xsl:call-template name ="templ_prop_OpenBracket"/>
									<xsl:value-of select="b:Source/b:Tag"/>
									<xsl:call-template name="templ_prop_CloseBracket"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:text>Source type not supported by this bibliography style.</xsl:text>
								</xsl:otherwise>
							</xsl:choose>
						</body>
					</html>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:for-each>
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

	<xsl:template name="VolumePages">
		<xsl:param name="displayAuthor"/>
		<xsl:param name="displayTitle"/>
		<xsl:param name="year"/>
		<xsl:param name="volume"/>
		<xsl:param name="volVolume"/>
		<xsl:param name="pPages"/>
		<xsl:param name="pages"/>
		<xsl:if test="string-length($volume) > 0 or string-length($pages) > 0">
			<xsl:choose>
				<xsl:when test="string-length($volume) > 0 and string-length($pages) > 0">
					<xsl:value-of select="$volume"/>
					<xsl:call-template name="templ_prop_Enum"/>
					<xsl:value-of select="$pages"/>
				</xsl:when>
				<xsl:when test="string-length($volVolume) > 0">
					<xsl:value-of select="$volVolume"/>
				</xsl:when>
				<xsl:when test="string-length($pPages) > 0">
					<xsl:value-of select="$pPages"/>
				</xsl:when>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="MainContributors">
		<xsl:param name="returnType"/>
		<xsl:param name ="countAuthors"/>
		<xsl:choose>
			<xsl:when test="./b:Source/b:SourceType='Book' or ./b:Source/b:SourceType='BookSection' or ./b:Source/b:SourceType='ConferenceProceedings' or ./b:Source/b:SourceType='Misc' or ./b:Source/b:SourceType='JournalArticle' or ./b:Source/b:SourceType='ArticleInAPeriodical'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Author)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Author/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Author/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Author/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Author/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:when test="string-length(./b:Source/b:Author/b:Editor)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Editor/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Editor/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Editor/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Editor/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:Source/b:SourceType='InternetSite' or ./b:Source/b:SourceType='ElectronicSource' or ./b:Source/b:SourceType='Report' or ./b:Source/b:SourceType='DocumentFromInternetSite'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Author)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Author/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Author/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Author/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Author/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Author/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:Source/b:SourceType='SoundRecording'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Composer)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Composer/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Composer/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Composer/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Composer/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:when test="string-length(./b:Source/b:Author/b:Conductor)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Conductor/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Conductor/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Conductor/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Conductor/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:when test="string-length(./b:Source/b:Author/b:Performer)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Performer/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Performer/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Performer/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Performer/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:Source/b:SourceType='Performance'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Writer)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Writer/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Writer/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Writer/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Writer/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:Source/b:SourceType='Art'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Artist)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Artist/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Artist/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Artist/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>

									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Artist/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:Source/b:SourceType='Interview'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Interviewee)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Interviewee/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Interviewee/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Interviewee/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Interviewee/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:Source/b:SourceType='Patent'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Source/b:Author/b:Inventor)>0">
						<xsl:choose>
							<xsl:when test="$returnType='Count'">
								<xsl:value-of select="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person)"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test ="$countAuthors=1">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Last"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:First"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Middle"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors=2">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Last, ' &amp; '), ./b:Source/b:Author/b:Inventor/b:NameList/b:Person[2]/b:Last)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:First, ' &amp; '), ./b:Source/b:Author/b:Inventor/b:NameList/b:Person[2]/b:First)"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(concat(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Middle, ' &amp; '), ./b:Source/b:Author/b:Inventor/b:NameList/b:Person[2]/b:Middle)"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
									<xsl:when test ="$countAuthors>=3">
										<xsl:choose>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Last)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Last, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:First)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:First, ', et al.')"/>
											</xsl:when>
											<xsl:when test ="count(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Middle)>0">
												<xsl:value-of select="concat(./b:Source/b:Author/b:Inventor/b:NameList/b:Person/b:Middle, ', et al.')"/>
											</xsl:when>
										</xsl:choose>
									</xsl:when>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template match="text()">
		<xsl:value-of select="." />
	</xsl:template>

	<xsl:template name="populateMain">
		<xsl:param name="Type"/>
		<xsl:element name="{$Type}">
			<xsl:for-each select="/*[$Type]/b:Source">
				<xsl:variable name="MostImportantAuthorLocalName">
					<xsl:call-template name="MainImportantContributors"/>
				</xsl:variable>
				<xsl:element name="{'b:Source'}">
					<b:SortingString>
						<xsl:variable name = "author0">
							<xsl:for-each select="./b:Author/*[local-name()=$MostImportantAuthorLocalName]">
								<xsl:call-template name="formatPersonsAuthor"/>
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
								<xsl:otherwise>
									<xsl:if test="./b:SourceType != 'Case' and ./b:SourceType != 'Film'">
										<xsl:text>Anon.</xsl:text>
									</xsl:if>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>

						<xsl:if test="string-length($author) > 0">
							<xsl:value-of select="$author"/>
						</xsl:if>

						<xsl:if test="b:SourceType = 'Case' or b:SourceType = 'Film'">
							<xsl:if test="string-length(b:Title) > 0">
								<xsl:value-of select="b:Title"/>
							</xsl:if>
						</xsl:if>

						<xsl:choose>
							<xsl:when test="string-length(b:Year) > 0">
								<xsl:value-of select="b:Year"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:text>n.d.</xsl:text>
							</xsl:otherwise>
						</xsl:choose>

						<xsl:if test="b:SourceType != 'Case' and b:SourceType != 'Film'">
							<xsl:if test="string-length(b:Title) > 0">
								<xsl:value-of select="b:Title"/>
							</xsl:if>
						</xsl:if>

					</b:SortingString>
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
							<xsl:element name="{name()}" namespace="{namespace-uri()}">
								<xsl:call-template name="copyNameNodes"/>
							</xsl:element>
						</xsl:for-each>
					</b:Author>
					<xsl:for-each select="*">
						<xsl:if test="name()!='Author' and not(name()='Title' and $Type='b:Citation')">
							<xsl:element name="{name()}" namespace="{namespace-uri()}">
								<xsl:call-template name="copyNodes"/>
							</xsl:element>
						</xsl:if>
					</xsl:for-each>
				</xsl:element>
				<xsl:for-each select="../*">
					<xsl:if test="local-name()!='Source' and namespace-uri()='http://schemas.openxmlformats.org/officeDocument/2006/bibliography'">
						<xsl:element name="{name()}" namespace="{namespace-uri()}">
							<xsl:call-template name="copyNodes"/>
						</xsl:element>
					</xsl:if>
				</xsl:for-each>
			</xsl:for-each>
			<xsl:copy-of select="/*[$Type]/b:Locals"/>
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
		<xsl:if test="string-length(b:Corporate)=0 and count(b:NameList/b:Person)=0">
			<b:NameList>
				<b:Person>
					<b:Last>
						<xsl:value-of select="'Anon.,'"/>
					</b:Last>
				</b:Person>
			</b:NameList>
		</xsl:if>
	</xsl:template>

	<xsl:template name="copyNodes">
		<xsl:value-of select="."/>
	</xsl:template>

	<xsl:template name="copyNodes2">
		<xsl:for-each select="@*">
			<xsl:attribute name="{name()}" namespace="{namespace-uri()}">
				<xsl:value-of select="."/>
			</xsl:attribute>
		</xsl:for-each>
		<xsl:for-each select="*">
			<xsl:element name="{name()}" namespace="{namespace-uri()}">
				<xsl:call-template name="copyNodes2"/>
			</xsl:element>
		</xsl:for-each>
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

	<xsl:template name="formatPersonsAuthor">
		<xsl:if test="string-length(b:Corporate)=0">
			<xsl:variable name ="cAuthors">
				<xsl:value-of select ="count(b:NameList/b:Person)"/>
			</xsl:variable>
			<xsl:for-each select="b:NameList/b:Person">
				<xsl:if test="position()&lt;5">
					<xsl:variable name ="cAuthorFirstName">
						<xsl:value-of select ="count(b:First)"/>
					</xsl:variable>
					<xsl:variable name ="cAuthorLastName">
						<xsl:value-of select ="count(b:Last)"/>
					</xsl:variable>
					<xsl:variable name ="cAuthorMiddleName">
						<xsl:value-of select ="count(b:Middle)"/>
					</xsl:variable>
					<xsl:if test="$cAuthorLastName=1">
						<xsl:value-of select ="b:Last"/>
					</xsl:if>
					<xsl:if test="$cAuthorFirstName=1">
						<xsl:call-template name ="splitNameSpace">
							<xsl:with-param name ="first" select="b:First"/>
						</xsl:call-template>
					</xsl:if>
					<xsl:if test="$cAuthorMiddleName=1">
						<xsl:call-template name ="splitNameSpace">
							<xsl:with-param name ="first" select="b:Middle"/>
						</xsl:call-template>
					</xsl:if>
				</xsl:if>
			</xsl:for-each>
		</xsl:if>

		<xsl:if test="string-length(b:Corporate)>0">
			<xsl:value-of select="b:Corporate"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="splitNameSpace">
		<xsl:param name ="first"/>
		<xsl:choose>
			<xsl:when test="contains($first, '&#32;')">
				<xsl:value-of select="substring(substring-before($first, '&#32;'),1,1)" />
				<xsl:call-template name="splitNameSpace">
					<xsl:with-param name="first" select="substring-after($first, '&#32;')" />
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($first,1,1)"/>
			</xsl:otherwise>
		</xsl:choose>
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
	<xsl:template name="formatMainAuthor">
		<xsl:call-template name="formatNameCore">
			<xsl:with-param name="FML">
				<xsl:call-template name="templ_prop_MLA_MainAuthor_FML"/>
			</xsl:with-param>
			<xsl:with-param name="FM">
				<xsl:call-template name="templ_prop_MLA_MainAuthor_FM"/>
			</xsl:with-param>
			<xsl:with-param name="ML">
				<xsl:call-template name="templ_prop_MLA_MainAuthor_ML"/>
			</xsl:with-param>
			<xsl:with-param name="FL">
				<xsl:call-template name="templ_prop_MLA_MainAuthor_FL"/>
			</xsl:with-param>
			<xsl:with-param name="upperLast">no</xsl:with-param>
			<xsl:with-param name="withDot">no</xsl:with-param>
		</xsl:call-template>
	</xsl:template>


	<xsl:template name="formatSecondaryName">
		<xsl:call-template name="formatNameCore">
			<xsl:with-param name="FML">
				<xsl:call-template name="templ_prop_MLA_SecondaryAuthors_FML"/>
			</xsl:with-param>
			<xsl:with-param name="FM">
				<xsl:call-template name="templ_prop_MLA_SecondaryAuthors_FM"/>
			</xsl:with-param>
			<xsl:with-param name="ML">
				<xsl:call-template name="templ_prop_MLA_SecondaryAuthors_ML"/>
			</xsl:with-param>
			<xsl:with-param name="FL">
				<xsl:call-template name="templ_prop_MLA_SecondaryAuthors_FL"/>
			</xsl:with-param>
			<xsl:with-param name="upperLast">no</xsl:with-param>
			<xsl:with-param name="withDot">no</xsl:with-param>
		</xsl:call-template>
	</xsl:template>


	<xsl:template name="formatOtherAuthors">
		<xsl:call-template name="formatNameCore">
			<xsl:with-param name="FML">
				<xsl:call-template name="templ_prop_MLA_OtherAuthors_FML"/>
			</xsl:with-param>
			<xsl:with-param name="FM">
				<xsl:call-template name="templ_prop_MLA_OtherAuthors_FM"/>
			</xsl:with-param>
			<xsl:with-param name="ML">
				<xsl:call-template name="templ_prop_MLA_OtherAuthors_ML"/>
			</xsl:with-param>
			<xsl:with-param name="FL">
				<xsl:call-template name="templ_prop_MLA_OtherAuthors_FL"/>
			</xsl:with-param>
			<xsl:with-param name="upperLast">no</xsl:with-param>
			<xsl:with-param name="withDot">no</xsl:with-param>
		</xsl:call-template>
	</xsl:template>


	<xsl:template name="formatPersonSeperator">
		<xsl:choose>
			<xsl:when test="count(../b:Person) > 3 and position() = 1">
				<xsl:call-template name="templ_prop_ListSeparator"/>
				<xsl:call-template name="templ_str_AndOthersUnCap"/>
			</xsl:when>
			<xsl:when test="count(../b:Person) > 3 and position() >= 2">
			</xsl:when>
			<xsl:when test="3 >= count(../b:Person) and position() = count(../b:Person) - 1">
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
			<xsl:when test="position() = count(../b:Person)">
				<xsl:text></xsl:text>
			</xsl:when>
			<xsl:when test="3 > position()">
				<xsl:call-template name="templ_prop_ListSeparator"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="formatPersons">
		<xsl:if test="string-length(b:Corporate)=0">
			<xsl:for-each select="b:NameList/b:Person">
				<xsl:if test="(count(../b:Person) > 3 and 1 = position()) or (3 >= count(../b:Person))">
					<xsl:call-template name="formatSecondaryName"/>
				</xsl:if>
				<xsl:call-template name="formatPersonSeperator"/>
			</xsl:for-each>
		</xsl:if>

		<xsl:if test="string-length(b:Corporate)>0">
			<xsl:value-of select="b:Corporate"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="formatAuthor">
		<xsl:for-each select="b:Author/b:Author">
			<xsl:call-template name="formatPersonsAuthor"/>
		</xsl:for-each>
	</xsl:template>

	<xsl:template name="formatMain">
		<xsl:for-each select="b:Author/b:Main">
			<xsl:call-template name="formatPersonsAuthor"/>
		</xsl:for-each>
	</xsl:template>

	<xsl:template name="templ_prop_SimpleAuthor_F" >
		<xsl:text>%F</xsl:text>
	</xsl:template>


	<xsl:template name="templ_prop_SimpleAuthor_M" >
		<xsl:text>%M</xsl:text>
	</xsl:template>


	<xsl:template name="templ_prop_SimpleAuthor_L" >
		<xsl:text>%L</xsl:text>
	</xsl:template>


	<xsl:template name="templ_prop_SimpleDate_D" >
		<xsl:text>%D</xsl:text>
	</xsl:template>


	<xsl:template name="templ_prop_SimpleDate_M" >
		<xsl:text>%M</xsl:text>
	</xsl:template>


	<xsl:template name="templ_prop_SimpleDate_Y" >
		<xsl:text>%Y</xsl:text>
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

	<xsl:template name="MainImportantContributors">
		<xsl:param name="SourceRoot"/>
		<xsl:choose>
			<xsl:when test="./b:SourceType='Book'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='BookSection'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
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
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='ConferenceProceedings'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Report'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='SoundRecording'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Composer)>0">Composer</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Conductor)>0">Conductor</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Performer)>0">Performer</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Performance'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Writer)>0">Writer</xsl:when>
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
				</xsl:choose>
			</xsl:when>

			<xsl:when test="./b:SourceType='Misc'">
				<xsl:choose>
					<xsl:when test="string-length(./b:Author/b:Author)>0">Author</xsl:when>
					<xsl:when test="string-length(./b:Author/b:Editor)>0">Editor</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="right-trim">
		<xsl:param name="s" />
		<xsl:choose>
			<xsl:when test="substring($s, 1, 1) = ''">
				<xsl:value-of select="$s"/>
			</xsl:when>
			<xsl:when test="normalize-space(substring($s, string-length($s))) = ''">
				<xsl:call-template name="right-trim">
					<xsl:with-param name="s" select="substring($s, 1, string-length($s) - 1)" />
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$s" />
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="left-trim">
		<xsl:param name="s" />
		<xsl:choose>
			<xsl:when test="substring($s,1,1) = ' '">
				<xsl:call-template name="left-trim">
					<xsl:with-param name="s" select="substring($s, 2)" />
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$s" />
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>