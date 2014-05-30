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
				<xsl:text>2006</xsl:text>
			</xsl:when>
      <xsl:when test="b:StyleNameLocalized">
        <xsl:choose>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1033'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1025'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1037'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1041'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2052'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1028'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1042'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1036'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1040'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='3082'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1043'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1031'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1046'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1049'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1035'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1032'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1081'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1054'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1057'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1086'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1066'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1053'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1069'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1027'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1030'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1110'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1044'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1061'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1062'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1063'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1045'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2070'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1029'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1055'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1038'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1048'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1058'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1026'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1050'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1087'">
            <xsl:text>Электр және электроника инженерлері институты</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='2074'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='3098'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1051'">
            <xsl:text>IEEE</xsl:text>
          </xsl:when>
          <xsl:when test="b:StyleNameLocalized/b:Lcid='1060'">
            <xsl:text>Način citiranja IEEE</xsl:text>
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
								<xsl:text>b:ConferenceName</xsl:text>
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
								<xsl:text>b:ProductionCompany</xsl:text>
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
								<xsl:text>b:CountryRegion</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:PatentNumber</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Day</xsl:text>
							</b:ImportantField>
							<b:ImportantField>
								<xsl:text>b:Month</xsl:text>
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

	<xsl:template name="templ_str_InUnCap" >
		<xsl:param name="LCID" />
		<xsl:variable name="_LCID">
			<xsl:call-template name="localLCID">
				<xsl:with-param name="LCID" select="$LCID"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="/*/b:Locals/b:Local[@LCID=$_LCID]/b:Strings/b:InNameUnCap"/>
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

	<xsl:template name="List_Separator_NoSpace">
		<xsl:variable name ="str_AccessedCap">
			<xsl:call-template name ="templ_prop_ListSeparator"/>
		</xsl:variable>

		<xsl:call-template name ="FindReplaceString">
			<xsl:with-param name="originalString" select="string($str_AccessedCap)"/>
			<xsl:with-param name="stringToBeReplaced" select="' '"/>
			<xsl:with-param name="stringReplacement" select="''"/>
		</xsl:call-template>

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
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_OnlineCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayStrFilm">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_Film"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayStrArt">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_ArtCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayStrSoundRecording">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_SoundRecordingCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayStrInterview">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:call-template name ="templ_str_InterviewCap"/>
		<xsl:call-template name ="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayDayMonthYearWebSiteJournal">
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
								<xsl:value-of select="b:Day"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Month"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:if test ="$cYear!=0">
							<xsl:value-of select="b:Year"/>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:if>
					</xsl:otherwise>

				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cMonth!=0">
				<xsl:choose>
					<xsl:when test ="$cYear!=0">
						<xsl:value-of select="b:Month"/>
						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:value-of select="b:Year"/>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$cDay!=0 and $cYear!=0 ">
				<xsl:value-of select="b:Year"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>


			<xsl:when test="$cYear!=0">
				<xsl:value-of select="b:Year"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
		</xsl:choose>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayDirector">
		<xsl:variable name="cDirector">
			<xsl:value-of select="count(b:Author/b:Director/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
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
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Director/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:value-of select="b:Author/b:Director/b:NameList/b:Person/b:First"/>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Director/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>

				<xsl:choose>
					<xsl:when test="$cDirectorMiddleName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Director/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Director/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Director/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>

				<xsl:choose>
					<xsl:when test="$cDirectorLastName=1">
						<xsl:value-of select="b:Author/b:Director/b:NameList/b:Person/b:Last"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
				</xsl:choose>

				<xsl:if test="$cDirector=1">
					<xsl:call-template name="templ_str_DirectorCap"/>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:if>
			</xsl:when>

			<xsl:when test="$cDirector>1">
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

						<xsl:when test =" $cDirector>1 and (position())=$cDirector">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:when>
					</xsl:choose>

					<xsl:choose>
						<xsl:when test="$cDirectorFirstName=1">
							<xsl:choose>
								<xsl:when test="contains(b:First,$prop_APA_FromToDash)">
									<xsl:call-template name="HandleSPaceHypenInAuthor">
										<xsl:with-param name="author">
											<xsl:call-template name="right-trim">
												<xsl:with-param name ="s" select="b:First"/>
											</xsl:call-template>
										</xsl:with-param>
									</xsl:call-template>
									<xsl:call-template name ="templ_prop_Space"/>
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
						<xsl:when test="$cDirectorMiddleName=1">
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

					<xsl:choose>
						<xsl:when test="$cDirectorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cDirector) and (position()&lt;$cDirector)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:call-template name ="templ_prop_ListSeparator"/>
				<xsl:if test="$cDirector>1">
					<xsl:call-template name="templ_str_DirectorsCap"/>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:if>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayCountryRegionPatent">
		<xsl:variable name="cCountryRegion">
			<xsl:value-of select="count(b:CountryRegion)"/>
		</xsl:variable>
		<xsl:variable name="cPatent">
			<xsl:value-of select="count(b:PatentNumber)"/>
		</xsl:variable>
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
			<xsl:when test ="$cCountryRegion!=0">
				<xsl:value-of select="b:CountryRegion"/>
				<xsl:choose>
					<xsl:when test ="$cPatent=0 and $cYear=0">
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayTitleJournal">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name ="cJournalName">
			<xsl:value-of select="count(b:JournalName)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>

			<xsl:choose>
				<xsl:when test="$cJournalName!=0 or $cVolume!=0 or $cIssue!=0 or $cPages!=0 or $cYear!=0 ">
					<xsl:call-template name ="List_Separator_NoSpace"/>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>


	<xsl:template name="BibDisplayTitleAP">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>

			<xsl:choose>
				<xsl:when test="$cVolume!=0 or $cIssue!=0 or $cPages!=0 or $cYear!=0 ">
					<xsl:call-template name ="List_Separator_NoSpace"/>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompanySRec">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:call-template name ="templ_prop_Dot"/>
				<xsl:call-template name ="templ_prop_Space"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompanyPerformance">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:choose >
					<xsl:when test="$cYear>0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompany">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:choose>
					<xsl:when test="$cYear>0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayProductionCompanywebsite">
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cURL">
			<xsl:value-of select="count(b:URL)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cProductionCompany!=0">
				<xsl:value-of select="b:ProductionCompany"/>
				<xsl:choose>
					<xsl:when test="$cMonth!=0 or $cDay!=0 or $cYear!=0 or $cURL!=0  ">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test="$cMonth=0 and $cDay=0 and $cYear=0 and $cURL=0" >
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayEditor">
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name ="corpAuthor">
			<xsl:value-of select ="count(b:Author/b:Author/b:Corporate)"/>
		</xsl:variable>

		<xsl:if test ="$cAuthors>0 or $corpAuthor>0">
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
					<xsl:if test="$cEditor=1">
						<xsl:call-template name="templ_str_EditorShortCap"/>
						<xsl:choose>
							<xsl:when test="$cCity!=0 or $cPublisher!=0 or $cStateProvince!=0 or $cYear!=0 or $cPages!=0 ">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:when test="$cCity=0 and $cPublisher=0 and $cStateProvince=0 and $cYear=0 and $cPages=0 ">
								<xsl:call-template name ="templ_prop_Space"/>

							</xsl:when>
						</xsl:choose>
					</xsl:if>
				</xsl:when>
				<xsl:when test="$cEditor>1">
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

							<xsl:when test ="$cEditor>1 and (position())=$cEditor">
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:call-template name ="templ_str_AndUnCap"/>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>

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
								<xsl:if test="((position()+1)!=$cEditor) and (position()&lt;$cEditor)">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:if>

							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
					<xsl:if test="$cEditor>1">
						<xsl:call-template name="templ_str_EditorsShortCap"/>
						<xsl:choose>
							<xsl:when test="$cCity!=0 or $cPublisher!=0 or $cStateProvince!=0 or $cYear!=0 or $cPages!=0 ">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:when test="$cCity=0 and $cPublisher=0 and $cStateProvince=0 and $cYear=0 and $cPages=0 ">
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>
					</xsl:if>
				</xsl:when>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayEditorBook">
		<xsl:variable name="cAuthor">
			<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name ="corpAuthor">
			<xsl:value-of select ="count(b:Author/b:Author/b:Corporate)"/>
		</xsl:variable>

		<xsl:if test ="$cAuthors>0 or $corpAuthor>0">
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
					<xsl:if test="$cEditor=1">
						<xsl:call-template name="templ_str_EditorShortCap"/>
						<xsl:choose>
							<xsl:when test="$cCity!=0 or $cPublisher!=0 or $cStateProvince!=0 or $cYear!=0 or $cPages!=0 ">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:when test="$cCity=0 and $cPublisher=0 and $cStateProvince=0 and $cYear=0 and $cPages=0 ">
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>
					</xsl:if>
				</xsl:when>
				<xsl:when test="$cEditor>1">
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
							<xsl:when test ="$cEditor>1 and (position())=$cEditor">
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:call-template name ="templ_str_AndUnCap"/>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>

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
								<xsl:if test="((position()+1)!=$cEditor) and (position()&lt;$cEditor)">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:if>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
					<xsl:if test="$cEditor>1">
						<xsl:call-template name="templ_str_EditorsShortCap"/>
						<xsl:choose>
							<xsl:when test="$cCity!=0 or $cPublisher!=0 or $cStateProvince!=0 or $cYear!=0 or $cPages!=0 ">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:when test="$cCity=0 and $cPublisher=0 and $cStateProvince=0 and $cYear=0 and $cPages=0 ">
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
						</xsl:choose>
					</xsl:if>
				</xsl:when>
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
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
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
											<xsl:with-param name ="s"  select="b:Author/b:Editor/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Editor/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cEditorLastName=1">
						<xsl:value-of select="b:Author/b:Editor/b:NameList/b:Person/b:Last"/>
						<xsl:call-template name="templ_prop_ListSeparator" />
					</xsl:when>
				</xsl:choose>
				<xsl:if test="$cEditor=1">
					<xsl:call-template name ="templ_str_EditorShortCap"/>
					<xsl:call-template name="Seperator"/>
				</xsl:if>
			</xsl:when>
			<xsl:when test="$cEditor>1">
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

						<xsl:when test ="$cEditor>1 and (position())=$cEditor">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cEditorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cEditor) and (position()&lt;$cEditor)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:call-template name ="templ_prop_ListSeparator"/>
				<xsl:if test="$cEditor>1">
					<xsl:call-template name ="templ_str_EditorsShortCap"/>
					<xsl:call-template name="Seperator"/>
				</xsl:if>
			</xsl:when>
		</xsl:choose>
	</xsl:template>


	<xsl:template name ="Seperator">
		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cEdition">
			<xsl:value-of select ="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cBookTitle">
			<xsl:value-of select ="count(b:BookTitle)"/>
		</xsl:variable>
		<xsl:variable name="cJournalName">
			<xsl:value-of select ="count(b:JournalName)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select ="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select ="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select ="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select ="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select ="count(b:Pages)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test="b:SourceType='Book' or b:SourceType='Misc'">
				<xsl:choose>
					<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="b:SourceType='BookSection'">
				<xsl:choose>
					<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
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
		<xsl:variable name="cCorporatePerformer">
			<xsl:value-of select="count(b:Author/b:Performer/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="$cComposer!=0">
				<xsl:choose>
					<xsl:when test="$cComposer = 1">
						<xsl:variable name ="cComposerFirstName">
							<xsl:value-of select ="count(b:Author/b:Composer/b:NameList/b:Person/b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cComposerLastName">
							<xsl:value-of select ="count(b:Author/b:Composer/b:NameList/b:Person/b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cComposerMiddleName">
							<xsl:value-of select ="count(b:Author/b:Composer/b:NameList/b:Person/b:Middle)"/>
						</xsl:variable>

						<xsl:choose>

							<xsl:when test="$cComposerFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Author/b:Composer/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Composer/b:NameList/b:Person/b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Composer/b:NameList/b:Person/b:First"/>
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
									<xsl:when test="contains(b:Author/b:Composer/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Composer/b:NameList/b:Person/b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Composer/b:NameList/b:Person/b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>

						<xsl:choose>
							<xsl:when test="$cComposerLastName=1">
								<xsl:value-of select="b:Author/b:Composer/b:NameList/b:Person/b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>

						<xsl:if test="$cComposer=1">
							<xsl:call-template name="templ_str_ComposerCap"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:if>
					</xsl:when>

					<xsl:when test="$cComposer>1">
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

								<xsl:when test =" $cComposer>1 and (position())=$cComposer">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_str_AndUnCap"/>
									<xsl:call-template name ="templ_prop_Space"/>
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
											<xsl:call-template name ="templ_prop_Space"/>
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

							<xsl:choose>
								<xsl:when test="$cComposerLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:if test="((position()+1)!=$cComposer) and (position()&lt;$cComposer)">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:if>

								</xsl:when>
							</xsl:choose>
						</xsl:for-each>
						<xsl:call-template name ="templ_prop_ListSeparator"/>

						<xsl:if test="$cComposer>1">
							<xsl:call-template name="templ_str_ComposersCap"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:if>

					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cConductor!=0">
				<xsl:choose>
					<xsl:when test="$cConductor = 1">
						<xsl:variable name ="cConductorFirstName">
							<xsl:value-of select ="count(b:Author/b:Conductor/b:NameList/b:Person/b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cConductorLastName">
							<xsl:value-of select ="count(b:Author/b:Conductor/b:NameList/b:Person/b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cConductorMiddleName">
							<xsl:value-of select ="count(b:Author/b:Conductor/b:NameList/b:Person/b:Middle)"/>
						</xsl:variable>

						<xsl:choose>

							<xsl:when test="$cConductorFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Author/b:Conductor/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Conductor/b:NameList/b:Person/b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Conductor/b:NameList/b:Person/b:First"/>
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
									<xsl:when test="contains(b:Author/b:Conductor/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Conductor/b:NameList/b:Person/b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Conductor/b:NameList/b:Person/b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>

						<xsl:choose>
							<xsl:when test="$cConductorLastName=1">
								<xsl:value-of select="b:Author/b:Conductor/b:NameList/b:Person/b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>

						<xsl:if test="$cConductor=1">
							<xsl:call-template name="templ_str_ConductorCap"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:if>
					</xsl:when>

					<xsl:when test="$cConductor>1">
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

								<xsl:when test =" $cConductor>1 and (position())=$cConductor">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_str_AndUnCap"/>
									<xsl:call-template name ="templ_prop_Space"/>
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
											<xsl:call-template name ="templ_prop_Space"/>
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

							<xsl:choose>
								<xsl:when test="$cConductorLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:if test="((position()+1)!=$cConductor) and (position()&lt;$cConductor)">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:if>
								</xsl:when>
							</xsl:choose>
						</xsl:for-each>
						<xsl:call-template name ="templ_prop_ListSeparator"/>

						<xsl:if test="$cConductor>1">
							<xsl:call-template name="templ_str_ConductorsCap"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:if>

					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cPerformer!=0">
				<xsl:choose>
					<xsl:when test="$cPerformer = 1">
						<xsl:variable name ="cPerformerFirstName">
							<xsl:value-of select ="count(b:Author/b:Performer/b:NameList/b:Person/b:First)"/>
						</xsl:variable>
						<xsl:variable name ="cPerformerLastName">
							<xsl:value-of select ="count(b:Author/b:Performer/b:NameList/b:Person/b:Last)"/>
						</xsl:variable>
						<xsl:variable name ="cPerformerMiddleName">
							<xsl:value-of select ="count(b:Author/b:Performer/b:NameList/b:Person/b:Middle)"/>
						</xsl:variable>

						<xsl:choose>

							<xsl:when test="$cPerformerFirstName=1">
								<xsl:choose>
									<xsl:when test="contains(b:Author/b:Performer/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Performer/b:NameList/b:Person/b:First"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Performer/b:NameList/b:Person/b:First"/>
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
									<xsl:when test="contains(b:Author/b:Performer/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
										<xsl:call-template name="HandleSPaceHypenInAuthor">
											<xsl:with-param name="author">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Performer/b:NameList/b:Person/b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name="splitAuthorSpace">
											<xsl:with-param name ="first">
												<xsl:call-template name="right-trim">
													<xsl:with-param name ="s" select="b:Author/b:Performer/b:NameList/b:Person/b:Middle"/>
												</xsl:call-template>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:call-template name ="templ_prop_Space"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
						</xsl:choose>

						<xsl:choose>
							<xsl:when test="$cPerformerLastName=1">
								<xsl:value-of select="b:Author/b:Performer/b:NameList/b:Person/b:Last"/>
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>

						<xsl:if test="$cPerformer=1">
							<xsl:call-template name="templ_str_PerformerCap"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:if>
					</xsl:when>

					<xsl:when test="$cPerformer>1">
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
								<xsl:when test =" $cPerformer>1 and (position())=$cPerformer">
									<xsl:call-template name ="templ_prop_Space"/>
									<xsl:call-template name ="templ_str_AndUnCap"/>
									<xsl:call-template name ="templ_prop_Space"/>
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
											<xsl:call-template name ="templ_prop_Space"/>
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

							<xsl:choose>
								<xsl:when test="$cPerformerLastName=1">
									<xsl:value-of select="b:Last"/>
									<xsl:if test="((position()+1)!=$cPerformer) and (position()&lt;$cPerformer)">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:if>
								</xsl:when>
							</xsl:choose>
						</xsl:for-each>
						<xsl:call-template name ="templ_prop_ListSeparator"/>

						<xsl:if test="$cPerformer>1">
							<xsl:call-template name="templ_str_PerformersCap"/>
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:if>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:if test="$cCorporatePerformer>0">
					<xsl:value-of select="b:Author/b:Performer/b:Corporate"/>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
					<xsl:call-template name="templ_str_PerformerCap"/>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayTitlePerformance">
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


	<xsl:template name="strinventorPatent">
		<xsl:text>Inventor</xsl:text>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="strinventorsPatent">
		<xsl:text>Inventors</xsl:text>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>
	<xsl:template name="strintervieweeInterview">
		<xsl:text>Interviewee</xsl:text>
		<xsl:call-template name ="templ_prop_ListSeparator"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="strintervieweesInterview">
		<xsl:text>Interviewees</xsl:text>
		<xsl:call-template name ="templ_prop_ListSeparator"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="strPerformance">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:text>Performance</xsl:text>
		<xsl:call-template name="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="strArtist">

		<xsl:text >Artist</xsl:text>
		<xsl:call-template name ="templ_prop_ListSeparator"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>
	<xsl:template name="strArtists">

		<xsl:text >Artists</xsl:text>
		<xsl:call-template name ="templ_prop_ListSeparator"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>
	<xsl:template name="strArt">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:text >Art</xsl:text>
		<xsl:call-template name="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Dot"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="BibDisplayAuthorPatent">
		<xsl:variable name="cInventor">
			<xsl:value-of select="count(b:Author/b:Inventor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>

			<xsl:when test="$cInventor = 1">
				<xsl:variable name ="cInventorFirstName">
					<xsl:value-of select ="count(b:Author/b:Inventor/b:NameList/b:Person/b:First)"/>
				</xsl:variable>
				<xsl:variable name ="cInventorLastName">
					<xsl:value-of select ="count(b:Author/b:Inventor/b:NameList/b:Person/b:Last)"/>
				</xsl:variable>
				<xsl:variable name ="cInventorMiddleName">
					<xsl:value-of select ="count(b:Author/b:Inventor/b:NameList/b:Person/b:Middle)"/>
				</xsl:variable>

				<xsl:choose>
					<xsl:when test="$cInventorFirstName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Inventor/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Inventor/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Inventor/b:NameList/b:Person/b:First"/>
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
							<xsl:when test="contains(b:Author/b:Inventor/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Inventor/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Inventor/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>

				<xsl:choose>
					<xsl:when test="$cInventorLastName=1">
						<xsl:value-of select="b:Author/b:Inventor/b:NameList/b:Person/b:Last"/>
						<xsl:choose>
							<xsl:when test="$cTitle!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cInventor>1">
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

						<xsl:when test =" $cInventor>1 and (position())=$cInventor">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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

					<xsl:choose>
						<xsl:when test="$cInventorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cInventor) and (position()&lt;$cInventor)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cTitle!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayAuthorPerformance">
		<xsl:variable name="cWriter">
			<xsl:value-of select="count(b:Author/b:Writer/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="$cWriter = 1">
				<xsl:variable name ="cWriterFirstName">
					<xsl:value-of select ="count(b:Author/b:Writer/b:NameList/b:Person/b:First)"/>
				</xsl:variable>
				<xsl:variable name ="cWriterLastName">
					<xsl:value-of select ="count(b:Author/b:Writer/b:NameList/b:Person/b:Last)"/>
				</xsl:variable>
				<xsl:variable name ="cWriterMiddleName">
					<xsl:value-of select ="count(b:Author/b:Writer/b:NameList/b:Person/b:Middle)"/>
				</xsl:variable>

				<xsl:choose>

					<xsl:when test="$cWriterFirstName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Writer/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Writer/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Writer/b:NameList/b:Person/b:First"/>
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
							<xsl:when test="contains(b:Author/b:Writer/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Writer/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Writer/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>

				<xsl:choose>
					<xsl:when test="$cWriterLastName=1">
						<xsl:value-of select="b:Author/b:Writer/b:NameList/b:Person/b:Last"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
				</xsl:choose>

				<xsl:if test="$cWriter=1">
					<xsl:call-template name="templ_str_WriterCap"/>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:if>
			</xsl:when>

			<xsl:when test="$cWriter>1">
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

						<xsl:when test =" $cWriter>1 and (position())=$cWriter">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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

					<xsl:choose>
						<xsl:when test="$cWriterLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cWriter) and (position()&lt;$cWriter)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:call-template name ="templ_prop_ListSeparator"/>

				<xsl:if test="$cWriter>1">
					<xsl:call-template name="templ_str_WritersCap"/>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:if>

			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayAuthorInterview">
		<xsl:variable name="cInterviewee">
			<xsl:value-of select="count(b:Author/b:Interviewee/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="$cInterviewee = 1">
				<xsl:variable name ="cIntervieweeFirstName">
					<xsl:value-of select ="count(b:Author/b:Interviewee/b:NameList/b:Person/b:First)"/>
				</xsl:variable>
				<xsl:variable name ="cIntervieweeLastName">
					<xsl:value-of select ="count(b:Author/b:Interviewee/b:NameList/b:Person/b:Last)"/>
				</xsl:variable>
				<xsl:variable name ="cIntervieweeMiddleName">
					<xsl:value-of select ="count(b:Author/b:Interviewee/b:NameList/b:Person/b:Middle)"/>
				</xsl:variable>

				<xsl:choose>

					<xsl:when test="$cIntervieweeFirstName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Interviewee/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Interviewee/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Interviewee/b:NameList/b:Person/b:First"/>
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
							<xsl:when test="contains(b:Author/b:Interviewee/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Interviewee/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Interviewee/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>

				<xsl:choose>
					<xsl:when test="$cIntervieweeLastName=1">
						<xsl:value-of select="b:Author/b:Interviewee/b:NameList/b:Person/b:Last"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
				</xsl:choose>

				<xsl:if test="$cInterviewee=1">
					<xsl:call-template name="strintervieweeInterview"/>
				</xsl:if>
			</xsl:when>

			<xsl:when test="$cInterviewee>1">
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

						<xsl:when test =" $cInterviewee>1 and (position())=$cInterviewee">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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

					<xsl:choose>
						<xsl:when test="$cIntervieweeLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cInterviewee) and (position()&lt;$cInterviewee)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:call-template name ="templ_prop_ListSeparator"/>

				<xsl:if test="$cInterviewee>1">
					<xsl:call-template name="strintervieweesInterview"/>
				</xsl:if>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayArtist">
		<xsl:variable name="cArtist">
			<xsl:value-of select="count(b:Author/b:Artist/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="$cArtist = 1">
				<xsl:variable name ="cArtistFirstName">
					<xsl:value-of select ="count(b:Author/b:Artist/b:NameList/b:Person/b:First)"/>
				</xsl:variable>
				<xsl:variable name ="cArtistLastName">
					<xsl:value-of select ="count(b:Author/b:Artist/b:NameList/b:Person/b:Last)"/>
				</xsl:variable>
				<xsl:variable name ="cArtistMiddleName">
					<xsl:value-of select ="count(b:Author/b:Artist/b:NameList/b:Person/b:Middle)"/>
				</xsl:variable>

				<xsl:choose>
					<xsl:when test="$cArtistFirstName=1">
						<xsl:choose>
							<xsl:when test="contains(b:Author/b:Artist/b:NameList/b:Person/b:First,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Artist/b:NameList/b:Person/b:First"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Artist/b:NameList/b:Person/b:First"/>
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
							<xsl:when test="contains(b:Author/b:Artist/b:NameList/b:Person/b:Middle,$prop_APA_FromToDash)">
								<xsl:call-template name="HandleSPaceHypenInAuthor">
									<xsl:with-param name="author">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Artist/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="splitAuthorSpace">
									<xsl:with-param name ="first">
										<xsl:call-template name="right-trim">
											<xsl:with-param name ="s" select="b:Author/b:Artist/b:NameList/b:Person/b:Middle"/>
										</xsl:call-template>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>

				<xsl:choose>
					<xsl:when test="$cArtistLastName=1">
						<xsl:value-of select="b:Author/b:Artist/b:NameList/b:Person/b:Last"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
				</xsl:choose>

				<xsl:if test="$cArtist=1">
					<xsl:call-template name="strArtist"/>
				</xsl:if>
			</xsl:when>

			<xsl:when test="$cArtist>1">
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

						<xsl:when test =" $cArtist>1 and (position())=$cArtist">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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

					<xsl:choose>
						<xsl:when test="$cArtistLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cArtist) and (position()&lt;$cArtist)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>

						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:call-template name ="templ_prop_ListSeparator"/>

				<xsl:if test="$cArtist>1">
					<xsl:call-template name="strArtists"/>
				</xsl:if>
			</xsl:when>
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



	<xsl:template name="BibDisplayAuthorBook">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cEdition">
			<xsl:value-of select ="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select ="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select ="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select ="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select ="count(b:Pages)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors=0">
						<xsl:choose>
							<xsl:when test ="$cEditor=0 or $DisplayEditorIfAuthorUnavailale!='true'">
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="BibDisplayEditorNL"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:choose>
							<xsl:when test="$cAuthors=0">
								<xsl:choose>
									<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Dot"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Dot"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cAuthors=1">
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test="$cAuthors=0">
									<xsl:choose>
										<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_Dot"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
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
				</xsl:for-each>

			</xsl:when>

			<xsl:when test="$cAuthors>1">
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
						<xsl:when test ="(position())=$cAuthors">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cAuthors) and (position()&lt;$cAuthors)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cAuthors=0">
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
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
	</xsl:template>

	<xsl:template name="BibDisplayAuthorBookSection">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cBookTitle">
			<xsl:value-of select ="count(b:BookTitle)"/>
		</xsl:variable>
		<xsl:variable name="cEdition">
			<xsl:value-of select ="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select ="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select ="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select ="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select ="count(b:Pages)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors=0">
						<xsl:choose>
							<xsl:when test ="$cEditor=0 or $DisplayEditorIfAuthorUnavailale!='true'">
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="BibDisplayEditorNL"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:choose>
							<xsl:when test="$cAuthors=0">
								<xsl:choose>
									<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Dot"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
										<xsl:call-template name ="templ_prop_ListSeparator"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:call-template name ="templ_prop_Dot"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cAuthors=1">
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test="$cAuthors=0">
									<xsl:choose>
										<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
											<xsl:call-template name ="templ_prop_ListSeparator"/>
										</xsl:when>
										<xsl:otherwise>
											<xsl:call-template name ="templ_prop_Dot"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
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
				</xsl:for-each>

			</xsl:when>

			<xsl:when test="$cAuthors>1">
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
						<xsl:when test ="(position())=$cAuthors">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cAuthors) and (position()&lt;$cAuthors)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cAuthors=0">
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
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
	</xsl:template>

	<xsl:template name="BibDisplayAuthorWebsite">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name ="cEditor">
			<xsl:value-of select ="count(b:Author/b:Editor/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select ="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors!=0">
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cAuthors=1">
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test="$cTitle!=0 or $cProductionCompany!=0 or $cYear!=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_Dot"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>

			</xsl:when>

			<xsl:when test="$cAuthors>1">
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
						<xsl:when test ="(position())=$cAuthors">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cAuthors) and (position()&lt;$cAuthors)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cTitle!=0 or $cProductionCompany!=0 or $cYear!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthorJArtcicle">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cJournalName">
			<xsl:value-of select ="count(b:JournalName)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select ="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select ="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select ="count(b:Pages)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors!=0">
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cJournalName!=0 or $cVolume!=0 or $cIssue!=0 or $cYear!=0 or $cPages!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test ="$cEditor=0 or $DisplayEditorIfAuthorUnavailale!='true'">
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="BibDisplayEditorNL"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cAuthors=1">
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test="$cTitle!=0 or $cJournalName!=0 or $cVolume!=0 or $cIssue!=0 or $cYear!=0 or $cPages!=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_Dot"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</xsl:when>

			<xsl:when test="$cAuthors>1">
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
						<xsl:when test ="(position())=$cAuthors">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cAuthors) and (position()&lt;$cAuthors)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cTitle!=0 or $cJournalName!=0 or $cVolume!=0 or $cIssue!=0 or $cYear!=0 or $cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthorConPr">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cConferenceName">
			<xsl:value-of select ="count(b:ConferenceName)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors!=0">
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cConferenceName!=0 or $cCity!=0 or $cYear!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cAuthors=1">
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test="$cTitle!=0 or $cConferenceName!=0 or $cCity!=0 or $cYear!=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_Dot"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>

			</xsl:when>

			<xsl:when test="$cAuthors>1">
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
						<xsl:when test ="(position())=$cAuthors">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cAuthors) and (position()&lt;$cAuthors)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cTitle!=0 or $cConferenceName!=0 or $cCity!=0 or $cYear!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayAuthorReport">
		<xsl:param name ="DisplayEditorIfAuthorUnavailale"/>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCorporateAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:Corporate)" />
		</xsl:variable>
		<xsl:variable name="prop_APA_FromToDash">
			<xsl:call-template name="templ_prop_FromToDash"/>
		</xsl:variable>

		<xsl:variable name="cTitle">
			<xsl:value-of select ="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select ="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cAuthors=0">
				<xsl:choose>
					<xsl:when test="$cCorporateAuthors!=0">
						<xsl:value-of select="b:Author/b:Author/b:Corporate"/>
						<xsl:choose>
							<xsl:when test="$cTitle!=0 or $cCity!=0 or $cPublisher!=0 or $cYear!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cAuthors=1">
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:choose>
								<xsl:when test="$cTitle!=0 or $cCity!=0 or $cPublisher!=0 or $cYear!=0">
									<xsl:call-template name ="templ_prop_ListSeparator"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name ="templ_prop_Dot"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>

			</xsl:when>

			<xsl:when test="$cAuthors>1">
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
						<xsl:when test ="(position())=$cAuthors">
							<xsl:call-template name ="templ_prop_Space"/>
							<xsl:call-template name ="templ_str_AndUnCap"/>
							<xsl:call-template name ="templ_prop_Space"/>
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
									<xsl:call-template name ="templ_prop_Space"/>
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
					<xsl:choose>
						<xsl:when test="$cAuthorLastName=1">
							<xsl:value-of select="b:Last"/>
							<xsl:if test="((position()+1)!=$cAuthors) and (position()&lt;$cAuthors)">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:if>
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
				<xsl:choose>
					<xsl:when test="$cTitle!=0 or $cCity!=0 or $cPublisher!=0 or $cYear!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
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
		</xsl:choose>
		<xsl:call-template name="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="BibDisplayTitleReport">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:choose>
				<xsl:when test=" $cCity!=0 or $cYear!=0 or  $cPublisher!=0  ">
					<xsl:call-template name ="List_Separator_NoSpace"/>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:when test="$cCity=0 and $cYear=0 and $cPublisher=0 ">
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name = "templ_prop_Dot"/>
				</xsl:when>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayYearCase">
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cYear=1">
				<xsl:value-of select = "b:Year"/>
				<xsl:call-template name = "templ_prop_Dot"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayInstitutionArt">
		<xsl:variable name="cInstitution">
			<xsl:value-of select="count(b:Institution)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cInstitution!=0">

				<xsl:value-of select = "b:Institution"/>
				<xsl:choose>
					<xsl:when test="$cYear>0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>



	<xsl:template name="BibDisplayTitleBook">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cEdition">
			<xsl:value-of select ="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select ="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cAuthor">
			<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select ="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select ="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select ="count(b:Pages)"/>
		</xsl:variable>

		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:choose>
				<xsl:when test="$cAuthor=0">
					<xsl:choose>
						<xsl:when test="$cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:when>
				<xsl:otherwise>
					<xsl:choose>
						<xsl:when test="$cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
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
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:call-template name ="templ_prop_Dot"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>


	<xsl:template name="BibDisplayYearSoundrecording">
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cYear=1">
				<xsl:value-of select = "b:Year"/>
				<xsl:call-template name = "templ_prop_Dot"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayTitleCase">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:if test="$cYear=1">
				<xsl:call-template name ="templ_prop_ListSeparator"/>
			</xsl:if >
			<xsl:if test="not($cYear=1)">
				<xsl:call-template name = "templ_prop_Dot"/>
			</xsl:if >
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayTitleBC">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cAuthor">
			<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cBookTitle">
			<xsl:value-of select ="count(b:BookTitle)"/>
		</xsl:variable>
		<xsl:variable name="cEdition">
			<xsl:value-of select ="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select ="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select ="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select ="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select ="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select ="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select ="count(b:Pages)"/>
		</xsl:variable>

		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:choose>
				<xsl:when test="$cAuthor=0">
					<xsl:choose>
						<xsl:when test="$cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
							<xsl:call-template name ="List_Separator_NoSpace"/>
							<xsl:call-template name="templ_prop_CloseQuote"/>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name="templ_prop_CloseQuote"/>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:when>
				<xsl:otherwise>
					<xsl:choose>
						<xsl:when test="$cBookTitle!=0 or $cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
							<xsl:call-template name ="List_Separator_NoSpace"/>
							<xsl:call-template name="templ_prop_CloseQuote"/>
							<xsl:call-template name ="templ_prop_Space"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name="templ_prop_CloseQuote"/>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayJournalName">
		<xsl:variable name ="cJournalName">
			<xsl:value-of select="count(b:JournalName)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:if test ="$cJournalName!=0">
			<xsl:value-of select="b:JournalName"/>
			<xsl:choose>
				<xsl:when test="$cVolume!=0 or $cIssue!=0 or $cPages!=0 or $cYear!=0">
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayJournalNameAP">
		<xsl:variable name ="cJournalName">
			<xsl:value-of select="count(b:PeriodicalTitle)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:if test ="$cJournalName!=0">
			<xsl:value-of select="b:PeriodicalTitle"/>
			<xsl:choose>
				<xsl:when test="$cVolume!=0 or $cIssue!=0 or $cPages!=0 or $cYear!=0">
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayVolumeJournal">
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name ="initValueOfVolume">
			<xsl:value-of select="b:Volume"/>
		</xsl:variable>
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cVolume!=0">
				<xsl:choose>
					<xsl:when test="contains($initValueOfVolume,'-') or contains($initValueOfVolume,',') ">
						<xsl:variable name="str_VolumesOfShortCap">
							<xsl:call-template name="templ_str_VolumesOfShortCap"/>
						</xsl:variable>
						<xsl:variable name="prop_EnumSeaparator">
							<xsl:call-template name="templ_prop_Space"/>
						</xsl:variable>
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="string($str_VolumesOfShortCap)"/>
							<xsl:with-param name="stringToBeReplaced" select="'%1 of %2'"/>
							<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
						</xsl:call-template>

						<xsl:value-of select="b:Volume"/>
					</xsl:when>

					<xsl:when test="not(contains($initValueOfVolume,'-')) or not(contains($initValueOfVolume,','))">
						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:variable name="str_VolumeShortUnCap">
							<xsl:call-template name="templ_str_VolumeShortUnCap"/>
						</xsl:variable>
						<xsl:variable name="prop_EnumSeaparator">
							<xsl:call-template name="templ_prop_Space"/>
						</xsl:variable>
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="string($str_VolumeShortUnCap)"/>
							<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
							<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
						</xsl:call-template>
						<xsl:value-of select="b:Volume"/>
					</xsl:when>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cPages!=0 or $cYear!=0 or $cIssue!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayVolumeBook">
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name ="initValueOfVolume">
			<xsl:value-of select="b:Volume"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cAuthors">
			<xsl:value-of select="count(b:Author/b:Author/b:NameList/b:Person)" />
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cVolume!=0">
				<xsl:choose>
					<xsl:when test="contains($initValueOfVolume,'-') or contains($initValueOfVolume,',') ">
						<xsl:variable name="str_VolumesOfShortCap">
							<xsl:call-template name="templ_str_VolumesOfShortCap"/>
						</xsl:variable>
						<xsl:variable name="prop_EnumSeaparator">
							<xsl:call-template name="templ_prop_Space"/>
						</xsl:variable>
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="string($str_VolumesOfShortCap)"/>
							<xsl:with-param name="stringToBeReplaced" select="'%1 of %2'"/>
							<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
						</xsl:call-template>

						<xsl:value-of select="b:Volume"/>
					</xsl:when>

					<xsl:when test="not(contains($initValueOfVolume,'-')) or not(contains($initValueOfVolume,','))">
						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:variable name="str_VolumeShortUnCap">
							<xsl:call-template name="templ_str_VolumeShortUnCap"/>
						</xsl:variable>
						<xsl:variable name="prop_EnumSeaparator">
							<xsl:call-template name="templ_prop_Space"/>
						</xsl:variable>
						<xsl:call-template name ="FindReplaceString">
							<xsl:with-param name="originalString" select="string($str_VolumeShortUnCap)"/>
							<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
							<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
						</xsl:call-template>
						<xsl:value-of select="b:Volume"/>
					</xsl:when>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="$cAuthors=0">
						<xsl:choose>
							<xsl:when test="$cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="$cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
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
	</xsl:template>

	<xsl:template name="BibDisplayIssueJournal">
		<xsl:variable name="cIssue">
			<xsl:value-of select="count(b:Issue)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cIssue!=0">
				<xsl:call-template name ="templ_prop_Space"/>

				<xsl:variable name="str_NumberShortUnCap">
					<xsl:call-template name="templ_str_NumberShortUnCap"/>
				</xsl:variable>
				<xsl:variable name="prop_EnumSeaparator">
					<xsl:call-template name="templ_prop_Space"/>
				</xsl:variable>
				<xsl:call-template name ="FindReplaceString">
					<xsl:with-param name="originalString" select="string($str_NumberShortUnCap)"/>
					<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
					<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
				</xsl:call-template>
				<xsl:value-of select="b:Issue"/>
				<xsl:choose>
					<xsl:when test="$cPages!=0 or $cYear!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:variable name ="initValueOfPages">
		<xsl:value-of select="b:Pages"/>
	</xsl:variable>

	<xsl:variable name ="pages">
		<xsl:choose>
			<xsl:when test="contains($initValueOfPages, '-')">
				<xsl:value-of select="concat('pp. ',$initValueOfPages)"/>
			</xsl:when>
			<xsl:when test="contains($initValueOfPages, ',')">
				<xsl:value-of select="concat('pp. ',$initValueOfPages)"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="concat('p. ',$initValueOfPages)"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:variable>

	<xsl:template name="BibDisplayPagesJournal">
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cMonth">
			<xsl:value-of select="count(b:Month)"/>
		</xsl:variable>
		<xsl:variable name ="cDay">
			<xsl:value-of select="count(b:Day)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name ="pages">
			<xsl:value-of select="b:Pages"/>
		</xsl:variable>
		<xsl:if test ="$cPages!=0">
			<xsl:call-template name ="DisplayPageOrPages">
				<xsl:with-param name="pages" select ="$pages"/>
			</xsl:call-template>
			<xsl:choose>
				<xsl:when test="$cYear=0">
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayTitleConferenceProceedings">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:variable name="cConferenceName">
			<xsl:value-of select="count(b:ConferenceName)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:choose>
				<xsl:when test ="$cConferenceName!=0 or $cCity!=0 or $cYear!=0">
					<xsl:call-template name ="List_Separator_NoSpace"/>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Space"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name="templ_prop_CloseQuote"/>
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayConferenceName">
		<xsl:variable name="cConferenceName">
			<xsl:value-of select="count(b:ConferenceName)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:variable name="str_InNameCap">
			<xsl:call-template name="templ_str_InUnCap"/>
		</xsl:variable>
		<xsl:variable name="prop_EnumSeaparator">
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:variable>


		<xsl:if test ="$cConferenceName!=0">
			<xsl:call-template name ="FindReplaceString">
				<xsl:with-param name="originalString" select="string($str_InNameCap)"/>
				<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
				<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
			</xsl:call-template>
			<xsl:call-template name ="templ_prop_Space"/>
			<i>
				<xsl:value-of select="b:ConferenceName"/>
			</i>
			<xsl:choose>
				<xsl:when test=" $cCity!=0 or $cYear!=0 ">

					<xsl:call-template name ="templ_prop_ListSeparator"/>
				</xsl:when>
				<xsl:when test=" $cCity=0 and $cYear=0">
					<xsl:call-template name ="templ_prop_Dot"/>
				</xsl:when>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayBookTitle">
		<xsl:variable name="cBookTitle">
			<xsl:value-of select="count(b:BookTitle)"/>
		</xsl:variable>
		<xsl:variable name="cEdition">
			<xsl:value-of select="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name ="cAuthor">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:variable name="str_InNameCap">
			<xsl:call-template name="templ_str_InUnCap"/>
		</xsl:variable>
		<xsl:variable name="prop_EnumSeaparator">
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:variable>


		<xsl:if test ="$cBookTitle!=0">
			<xsl:call-template name ="FindReplaceString">
				<xsl:with-param name="originalString" select="string($str_InNameCap)"/>
				<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
				<xsl:with-param name="stringReplacement" select="$prop_EnumSeaparator"/>
			</xsl:call-template>
			<xsl:call-template name ="templ_prop_Space"/>
			<i>
				<xsl:value-of select="b:BookTitle"/>
			</i>
			<xsl:choose>
				<xsl:when test="$cAuthor=0">
					<xsl:choose>
						<xsl:when test="$cEdition!=0 or $cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:when>
				<xsl:otherwise>
					<xsl:choose>
						<xsl:when test="$cEdition!=0 or $cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
							<xsl:call-template name ="templ_prop_ListSeparator"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayStateProvinceBook">
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cStateProvince!=0">
				<xsl:value-of select="b:StateProvince"/>
				<xsl:choose>
					<xsl:when test="$cPublisher>0">
						<xsl:call-template name ="templ_prop_EnumSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:when test="$cPublisher=0 and ($cYear!=0 or $cPages!=0)">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test="$cPublisher=0 and $cYear=0 and $cPages=0 " >
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayStateProvinceBC">
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cStateProvince!=0">
				<xsl:value-of select="b:StateProvince"/>
				<xsl:choose>
					<xsl:when test="$cPublisher>0">
						<xsl:call-template name ="templ_prop_EnumSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:when>
					<xsl:when test="$cPublisher=0 and ($cYear!=0 or $cPages!=0)">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test="$cPublisher=0 and $cYear=0 and $cPages=0 " >
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayYearBC">
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cYear=1">
				<xsl:value-of select = "b:Year"/>

				<xsl:choose>

					<xsl:when test="$cPages>0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>

						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>

				</xsl:choose>


			</xsl:when>
		</xsl:choose>
		<xsl:call-template name="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name="BibDisplayCityBookSection">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
				<xsl:choose>
					<xsl:when test="$cPublisher!=0 or $cStateProvince!=0 or $cYear!=0 or $cPages!=0 " >
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test="$cPublisher=0 and $cStateProvince=0 and $cYear=0 and $cPages=0 " >
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>

				</xsl:choose>
			</xsl:when>
		</xsl:choose>

	</xsl:template>

	<xsl:template name="BibDisplayCity">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0 ">
				<xsl:value-of select="b:City"/>
				<xsl:choose>
					<xsl:when test="$cPublisher!=0 and $cStateProvince=0">
						<xsl:call-template name ="templ_prop_EnumSeparator"/>
					</xsl:when>
					<xsl:when test="$cStateProvince!=0 or $cYear!=0 or $cPages!=0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test="$cStateProvince=0 and $cYear=0 and $cPages=0 " >
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayTitlePatent">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:call-template name="templ_prop_CloseQuote"/>
			<xsl:call-template name ="templ_prop_Dot"/>
			<xsl:call-template name="templ_prop_Space"/>
		</xsl:if>
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

	<xsl:template name="BibDisplayCityReport">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
				<xsl:choose>
					<xsl:when test ="$cYear=0">
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayCountryRegionFilm">
		<xsl:variable name="cCountryRegion">
			<xsl:value-of select="count(b:CountryRegion)"/>
		</xsl:variable>
		<xsl:variable name="cProductionCompany">
			<xsl:value-of select="count(b:ProductionCompany)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCountryRegion!=0">
				<xsl:value-of select="b:CountryRegion"/>
				<xsl:choose>
					<xsl:when test ="$cProductionCompany=0">
						<xsl:call-template name = "templ_prop_Dot"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_EnumSeparator"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayConfCityConfProc">
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cCity!=0">
				<xsl:value-of select="b:City"/>
				<xsl:choose>
					<xsl:when test="$cYear>0">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>


	<xsl:template name="BibDisplayPublisher">
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cPublisher!=0">
				<xsl:value-of select="b:Publisher"/>
				<xsl:choose>
					<xsl:when test=" $cCity!=0 or $cYear!=0 ">
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test="$cCity=0 and $cYear=0">
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayPublisherBC">
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cPublisher!=0">
				<xsl:value-of select="b:Publisher"/>
				<xsl:choose>
					<xsl:when test=" $cYear!=0 or $cPages!=0 " >
						<xsl:call-template name ="templ_prop_ListSeparator"/>
					</xsl:when>
					<xsl:when test=" $cYear=0 and $cPages=0 " >
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayEdition">
		<xsl:variable name="cEdition">
			<xsl:value-of select="count(b:Edition)"/>
		</xsl:variable>
		<xsl:variable name="cVolume">
			<xsl:value-of select="count(b:Volume)"/>
		</xsl:variable>
		<xsl:variable name="cEditor">
			<xsl:value-of select="count(b:Author/b:Editor/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name ="cAuthors">
			<xsl:value-of select ="count(b:Author/b:Author/b:NameList/b:Person)"/>
		</xsl:variable>
		<xsl:variable name="cCity">
			<xsl:value-of select="count(b:City)"/>
		</xsl:variable>
		<xsl:variable name="cStateProvince">
			<xsl:value-of select="count(b:StateProvince)"/>
		</xsl:variable>
		<xsl:variable name="cPublisher">
			<xsl:value-of select="count(b:Publisher)"/>
		</xsl:variable>
		<xsl:variable name="cPages">
			<xsl:value-of select="count(b:Pages)"/>
		</xsl:variable>
		<xsl:variable name ="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>

		<xsl:choose>
			<xsl:when test ="$cEdition!=0">
				<xsl:value-of select="b:Edition"/>
				<xsl:call-template name ="templ_prop_Space"/>
				<xsl:call-template name="templ_str_EditorShortUnCap"/>
				<xsl:choose>
					<xsl:when test="$cAuthors=0">
						<xsl:choose>
							<xsl:when test="$cVolume!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="$cVolume!=0 or $cEditor!=0 or $cCity!=0 or $cStateProvince!=0 or $cPublisher!=0 or $cYear!=0 or $cPages!=0">
								<xsl:call-template name ="templ_prop_ListSeparator"/>
							</xsl:when>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
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
							<xsl:if test="$cYearAccessed!=0">
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
						</xsl:otherwise>
					</xsl:choose>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:call-template name ="templ_prop_Dot"/>
		</xsl:if>
	</xsl:template>


	<xsl:template name="BibDisplayPatent">
		<xsl:variable name="cPatent">
			<xsl:value-of select="count(b:PatentNumber)"/>
		</xsl:variable>
		<xsl:variable name ="str_PatentCap">
			<xsl:call-template name ="templ_str_PatentCap"/>
		</xsl:variable>
		<xsl:variable name ="prop_Space">
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:variable>

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
			<xsl:when test="$cPatent!=0">
				<xsl:call-template name ="FindReplaceString">
					<xsl:with-param name="originalString" select="string($str_PatentCap)"/>
					<xsl:with-param name="stringToBeReplaced" select="' %1'"/>
					<xsl:with-param name="stringReplacement" select="$prop_Space"/>
				</xsl:call-template>
				<xsl:value-of select="b:PatentNumber"/>
				<xsl:choose>
					<xsl:when test="$cYear=0">
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name ="templ_prop_ListSeparator"/>
						<xsl:call-template name ="templ_prop_Space"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name ="BibDisplayDayMonthYearInterview">
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
								<xsl:value-of select="b:Day"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Month"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:if test ="$cYear!=0">
							<xsl:value-of select="b:Year"/>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:if>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:choose>
					<xsl:when test ="$cYear!=0">
						<xsl:choose>
							<xsl:when test ="$cMonth!=0">
								<xsl:value-of select="b:Month"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
							<xsl:when test="$cDay!=0 and $cYear!=0">
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>

				</xsl:choose>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayTitleWebSite">
		<xsl:variable name="cTitle">
			<xsl:value-of select="count(b:Title)"/>
		</xsl:variable>
		<xsl:if test ="$cTitle!=0">
			<xsl:call-template name="templ_prop_OpenQuote"/>
			<xsl:call-template name="right-trim">
				<xsl:with-param name ="s" select="b:Title"/>
			</xsl:call-template>
			<xsl:call-template name ="List_Separator_NoSpace"/>
			<xsl:call-template name="templ_prop_CloseQuote"/>
			<xsl:call-template name ="templ_prop_Space"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name ="BibDisplayDayMonthYearPatent">
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
								<xsl:value-of select="b:Day"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Month"/>
								<xsl:call-template name ="templ_prop_Space"/>
								<xsl:value-of select="b:Year"/>
								<xsl:call-template name ="templ_prop_Dot"/>
							</xsl:when>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:if test ="$cYear!=0">
							<xsl:value-of select="b:Year"/>
							<xsl:call-template name ="templ_prop_Dot"/>
						</xsl:if>
					</xsl:otherwise>

				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cMonth!=0">
				<xsl:choose>
					<xsl:when test ="$cYear!=0">
						<xsl:value-of select="b:Month"/>
						<xsl:call-template name ="templ_prop_Space"/>
						<xsl:value-of select="b:Year"/>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cDay!=0">
				<xsl:choose>
					<xsl:when test="$cYear!=0">
						<xsl:value-of select="b:Year"/>
						<xsl:call-template name ="templ_prop_Dot"/>
					</xsl:when>
				</xsl:choose>
			</xsl:when>

			<xsl:when test="$cYear!=0">
				<xsl:value-of select="b:Year"/>
				<xsl:call-template name ="templ_prop_Dot"/>
			</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template name="BibDisplayURL">
		<xsl:variable name="cURL">
			<xsl:value-of select="count(b:URL)"/>
		</xsl:variable>
		<xsl:if test ="$cURL!=0">
			<xsl:text>Available:</xsl:text>
			<xsl:call-template name ="templ_prop_Space"/>
			<xsl:value-of select="b:URL"/>
			<xsl:call-template name ="templ_prop_Dot"/>
		</xsl:if>
	</xsl:template>

	<xsl:template name="BibDisplayYearReport">
		<xsl:variable name="cYear">
			<xsl:value-of select="count(b:Year)"/>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test ="$cYear=1">
				<xsl:value-of select = "b:Year"/>
				<xsl:call-template name = "templ_prop_Dot"/>
			</xsl:when>
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


	<xsl:template match ="b:Source">
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
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name ="BibDisplayAuthorBook">
								<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
							</xsl:call-template>
							<xsl:call-template name = "BibDisplayTitleBook"/>
							<xsl:call-template name = "BibDisplayEdition"/>
							<xsl:call-template name="BibDisplayVolumeBook"/>
							<xsl:call-template name="BibDisplayEditorBook"/>

							<xsl:call-template name = "BibDisplayCity"/>
							<xsl:call-template name = "BibDisplayStateProvinceBook"/>

							<xsl:call-template name = "BibDisplayPublisherBC"/>
							<xsl:call-template name = "BibDisplayYearBC"/>
							<xsl:call-template name ="BibDisplayPages"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>
			<xsl:when test="$SourceType = 'BookSection'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorBookSection">
								<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
							</xsl:call-template>
							<xsl:call-template name = "BibDisplayTitleBC"/>
							<xsl:call-template name ="BibDisplayBookTitle"/>
							<xsl:call-template name = "BibDisplayEdition"/>
							<xsl:call-template name="BibDisplayVolumeBook"/>
							<xsl:call-template name="BibDisplayEditor"/>
							<xsl:call-template name = "BibDisplayCityBookSection"/>
							<xsl:call-template name = "BibDisplayStateProvinceBC"/>
							<xsl:call-template name = "BibDisplayPublisherBC"/>
							<xsl:call-template name = "BibDisplayYearBC"/>
							<xsl:call-template name ="BibDisplayPages"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'DocumentFromInternetSite'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorWebsite"/>
							<xsl:call-template name ="BibDisplayTitleWebSite"/>
							<xsl:call-template name ="BibDisplayProductionCompanywebsite"/>
							<xsl:call-template name = "BibDisplayDayMonthYearWebSiteJournal"/>
							<xsl:call-template name ="BibDisplayStrOnline"/>
							<xsl:call-template name ="BibDisplayURL"/>
							<xsl:call-template name ="BibDisplayAccessedDates"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'JournalArticle'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorJArtcicle">
								<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
							</xsl:call-template>
							<xsl:call-template name = "BibDisplayTitleJournal"/>
							<i>
								<xsl:call-template name ="BibDisplayJournalName"/>
							</i>
							<xsl:call-template name="BibDisplayVolumeJournal"/>
							<xsl:call-template name ="BibDisplayIssueJournal"/>
							<xsl:call-template name ="BibDisplayPagesJournal"/>
							<xsl:call-template name = "BibDisplayDayMonthYearWebSiteJournal"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'ArticleInAPeriodical'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorJArtcicle">
								<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
							</xsl:call-template>
							<xsl:call-template name = "BibDisplayTitleAP"/>
							<i>
								<xsl:call-template name ="BibDisplayJournalNameAP"/>
							</i>
							<xsl:call-template name="BibDisplayVolumeJournal"/>
							<xsl:call-template name ="BibDisplayIssueJournal"/>
							<xsl:call-template name="BibDisplayPagesJournal"/>
							<xsl:call-template name = "BibDisplayDayMonthYearWebSiteJournal"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'ConferenceProceedings'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorConPr"/>
							<xsl:call-template name ="BibDisplayTitleConferenceProceedings"/>
							<xsl:call-template name="BibDisplayConferenceName" />
							<xsl:call-template name ="BibDisplayConfCityConfProc"/>
							<xsl:call-template name ="BibDisplayYear"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Report'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name ="BibDisplayAuthorReport"/>
							<xsl:call-template name ="BibDisplayTitleReport"/>
							<xsl:call-template name ="BibDisplayPublisher"/>
							<xsl:call-template name ="BibDisplayCityReport"/>
							<xsl:call-template name ="BibDisplayYearReport"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Art'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name ="BibDisplayArtist"/>
							<i>
								<xsl:call-template name ="BibDisplayTitle"/>
							</i>
							<xsl:call-template name ="strArt"/>
							<xsl:call-template name ="BibDisplayInstitutionArt"/>
							<xsl:call-template name ="BibDisplayYear"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'SoundRecording'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name ="BibDisplayAuthorSoundRec"/>
							<i>
								<xsl:call-template name ="BibDisplayTitle"/>
							</i>
							<xsl:call-template name ="BibDisplayStrSoundRecording"/>
							<xsl:call-template name ="BibDisplayProductionCompanySRec"/>
							<xsl:call-template name ="BibDisplayYearSoundrecording"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Performance'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorPerformance"/>
							<i>
								<xsl:call-template name ="BibDisplayTitlePerformance"/>
							</i>
							<xsl:call-template name="strPerformance"/>
							<xsl:call-template name ="BibDisplayProductionCompanyPerformance"/>
							<xsl:call-template name ="BibDisplayYear"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'InternetSite'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorWebsite"/>
							<xsl:call-template name ="BibDisplayTitleWebSite"/>
							<xsl:call-template name ="BibDisplayProductionCompanywebsite"/>
							<xsl:call-template name = "BibDisplayDayMonthYearWebSiteJournal"/>
							<xsl:call-template name ="BibDisplayStrOnline"/>
							<xsl:call-template name ="BibDisplayURL"/>
							<xsl:call-template name ="BibDisplayAccessedDates"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>


			<xsl:when test="$SourceType = 'Interview'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorInterview"/>
							<i>
								<xsl:call-template name ="BibDisplayTitleInt"/>
							</i>
							<xsl:call-template name="BibDisplayStrInterview"/>
							<xsl:call-template name ="BibDisplayDayMonthYearInterview"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Patent'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorPatent"/>
							<xsl:call-template name ="BibDisplayTitlePatent"/>
							<xsl:call-template name ="BibDisplayCountryRegionPatent"/>
							<xsl:call-template name="BibDisplayPatent"/>
							<xsl:call-template name ="BibDisplayDayMonthYearPatent"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Film'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name ="BibDisplayDirector"/>
							<i>
								<xsl:call-template name ="BibDisplayTitle"/>
							</i>
							<xsl:call-template name ="BibDisplayStrFilm"/>
							<xsl:call-template name ="BibDisplayCountryRegionFilm"/>
							<xsl:call-template name ="BibDisplayProductionCompany"/>
							<xsl:call-template name ="BibDisplayYear"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Case'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<i>
								<xsl:call-template name ="BibDisplayTitleCase"/>
							</i>
							<xsl:call-template name ="BibDisplayYearCase"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'ElectronicSource'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name ="BibDisplayAuthorReport"/>
							<xsl:call-template name ="BibDisplayTitleReport"/>
							<xsl:call-template name ="BibDisplayPublisher"/>
							<xsl:call-template name ="BibDisplayCityReport"/>
							<xsl:call-template name ="BibDisplayYearReport"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>

			<xsl:when test="$SourceType = 'Misc'">
				<xsl:element name="tr">
					<xsl:element name="td">
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:attribute name="width">
							<xsl:value-of select="'1%'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name="BibRefOrder"/>
						</xsl:element>
					</xsl:element>
					<xsl:element name="td">
						<xsl:attribute name="style">
							<xsl:value-of select="'text-align:left'"/>
						</xsl:attribute>
						<xsl:attribute name="valign">
							<xsl:value-of select="'top'"/>
						</xsl:attribute>
						<xsl:element name="p">
							<xsl:call-template name = "BibAddParagraphAttributes"/>
							<xsl:call-template name = "BibDisplayAuthorBook">
								<xsl:with-param name ="DisplayEditorIfAuthorUnavailale" select="'true'" />
							</xsl:call-template>
							<i>
								<xsl:call-template name = "BibDisplayTitleBook"/>
							</i>
							<xsl:call-template name = "BibDisplayEdition"/>
							<xsl:call-template name="BibDisplayVolumeBook"/>
							<xsl:call-template name="BibDisplayEditor"/>
							<xsl:call-template name = "BibDisplayCity"/>
							<xsl:call-template name = "BibDisplayStateProvinceBook"/>
							<xsl:call-template name = "BibDisplayPublisherBC"/>
							<xsl:call-template name = "BibDisplayYearBC"/>
							<xsl:call-template name ="BibDisplayPages"/>
						</xsl:element>
					</xsl:element>
				</xsl:element>
			</xsl:when>
			<xsl:otherwise>
				<xsl:element name="p">
					<xsl:call-template name ="BibAddParagraphAttributes"/>
				</xsl:element>
			</xsl:otherwise>
		</xsl:choose>

	</xsl:template>

	<xsl:template name="Bibliography">
		<html xmlns="http://www.w3.org/TR/REC-html40">
			<head>
				<style>
					p.MsoBibliography, li.MsoBibliography, div.MsoBibliography
				</style>
			</head>
			<body>
				<xsl:element name="table">
					<xsl:attribute name="class">
						<xsl:value-of select="'MsoBibliography'"/>
					</xsl:attribute>
					<xsl:attribute name="width">
						<xsl:value-of select="'100%'"/>
					</xsl:attribute>
					<xsl:for-each select ="b:Bibliography">
						<xsl:apply-templates select="b:Source">
							<xsl:sort select="b:RefOrder" order="ascending" data-type="number"/>
						</xsl:apply-templates>
					</xsl:for-each>
				</xsl:element>
			</body>
		</html>
	</xsl:template>


	<xsl:template name="RefOrder">
		<xsl:value-of select="b:Source/b:RefOrder"/>
	</xsl:template>

	<xsl:template name="BibRefOrder">
		<xsl:call-template name ="templ_prop_SecondaryOpen"/>
		<xsl:value-of select="b:RefOrder"/>
		<xsl:call-template name="templ_prop_SecondaryClose"/>
		<xsl:call-template name ="templ_prop_Space"/>
	</xsl:template>

	<xsl:template name ="displayPageOrPages">
		<xsl:param name ="pages"/>
		<xsl:if test="$pages">
			<xsl:call-template name="templ_prop_ListSeparator"/>
		</xsl:if>
		<xsl:value-of select="$pages"/>
	</xsl:template>

	<xsl:template name="Citation">
		<xsl:for-each select="b:Citation">
			<xsl:variable name="SourceType">
				<xsl:value-of select="b:Source/b:SourceType"/>
			</xsl:variable>
			<xsl:choose>
				<xsl:when test="$SourceType = 'Book' or 
                $SourceType = 'BookSection' or
                $SourceType = 'Film' or
				$SourceType = 'Case' or
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
			    $SourceType = 'InternetSite' or
				$SourceType = 'Patent' or
                $SourceType = 'ConferenceProceedings' ">
					<html xmlns="http://www.w3.org/TR/REC-html40">
						<body>

							<xsl:variable name ="cPages">
								<xsl:value-of select="count(b:Pages)" />
							</xsl:variable>

							<xsl:variable name ="initValueOfPages">
								<xsl:value-of select="b:Pages"/>
							</xsl:variable>

							<xsl:variable name ="pages">
								<xsl:choose>
									<xsl:when test="contains($initValueOfPages, '-')">
										<xsl:value-of select="concat('pp. ',$initValueOfPages)"/>
									</xsl:when>
									<xsl:when test="contains($initValueOfPages, ',')">
										<xsl:value-of select="concat('pp. ',$initValueOfPages)"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="concat('p. ',$initValueOfPages)"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>


							<xsl:if test="b:FirstAuthor">
								<xsl:call-template name ="templ_prop_SecondaryOpen"/>
							</xsl:if>

							<xsl:call-template  name="RefOrder"/>

							<xsl:if test="count(b:Pages)>0">
								<xsl:call-template name="displayPageOrPages" >
									<xsl:with-param name="pages" select ="$pages"/>
								</xsl:call-template>
							</xsl:if>

							<xsl:if test="b:LastAuthor">
								<xsl:call-template name="templ_prop_SecondaryClose"/>
							</xsl:if>

							<xsl:if test="not(b:LastAuthor)">
								<xsl:call-template name="templ_prop_ListSeparator"/>
								<xsl:call-template name ="templ_prop_Space"/>
							</xsl:if>
						</body>
					</html>
				</xsl:when>
			</xsl:choose>
		</xsl:for-each>
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
