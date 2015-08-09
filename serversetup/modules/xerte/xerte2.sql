-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: xerte
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `additional_sharing`
--

DROP TABLE IF EXISTS `additional_sharing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `additional_sharing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `template_id` int(11) DEFAULT NULL,
  `sharing_type` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `extra` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additional_sharing`
--

LOCK TABLES `additional_sharing` WRITE;
/*!40000 ALTER TABLE `additional_sharing` DISABLE KEYS */;
/*!40000 ALTER TABLE `additional_sharing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `folderdetails`
--

DROP TABLE IF EXISTS `folderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `folderdetails` (
  `folder_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `login_id` bigint(20) DEFAULT NULL,
  `folder_parent` bigint(20) DEFAULT NULL,
  `folder_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_created` date DEFAULT '2008-12-08',
  PRIMARY KEY (`folder_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `folderdetails`
--

LOCK TABLES `folderdetails` WRITE;
/*!40000 ALTER TABLE `folderdetails` DISABLE KEYS */;
INSERT INTO `folderdetails` VALUES (1,1,0,'guest2','2008-12-08'),(2,1,0,'recyclebin','2008-12-08'),(4,2,0,'recyclebin','2008-12-08'),(6,3,0,'recyclebin','2008-12-08'),(8,4,0,'recyclebin','2008-12-08');
/*!40000 ALTER TABLE `folderdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ldap`
--

DROP TABLE IF EXISTS `ldap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ldap` (
  `ldap_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ldap_knownname` text COLLATE utf8_unicode_ci NOT NULL,
  `ldap_host` text COLLATE utf8_unicode_ci NOT NULL,
  `ldap_port` text COLLATE utf8_unicode_ci NOT NULL,
  `ldap_username` text COLLATE utf8_unicode_ci,
  `ldap_password` text COLLATE utf8_unicode_ci,
  `ldap_basedn` text COLLATE utf8_unicode_ci,
  `ldap_filter` text COLLATE utf8_unicode_ci,
  `ldap_filter_attr` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`ldap_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ldap`
--

LOCK TABLES `ldap` WRITE;
/*!40000 ALTER TABLE `ldap` DISABLE KEYS */;
INSERT INTO `ldap` VALUES (1,'hydrogen.elements.com','127.0.0.1','389','','','OU=People,DC=elements,DC=com','cn','cn');
/*!40000 ALTER TABLE `ldap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logindetails`
--

DROP TABLE IF EXISTS `logindetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logindetails` (
  `login_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lastlogin` date DEFAULT NULL,
  `firstname` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `surname` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logindetails`
--

LOCK TABLES `logindetails` WRITE;
/*!40000 ALTER TABLE `logindetails` DISABLE KEYS */;
INSERT INTO `logindetails` VALUES (1,'guest2','2015-08-08','Guest','User');
/*!40000 ALTER TABLE `logindetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lti_context`
--

DROP TABLE IF EXISTS `lti_context`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lti_context` (
  `lti_context_key` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `c_internal_id` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `updated_on` datetime NOT NULL,
  PRIMARY KEY (`lti_context_key`),
  KEY `c_internal_id` (`c_internal_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lti_context`
--

LOCK TABLES `lti_context` WRITE;
/*!40000 ALTER TABLE `lti_context` DISABLE KEYS */;
/*!40000 ALTER TABLE `lti_context` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lti_keys`
--

DROP TABLE IF EXISTS `lti_keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lti_keys` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `oauth_consumer_key` char(255) COLLATE utf8_unicode_ci NOT NULL,
  `secret` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `context_id` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `deleted` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oauth_consumer_key` (`oauth_consumer_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lti_keys`
--

LOCK TABLES `lti_keys` WRITE;
/*!40000 ALTER TABLE `lti_keys` DISABLE KEYS */;
/*!40000 ALTER TABLE `lti_keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lti_resource`
--

DROP TABLE IF EXISTS `lti_resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lti_resource` (
  `lti_resource_key` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `internal_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `internal_type` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`lti_resource_key`),
  KEY `destination2` (`internal_type`),
  KEY `destination` (`internal_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lti_resource`
--

LOCK TABLES `lti_resource` WRITE;
/*!40000 ALTER TABLE `lti_resource` DISABLE KEYS */;
/*!40000 ALTER TABLE `lti_resource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lti_user`
--

DROP TABLE IF EXISTS `lti_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lti_user` (
  `lti_user_key` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `lti_user_equ` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `updated_on` datetime NOT NULL,
  PRIMARY KEY (`lti_user_key`),
  KEY `lti_user_equ` (`lti_user_equ`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lti_user`
--

LOCK TABLES `lti_user` WRITE;
/*!40000 ALTER TABLE `lti_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `lti_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `originaltemplatesdetails`
--

DROP TABLE IF EXISTS `originaltemplatesdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `originaltemplatesdetails` (
  `template_type_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `template_framework` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `template_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_uploaded` date DEFAULT NULL,
  `display_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `display_id` bigint(20) DEFAULT NULL,
  `access_rights` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`template_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `originaltemplatesdetails`
--

LOCK TABLES `originaltemplatesdetails` WRITE;
/*!40000 ALTER TABLE `originaltemplatesdetails` DISABLE KEYS */;
INSERT INTO `originaltemplatesdetails` VALUES (5,'xerte','Nottingham','A flexible template for creating interactive learning objects.','2009-09-02','Xerte Online Toolkit',0,'*',1),(8,'xerte','Rss','Easily create and maintain an RSS Feed.','2008-04-02','RSS Feed',0,'*',1),(14,'xerte','multipersp','A template for creating learning objects to present multiple perspectives on a topic','2009-07-08','Multiple Perspectives',0,'*',0),(15,'xerte','mediaInteractions','A  template for presenting a piece of media and creating a series of interactions','2009-09-01','Media Interactions',0,'*',0),(16,'site','site','A responsive template for delivering content to all devices.','2009-04-02','Bootstrap Template',0,'*',1),(17,'decision','decision','A template for presenting a series of questions to reach a solution to a problem.','2009-01-01','Decision Tree Template',0,'*',1);
/*!40000 ALTER TABLE `originaltemplatesdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `play_security_details`
--

DROP TABLE IF EXISTS `play_security_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `play_security_details` (
  `security_id` int(11) NOT NULL AUTO_INCREMENT,
  `security_setting` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `security_data` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `security_info` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`security_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `play_security_details`
--

LOCK TABLES `play_security_details` WRITE;
/*!40000 ALTER TABLE `play_security_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `play_security_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sitedetails`
--

DROP TABLE IF EXISTS `sitedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sitedetails` (
  `site_id` int(11) NOT NULL AUTO_INCREMENT,
  `site_url` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apache` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mimetypes` text COLLATE utf8_unicode_ci,
  `site_session_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `LDAP_preference` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `LDAP_filter` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `integration_config_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `admin_username` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `admin_password` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `site_title` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `site_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `site_logo` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `organisational_logo` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `welcome_message` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `site_text` text COLLATE utf8_unicode_ci,
  `news_text` text COLLATE utf8_unicode_ci,
  `pod_one` text COLLATE utf8_unicode_ci,
  `pod_two` text COLLATE utf8_unicode_ci,
  `copyright` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rss_title` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `synd_publisher` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `synd_rights` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `synd_license` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `demonstration_page` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `form_string` text COLLATE utf8_unicode_ci,
  `peer_form_string` text COLLATE utf8_unicode_ci,
  `module_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website_code_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `users_file_area_short` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `php_library_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `import_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `root_file_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `play_edit_preview_query` text COLLATE utf8_unicode_ci,
  `error_log_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email_error_list` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `error_log_message` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `max_error_size` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `error_email_message` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ldap_host` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ldap_port` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bind_pwd` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `basedn` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bind_dn` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `flash_save_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `flash_upload_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `flash_preview_check_path` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `flash_flv_skin` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `site_email_account` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `headers` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email_to_add_to_username` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `proxy1` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `port1` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `feedback_list` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`site_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sitedetails`
--

LOCK TABLES `sitedetails` WRITE;
/*!40000 ALTER TABLE `sitedetails` DISABLE KEYS */;
INSERT INTO `sitedetails` VALUES (1,'https://elearning.elements.com/xerte/','false','text/xml,application/msword,application/x-shockwave-flash,image/jpeg,image/pjpeg,image/png,image/gif,image/x-png,audio/mpeg,application/vnd.ms-excel,application/pdf,application/vnd.ms-powerpoint,video/x-ms-wmv,text/html,video/mp4,video/avi,audio/wav,text/plain,video/quicktime,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.presentationml.presentation','XERTE_TOOLKITS','sAMAccountName','cn','','admin','admin','Welcome to Xerte Online Toolkits','Xerte Online Toolkits','website_code/images/xerteLogo.jpg','website_code/images/UofNLogo.jpg','Welcome to Xerte Online Toolkits','Welcome to the toolkits front page, developed by the Apereo Foundation','PHAgY2xhc3M9Im5ld3NfdGl0bGUiPk90aGVyIHJlc291cmNlczwvcD48cCBjbGFzcz0ibmV3c19zdG9yeSI+PGEgaHJlZj0iIj5TaXRlIDE8L2E+PC9wPjxwIGNsYXNzPSJuZXdzX3N0b3J5Ij48YSBocmVmPSIiPlNpdGUgMjwvYT48L3A+PHAgY2xhc3M9Im5ld3Nfc3RvcnkiPjxhIGhyZWY9IiI+U2l0ZSAzPC9hPjwvcD4=','PHAgY2xhc3M9Im5ld3NfdGl0bGUiPlJlc291cmNlczwvcD48cCBjbGFzcz0iZGVtbyI+PGEgaHJlZj0iaHR0cDovL3d3dy54ZXJ0ZS5vcmcudWsiPkNvbW11bml0eSBSZXNvdXJjZXM8L2E+PGJyIC8+VGhlIFhlcnRlIHVzZXIgY29tbXVuaXR5IHdlYnNpdGUuPC9wPjxwIGNsYXNzPSJkZW1vIj48YSBocmVmPSJodHRwOi8vd3d3Lm5vdHRpbmdoYW0uYWMudWsvdG9vbGtpdHMvcGxheV81NjAiPkxlYXJuaW5nIE9iamVjdCBEZW1vPC9hPjxiciAvPkEgY29tcHJlaGVuc2l2ZSBkZW1vIG9mIGFsbCB0aGUgcGFnZSB0ZW1wbGF0ZXMuPC9wPg==','PHAgY2xhc3M9Im5ld3NfdGl0bGUiPldhbnQgdG8gc2hhcmUgc29tZSB0aG91Z2h0cz88L3A+PHAgY2xhc3M9ImdlbmVyYWwiPklmIHlvdSBoYXZlIGFueSBxdWVzdGlvbnMsIHJlcXVlc3RzIGZvciBoZWxwLCBpZGVhcyBmb3IgbmV3IHByb2plY3RzIG9yIHByb2JsZW1zIHRvIHJlcG9ydCwgdGhlbiBwbGVhc2UgZ2V0IGluIHRvdWNoLjwvcD48cCBjbGFzcz0iZ2VuZXJhbCI+UGxlYXNlIHVzZSBvdXIgPGEgaHJlZj0iZmVlZGJhY2svIiBzdHlsZT0iY29sb3I6IzAwMCI+RmVlZGJhY2sgRm9ybTwvYT48L3A+','Copyright Apereo Foundation 2015','Xerte Online Toolkits RSS Feed','elements.com','Licensed under a Creative Commons Attribution - NonCommercial-ShareAlike 2.0 Licence - see http://creativecommons.org/licenses/by-nc-sa/2.0/uk/','Licensed under a Creative Commons Attribution - NonCommercial-ShareAlike 2.0 Licence - see http://creativecommons.org/licenses/by-nc-sa/2.0/uk/','modules/xerte/training/toolkits.htm','PGh0bWw+PGJvZHk+PGNlbnRlcj48cD48Zm9ybSBtZXRob2Q9InBvc3QiIGFjdGlvbj0iIj48cD5Vc2VybmFtZSA8aW5wdXQgdHlwZT0idGV4dCIgc2l6ZT0iMjAiIG1heGxlbmd0aD0iMTIiIG5hbWU9ImxvZ2luIiAvPjwvcD48cD5QYXNzd29yZCA8aW5wdXQgdHlwZT0icGFzc3dvcmQiIHNpemU9IjIwIiBtYXhsZW5ndGg9IjM2IiBuYW1lPSJwYXNzd29yZCIgLz48L3A+PHA+PGlucHV0IHR5cGU9ImltYWdlIiBzcmM9IndlYnNpdGVfY29kZS9pbWFnZXMvQnR0bl9Mb2dpbk9mZi5naWYiIG9ubW91c2VvdmVyPSJ0aGlzLnNyYz0nd2Vic2l0ZV9jb2RlL2ltYWdlcy9CdHRuX0xvZ2luT24uZ2lmJyIgb25tb3VzZWRvd249InRoaXMuc3JjPSd3ZWJzaXRlX2NvZGUvaW1hZ2VzL0J0dG5fTG9naW5DbGljay5naWYnIiBvbm1vdXNlb3V0PSJ0aGlzLnNyYz0nd2Vic2l0ZV9jb2RlL2ltYWdlcy9CdHRuX0xvZ2luT2ZmLmdpZiciIC8+PC9wPg==','PGh0bWw+PGJvZHk+PGNlbnRlcj48cD48Zm9ybSBtZXRob2Q9InBvc3QiIGFjdGlvbj0iIj48cD5QYXNzd29yZCA8aW5wdXQgdHlwZT0icGFzc3dvcmQiIHNpemU9IjIwIiBtYXhsZW5ndGg9IjM2IiBuYW1lPSJwYXNzd29yZCIgLz48L3A+PHA+PGlucHV0IHR5cGU9ImltYWdlIiBzcmM9IndlYnNpdGVfY29kZS9pbWFnZXMvQnR0bl9Mb2dpbk9mZi5naWYiIG9ubW91c2VvdmVyPSJ0aGlzLnNyYz0nd2Vic2l0ZV9jb2RlL2ltYWdlcy9CdHRuX0xvZ2luT24uZ2lmJyIgb25tb3VzZWRvd249InRoaXMuc3JjPSd3ZWJzaXRlX2NvZGUvaW1hZ2VzL0J0dG5fTG9naW5DbGljay5naWYnIiBvbm1vdXNlb3V0PSJ0aGlzLnNyYz0nd2Vic2l0ZV9jb2RlL2ltYWdlcy9CdHRuX0xvZ2luT2ZmLmdpZiciIC8+PC9wPg==','modules/','website_code/','USER-FILES/','website_code/php/','/var/www/html/xerte/import/','/var/www/html/xerte/','c2VsZWN0ICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gIm9yaWdpbmFsdGVtcGxhdGVzZGV0YWlscy50ZW1wbGF0ZV9uYW1lLCAiIC4gJHhlcnRlX3Rvb2xraXRzX3NpdGUtPmRhdGFiYXNlX3RhYmxlX3ByZWZpeCAuICJsb2dpbmRldGFpbHMudXNlcm5hbWUsICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gIm9yaWdpbmFsdGVtcGxhdGVzZGV0YWlscy50ZW1wbGF0ZV9mcmFtZXdvcmssICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlcmlnaHRzLnVzZXJfaWQsICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlcmlnaHRzLmZvbGRlciwgIiAuICR4ZXJ0ZV90b29sa2l0c19zaXRlLT5kYXRhYmFzZV90YWJsZV9wcmVmaXggLiAidGVtcGxhdGVyaWdodHMudGVtcGxhdGVfaWQsICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlZGV0YWlscy5hY2Nlc3NfdG9fd2hvbSBmcm9tICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gIm9yaWdpbmFsdGVtcGxhdGVzZGV0YWlscywgIiAuICR4ZXJ0ZV90b29sa2l0c19zaXRlLT5kYXRhYmFzZV90YWJsZV9wcmVmaXggLiAidGVtcGxhdGVyaWdodHMsICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlZGV0YWlscywgIiAuICR4ZXJ0ZV90b29sa2l0c19zaXRlLT5kYXRhYmFzZV90YWJsZV9wcmVmaXggLiAibG9naW5kZXRhaWxzIHdoZXJlICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlZGV0YWlscy50ZW1wbGF0ZV90eXBlX2lkID0gIiAuICR4ZXJ0ZV90b29sa2l0c19zaXRlLT5kYXRhYmFzZV90YWJsZV9wcmVmaXggLiAib3JpZ2luYWx0ZW1wbGF0ZXNkZXRhaWxzLnRlbXBsYXRlX3R5cGVfaWQgYW5kICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlZGV0YWlscy5jcmVhdG9yX2lkID0gIiAuICR4ZXJ0ZV90b29sa2l0c19zaXRlLT5kYXRhYmFzZV90YWJsZV9wcmVmaXggLiAibG9naW5kZXRhaWxzLmxvZ2luX2lkIGFuZCAiIC4gJHhlcnRlX3Rvb2xraXRzX3NpdGUtPmRhdGFiYXNlX3RhYmxlX3ByZWZpeCAuICJ0ZW1wbGF0ZXJpZ2h0cy50ZW1wbGF0ZV9pZCA9ICIgLiAkeGVydGVfdG9vbGtpdHNfc2l0ZS0+ZGF0YWJhc2VfdGFibGVfcHJlZml4IC4gInRlbXBsYXRlZGV0YWlscy50ZW1wbGF0ZV9pZCBhbmQgIiAuICR4ZXJ0ZV90b29sa2l0c19zaXRlLT5kYXRhYmFzZV90YWJsZV9wcmVmaXggLiAidGVtcGxhdGVyaWdodHMudGVtcGxhdGVfaWQ9IlRFTVBMQVRFX0lEX1RPX1JFUExBQ0UiIGFuZCByb2xlPSJjcmVhdG9yIg==','error_logs/','','false','10','false','127.0.0.1','389','','OU=People,DC=elements,DC=com','','modules/xerte/engine/save.php','upload.php?path=','modules/xerte/engine/file_exists.php','modules/xerte/engine/tools/SteelOverAll.swf','','','','','','');
/*!40000 ALTER TABLE `sitedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `syndicationcategories`
--

DROP TABLE IF EXISTS `syndicationcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `syndicationcategories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `syndicationcategories`
--

LOCK TABLES `syndicationcategories` WRITE;
/*!40000 ALTER TABLE `syndicationcategories` DISABLE KEYS */;
INSERT INTO `syndicationcategories` VALUES (1,'American and Canadian Studies'),(2,'Biology'),(3,'Biomedical Sciences'),(4,'Biosciences'),(5,'Built Environment, The'),(6,'Centre for English Language Education'),(7,'Chemistry'),(9,'Community Health Sciences'),(10,'Computer Science'),(11,'Contemporary Chinese Studies'),(12,'Economics'),(13,'Education'),(14,'English Studies'),(15,'Geography'),(16,'Medicine and Health'),(17,'History'),(18,'Humanities'),(20,'Mathematical Sciences'),(21,'Modern Languages and Cultures'),(22,'Nursing, Midwifery and Physiotherapy'),(23,'Pharmacy'),(24,'Physics & Astronomy'),(25,'Politics and International Relations'),(26,'Psychology'),(27,'Sociology & Social Policy'),(28,'Veterinary Medicine and Science');
/*!40000 ALTER TABLE `syndicationcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `syndicationlicenses`
--

DROP TABLE IF EXISTS `syndicationlicenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `syndicationlicenses` (
  `license_id` int(11) NOT NULL AUTO_INCREMENT,
  `license_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`license_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `syndicationlicenses`
--

LOCK TABLES `syndicationlicenses` WRITE;
/*!40000 ALTER TABLE `syndicationlicenses` DISABLE KEYS */;
INSERT INTO `syndicationlicenses` VALUES (6,'Creative Commons Attribution-ShareAlike'),(5,'Creative Commons Attribution-NonCommercial-ShareAlike'),(4,'Creative Commons Attribution-NonCommercial'),(3,'Creative Commons Attribution-NonCommercial-NoDerivs'),(2,'Creative Commons Attribution-NoDerivs');
/*!40000 ALTER TABLE `syndicationlicenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `templatedetails`
--

DROP TABLE IF EXISTS `templatedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `templatedetails` (
  `template_id` bigint(20) NOT NULL,
  `creator_id` bigint(20) DEFAULT NULL,
  `template_type_id` bigint(20) DEFAULT NULL,
  `template_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_created` date DEFAULT NULL,
  `date_modified` date DEFAULT NULL,
  `date_accessed` date DEFAULT NULL,
  `number_of_uses` bigint(20) DEFAULT NULL,
  `access_to_whom` text COLLATE utf8_unicode_ci,
  `extra_flags` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`template_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templatedetails`
--

LOCK TABLES `templatedetails` WRITE;
/*!40000 ALTER TABLE `templatedetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `templatedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `templaterights`
--

DROP TABLE IF EXISTS `templaterights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `templaterights` (
  `template_id` bigint(20) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `role` text COLLATE utf8_unicode_ci,
  `folder` bigint(20) DEFAULT NULL,
  `notes` char(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templaterights`
--

--
-- Table structure for table `templatesyndication`
--

DROP TABLE IF EXISTS `templatesyndication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `templatesyndication` (
  `template_id` bigint(20) NOT NULL,
  `description` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `keywords` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rss` text COLLATE utf8_unicode_ci,
  `export` text COLLATE utf8_unicode_ci,
  `syndication` text COLLATE utf8_unicode_ci,
  `category` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `license` char(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templatesyndication`
--

LOCK TABLES `templatesyndication` WRITE;
/*!40000 ALTER TABLE `templatesyndication` DISABLE KEYS */;
/*!40000 ALTER TABLE `templatesyndication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `firstname` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `surname` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`iduser`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_sessions`
--

DROP TABLE IF EXISTS `user_sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_sessions` (
  `session_id` varchar(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `access` int(10) unsigned DEFAULT NULL,
  `data` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`session_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_sessions`
--

LOCK TABLES `user_sessions` WRITE;
/*!40000 ALTER TABLE `user_sessions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_sessions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-08 14:30:39
