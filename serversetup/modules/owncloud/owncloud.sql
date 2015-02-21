-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: owncloud
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.04.1

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
-- Table structure for table `oc_activity`
--

DROP TABLE IF EXISTS `oc_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_activity` (
  `activity_id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` int(11) NOT NULL DEFAULT '0',
  `priority` int(11) NOT NULL DEFAULT '0',
  `type` varchar(255) COLLATE utf8_bin NOT NULL,
  `user` varchar(64) COLLATE utf8_bin NOT NULL,
  `affecteduser` varchar(64) COLLATE utf8_bin NOT NULL,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `subject` varchar(255) COLLATE utf8_bin NOT NULL,
  `subjectparams` varchar(255) COLLATE utf8_bin NOT NULL,
  `message` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `messageparams` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `file` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `link` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`activity_id`),
  KEY `activity_user_time` (`affecteduser`,`timestamp`),
  KEY `activity_filter_by` (`affecteduser`,`user`,`timestamp`),
  KEY `activity_filter_app` (`affecteduser`,`app`,`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity`
--

LOCK TABLES `oc_activity` WRITE;
/*!40000 ALTER TABLE `oc_activity` DISABLE KEYS */;
INSERT INTO `oc_activity` VALUES (1,1424507999,40,'file_created','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','files','created_self','a:1:{i:0;s:23:\"/home/New text file.txt\";}','','a:0:{}','/home/New text file.txt','https://CHANGETHISREALM/owncloud/index.php/apps/files?dir=%2Fhome'),(2,1424508060,40,'file_created','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','files','created_self','a:1:{i:0;s:17:\"/New Document.odt\";}','','a:0:{}','/New Document.odt','https://CHANGETHISREALM/owncloud/index.php/apps/files?dir=%2F'),(3,1424508091,40,'file_changed','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','files','changed_self','a:1:{i:0;s:17:\"/New Document.odt\";}','','a:0:{}','/New Document.odt','https://CHANGETHISREALM/owncloud/index.php/apps/files?dir=%2F'),(4,1424508098,40,'file_created','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','files','created_self','a:1:{i:0;s:21:\"/New Document (2).odt\";}','','a:0:{}','/New Document (2).odt','https://CHANGETHISREALM/owncloud/index.php/apps/files?dir=%2F'),(5,1424508249,40,'file_created','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','files','created_self','a:1:{i:0;s:14:\"/home/test.odt\";}','','a:0:{}','/home/test.odt','https://CHANGETHISREALM/owncloud/index.php/apps/files?dir=%2Fhome'),(6,1424508267,40,'file_changed','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','files','changed_self','a:1:{i:0;s:14:\"/home/test.odt\";}','','a:0:{}','/home/test.odt','https://CHANGETHISREALM/owncloud/index.php/apps/files?dir=%2Fhome');
/*!40000 ALTER TABLE `oc_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_activity_mq`
--

DROP TABLE IF EXISTS `oc_activity_mq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_activity_mq` (
  `mail_id` int(11) NOT NULL AUTO_INCREMENT,
  `amq_timestamp` int(11) NOT NULL DEFAULT '0',
  `amq_latest_send` int(11) NOT NULL DEFAULT '0',
  `amq_type` varchar(255) COLLATE utf8_bin NOT NULL,
  `amq_affecteduser` varchar(64) COLLATE utf8_bin NOT NULL,
  `amq_appid` varchar(255) COLLATE utf8_bin NOT NULL,
  `amq_subject` varchar(255) COLLATE utf8_bin NOT NULL,
  `amq_subjectparams` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`mail_id`),
  KEY `amp_user` (`amq_affecteduser`),
  KEY `amp_latest_send_time` (`amq_latest_send`),
  KEY `amp_timestamp_time` (`amq_timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity_mq`
--

LOCK TABLES `oc_activity_mq` WRITE;
/*!40000 ALTER TABLE `oc_activity_mq` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_activity_mq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_appconfig`
--

DROP TABLE IF EXISTS `oc_appconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_appconfig` (
  `appid` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `configkey` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `configvalue` longtext COLLATE utf8_bin,
  PRIMARY KEY (`appid`,`configkey`),
  KEY `appconfig_config_key_index` (`configkey`),
  KEY `appconfig_appid_key` (`appid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_appconfig`
--

LOCK TABLES `oc_appconfig` WRITE;
/*!40000 ALTER TABLE `oc_appconfig` DISABLE KEYS */;
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','1.2.0'),('activity','ocsid','166038'),('activity','types','filesystem'),('backgroundjob','lastjob','2'),('bookmarks','enabled','yes'),('bookmarks','installed_version','0.4'),('bookmarks','ocsid','168710'),('bookmarks','types',''),('calendar','enabled','yes'),('calendar','installed_version','0.6.4'),('calendar','ocsid','168707'),('calendar','types',''),('contacts','enabled','yes'),('contacts','installed_version','0.3.0.18'),('contacts','ocsid','168708'),('contacts','types',''),('core','global_cache_gc_lastrun','1424508184'),('core','installedat','1424501499.0977'),('core','lastcron','1424508304'),('core','lastupdateResult','{\"version\":{},\"versionstring\":{},\"url\":{},\"web\":{}}'),('core','lastupdatedat','1424507953'),('core','public_caldav','calendar/share.php'),('core','public_calendar','calendar/share.php'),('core','public_documents','documents/public.php'),('core','public_files','files_sharing/public.php'),('core','public_gallery','gallery/public.php'),('core','public_webdav','files_sharing/publicwebdav.php'),('core','remote_caldav','calendar/appinfo/remote.php'),('core','remote_calendar','calendar/appinfo/remote.php'),('core','remote_carddav','contacts/appinfo/remote.php'),('core','remote_contacts','contacts/appinfo/remote.php'),('core','remote_files','files/appinfo/remote.php'),('core','remote_webdav','files/appinfo/remote.php'),('documents','enabled','yes'),('documents','installed_version','0.9.0'),('documents','ocsid','168711'),('documents','types',''),('files','enabled','yes'),('files','installed_version','1.1.9'),('files','types','filesystem'),('files_external','/home','1424502932'),('files_external','/mwilson12','1424502790'),('files_external','/test','1424502802'),('files_external','allow_user_mounting','yes'),('files_external','enabled','yes'),('files_external','installed_version','0.2.3'),('files_external','ocsid','166048'),('files_external','types','filesystem'),('files_external','user_mounting_backends','\\OC\\Files\\Storage\\Dropbox,\\OC\\Files\\Storage\\Google,\\OC\\Files\\Storage\\OwnCloud,\\OC\\Files\\Storage\\SMB_OC'),('files_locking','enabled','yes'),('files_locking','installed_version',''),('files_locking','types','filesystem'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','0.7'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','0.6.0'),('files_sharing','ocsid','166050'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','0.4'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','0.6.2'),('files_trashbin','ocsid','166052'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.0.5'),('files_versions','ocsid','166053'),('files_versions','types','filesystem'),('files_videoviewer','enabled','yes'),('files_videoviewer','installed_version','0.1.3'),('files_videoviewer','ocsid','166054'),('files_videoviewer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','1.1'),('firstrunwizard','ocsid','166055'),('firstrunwizard','types',''),('gallery','enabled','yes'),('gallery','installed_version','0.6.0'),('gallery','ocsid','166056'),('gallery','types',''),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','0.2'),('provisioning_api','types','filesystem'),('templateeditor','enabled','yes'),('templateeditor','installed_version','0.1'),('templateeditor','types',''),('updater','enabled','yes'),('updater','installed_version','0.4'),('updater','ocsid','166059'),('updater','types',''),('user_ldap','cleanUpJobOffset','0'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','0.5.0'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayname'),('user_ldap','ldap_dn',''),('user_ldap','ldap_email_attr','mail'),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr',''),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','member'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','ldap://127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=person)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_nocase','0'),('user_ldap','ldap_override_main_server','0'),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','person'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=person)))'),('user_ldap','ocsid','166061'),('user_ldap','types','authentication');
/*!40000 ALTER TABLE `oc_appconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_bookmarks`
--

DROP TABLE IF EXISTS `oc_bookmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_bookmarks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(4096) COLLATE utf8_bin NOT NULL DEFAULT '',
  `title` varchar(140) COLLATE utf8_bin NOT NULL DEFAULT '',
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `description` varchar(4096) COLLATE utf8_bin NOT NULL DEFAULT '',
  `public` smallint(6) DEFAULT '0',
  `added` int(10) unsigned DEFAULT '0',
  `lastmodified` int(10) unsigned DEFAULT '0',
  `clickcount` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_bookmarks`
--

LOCK TABLES `oc_bookmarks` WRITE;
/*!40000 ALTER TABLE `oc_bookmarks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_bookmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_bookmarks_tags`
--

DROP TABLE IF EXISTS `oc_bookmarks_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_bookmarks_tags` (
  `bookmark_id` bigint(20) DEFAULT NULL,
  `tag` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  UNIQUE KEY `bookmark_tag` (`bookmark_id`,`tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_bookmarks_tags`
--

LOCK TABLES `oc_bookmarks_tags` WRITE;
/*!40000 ALTER TABLE `oc_bookmarks_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_bookmarks_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_clndr_calendars`
--

DROP TABLE IF EXISTS `oc_clndr_calendars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_clndr_calendars` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `displayname` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `active` int(11) NOT NULL DEFAULT '1',
  `ctag` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarorder` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarcolor` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `timezone` longtext COLLATE utf8_bin,
  `components` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_clndr_calendars`
--

LOCK TABLES `oc_clndr_calendars` WRITE;
/*!40000 ALTER TABLE `oc_clndr_calendars` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_clndr_calendars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_clndr_objects`
--

DROP TABLE IF EXISTS `oc_clndr_objects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_clndr_objects` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `calendarid` int(10) unsigned NOT NULL DEFAULT '0',
  `objecttype` varchar(40) COLLATE utf8_bin NOT NULL DEFAULT '',
  `startdate` datetime DEFAULT '1970-01-01 00:00:00',
  `enddate` datetime DEFAULT '1970-01-01 00:00:00',
  `repeating` int(11) DEFAULT '0',
  `summary` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `calendardata` longtext COLLATE utf8_bin,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `lastmodified` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_clndr_objects`
--

LOCK TABLES `oc_clndr_objects` WRITE;
/*!40000 ALTER TABLE `oc_clndr_objects` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_clndr_objects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_clndr_repeat`
--

DROP TABLE IF EXISTS `oc_clndr_repeat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_clndr_repeat` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `eventid` int(10) unsigned NOT NULL DEFAULT '0',
  `calid` int(10) unsigned NOT NULL DEFAULT '0',
  `startdate` datetime DEFAULT '1970-01-01 00:00:00',
  `enddate` datetime DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_clndr_repeat`
--

LOCK TABLES `oc_clndr_repeat` WRITE;
/*!40000 ALTER TABLE `oc_clndr_repeat` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_clndr_repeat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_clndr_share_calendar`
--

DROP TABLE IF EXISTS `oc_clndr_share_calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_clndr_share_calendar` (
  `owner` varchar(255) COLLATE utf8_bin NOT NULL,
  `share` varchar(255) COLLATE utf8_bin NOT NULL,
  `sharetype` varchar(6) COLLATE utf8_bin NOT NULL,
  `calendarid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `permissions` smallint(6) NOT NULL,
  `active` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_clndr_share_calendar`
--

LOCK TABLES `oc_clndr_share_calendar` WRITE;
/*!40000 ALTER TABLE `oc_clndr_share_calendar` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_clndr_share_calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_clndr_share_event`
--

DROP TABLE IF EXISTS `oc_clndr_share_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_clndr_share_event` (
  `owner` varchar(255) COLLATE utf8_bin NOT NULL,
  `share` varchar(255) COLLATE utf8_bin NOT NULL,
  `sharetype` varchar(6) COLLATE utf8_bin NOT NULL,
  `eventid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `permissions` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_clndr_share_event`
--

LOCK TABLES `oc_clndr_share_event` WRITE;
/*!40000 ALTER TABLE `oc_clndr_share_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_clndr_share_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_contacts_addressbooks`
--

DROP TABLE IF EXISTS `oc_contacts_addressbooks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_contacts_addressbooks` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `displayname` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `uri` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `ctag` int(10) unsigned NOT NULL DEFAULT '1',
  `active` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `c_addressbook_userid_index` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_contacts_addressbooks`
--

LOCK TABLES `oc_contacts_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_contacts_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_contacts_addressbooks` VALUES (1,'admin','Contacts','contacts','',1424507946,1),(2,'5D26E309-DDA4-40D4-86D6-EF71C36938DE','Contacts','contacts','',1424507983,1);
/*!40000 ALTER TABLE `oc_contacts_addressbooks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_contacts_cards`
--

DROP TABLE IF EXISTS `oc_contacts_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_contacts_cards` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `addressbookid` int(10) unsigned NOT NULL DEFAULT '0',
  `fullname` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `carddata` longtext COLLATE utf8_bin,
  `uri` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `c_addressbookid_index` (`addressbookid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_contacts_cards`
--

LOCK TABLES `oc_contacts_cards` WRITE;
/*!40000 ALTER TABLE `oc_contacts_cards` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_contacts_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_contacts_cards_properties`
--

DROP TABLE IF EXISTS `oc_contacts_cards_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_contacts_cards_properties` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `contactid` int(10) unsigned NOT NULL DEFAULT '0',
  `name` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `value` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `preferred` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `cp_contactid_index` (`contactid`),
  KEY `cp_name_index` (`name`),
  KEY `cp_value_index` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_contacts_cards_properties`
--

LOCK TABLES `oc_contacts_cards_properties` WRITE;
/*!40000 ALTER TABLE `oc_contacts_cards_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_contacts_cards_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_documents_invite`
--

DROP TABLE IF EXISTS `oc_documents_invite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_documents_invite` (
  `es_id` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Related editing session id',
  `uid` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `status` smallint(6) DEFAULT '0',
  `sent_on` int(10) unsigned DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_invite`
--

LOCK TABLES `oc_documents_invite` WRITE;
/*!40000 ALTER TABLE `oc_documents_invite` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_documents_invite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_documents_member`
--

DROP TABLE IF EXISTS `oc_documents_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_documents_member` (
  `member_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Unique per user and session',
  `es_id` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Related editing session id',
  `uid` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `color` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `last_activity` int(10) unsigned DEFAULT NULL,
  `is_guest` smallint(5) unsigned NOT NULL DEFAULT '0',
  `token` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `status` smallint(5) unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_member`
--

LOCK TABLES `oc_documents_member` WRITE;
/*!40000 ALTER TABLE `oc_documents_member` DISABLE KEYS */;
INSERT INTO `oc_documents_member` VALUES (2,'np0nzjsm6tg74iuwsv9h8gkmgb3tio','5D26E309-DDA4-40D4-86D6-EF71C36938DE','#0f9965',1424508109,0,'',2),(3,'d6vakpi4fc9lm249898348way0p73n','5D26E309-DDA4-40D4-86D6-EF71C36938DE','#0f9965',1424508166,0,'',2),(4,'np0nzjsm6tg74iuwsv9h8gkmgb3tio','5D26E309-DDA4-40D4-86D6-EF71C36938DE','#0f9965',1424508201,0,'',2),(5,'np0nzjsm6tg74iuwsv9h8gkmgb3tio','5D26E309-DDA4-40D4-86D6-EF71C36938DE','#0f9965',1424508222,0,'',2);
/*!40000 ALTER TABLE `oc_documents_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_documents_op`
--

DROP TABLE IF EXISTS `oc_documents_op`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_documents_op` (
  `seq` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Sequence number',
  `es_id` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Editing session id',
  `member` int(10) unsigned NOT NULL DEFAULT '1' COMMENT 'User and time specific',
  `optype` varchar(64) COLLATE utf8_bin DEFAULT NULL COMMENT 'Operation type',
  `opspec` longtext COLLATE utf8_bin COMMENT 'json-string',
  PRIMARY KEY (`seq`),
  UNIQUE KEY `documents_op_eis_idx` (`es_id`,`seq`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_op`
--

LOCK TABLES `oc_documents_op` WRITE;
/*!40000 ALTER TABLE `oc_documents_op` DISABLE KEYS */;
INSERT INTO `oc_documents_op` VALUES (30,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',2,'AddMember','{\"optype\":\"AddMember\",\"memberid\":\"2\",\"timestamp\":\"1424508099\",\"setProperties\":{\"fullName\":\"Ian Smith\",\"color\":\"#0f9965\",\"imageUrl\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\",\"uid\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\"}}'),(31,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',2,'AddCursor','{\"optype\":\"AddCursor\",\"memberid\":\"2\",\"timestamp\":1424508100089}'),(32,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',2,'RemoveCursor','{\"optype\":\"RemoveCursor\",\"memberid\":\"2\",\"timestamp\":1424508109793}'),(33,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',2,'RemoveMember','{\"optype\":\"RemoveMember\",\"memberid\":\"2\",\"timestamp\":\"1424508110\"}'),(34,'d6vakpi4fc9lm249898348way0p73n',3,'AddMember','{\"optype\":\"AddMember\",\"memberid\":\"3\",\"timestamp\":\"1424508161\",\"setProperties\":{\"fullName\":\"Ian Smith\",\"color\":\"#0f9965\",\"imageUrl\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\",\"uid\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\"}}'),(35,'d6vakpi4fc9lm249898348way0p73n',3,'AddCursor','{\"optype\":\"AddCursor\",\"memberid\":\"3\",\"timestamp\":1424508163111}'),(36,'d6vakpi4fc9lm249898348way0p73n',3,'RemoveCursor','{\"optype\":\"RemoveCursor\",\"memberid\":\"3\",\"timestamp\":1424508165850}'),(37,'d6vakpi4fc9lm249898348way0p73n',3,'RemoveMember','{\"optype\":\"RemoveMember\",\"memberid\":\"3\",\"timestamp\":\"1424508166\"}'),(38,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',4,'AddMember','{\"optype\":\"AddMember\",\"memberid\":\"4\",\"timestamp\":\"1424508192\",\"setProperties\":{\"fullName\":\"Ian Smith\",\"color\":\"#0f9965\",\"imageUrl\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\",\"uid\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\"}}'),(39,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',4,'AddCursor','{\"optype\":\"AddCursor\",\"memberid\":\"4\",\"timestamp\":1424508193450}'),(40,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',4,'RemoveCursor','{\"optype\":\"RemoveCursor\",\"memberid\":\"4\",\"timestamp\":1424508201479}'),(41,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',4,'RemoveMember','{\"optype\":\"RemoveMember\",\"memberid\":\"4\",\"timestamp\":\"1424508202\"}'),(42,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',5,'AddMember','{\"optype\":\"AddMember\",\"memberid\":\"5\",\"timestamp\":\"1424508216\",\"setProperties\":{\"fullName\":\"Ian Smith\",\"color\":\"#0f9965\",\"imageUrl\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\",\"uid\":\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\"}}'),(43,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',5,'AddCursor','{\"optype\":\"AddCursor\",\"memberid\":\"5\",\"timestamp\":1424508217908}'),(44,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',5,'RemoveCursor','{\"optype\":\"RemoveCursor\",\"memberid\":\"5\",\"timestamp\":1424508222716}'),(45,'np0nzjsm6tg74iuwsv9h8gkmgb3tio',5,'RemoveMember','{\"optype\":\"RemoveMember\",\"memberid\":\"5\",\"timestamp\":\"1424508223\"}');
/*!40000 ALTER TABLE `oc_documents_op` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_documents_revisions`
--

DROP TABLE IF EXISTS `oc_documents_revisions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_documents_revisions` (
  `es_id` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Related editing session id',
  `seq_head` int(10) unsigned NOT NULL COMMENT 'Sequence head number',
  `member_id` int(10) unsigned NOT NULL COMMENT 'the member that saved the revision',
  `file_id` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT 'Relative to storage e.g. /welcome.odt',
  `save_hash` varchar(128) COLLATE utf8_bin NOT NULL COMMENT 'used to lookup revision in documents folder of member, eg hash.odt',
  UNIQUE KEY `documents_rev_eis_idx` (`es_id`,`seq_head`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_revisions`
--

LOCK TABLES `oc_documents_revisions` WRITE;
/*!40000 ALTER TABLE `oc_documents_revisions` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_documents_revisions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_documents_session`
--

DROP TABLE IF EXISTS `oc_documents_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_documents_session` (
  `es_id` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Editing session id',
  `genesis_url` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT 'Relative to owner documents storage /welcome.odt',
  `genesis_hash` varchar(128) COLLATE utf8_bin NOT NULL COMMENT 'To be sure the genesis did not change',
  `file_id` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT 'Relative to storage e.g. /welcome.odt',
  `owner` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'oC user who created the session',
  PRIMARY KEY (`es_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_session`
--

LOCK TABLES `oc_documents_session` WRITE;
/*!40000 ALTER TABLE `oc_documents_session` DISABLE KEYS */;
INSERT INTO `oc_documents_session` VALUES ('d6vakpi4fc9lm249898348way0p73n','/documents/f148fa6af17cfad9aa09f8e88baefb2b0950e137.odt','f148fa6af17cfad9aa09f8e88baefb2b0950e137','72','5D26E309-DDA4-40D4-86D6-EF71C36938DE'),('np0nzjsm6tg74iuwsv9h8gkmgb3tio','/documents/5fc55a1f23a1183afaed4d90b50a8a69b3d69719.odt','5fc55a1f23a1183afaed4d90b50a8a69b3d69719','77','5D26E309-DDA4-40D4-86D6-EF71C36938DE');
/*!40000 ALTER TABLE `oc_documents_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_file_map`
--

DROP TABLE IF EXISTS `oc_file_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_file_map` (
  `logic_path` varchar(512) COLLATE utf8_bin NOT NULL DEFAULT '',
  `logic_path_hash` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `physic_path` varchar(512) COLLATE utf8_bin NOT NULL DEFAULT '',
  `physic_path_hash` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`logic_path_hash`),
  UNIQUE KEY `file_map_pp_index` (`physic_path_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_map`
--

LOCK TABLES `oc_file_map` WRITE;
/*!40000 ALTER TABLE `oc_file_map` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_file_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_filecache`
--

DROP TABLE IF EXISTS `oc_filecache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_filecache` (
  `fileid` int(11) NOT NULL AUTO_INCREMENT,
  `storage` int(11) NOT NULL DEFAULT '0',
  `path` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `path_hash` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `parent` int(11) NOT NULL DEFAULT '0',
  `name` varchar(250) COLLATE utf8_bin DEFAULT NULL,
  `mimetype` int(11) NOT NULL DEFAULT '0',
  `mimepart` int(11) NOT NULL DEFAULT '0',
  `size` bigint(20) NOT NULL DEFAULT '0',
  `mtime` int(11) NOT NULL DEFAULT '0',
  `storage_mtime` int(11) NOT NULL DEFAULT '0',
  `encrypted` int(11) NOT NULL DEFAULT '0',
  `unencrypted_size` bigint(20) NOT NULL DEFAULT '0',
  `etag` varchar(40) COLLATE utf8_bin DEFAULT NULL,
  `permissions` int(11) DEFAULT '0',
  PRIMARY KEY (`fileid`),
  UNIQUE KEY `fs_storage_path_hash` (`storage`,`path_hash`),
  KEY `fs_parent_name_hash` (`parent`,`name`),
  KEY `fs_storage_mimetype` (`storage`,`mimetype`),
  KEY `fs_storage_mimepart` (`storage`,`mimepart`),
  KEY `fs_storage_size` (`storage`,`size`,`fileid`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,6038748,1424501500,1424501499,0,0,'54e82afca01bc',23),(2,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1424501499,1424501499,0,0,'54e82afb32ef6',31),(3,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,6038748,1424502943,1424500831,0,0,'54e8309ff2f99',31),(4,1,'files/photos','923e51351db3e8726f22ba0fa1c04d5a',3,'photos',2,1,678556,1424501500,1424500831,0,0,'54e82afca36d6',31),(5,1,'files/documents','2d30f25cef1a92db784bc537e8bf128d',3,'documents',2,1,23383,1424501500,1424500831,0,0,'54e82afca2579',31),(6,1,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',3,'ownCloudUserManual.pdf',4,3,1572005,1424500831,1424500831,0,0,'8c0764cc10f17a5002037178a130186a',27),(7,1,'files/music','1f8cfec283cd675038bb95b599fdc75a',3,'music',2,1,3764804,1424501500,1424500831,0,0,'54e82afca1570',31),(8,1,'files/music/projekteva-letitrain.mp3','da7d05a957a2bbbf0e74b12c1b5fcfee',7,'projekteva-letitrain.mp3',6,5,3764804,1424500831,1424500831,0,0,'f8b851c7c09a12a42df426f7b3d14779',27),(9,1,'files/documents/example.odt','f51311bd6910ec7356d79286dcb24dec',5,'example.odt',7,3,23383,1424500831,1424500831,0,0,'6b6799c27b9f9856f99c8d29328f444b',27),(10,1,'files/photos/paris.jpg','65154b90b985bff20d4923f224ca1c33',4,'paris.jpg',9,8,228761,1424500831,1424500831,0,0,'fea5ada417982b79824e13aa07314e51',27),(11,1,'files/photos/squirrel.jpg','e462c24fc17cb1a3fa3bca86d7f89593',4,'squirrel.jpg',9,8,233724,1424500831,1424500831,0,0,'14879684fccd54a70b79c3afbc17a152',27),(12,1,'files/photos/san francisco.jpg','e86e87a4ecd557753734e1d34fbeecec',4,'san francisco.jpg',9,8,216071,1424500831,1424500831,0,0,'ddca345546a73b2b1056629ed31a0e3d',27),(13,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,2486024,1424508266,1424508090,0,0,'54e8456adcda8',23),(14,3,'cache','0fea6a13c52b4d4725368f24b045ca84',13,'cache',2,1,0,1424502420,1424502420,0,0,'54e82e948ac01',31),(15,3,'files','45b963397aa40d4a0063e0d85e4fe7a1',13,'files',2,1,2526709,1424508279,1424508098,0,0,'54e8457718d46',31),(16,3,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',15,'ownCloudUserManual.pdf',4,3,1771241,1424502420,1424502420,0,0,'6363c95eb190d6688f2aee1abc213df3',27),(17,3,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',15,'Documents',2,1,36227,1424502420,1424502420,0,0,'54e82e94e2981',31),(18,3,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',17,'Example.odt',7,3,36227,1424502420,1424502420,0,0,'e385136fa1f8304f556b0c0c4253bc26',27),(19,3,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',15,'Photos',2,1,678556,1424502421,1424502421,0,0,'54e82e950cc08',31),(20,3,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',19,'San Francisco.jpg',9,8,216071,1424502420,1424502420,0,0,'28e4301f2988232519aba57b9ce76bdd',27),(21,3,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',19,'Paris.jpg',9,8,228761,1424502421,1424502421,0,0,'a965e5df57c2fdd85fa16d97463818d1',27),(22,3,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',19,'Squirrel.jpg',9,8,233724,1424502421,1424502421,0,0,'02c65b6f3725d54dcbd634e78cf2a871',27),(23,4,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,2486024,1424502607,1424502607,0,0,'54e82f4fa90ac',23),(24,4,'cache','0fea6a13c52b4d4725368f24b045ca84',23,'cache',2,1,0,1424502607,1424502607,0,0,'54e82f4f68f2a',31),(25,4,'files','45b963397aa40d4a0063e0d85e4fe7a1',23,'files',2,1,2486024,1424503063,1424502607,0,0,'54e831176b8c4',31),(26,4,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',25,'ownCloudUserManual.pdf',4,3,1771241,1424502607,1424502607,0,0,'f2071cb99dbd7001cf74193baec8cbfb',27),(27,4,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',25,'Documents',2,1,36227,1424502607,1424502607,0,0,'54e82f4f8b08f',31),(28,4,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',27,'Example.odt',7,3,36227,1424502607,1424502607,0,0,'c0497830291fdfc0e4324472d707ef74',27),(29,4,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',25,'Photos',2,1,678556,1424502607,1424502607,0,0,'54e82f4fa9ddc',31),(30,4,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',29,'San Francisco.jpg',9,8,216071,1424502607,1424502607,0,0,'0b50bead6864b5b6d3db612013c55af5',27),(31,4,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',29,'Paris.jpg',9,8,228761,1424502607,1424502607,0,0,'1c398b9dae1e521b1c091379811d29e1',27),(32,4,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',29,'Squirrel.jpg',9,8,233724,1424502607,1424502607,0,0,'5ca14c854287652800009d13793520ba',27),(33,6,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,0,0,0,0,'54e831132a647',7),(34,9,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,2486024,1424503072,1424503072,0,0,'54e8312083652',23),(35,9,'cache','0fea6a13c52b4d4725368f24b045ca84',34,'cache',2,1,0,1424503072,1424503072,0,0,'54e8312041173',31),(36,9,'files','45b963397aa40d4a0063e0d85e4fe7a1',34,'files',2,1,2486024,1424503072,1424503072,0,0,'54e8312083b6d',31),(37,9,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',36,'ownCloudUserManual.pdf',4,3,1771241,1424503072,1424503072,0,0,'92e10459b2c55d929c8fc178d4e76d6e',27),(38,9,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',36,'Documents',2,1,36227,1424503072,1424503072,0,0,'54e83120675f0',31),(39,9,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',38,'Example.odt',7,3,36227,1424503072,1424503072,0,0,'f16f75307c11ca78193355d0d70633c6',27),(40,9,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',36,'Photos',2,1,678556,1424503072,1424503072,0,0,'54e831208403e',31),(41,9,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',40,'San Francisco.jpg',9,8,216071,1424503072,1424503072,0,0,'37802280b27a104535860e7e36aaa9cf',27),(42,9,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',40,'Paris.jpg',9,8,228761,1424503072,1424503072,0,0,'17e7acbf4599d306581a87e8e01a4793',27),(43,9,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',40,'Squirrel.jpg',9,8,233724,1424503072,1424503072,0,0,'2e244861f2dca4f71567dacbea21f189',27),(44,10,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,2486024,1424503189,1424503189,0,0,'54e831957e968',23),(45,10,'cache','0fea6a13c52b4d4725368f24b045ca84',44,'cache',2,1,0,1424503189,1424503189,0,0,'54e831953dd1c',31),(46,10,'files','45b963397aa40d4a0063e0d85e4fe7a1',44,'files',2,1,2486024,1424503189,1424503189,0,0,'54e831957f264',31),(47,10,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',46,'ownCloudUserManual.pdf',4,3,1771241,1424503189,1424503189,0,0,'29f3a058c0c66838c2069db8b79831b1',27),(48,10,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',46,'Documents',2,1,36227,1424503189,1424503189,0,0,'54e831955fda3',31),(49,10,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',48,'Example.odt',7,3,36227,1424503189,1424503189,0,0,'584c2c3ebee025779ad4bd964cb22f36',27),(50,10,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',46,'Photos',2,1,678556,1424503189,1424503189,0,0,'54e831957fd24',31),(51,10,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',50,'San Francisco.jpg',9,8,216071,1424503189,1424503189,0,0,'4e562dfa8000fcdcfcd132c51efacbc6',27),(52,10,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',50,'Paris.jpg',9,8,228761,1424503189,1424503189,0,0,'9e3aff295a9521b9d964a02ff4ad8508',27),(53,10,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',50,'Squirrel.jpg',9,8,233724,1424503189,1424503189,0,0,'d8b35d77a561d4a156e57eb76b037322',27),(54,11,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,2486024,1424503510,1424503510,0,0,'54e832d6e79e5',23),(55,11,'cache','0fea6a13c52b4d4725368f24b045ca84',54,'cache',2,1,0,1424503510,1424503510,0,0,'54e832d6a93fb',31),(56,11,'files','45b963397aa40d4a0063e0d85e4fe7a1',54,'files',2,1,2486024,1424506280,1424503510,0,0,'54e83da813c47',31),(57,11,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',56,'ownCloudUserManual.pdf',4,3,1771241,1424503510,1424503510,0,0,'4f0b8258fe0527f39b5b061e2c55b2f3',27),(58,11,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',56,'Documents',2,1,36227,1424503510,1424503510,0,0,'54e832d6cd4c0',31),(59,11,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',58,'Example.odt',7,3,36227,1424503510,1424503510,0,0,'15aa3361a0378f0caf63e238d3283876',27),(60,11,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',56,'Photos',2,1,678556,1424503510,1424503510,0,0,'54e832d6e886e',31),(61,11,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',60,'San Francisco.jpg',9,8,216071,1424503510,1424503510,0,0,'e3179ccca5fe24bbe463a26f3049e562',27),(62,11,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',60,'Paris.jpg',9,8,228761,1424503510,1424503510,0,0,'cc21659425d387682f7ae8579cf282c7',27),(63,11,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',60,'Squirrel.jpg',9,8,233724,1424503510,1424503510,0,0,'4c9421f606c41fdb7f2f9abc7b3e6b6c',27),(64,17,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,1424503552,1424503552,0,0,'54e83da44d6b9',7),(65,17,'test','098f6bcd4621d373cade4e832627b4f6',64,'test',10,3,0,1424503552,1424503552,0,0,'54e83da784a11',11),(66,14,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,146,1424505956,1424505956,0,0,'54e84030d4c96',7),(67,14,'test','098f6bcd4621d373cade4e832627b4f6',66,'test',10,3,0,1424505956,1424505956,0,0,'54e84033dd480',11),(68,14,'.bash_history','0a97c9183c241136b2330a66266325fc',66,'.bash_history',10,3,146,1424446945,1424446945,0,0,'54e84033f0510',11),(69,13,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,32241,1424508266,1424508266,0,0,'54e84575ed958',7),(70,13,'.bash_history','0a97c9183c241136b2330a66266325fc',69,'.bash_history',10,3,47,1424447742,1424447742,0,0,'54e841b1ec139',11),(71,13,'New text file.txt','789998b176568ab184db839489a6211e',69,'New text file.txt',12,11,0,1424507999,1424507999,0,0,'54e8445f98319',11),(72,3,'files/New Document.odt','b72283b97b116dba7aa1550dc8c1312c',15,'New Document.odt',7,3,32236,1424508091,1424508091,0,0,'2205901b9276949483a4a866523ee88c',27),(73,3,'documents','21f64da1e5792c8295b964d159a14491',13,'documents',2,1,40685,1424508161,1424508161,0,0,'54e84501dc9d9',31),(74,3,'documents/5fc55a1f23a1183afaed4d90b50a8a69b3d69719.odt','cf8c28fd09c0ee7bec80c6bd40100501',73,'5fc55a1f23a1183afaed4d90b50a8a69b3d69719.odt',7,3,8449,1424508060,1424508060,0,0,'a30a49935527a21583a9e95b6391f5e7',27),(75,3,'files_versions','9692aae50022f45f1098646939b287b1',13,'files_versions',2,1,16898,1424508266,1424508266,0,0,'54e8456add5fe',31),(76,3,'files_versions/New Document.odt.v1424508060','93e04c491c6883873617930eb8c2c629',75,'New Document.odt.v1424508060',10,3,8449,1424508091,1424508091,0,0,'18fab00986157fc4038ac19d0a5a6ad4',27),(77,3,'files/New Document (2).odt','a97944ee230ca5044998aac5038d399b',15,'New Document (2).odt',7,3,8449,1424508098,1424508098,0,0,'2947b814ce756238ce81de9f3bc18154',27),(78,3,'documents/f148fa6af17cfad9aa09f8e88baefb2b0950e137.odt','7b2ab8dd737ecf5f2e27b7730a2de021',73,'f148fa6af17cfad9aa09f8e88baefb2b0950e137.odt',7,3,32236,1424508161,1424508161,0,0,'8b9b4831d79dea1d4deab0603c6bf888',27),(79,13,'test.odt','42c9d24809ca19a2de2dabadb193afb9',69,'test.odt',7,3,32194,1424508266,1424508266,0,0,'54e8456b03be4',11),(80,3,'files_versions/home','d02686a86b8d8e8064e284835fdbeb94',75,'home',2,1,8449,1424508266,1424508266,0,0,'54e8456adda9d',31),(81,3,'files_versions/home/test.odt.v1424508249','d1348d64ae9340cc2df59395833e9a7a',80,'test.odt.v1424508249',10,3,8449,1424508266,1424508266,0,0,'fcc8a6db244f0e406c6a5c259e2fdea4',27);
/*!40000 ALTER TABLE `oc_filecache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_files_trash`
--

DROP TABLE IF EXISTS `oc_files_trash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_files_trash` (
  `auto_id` int(11) NOT NULL AUTO_INCREMENT,
  `id` varchar(250) COLLATE utf8_bin NOT NULL DEFAULT '',
  `user` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `timestamp` varchar(12) COLLATE utf8_bin NOT NULL DEFAULT '',
  `location` varchar(512) COLLATE utf8_bin NOT NULL DEFAULT '',
  `type` varchar(4) COLLATE utf8_bin DEFAULT NULL,
  `mime` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`auto_id`),
  KEY `id_index` (`id`),
  KEY `timestamp_index` (`timestamp`),
  KEY `user_index` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_files_trash`
--

LOCK TABLES `oc_files_trash` WRITE;
/*!40000 ALTER TABLE `oc_files_trash` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_files_trash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_group_admin`
--

DROP TABLE IF EXISTS `oc_group_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_group_admin` (
  `gid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `uid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`,`uid`),
  KEY `group_admin_uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_group_admin`
--

LOCK TABLES `oc_group_admin` WRITE;
/*!40000 ALTER TABLE `oc_group_admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_group_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_group_user`
--

DROP TABLE IF EXISTS `oc_group_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_group_user` (
  `gid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `uid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`,`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_group_user`
--

LOCK TABLES `oc_group_user` WRITE;
/*!40000 ALTER TABLE `oc_group_user` DISABLE KEYS */;
INSERT INTO `oc_group_user` VALUES ('admin','admin');
/*!40000 ALTER TABLE `oc_group_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_groups`
--

DROP TABLE IF EXISTS `oc_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_groups` (
  `gid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_groups`
--

LOCK TABLES `oc_groups` WRITE;
/*!40000 ALTER TABLE `oc_groups` DISABLE KEYS */;
INSERT INTO `oc_groups` VALUES ('admin');
/*!40000 ALTER TABLE `oc_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_jobs`
--

DROP TABLE IF EXISTS `oc_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_jobs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `class` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `argument` varchar(256) COLLATE utf8_bin NOT NULL DEFAULT '',
  `last_run` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `job_class_index` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OC\\Cache\\FileGlobalGC','null',1424508275),(2,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1424507441),(3,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1424501923),(4,'OCA\\user_ldap\\lib\\Jobs','null',1424506275),(5,'\\OCA\\User_LDAP\\Jobs\\CleanUp','null',1424506014);
/*!40000 ALTER TABLE `oc_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_group_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_group_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_mapping` (
  `ldap_dn` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `owncloud_name` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `directory_uuid` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`ldap_dn`),
  UNIQUE KEY `owncloud_name_groups` (`owncloud_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_group_mapping`
--

LOCK TABLES `oc_ldap_group_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_group_mapping` DISABLE KEYS */;
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=amay17,ou=yr2017,ou=students,ou=people,CHANGETHISLDAPBASE','amay17','6A406AA0-15AA-4EA2-B843-F4D2E893A80A'),('cn=bursar,ou=groups,ou=people,CHANGETHISLDAPBASE','bursar','EE64A085-294F-42F8-9A2B-651A6E8A4570'),('cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam1','ADD1EFB6-3763-46F8-9886-2700B090144D'),('cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam2','97DC48E3-72AB-4FAC-B9C9-9905508AC1F2'),('cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam3','29C3A64A-97C6-4DBD-8A1F-8FDD44BF54D6'),('cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam4','06672595-6F33-46B9-99BB-910A4742D3F4'),('cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam5','794BF5E7-F080-4D70-94E9-B956EF68F3EA'),('cn=exams,ou=groups,ou=people,CHANGETHISLDAPBASE','exams','899E0159-CE7D-4651-89E0-3866C65F4A02'),('cn=governors,ou=groups,ou=people,CHANGETHISLDAPBASE','governors','2358ABE9-170C-434A-8986-CFA839A511C8'),('cn=guardians,ou=groups,ou=people,CHANGETHISLDAPBASE','guardians','92DC1516-32C9-4448-908E-54C2175AAF74'),('cn=guestusers,ou=groups,ou=people,CHANGETHISLDAPBASE','guestusers','F6550538-D9BE-4E8A-9CD5-C1B3643904D8'),('cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','ismith','5D26E309-DDA4-40D4-86D6-EF71C36938DE'),('cn=itadmin,ou=groups,ou=people,CHANGETHISLDAPBASE','itadmin','461CFF80-3531-4C4C-BA64-A7E8E395D65C'),('cn=jjones,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','jjones','C34FE89D-1621-441C-BAD3-4873420D9F31'),('cn=nfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','nfrog15','803F2C95-151D-40D2-998F-832C9E1C8552'),('cn=nonteachingstaff,ou=groups,ou=people,CHANGETHISLDAPBASE','nonteachingstaff','55E613DC-096F-41EF-AB1D-561AB6A4F4D4'),('cn=officestaff,ou=groups,ou=people,CHANGETHISLDAPBASE','officestaff','26F4EC62-21A2-4C7B-912B-BF9340C746B2'),('cn=ofrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','ofrog15','90020675-8638-4854-BF87-B5A51B53523C'),('cn=pfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','pfrog15','3E169DCC-FEB9-4FDB-A0F5-901AEFBB430E'),('cn=profilemanagement,ou=groups,ou=people,CHANGETHISLDAPBASE','profilemanagement','02FBE1E7-4F9C-4AB4-9A7A-6D8AE89BA109'),('cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE','profileuser','D1F5EFC8-F974-48BC-A8E0-C60595DB4139'),('cn=rfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','rfrog15','A4C4282C-7DBF-476A-99F0-E36E392B87E4'),('cn=sfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','sfrog15','6E62EEB0-B080-4D1F-BF76-15D128DA5CE2'),('cn=smt,ou=groups,ou=people,CHANGETHISLDAPBASE','smt','F9130416-C733-4129-8B4B-4AE7B020287D'),('cn=staff,ou=groups,ou=people,CHANGETHISLDAPBASE','staff','01CF5E43-CEF9-4593-A005-2459D7E43D14'),('cn=studentstaff,ou=groups,ou=people,CHANGETHISLDAPBASE','studentstaff','0F75CFCE-C041-4D8D-9983-02AF1E9D04E9'),('cn=tech,ou=groups,ou=people,CHANGETHISLDAPBASE','tech','621D6092-AD7F-434B-AF82-DDD86BEAC92D'),('cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech1','42B2A3A5-BF9C-42EE-BDBE-90B58FA2F14C'),('cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech2','E410B1F1-E185-4B03-AE29-8DC0779CFECA'),('cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech3','5296731E-4264-450D-902D-312FCF65E366'),('cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech4','19166BD1-62A8-4E98-B467-93F011BC900B'),('cn=tfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','tfrog15','8A506523-CC7A-4535-A5BC-E10DC12879A1'),('cn=ufrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','ufrog15','1C3F8C1C-AE4F-4AAE-80F4-8D36E85D9733'),('cn=yr2006,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2006','7EA5CACB-B269-4012-BA5C-C767CBDFA98B'),('cn=yr2007,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2007','CDA3EEFB-A357-4B00-A8E8-E553E679966F'),('cn=yr2008,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2008','FCD8883E-F01A-416E-96DC-E697988B946D'),('cn=yr2009,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2009','4A1F8A41-EDB4-4F9E-9964-241466A19106'),('cn=yr2010,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2010','69AA884D-8AE8-46E8-8626-8FB57182A993'),('cn=yr2011,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2011','25D24002-7BA6-4C58-9E01-26FA6FB9DCC6'),('cn=yr2012,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2012','4E599E20-D6FC-4675-B545-4A6BC76B1665'),('cn=yr2013,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2013','079067FB-DEB4-42D1-AB20-0321D867799C'),('cn=yr2014,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2014','4CD5F24C-2546-4763-B92E-9F87BC85CFAD'),('cn=yr2015,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2015','E2B31BB0-43EA-4B4A-BAFC-322228B22329'),('cn=yr2016,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2016','C599555A-F98D-4C25-BE01-0A36BAF88448'),('cn=yr2017,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2017','37C9578E-813F-4FF9-992E-766412B22699'),('cn=yr2018,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2018','0885F1D7-63A4-434A-A975-A68D5126C66B'),('cn=yr2019,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2019','A109348E-EABC-4BF9-8C4B-858AA0AD5AF9'),('cn=yr2020,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2020','CF674E58-CC08-4944-8322-2E944A4C5BB0'),('cn=yr2021,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2021','B74C81FB-0C7F-4AFF-9B10-AB38170388EA'),('cn=yr2022,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2022','964D6D13-0F1A-4C0B-B294-A0D2B6F1E281'),('cn=yr2023,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2023','8D97CC8C-D30B-40EC-84BE-C489F9A67A7A'),('cn=yr2024,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2024','6C7154AC-0167-4E57-8CDE-11A5F032EA23'),('cn=yr2025,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2025','C30C974B-1825-4856-A411-0F6F94451C81'),('cn=yr2026,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2026','25A4B91B-54B1-4CB4-9001-58C544809494'),('cn=yr2027,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2027','1D85133C-FD72-4CEC-B0D9-E30527E62CC5'),('cn=yr2028,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2028','AFB658E9-4D41-447E-BE06-996AEB9AEC17'),('cn=yr2029,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2029','3E1D8C18-7F67-40DE-BDF6-8B44DD1972F3'),('cn=yr2030,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2030','57954B4C-E530-442D-ACAC-2B063A42B820'),('cn=yr2031,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2031','3EE33AE7-F850-4664-920C-707D3E13DE07'),('cn=yr2032,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2032','9AE236DD-02E7-49D8-A7C2-CE211C09166F'),('cn=yr2033,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2033','1864AFE6-2EFF-4DDD-92D4-9CE918B9A910'),('cn=yr2034,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2034','41E1A7AE-4072-4FFD-AAEF-A775F7696807'),('cn=yr2035,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2035','9665DD72-A861-45E6-AEFC-BED39B78E70A'),('cn=yr2036,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2036','AB904406-C1B8-4059-9515-0B8C1636C1C6'),('cn=yr2037,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2037','0B32FEBB-0010-4847-922A-2FABDE2B08FD'),('cn=yr2038,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2038','98A76D4A-C472-4D2C-BEC0-07BE5B182AFD'),('cn=yr2039,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2039','4FCA1DBF-674B-4637-B859-AB024BF1DEC2'),('cn=yr2040,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2040','B6CAA4C1-9AD6-45F6-8ABB-1FA037653CF4'),('cn=yr2041,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2041','852AF739-0AA3-4EF8-8CFE-36EA1300EA3C'),('cn=yr2042,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2042','20BC89B4-F335-49BF-9E00-AF928A4B6BBE'),('cn=yr2043,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2043','09FA0A12-9AC8-4CDA-B7F8-F30F875E9CD2'),('cn=yr2044,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2044','F1F1FC32-9303-41D1-9473-E4E531886E26'),('cn=yr2045,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2045','82BB3C61-2FAC-406A-8B7A-3B2986E3A92E'),('cn=yr2046,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2046','F7EA6381-7A37-483B-98B5-8BB96AC9393C'),('cn=yr2047,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2047','A4F2A404-362D-4B4B-A259-262CCAAA1D0D'),('cn=yr2048,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2048','9D5617E4-836B-4AC3-AC58-7E0172FC287D');
/*!40000 ALTER TABLE `oc_ldap_group_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_group_members`
--

DROP TABLE IF EXISTS `oc_ldap_group_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_members` (
  `owncloudname` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `owncloudusers` longtext COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`owncloudname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_group_members`
--

LOCK TABLES `oc_ldap_group_members` WRITE;
/*!40000 ALTER TABLE `oc_ldap_group_members` DISABLE KEYS */;
INSERT INTO `oc_ldap_group_members` VALUES ('bursar','a:0:{}'),('exams','a:0:{}'),('governors','a:0:{}'),('guardians','a:0:{}'),('guestusers','a:10:{i:0;s:36:\"0EA7FCEF-8021-47CF-BD5D-48BE7E8FAB68\";i:1;s:36:\"1FDF58EB-9C96-4C82-94E3-593127F8E905\";i:2;s:36:\"5E62BA41-A18B-4B62-999F-D1E1F942D1A8\";i:3;s:36:\"650CB589-DDF4-4BBB-BD8F-9A9722CFAA04\";i:4;s:36:\"78925BF6-70F0-4269-A771-B0588BA1C105\";i:5;s:36:\"A012E6D3-51BE-4E2D-A242-2607C7271B27\";i:6;s:36:\"C478C55F-AC04-4B5D-A616-835045A890EA\";i:7;s:36:\"EB6E0429-69DF-4776-B712-CE3DA1C8252A\";i:8;s:36:\"F6109BF9-0FB0-4210-A0C9-6C1E21EEE269\";i:9;s:36:\"FCC5C127-D445-45A7-B117-53B160757D62\";}'),('itadmin','a:2:{i:0;s:36:\"3FC6981B-0194-4AF8-9B3C-1924A8E7B5B5\";i:1;s:36:\"B1BADB37-C6CE-4EF9-8D16-827BAB398B1F\";}'),('nonteachingstaff','a:0:{}'),('officestaff','a:1:{i:0;s:36:\"B1BADB37-C6CE-4EF9-8D16-827BAB398B1F\";}'),('profilemanagement','a:1:{i:0;s:36:\"D1F5EFC8-F974-48BC-A8E0-C60595DB4139\";}'),('smt','a:0:{}'),('staff','a:3:{i:0;s:36:\"5D26E309-DDA4-40D4-86D6-EF71C36938DE\";i:1;s:36:\"B1BADB37-C6CE-4EF9-8D16-827BAB398B1F\";i:2;s:36:\"C34FE89D-1621-441C-BAD3-4873420D9F31\";}'),('studentstaff','a:0:{}'),('tech','a:0:{}'),('yr2006','a:0:{}'),('yr2007','a:0:{}'),('yr2008','a:0:{}'),('yr2009','a:0:{}'),('yr2010','a:0:{}'),('yr2011','a:0:{}'),('yr2012','a:1:{i:0;s:36:\"B475C529-6B25-47A5-95A8-AABACEAB40A5\";}'),('yr2013','a:0:{}'),('yr2014','a:0:{}'),('yr2015','a:23:{i:0;s:36:\"0AD22A9D-8B9C-4CA4-A5D2-77612ECA86B6\";i:1;s:36:\"1AAE1024-C107-4E54-AB96-5D82024AF58C\";i:2;s:36:\"1C3F8C1C-AE4F-4AAE-80F4-8D36E85D9733\";i:3;s:36:\"1CA98691-4A66-42D4-A6C6-89228A1836F9\";i:4;s:36:\"2FB56915-986F-4E45-A7EB-DC2395F6C97E\";i:5;s:36:\"3E169DCC-FEB9-4FDB-A0F5-901AEFBB430E\";i:6;s:36:\"6E62EEB0-B080-4D1F-BF76-15D128DA5CE2\";i:7;s:36:\"8A974C58-5420-4863-81B5-BF5676C365B9\";i:8;s:36:\"8A506523-CC7A-4535-A5BC-E10DC12879A1\";i:9;s:36:\"33CB28D4-71C2-4FF2-870C-67F3586F97C2\";i:10;s:36:\"75C7BE89-0BCB-4D2A-B67A-D2374AE18361\";i:11;s:36:\"84ED3159-F105-4A7C-B9BE-5E6C6E96DD81\";i:12;s:36:\"94D34990-DCAA-49C2-8116-026D95957A91\";i:13;s:36:\"592F003E-B7FF-4863-9440-8A7C5B671304\";i:14;s:36:\"803F2C95-151D-40D2-998F-832C9E1C8552\";i:15;s:36:\"2410F17F-4BC0-43CD-A6E1-1327AA009F75\";i:16;s:36:\"43628C0D-F859-4A9A-A880-1DD7A7127972\";i:17;s:36:\"26814839-C373-42FB-8F13-BD30A4737ECE\";i:18;s:36:\"90020675-8638-4854-BF87-B5A51B53523C\";i:19;s:36:\"A4C4282C-7DBF-476A-99F0-E36E392B87E4\";i:20;s:36:\"A5543BBC-EC60-4398-9014-1D572839C0E2\";i:21;s:36:\"C73FE7E2-AEFD-48B3-90BA-363FDE2E0F12\";i:22;s:36:\"CD3311E2-89DE-4026-8C21-4940BE0D86BB\";}'),('yr2016','a:0:{}'),('yr2017','a:1:{i:0;s:36:\"6A406AA0-15AA-4EA2-B843-F4D2E893A80A\";}'),('yr2018','a:0:{}'),('yr2019','a:0:{}'),('yr2020','a:0:{}'),('yr2021','a:0:{}'),('yr2022','a:0:{}'),('yr2023','a:0:{}'),('yr2024','a:0:{}'),('yr2025','a:0:{}'),('yr2026','a:0:{}'),('yr2027','a:0:{}'),('yr2028','a:0:{}'),('yr2029','a:0:{}'),('yr2030','a:1:{i:0;s:36:\"FE6FDE06-8284-40D4-B556-B391D61E742E\";}'),('yr2031','a:0:{}'),('yr2032','a:0:{}'),('yr2033','a:0:{}'),('yr2034','a:0:{}'),('yr2035','a:0:{}'),('yr2036','a:0:{}'),('yr2037','a:0:{}'),('yr2038','a:0:{}'),('yr2039','a:0:{}'),('yr2040','a:0:{}'),('yr2041','a:0:{}'),('yr2042','a:0:{}'),('yr2043','a:0:{}'),('yr2044','a:0:{}'),('yr2045','a:0:{}'),('yr2046','a:0:{}'),('yr2047','a:0:{}'),('yr2048','a:0:{}');
/*!40000 ALTER TABLE `oc_ldap_group_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_user_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_user_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_user_mapping` (
  `ldap_dn` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `owncloud_name` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `directory_uuid` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`owncloud_name`),
  UNIQUE KEY `ldap_dn_users` (`ldap_dn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_user_mapping`
--

LOCK TABLES `oc_ldap_user_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_user_mapping` DISABLE KEYS */;
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','06672595-6F33-46B9-99BB-910A4742D3F4','06672595-6F33-46B9-99BB-910A4742D3F4'),('cn=jfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','0AD22A9D-8B9C-4CA4-A5D2-77612ECA86B6','0AD22A9D-8B9C-4CA4-A5D2-77612ECA86B6'),('cn=guest2,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','0EA7FCEF-8021-47CF-BD5D-48BE7E8FAB68','0EA7FCEF-8021-47CF-BD5D-48BE7E8FAB68'),('cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','19166BD1-62A8-4E98-B467-93F011BC900B','19166BD1-62A8-4E98-B467-93F011BC900B'),('cn=bfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','1AAE1024-C107-4E54-AB96-5D82024AF58C','1AAE1024-C107-4E54-AB96-5D82024AF58C'),('cn=ufrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','1C3F8C1C-AE4F-4AAE-80F4-8D36E85D9733','1C3F8C1C-AE4F-4AAE-80F4-8D36E85D9733'),('cn=mfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','1CA98691-4A66-42D4-A6C6-89228A1836F9','1CA98691-4A66-42D4-A6C6-89228A1836F9'),('cn=guest8,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','1FDF58EB-9C96-4C82-94E3-593127F8E905','1FDF58EB-9C96-4C82-94E3-593127F8E905'),('cn=kfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','2410F17F-4BC0-43CD-A6E1-1327AA009F75','2410F17F-4BC0-43CD-A6E1-1327AA009F75'),('cn=nfrog151,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','26814839-C373-42FB-8F13-BD30A4737ECE','26814839-C373-42FB-8F13-BD30A4737ECE'),('cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','29C3A64A-97C6-4DBD-8A1F-8FDD44BF54D6','29C3A64A-97C6-4DBD-8A1F-8FDD44BF54D6'),('cn=efrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','2FB56915-986F-4E45-A7EB-DC2395F6C97E','2FB56915-986F-4E45-A7EB-DC2395F6C97E'),('cn=lfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','33CB28D4-71C2-4FF2-870C-67F3586F97C2','33CB28D4-71C2-4FF2-870C-67F3586F97C2'),('cn=pfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','3E169DCC-FEB9-4FDB-A0F5-901AEFBB430E','3E169DCC-FEB9-4FDB-A0F5-901AEFBB430E'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE','3FC6981B-0194-4AF8-9B3C-1924A8E7B5B5','3FC6981B-0194-4AF8-9B3C-1924A8E7B5B5'),('cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','42B2A3A5-BF9C-42EE-BDBE-90B58FA2F14C','42B2A3A5-BF9C-42EE-BDBE-90B58FA2F14C'),('cn=gfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','43628C0D-F859-4A9A-A880-1DD7A7127972','43628C0D-F859-4A9A-A880-1DD7A7127972'),('cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','5296731E-4264-450D-902D-312FCF65E366','5296731E-4264-450D-902D-312FCF65E366'),('cn=bjones15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','592F003E-B7FF-4863-9440-8A7C5B671304','592F003E-B7FF-4863-9440-8A7C5B671304'),('cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','5D26E309-DDA4-40D4-86D6-EF71C36938DE','5D26E309-DDA4-40D4-86D6-EF71C36938DE'),('cn=guest1,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','5E62BA41-A18B-4B62-999F-D1E1F942D1A8','5E62BA41-A18B-4B62-999F-D1E1F942D1A8'),('cn=guest9,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','650CB589-DDF4-4BBB-BD8F-9A9722CFAA04','650CB589-DDF4-4BBB-BD8F-9A9722CFAA04'),('cn=amay17,ou=yr2017,ou=students,ou=people,CHANGETHISLDAPBASE','6A406AA0-15AA-4EA2-B843-F4D2E893A80A','6A406AA0-15AA-4EA2-B843-F4D2E893A80A'),('cn=sfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','6E62EEB0-B080-4D1F-BF76-15D128DA5CE2','6E62EEB0-B080-4D1F-BF76-15D128DA5CE2'),('cn=cfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','75C7BE89-0BCB-4D2A-B67A-D2374AE18361','75C7BE89-0BCB-4D2A-B67A-D2374AE18361'),('cn=guest5,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','78925BF6-70F0-4269-A771-B0588BA1C105','78925BF6-70F0-4269-A771-B0588BA1C105'),('cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','794BF5E7-F080-4D70-94E9-B956EF68F3EA','794BF5E7-F080-4D70-94E9-B956EF68F3EA'),('cn=nfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','803F2C95-151D-40D2-998F-832C9E1C8552','803F2C95-151D-40D2-998F-832C9E1C8552'),('cn=ifrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','84ED3159-F105-4A7C-B9BE-5E6C6E96DD81','84ED3159-F105-4A7C-B9BE-5E6C6E96DD81'),('cn=tfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','8A506523-CC7A-4535-A5BC-E10DC12879A1','8A506523-CC7A-4535-A5BC-E10DC12879A1'),('cn=mfrog151,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','8A974C58-5420-4863-81B5-BF5676C365B9','8A974C58-5420-4863-81B5-BF5676C365B9'),('cn=ofrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','90020675-8638-4854-BF87-B5A51B53523C','90020675-8638-4854-BF87-B5A51B53523C'),('cn=pfrog151,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','94D34990-DCAA-49C2-8116-026D95957A91','94D34990-DCAA-49C2-8116-026D95957A91'),('cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','97DC48E3-72AB-4FAC-B9C9-9905508AC1F2','97DC48E3-72AB-4FAC-B9C9-9905508AC1F2'),('cn=guest3,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','A012E6D3-51BE-4E2D-A242-2607C7271B27','A012E6D3-51BE-4E2D-A242-2607C7271B27'),('cn=rfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','A4C4282C-7DBF-476A-99F0-E36E392B87E4','A4C4282C-7DBF-476A-99F0-E36E392B87E4'),('cn=afrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','A5543BBC-EC60-4398-9014-1D572839C0E2','A5543BBC-EC60-4398-9014-1D572839C0E2'),('cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','ADD1EFB6-3763-46F8-9886-2700B090144D','ADD1EFB6-3763-46F8-9886-2700B090144D'),('cn=psharrad,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE','B1BADB37-C6CE-4EF9-8D16-827BAB398B1F','B1BADB37-C6CE-4EF9-8D16-827BAB398B1F'),('cn=mwilson12,ou=yr2012,ou=students,ou=people,CHANGETHISLDAPBASE','B475C529-6B25-47A5-95A8-AABACEAB40A5','B475C529-6B25-47A5-95A8-AABACEAB40A5'),('cn=jjones,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','C34FE89D-1621-441C-BAD3-4873420D9F31','C34FE89D-1621-441C-BAD3-4873420D9F31'),('cn=guest4,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','C478C55F-AC04-4B5D-A616-835045A890EA','C478C55F-AC04-4B5D-A616-835045A890EA'),('cn=hfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','C73FE7E2-AEFD-48B3-90BA-363FDE2E0F12','C73FE7E2-AEFD-48B3-90BA-363FDE2E0F12'),('cn=dfrog15,ou=yr2015,ou=students,ou=people,CHANGETHISLDAPBASE','CD3311E2-89DE-4026-8C21-4940BE0D86BB','CD3311E2-89DE-4026-8C21-4940BE0D86BB'),('cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE','D1F5EFC8-F974-48BC-A8E0-C60595DB4139','D1F5EFC8-F974-48BC-A8E0-C60595DB4139'),('cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','E410B1F1-E185-4B03-AE29-8DC0779CFECA','E410B1F1-E185-4B03-AE29-8DC0779CFECA'),('cn=guest6,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','EB6E0429-69DF-4776-B712-CE3DA1C8252A','EB6E0429-69DF-4776-B712-CE3DA1C8252A'),('cn=guest7,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','F6109BF9-0FB0-4210-A0C9-6C1E21EEE269','F6109BF9-0FB0-4210-A0C9-6C1E21EEE269'),('cn=guest10,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','FCC5C127-D445-45A7-B117-53B160757D62','FCC5C127-D445-45A7-B117-53B160757D62'),('cn=jsmith30,ou=yr2030,ou=students,ou=people,CHANGETHISLDAPBASE','FE6FDE06-8284-40D4-B556-B391D61E742E','FE6FDE06-8284-40D4-B556-B391D61E742E');
/*!40000 ALTER TABLE `oc_ldap_user_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_locks`
--

DROP TABLE IF EXISTS `oc_locks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_locks` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `owner` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `timeout` int(10) unsigned DEFAULT NULL,
  `created` bigint(20) DEFAULT NULL,
  `token` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `scope` smallint(6) DEFAULT NULL,
  `depth` smallint(6) DEFAULT NULL,
  `uri` longtext COLLATE utf8_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_locks`
--

LOCK TABLES `oc_locks` WRITE;
/*!40000 ALTER TABLE `oc_locks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_locks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_mimetypes`
--

DROP TABLE IF EXISTS `oc_mimetypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_mimetypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mimetype` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mimetype_id_index` (`mimetype`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (3,'application'),(10,'application/octet-stream'),(4,'application/pdf'),(7,'application/vnd.oasis.opendocument.text'),(5,'audio'),(6,'audio/mpeg'),(1,'httpd'),(2,'httpd/unix-directory'),(8,'image'),(9,'image/jpeg'),(11,'text'),(12,'text/plain');
/*!40000 ALTER TABLE `oc_mimetypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_preferences`
--

DROP TABLE IF EXISTS `oc_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_preferences` (
  `userid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `appid` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `configkey` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `configvalue` longtext COLLATE utf8_bin,
  PRIMARY KEY (`userid`,`appid`,`configkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_preferences`
--

LOCK TABLES `oc_preferences` WRITE;
/*!40000 ALTER TABLE `oc_preferences` DISABLE KEYS */;
INSERT INTO `oc_preferences` VALUES ('06672595-6F33-46B9-99BB-910A4742D3F4','user_ldap','homePath',''),('0AD22A9D-8B9C-4CA4-A5D2-77612ECA86B6','user_ldap','homePath',''),('0EA7FCEF-8021-47CF-BD5D-48BE7E8FAB68','user_ldap','homePath',''),('19166BD1-62A8-4E98-B467-93F011BC900B','user_ldap','homePath',''),('1AAE1024-C107-4E54-AB96-5D82024AF58C','user_ldap','homePath',''),('1C3F8C1C-AE4F-4AAE-80F4-8D36E85D9733','user_ldap','homePath',''),('1CA98691-4A66-42D4-A6C6-89228A1836F9','user_ldap','homePath',''),('1FDF58EB-9C96-4C82-94E3-593127F8E905','user_ldap','homePath',''),('2410F17F-4BC0-43CD-A6E1-1327AA009F75','user_ldap','homePath',''),('26814839-C373-42FB-8F13-BD30A4737ECE','user_ldap','homePath',''),('29C3A64A-97C6-4DBD-8A1F-8FDD44BF54D6','user_ldap','homePath',''),('2FB56915-986F-4E45-A7EB-DC2395F6C97E','user_ldap','homePath',''),('33CB28D4-71C2-4FF2-870C-67F3586F97C2','user_ldap','homePath',''),('3E169DCC-FEB9-4FDB-A0F5-901AEFBB430E','user_ldap','homePath',''),('3FC6981B-0194-4AF8-9B3C-1924A8E7B5B5','user_ldap','homePath',''),('42B2A3A5-BF9C-42EE-BDBE-90B58FA2F14C','user_ldap','homePath',''),('43628C0D-F859-4A9A-A880-1DD7A7127972','user_ldap','homePath',''),('5296731E-4264-450D-902D-312FCF65E366','user_ldap','homePath',''),('592F003E-B7FF-4863-9440-8A7C5B671304','core','timezone','Europe/London'),('592F003E-B7FF-4863-9440-8A7C5B671304','files_external','/home','1424503189'),('592F003E-B7FF-4863-9440-8A7C5B671304','files_external','/mwilson12','1424503189'),('592F003E-B7FF-4863-9440-8A7C5B671304','files_external','/test','1424503189'),('592F003E-B7FF-4863-9440-8A7C5B671304','firstrunwizard','show','0'),('592F003E-B7FF-4863-9440-8A7C5B671304','login','lastLogin','1424503401'),('592F003E-B7FF-4863-9440-8A7C5B671304','settings','email','bjones15@karoshi.testing.com'),('592F003E-B7FF-4863-9440-8A7C5B671304','user_ldap','displayName','Bob Jones'),('592F003E-B7FF-4863-9440-8A7C5B671304','user_ldap','firstLoginAccomplished','1'),('592F003E-B7FF-4863-9440-8A7C5B671304','user_ldap','homePath',''),('592F003E-B7FF-4863-9440-8A7C5B671304','user_ldap','lastFeatureRefresh','1424503189'),('592F003E-B7FF-4863-9440-8A7C5B671304','user_ldap','uid','bjones15'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','core','timezone','Europe/London'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','files_external','/home','1424503037'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','files_external','/mwilson12','1424503037'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','files_external','/test','1424503037'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','firstrunwizard','show','0'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','login','lastLogin','1424508048'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','settings','email','ismith@karoshi.testing.com'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','user_ldap','displayName','Ian Smith'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','user_ldap','firstLoginAccomplished','1'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','user_ldap','homePath',''),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','user_ldap','lastFeatureRefresh','1424502420'),('5D26E309-DDA4-40D4-86D6-EF71C36938DE','user_ldap','uid','ismith'),('5E62BA41-A18B-4B62-999F-D1E1F942D1A8','user_ldap','homePath',''),('650CB589-DDF4-4BBB-BD8F-9A9722CFAA04','user_ldap','homePath',''),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','core','timezone','Europe/London'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','files_external','/home','1424503510'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','files_external','/mwilson12','1424503510'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','files_external','/test','1424503510'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','firstrunwizard','show','0'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','login','lastLogin','1424506274'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','settings','email','amay17@karoshi.testing.com'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','user_ldap','displayName','Amy May'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','user_ldap','firstLoginAccomplished','1'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','user_ldap','homePath',''),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','user_ldap','lastFeatureRefresh','1424503510'),('6A406AA0-15AA-4EA2-B843-F4D2E893A80A','user_ldap','uid','amay17'),('6E62EEB0-B080-4D1F-BF76-15D128DA5CE2','user_ldap','homePath',''),('75C7BE89-0BCB-4D2A-B67A-D2374AE18361','user_ldap','homePath',''),('78925BF6-70F0-4269-A771-B0588BA1C105','user_ldap','homePath',''),('794BF5E7-F080-4D70-94E9-B956EF68F3EA','user_ldap','homePath',''),('803F2C95-151D-40D2-998F-832C9E1C8552','user_ldap','homePath',''),('84ED3159-F105-4A7C-B9BE-5E6C6E96DD81','user_ldap','homePath',''),('8A506523-CC7A-4535-A5BC-E10DC12879A1','user_ldap','homePath',''),('8A974C58-5420-4863-81B5-BF5676C365B9','user_ldap','homePath',''),('90020675-8638-4854-BF87-B5A51B53523C','user_ldap','homePath',''),('94D34990-DCAA-49C2-8116-026D95957A91','user_ldap','homePath',''),('97DC48E3-72AB-4FAC-B9C9-9905508AC1F2','user_ldap','homePath',''),('A012E6D3-51BE-4E2D-A242-2607C7271B27','user_ldap','homePath',''),('A4C4282C-7DBF-476A-99F0-E36E392B87E4','user_ldap','homePath',''),('A5543BBC-EC60-4398-9014-1D572839C0E2','user_ldap','homePath',''),('ADD1EFB6-3763-46F8-9886-2700B090144D','user_ldap','homePath',''),('B1BADB37-C6CE-4EF9-8D16-827BAB398B1F','user_ldap','homePath',''),('B475C529-6B25-47A5-95A8-AABACEAB40A5','core','timezone','Europe/London'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','files_external','/home','1424503057'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','files_external','/mwilson12','1424502820'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','files_external','/test','1424502820'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','firstrunwizard','show','0'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','login','lastLogin','1424503057'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','settings','email','mwilson12@karoshi.testing.com'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','user_ldap','displayName','Mark Wilson'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','user_ldap','firstLoginAccomplished','1'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','user_ldap','homePath',''),('B475C529-6B25-47A5-95A8-AABACEAB40A5','user_ldap','lastFeatureRefresh','1424502607'),('B475C529-6B25-47A5-95A8-AABACEAB40A5','user_ldap','uid','mwilson12'),('C34FE89D-1621-441C-BAD3-4873420D9F31','core','timezone','Europe/London'),('C34FE89D-1621-441C-BAD3-4873420D9F31','files_external','/home','1424503072'),('C34FE89D-1621-441C-BAD3-4873420D9F31','files_external','/mwilson12','1424503072'),('C34FE89D-1621-441C-BAD3-4873420D9F31','files_external','/test','1424503072'),('C34FE89D-1621-441C-BAD3-4873420D9F31','firstrunwizard','show','0'),('C34FE89D-1621-441C-BAD3-4873420D9F31','login','lastLogin','1424503072'),('C34FE89D-1621-441C-BAD3-4873420D9F31','user_ldap','displayName','John Jones'),('C34FE89D-1621-441C-BAD3-4873420D9F31','user_ldap','firstLoginAccomplished','1'),('C34FE89D-1621-441C-BAD3-4873420D9F31','user_ldap','homePath',''),('C34FE89D-1621-441C-BAD3-4873420D9F31','user_ldap','uid','jjones'),('C478C55F-AC04-4B5D-A616-835045A890EA','user_ldap','homePath',''),('C73FE7E2-AEFD-48B3-90BA-363FDE2E0F12','user_ldap','homePath',''),('CD3311E2-89DE-4026-8C21-4940BE0D86BB','user_ldap','homePath',''),('D1F5EFC8-F974-48BC-A8E0-C60595DB4139','user_ldap','homePath',''),('E410B1F1-E185-4B03-AE29-8DC0779CFECA','user_ldap','homePath',''),('EB6E0429-69DF-4776-B712-CE3DA1C8252A','user_ldap','homePath',''),('F6109BF9-0FB0-4210-A0C9-6C1E21EEE269','user_ldap','homePath',''),('FCC5C127-D445-45A7-B117-53B160757D62','user_ldap','homePath',''),('FE6FDE06-8284-40D4-B556-B391D61E742E','user_ldap','homePath',''),('admin','core','timezone','Europe/London'),('admin','files_external','/home','1424502943'),('admin','files_external','/mwilson12','1424502802'),('admin','files_external','/test','1424502805'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1424508029');
/*!40000 ALTER TABLE `oc_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_privatedata`
--

DROP TABLE IF EXISTS `oc_privatedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_privatedata` (
  `keyid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `app` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `key` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `value` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`keyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_privatedata`
--

LOCK TABLES `oc_privatedata` WRITE;
/*!40000 ALTER TABLE `oc_privatedata` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_privatedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_properties`
--

DROP TABLE IF EXISTS `oc_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_properties` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `propertypath` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `propertyname` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `propertyvalue` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_index` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_properties`
--

LOCK TABLES `oc_properties` WRITE;
/*!40000 ALTER TABLE `oc_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_share`
--

DROP TABLE IF EXISTS `oc_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `share_type` smallint(6) NOT NULL DEFAULT '0',
  `share_with` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `uid_owner` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `parent` int(11) DEFAULT NULL,
  `item_type` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `item_source` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `item_target` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `file_source` int(11) DEFAULT NULL,
  `file_target` varchar(512) COLLATE utf8_bin DEFAULT NULL,
  `permissions` smallint(6) NOT NULL DEFAULT '0',
  `stime` bigint(20) NOT NULL DEFAULT '0',
  `accepted` smallint(6) NOT NULL DEFAULT '0',
  `expiration` datetime DEFAULT NULL,
  `token` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `mail_send` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `item_share_type_index` (`item_type`,`share_type`),
  KEY `file_source_index` (`file_source`),
  KEY `token_index` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_share`
--

LOCK TABLES `oc_share` WRITE;
/*!40000 ALTER TABLE `oc_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_share` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_share_external`
--

DROP TABLE IF EXISTS `oc_share_external`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_share_external` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remote` varchar(512) COLLATE utf8_bin NOT NULL COMMENT 'Url of the remove owncloud instance',
  `remote_id` int(11) NOT NULL,
  `share_token` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Public share token',
  `password` varchar(64) COLLATE utf8_bin DEFAULT NULL COMMENT 'Optional password for the public share',
  `name` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Original name on the remote server',
  `owner` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'User that owns the public share on the remote server',
  `user` varchar(64) COLLATE utf8_bin NOT NULL COMMENT 'Local user which added the external share',
  `mountpoint` varchar(4000) COLLATE utf8_bin NOT NULL COMMENT 'Full path where the share is mounted',
  `mountpoint_hash` varchar(32) COLLATE utf8_bin NOT NULL COMMENT 'md5 hash of the mountpoint',
  `accepted` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `sh_external_mp` (`user`,`mountpoint_hash`),
  KEY `sh_external_user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_share_external`
--

LOCK TABLES `oc_share_external` WRITE;
/*!40000 ALTER TABLE `oc_share_external` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_share_external` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_storages`
--

DROP TABLE IF EXISTS `oc_storages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_storages` (
  `id` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `numeric_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`numeric_id`),
  UNIQUE KEY `storages_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('5fd1e3454db5b2753e6534805544b50a',16),('e8a680d6566b3766e2d8fe4c5fc36716',12),('fcf92de4e01b734e2ebfe1b8ae6f3abb',5),('home::592F003E-B7FF-4863-9440-8A7C5B671304',10),('home::5D26E309-DDA4-40D4-86D6-EF71C36938DE',3),('home::6A406AA0-15AA-4EA2-B843-F4D2E893A80A',11),('home::B475C529-6B25-47A5-95A8-AABACEAB40A5',4),('home::C34FE89D-1621-441C-BAD3-4873420D9F31',9),('home::admin',1),('local::/home/owncloud/data/',2),('smb::amay17@athena.karoshi.testing.com//amay17//',17),('smb::ismith@apollo.karoshi.testing.com//ismith//',13),('smb::ismith@athena.karoshi.testing.com//ismith//',14),('smb::ismith@hera.karoshi.testing.com//ismith//',15),('smb::mwilson12@apollo.karoshi.testing.com//mwilson12//',6),('smb::mwilson12@appollo.karoshi.testing.com//mwilson12//',8),('smb::mwilson12@hera.karoshi.testing.com//mwilson12//',7);
/*!40000 ALTER TABLE `oc_storages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_users`
--

DROP TABLE IF EXISTS `oc_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_users` (
  `uid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `displayname` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_users`
--

LOCK TABLES `oc_users` WRITE;
/*!40000 ALTER TABLE `oc_users` DISABLE KEYS */;
INSERT INTO `oc_users` VALUES ('admin',NULL,'1|$2y$10$zJPnelszrczkGnsjV2amD.aIL.oCJ1aV7XsTm1o393OI4XdAp.fx6');
/*!40000 ALTER TABLE `oc_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_vcategory`
--

DROP TABLE IF EXISTS `oc_vcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_vcategory` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `type` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `category` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `uid_index` (`uid`),
  KEY `type_index` (`type`),
  KEY `category_index` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_vcategory`
--

LOCK TABLES `oc_vcategory` WRITE;
/*!40000 ALTER TABLE `oc_vcategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_vcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_vcategory_to_object`
--

DROP TABLE IF EXISTS `oc_vcategory_to_object`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_vcategory_to_object` (
  `objid` int(10) unsigned NOT NULL DEFAULT '0',
  `categoryid` int(10) unsigned NOT NULL DEFAULT '0',
  `type` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`categoryid`,`objid`,`type`),
  KEY `vcategory_objectd_index` (`objid`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_vcategory_to_object`
--

LOCK TABLES `oc_vcategory_to_object` WRITE;
/*!40000 ALTER TABLE `oc_vcategory_to_object` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_vcategory_to_object` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-21  8:45:56
