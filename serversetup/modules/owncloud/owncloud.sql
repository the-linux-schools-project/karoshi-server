-- MySQL dump 10.13  Distrib 5.5.34, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: owncloud
-- ------------------------------------------------------
-- Server version	5.5.34-0ubuntu0.12.04.1

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
-- Table structure for table `oc_appconfig`
--

DROP TABLE IF EXISTS `oc_appconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_appconfig` (
  `appid` varchar(32) NOT NULL DEFAULT '',
  `configkey` varchar(64) NOT NULL DEFAULT '',
  `configvalue` longtext,
  PRIMARY KEY (`appid`,`configkey`),
  KEY `appconfig_config_key_index` (`configkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_appconfig`
--

LOCK TABLES `oc_appconfig` WRITE;
/*!40000 ALTER TABLE `oc_appconfig` DISABLE KEYS */;
INSERT INTO `oc_appconfig` VALUES ('admin_migrate','enabled','no'),('admin_migrate','installed_version','0.1'),('admin_migrate','types',NULL),('backgroundjob','lastjob','1'),('calendar','enabled','yes'),('calendar','installed_version','0.6.3'),('calendar','types',NULL),('contacts','enabled','yes'),('contacts','installed_version','0.3'),('contacts','types',''),('core','backgroundjobs_step','regular_tasks'),('core','backgroundjobs_task',''),('core','global_cache_gc_lastrun','1387461940'),('core','installedat','1386078554.6398'),('core','lastupdatedat','1387461459'),('core','lastupdateResult','{\"version\":\"6.0.0.14\",\"versionstring\":\"ownCloud 6.0.0a\",\"url\":\"http:\\/\\/download.owncloud.org\\/community\\/owncloud-6.0.0a.tar.bz2\",\"web\":\"http:\\/\\/owncloud.org\\/\"}'),('core','public_caldav','calendar/share.php'),('core','public_calendar','calendar/share.php'),('core','public_files','files_sharing/public.php'),('core','public_gallery','gallery/public.php'),('core','public_webdav','files_sharing/public.php'),('core','remote_ampache','media/remote.php'),('core','remote_caldav','calendar/appinfo/remote.php'),('core','remote_calendar','calendar/appinfo/remote.php'),('core','remote_carddav','contacts/appinfo/remote.php'),('core','remote_contacts','contacts/appinfo/remote.php'),('core','remote_contactthumbnail','contacts/thumbnail.php'),('core','remote_core.css','/core/minimizer.php'),('core','remote_core.js','/core/minimizer.php'),('core','remote_files','files/appinfo/remote.php'),('core','remote_filesync','files/appinfo/filesync.php'),('core','remote_webdav','files/appinfo/remote.php'),('core','shareapi_allow_links','no'),('core','shareapi_allow_resharing','no'),('files','backgroundwatcher_previous_file','15'),('files','backgroundwatcher_previous_folder','6'),('files','default_quota','50 GB'),('files','enabled','yes'),('files','installed_version','1.1.7'),('files','types','filesystem'),('files_encryption','enabled','yes'),('files_encryption','installed_version','0.5'),('files_encryption','publicShareKeyId','pubShare_df7de1ac'),('files_encryption','types','filesystem'),('files_external','allow_user_mounting','no'),('files_external','enabled','no'),('files_external','installed_version','0.2'),('files_external','types','filesystem'),('files_imageviewer','enabled','no'),('files_imageviewer','installed_version','1.0'),('files_imageviewer','types',NULL),('files_odfviewer','enabled','no'),('files_odfviewer','installed_version','0.1'),('files_odfviewer','types',NULL),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','0.2'),('files_pdfviewer','types',NULL),('files_sharing','enabled','yes'),('files_sharing','installed_version','0.3.5'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','0.3'),('files_texteditor','types',NULL),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','0.4'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.0.3'),('files_versions','types','filesystem'),('files_videoviewer','enabled','yes'),('files_videoviewer','installed_version','0.1.1'),('files_videoviewer','types',NULL),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','1.0'),('firstrunwizard','types',NULL),('gallery','enabled','yes'),('gallery','installed_version','0.5.3'),('gallery','types','filesystem'),('media','enabled','no'),('media','installed_version','0.4.3'),('media','types',NULL),('search_lucene','enabled','yes'),('search_lucene','installed_version','0.5.2'),('search_lucene','types','filesystem'),('tasks','enabled','yes'),('tasks','installed_version','0.1'),('tasks','types',''),('updater','enabled','yes'),('updater','installed_version','0.3'),('updater','types',NULL),('user_ldap','bgjUpdateGroupsLastRun','1387461455'),('user_ldap','enabled','yes'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','0.4.1'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port','389'),('user_ldap','ldap_base','DC=blackmesa,DC=org'),('user_ldap','ldap_base_groups','OU=Groups,OU=People,DC=blackmesa,DC=org'),('user_ldap','ldap_base_users','OU=People,DC=blackmesa,DC=org'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','cn'),('user_ldap','ldap_dn',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_expert_username_attr',''),('user_ldap','ldap_expert_uuid_attr',''),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','objectClass=posixGroup'),('user_ldap','ldap_group_member_assoc_attribute','member'),('user_ldap','ldap_host','ldap://127.0.0.1'),('user_ldap','ldap_login_filter','sAMAccountName=%uid'),('user_ldap','ldap_nocase',''),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls',''),('user_ldap','ldap_turn_off_cert_check',''),('user_ldap','ldap_userlist_filter','objectClass=person'),('user_ldap','ldap_uuid_attribute','objectguid'),('user_ldap','ldap_uuid_group_attribute','objectguid'),('user_ldap','ldap_uuid_user_attribute','objectguid'),('user_ldap','types','authentication'),('user_migrate','enabled','no'),('user_migrate','installed_version','0.1'),('user_migrate','types',NULL);
/*!40000 ALTER TABLE `oc_appconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_clndr_calendars`
--

DROP TABLE IF EXISTS `oc_clndr_calendars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_clndr_calendars` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) DEFAULT NULL,
  `displayname` varchar(100) DEFAULT NULL,
  `uri` varchar(255) DEFAULT NULL,
  `active` int(11) NOT NULL DEFAULT '1',
  `ctag` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarorder` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarcolor` varchar(10) DEFAULT NULL,
  `timezone` longtext,
  `components` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `objecttype` varchar(40) NOT NULL DEFAULT ' ',
  `startdate` datetime DEFAULT '1970-01-01 00:00:00',
  `enddate` datetime DEFAULT '1970-01-01 00:00:00',
  `repeating` int(11) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `calendardata` longtext,
  `uri` varchar(255) DEFAULT NULL,
  `lastmodified` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `owner` varchar(255) NOT NULL DEFAULT ' ',
  `share` varchar(255) NOT NULL DEFAULT ' ',
  `sharetype` varchar(6) NOT NULL DEFAULT ' ',
  `calendarid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `permissions` tinyint(4) NOT NULL DEFAULT '0',
  `active` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `owner` varchar(255) NOT NULL DEFAULT ' ',
  `share` varchar(255) NOT NULL DEFAULT ' ',
  `sharetype` varchar(6) NOT NULL DEFAULT ' ',
  `eventid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `permissions` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `userid` varchar(255) NOT NULL DEFAULT '',
  `displayname` varchar(255) DEFAULT NULL,
  `uri` varchar(200) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `ctag` int(10) unsigned NOT NULL DEFAULT '1',
  `active` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_contacts_addressbooks`
--

LOCK TABLES `oc_contacts_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_contacts_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_contacts_addressbooks` VALUES (1,'admin','Contacts','contacts','Default Address Book',1,1);
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
  `fullname` varchar(255) DEFAULT NULL,
  `carddata` longtext,
  `uri` varchar(200) DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `userid` varchar(255) NOT NULL DEFAULT '',
  `contactid` int(10) unsigned NOT NULL DEFAULT '0',
  `name` varchar(64) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `preferred` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `cp_name_index` (`name`),
  KEY `cp_value_index` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_contacts_cards_properties`
--

LOCK TABLES `oc_contacts_cards_properties` WRITE;
/*!40000 ALTER TABLE `oc_contacts_cards_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_contacts_cards_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_encryption`
--

DROP TABLE IF EXISTS `oc_encryption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_encryption` (
  `uid` varchar(64) NOT NULL,
  `mode` varchar(64) NOT NULL,
  `recovery_enabled` int(11) NOT NULL DEFAULT '0',
  `migration_status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_encryption`
--

LOCK TABLES `oc_encryption` WRITE;
/*!40000 ALTER TABLE `oc_encryption` DISABLE KEYS */;
INSERT INTO `oc_encryption` VALUES ('admin','server-side',0,1),('62502FA8-1105-4346-A829-218EA2A8B6B6','server-side',0,1);
/*!40000 ALTER TABLE `oc_encryption` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_file_map`
--

DROP TABLE IF EXISTS `oc_file_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_file_map` (
  `logic_path` varchar(512) NOT NULL DEFAULT '',
  `logic_path_hash` varchar(32) NOT NULL DEFAULT '',
  `physic_path` varchar(512) NOT NULL DEFAULT '',
  `physic_path_hash` varchar(32) NOT NULL DEFAULT '',
  PRIMARY KEY (`logic_path_hash`),
  UNIQUE KEY `file_map_pp_index` (`physic_path_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `path` varchar(512) DEFAULT NULL,
  `path_hash` varchar(32) NOT NULL DEFAULT '',
  `parent` int(11) NOT NULL DEFAULT '0',
  `name` varchar(250) DEFAULT NULL,
  `mimetype` int(11) NOT NULL DEFAULT '0',
  `mimepart` int(11) NOT NULL DEFAULT '0',
  `size` bigint(20) NOT NULL DEFAULT '0',
  `mtime` int(11) NOT NULL DEFAULT '0',
  `encrypted` int(11) NOT NULL DEFAULT '0',
  `unencrypted_size` bigint(20) NOT NULL DEFAULT '0',
  `etag` varchar(40) DEFAULT NULL,
  `storage_mtime` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`fileid`),
  UNIQUE KEY `fs_storage_path_hash` (`storage`,`path_hash`),
  KEY `fs_parent_name_hash` (`parent`,`name`),
  KEY `fs_storage_mimetype` (`storage`,`mimetype`),
  KEY `fs_storage_mimepart` (`storage`,`mimepart`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,856,1387462010,0,0,'52b2fd7a76ab4',0),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,0,1387462010,0,0,'52b2fd7a75dfc',1387462010),(3,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1387205082,0,0,'52b2fd4d2b37e',1387205082),(4,2,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,1386079307,0,0,'529de46467266',0),(5,2,'files','45b963397aa40d4a0063e0d85e4fe7a1',4,'files',2,1,54840,1387205084,0,0,'52b2fd5a2d270',1387205084),(6,2,'files/test1','76f319578995011a1b66bff4f2495d37',5,'test1',2,1,0,1387205082,0,0,'52b2fd5a3064c',1387205082),(7,2,'files/pseudocode.odt','a3ca53892eb4ec4f73f7b1cbb08e9c83',5,'pseudocode.odt',4,3,25576,1386085875,1,19110,'529de7093c13b',0),(8,2,'files/Year 9 Computing Grades.ods','d1d5a96fd55710daf33aac64900e466d',5,'Year 9 Computing Grades.ods',5,3,29264,1386085876,1,21874,'529de748ba783',0),(9,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,54840,1386079307,0,0,'529debe3b3fdb',0),(10,3,'62502FA8-1105-4346-A829-218EA2A8B6B6','cf749073bb3dc472fd8f236bb80a89b0',9,'62502FA8-1105-4346-A829-218EA2A8B6B6',2,1,54840,1386079547,0,0,'529debe3b3d82',0),(11,3,'62502FA8-1105-4346-A829-218EA2A8B6B6/files','66c78424e1e234db0a3604057a552e24',10,'files',2,1,54840,1386080072,0,0,'529debe3b3b21',0),(12,3,'62502FA8-1105-4346-A829-218EA2A8B6B6/files/pseudocode.odt','bd0292a69c31881ef480a9a994f07a75',11,'pseudocode.odt',4,3,25576,1386085875,0,0,'529dfdfd74c0f',0),(13,3,'62502FA8-1105-4346-A829-218EA2A8B6B6/files/Year 9 Computing Grades.ods','f77d34e4f617ab101e8ddc844e16edc4',11,'Year 9 Computing Grades.ods',5,3,29264,1386085876,0,0,'529dfe35ef0c7',0),(14,4,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df22d20a27',0),(15,5,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df2bf24873',0),(16,6,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,0,0,0,'529df2e38aa42',0),(17,7,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df3186a100',0),(18,8,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df3b3b8dbd',0),(19,9,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,1385562213,0,0,'529df3cb82798',0),(20,10,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df44f0b70b',0),(21,11,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df643104fb',0),(22,12,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,0,0,0,'529df677c0030',0),(23,13,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df6911715c',0),(24,14,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,0,0,0,'529df70008439',0),(26,2,'files/test2','83a97dfef853db52113c0ca6cfb15c5e',5,'test2',10,3,0,1386675240,0,0,'52a6fc4e9a24b',0),(27,3,'62502FA8-1105-4346-A829-218EA2A8B6B6/files/test2','88245b8635e637b8a037cd506575fb44',11,'test2',6,3,0,1386675240,0,0,'52a6fe89e1e9c',0),(28,1,'files_trashbin','fb66dca5f27af6f15c1d1d81e6f8d28b',1,'files_trashbin',2,1,856,1387462010,0,0,'52b2fd7ad850c',1387462010),(29,1,'files_trashbin/files','3014a771cbe30761f2e9ff3272110dbf',28,'files',2,1,100,1387462010,0,0,'52b2fd7ad7f1b',1387462010),(30,1,'files_trashbin/files/karoshi_setup.d1387462010','1252b45ba026d930c5e39ed5f08ee2ea',29,'karoshi_setup.d1387462010',10,3,100,1386086046,0,0,'52b2fd7adb4c0',1386086046),(31,1,'files_trashbin/share-keys','efadb182f5229706b54ec20d20e8c46d',28,'share-keys',2,1,512,1387462010,0,0,'52b2fdde55e7d',1387462010),(32,1,'files_trashbin/versions','c639d144d3f1014051e14a98beac5705',28,'versions',2,1,0,1387462010,0,0,'52b2fdde56d9e',1387462010),(33,1,'files_trashbin/keyfiles','728c7d8454e585e21166e28b78be8546',28,'keyfiles',2,1,244,1387462010,0,0,'52b2fdde57c3d',1387462010),(34,1,'files_trashbin/share-keys/karoshi_setup.admin.shareKey.d1387462010','0c550040f13d13ffb4586f62c75ea352',31,'karoshi_setup.admin.shareKey.d1387462010',10,3,512,1386086046,0,0,'52b2fdde5dc69',1386086046),(35,1,'files_trashbin/keyfiles/karoshi_setup.key.d1387462010','dff155fe346fa55f6ad214bf9e56a527',33,'karoshi_setup.key.d1387462010',10,3,244,1386086046,0,0,'52b2fdde63046',1386086046);
/*!40000 ALTER TABLE `oc_filecache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_files_trash`
--

DROP TABLE IF EXISTS `oc_files_trash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_files_trash` (
  `id` varchar(250) NOT NULL DEFAULT ' ',
  `user` varchar(64) NOT NULL DEFAULT ' ',
  `timestamp` varchar(12) NOT NULL DEFAULT ' ',
  `location` varchar(512) NOT NULL DEFAULT ' ',
  `type` varchar(4) NOT NULL DEFAULT ' ',
  `mime` varchar(30) NOT NULL DEFAULT ' ',
  KEY `id_index` (`id`),
  KEY `timestamp_index` (`timestamp`),
  KEY `user_index` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_files_trash`
--

LOCK TABLES `oc_files_trash` WRITE;
/*!40000 ALTER TABLE `oc_files_trash` DISABLE KEYS */;
INSERT INTO `oc_files_trash` VALUES ('karoshi_setup','admin','1387462010','/','file','application/octet-stream');
/*!40000 ALTER TABLE `oc_files_trash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_files_trashsize`
--

DROP TABLE IF EXISTS `oc_files_trashsize`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_files_trashsize` (
  `user` varchar(64) NOT NULL DEFAULT ' ',
  `size` varchar(50) NOT NULL DEFAULT ' '
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_files_trashsize`
--

LOCK TABLES `oc_files_trashsize` WRITE;
/*!40000 ALTER TABLE `oc_files_trashsize` DISABLE KEYS */;
INSERT INTO `oc_files_trashsize` VALUES ('admin','856');
/*!40000 ALTER TABLE `oc_files_trashsize` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_files_versions`
--

DROP TABLE IF EXISTS `oc_files_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_files_versions` (
  `user` varchar(64) NOT NULL DEFAULT ' ',
  `size` varchar(50) NOT NULL DEFAULT ' '
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_files_versions`
--

LOCK TABLES `oc_files_versions` WRITE;
/*!40000 ALTER TABLE `oc_files_versions` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_files_versions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_gallery_sharing`
--

DROP TABLE IF EXISTS `oc_gallery_sharing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_gallery_sharing` (
  `token` varchar(64) NOT NULL,
  `gallery_id` int(11) NOT NULL DEFAULT '0',
  `recursive` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_gallery_sharing`
--

LOCK TABLES `oc_gallery_sharing` WRITE;
/*!40000 ALTER TABLE `oc_gallery_sharing` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_gallery_sharing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_group_admin`
--

DROP TABLE IF EXISTS `oc_group_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_group_admin` (
  `gid` varchar(64) NOT NULL DEFAULT '',
  `uid` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`,`uid`),
  KEY `group_admin_uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `gid` varchar(64) NOT NULL DEFAULT '',
  `uid` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`,`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `gid` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `class` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `argument` varchar(256) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `last_run` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `job_class_index` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OC\\BackgroundJob\\Legacy\\RegularJob','[\"\\\\OC\\\\Files\\\\Cache\\\\BackgroundWatcher\",\"checkNext\"]',1387462194),(2,'OCA\\user_ldap\\lib\\Jobs','null',1387461932),(3,'OC\\Cache\\FileGlobalGC','null',1387462142);
/*!40000 ALTER TABLE `oc_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_group_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_group_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_mapping` (
  `ldap_dn` varchar(255) NOT NULL DEFAULT '',
  `owncloud_name` varchar(255) NOT NULL DEFAULT '',
  `directory_uuid` varchar(255) NOT NULL DEFAULT '',
  UNIQUE KEY `ldap_dn_groups` (`ldap_dn`),
  UNIQUE KEY `owncloud_name_groups` (`owncloud_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_group_mapping`
--

LOCK TABLES `oc_ldap_group_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_group_mapping` DISABLE KEYS */;
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=bursar,ou=groups,ou=people,DC=blackmesa,DC=org','bursar','46666E6C-F7A1-45AF-9E0C-D931C59FBA05'),('cn=exams,ou=groups,ou=people,DC=blackmesa,DC=org','exams','F8E473CD-06F1-498F-B442-AA8B07CB5D54'),('cn=governors,ou=groups,ou=people,DC=blackmesa,DC=org','governors','8D29FABF-EC94-4DE6-9A5C-966D63A2D56F'),('cn=guardians,ou=groups,ou=people,DC=blackmesa,DC=org','guardians','6844675E-3E4B-44C7-BF4A-557714E3BCE8'),('cn=guestusers,ou=groups,ou=people,DC=blackmesa,DC=org','guestusers','6CD43D1E-82F7-45C7-B717-9BD83CE87A13'),('cn=itadmin,ou=groups,ou=people,DC=blackmesa,DC=org','itadmin','32CC7AD2-F6B9-4C82-9A47-1D2526182127'),('cn=nonteachingstaff,ou=groups,ou=people,DC=blackmesa,DC=org','nonteachingstaff','5A6BC5F8-D586-4064-AD5E-2B26524D14D7'),('cn=officestaff,ou=groups,ou=people,DC=blackmesa,DC=org','officestaff','C708BA45-41B4-4169-98C0-4FF36EB2A99E'),('cn=profilemanagement,ou=groups,ou=people,DC=blackmesa,DC=org','profilemanagement','A419A9E8-886C-42EB-AB3D-BED881CAF45C'),('cn=smt,ou=groups,ou=people,DC=blackmesa,DC=org','smt','16583543-B5EE-4137-B5DD-96BBBCAAC358'),('cn=staff,ou=groups,ou=people,DC=blackmesa,DC=org','staff','C25082DB-6EFA-48CD-97F4-B1A9F1E4568F'),('cn=studentstaff,ou=groups,ou=people,DC=blackmesa,DC=org','studentstaff','E06EBC27-A2C2-454D-8677-CC8DDA488023'),('cn=tech,ou=groups,ou=people,DC=blackmesa,DC=org','tech','0E73BC7B-EC5C-45F6-B893-5BF341F0D1F2'),('cn=yr2001,ou=groups,ou=people,DC=blackmesa,DC=org','yr2001','509916FC-DCC5-49E2-BF18-E86AFA727E71'),('cn=yr2002,ou=groups,ou=people,DC=blackmesa,DC=org','yr2002','A80D464D-D206-48B6-8773-783B130A1762'),('cn=yr2003,ou=groups,ou=people,DC=blackmesa,DC=org','yr2003','A488DFA2-009C-411B-A42A-8DD82818AB54'),('cn=yr2004,ou=groups,ou=people,DC=blackmesa,DC=org','yr2004','18E64A12-9B55-46A3-BAA1-821AA87499FF'),('cn=yr2005,ou=groups,ou=people,DC=blackmesa,DC=org','yr2005','97A2960F-B2F3-45AE-A1A7-535C19B873D0'),('cn=yr2006,ou=groups,ou=people,DC=blackmesa,DC=org','yr2006','7CEB2AA8-3542-446B-8B11-5F78EBE283C6'),('cn=yr2007,ou=groups,ou=people,DC=blackmesa,DC=org','yr2007','337F4C8A-190D-4A97-A401-972F74859DCA'),('cn=yr2008,ou=groups,ou=people,DC=blackmesa,DC=org','yr2008','CED88B1F-AE33-465A-9C23-C00304050EC4'),('cn=yr2009,ou=groups,ou=people,DC=blackmesa,DC=org','yr2009','CF2626EC-2EC4-4130-955B-69861EEA07CD'),('cn=yr2010,ou=groups,ou=people,DC=blackmesa,DC=org','yr2010','ED57C47A-59E6-4AD6-A09D-9C23A94C3BCA'),('cn=yr2011,ou=groups,ou=people,DC=blackmesa,DC=org','yr2011','3A36682D-745F-4421-BF00-846CEB2B8DD2'),('cn=yr2012,ou=groups,ou=people,DC=blackmesa,DC=org','yr2012','ADCEED06-9F10-4CF7-AB18-F10CF1EF51AA'),('cn=yr2013,ou=groups,ou=people,DC=blackmesa,DC=org','yr2013','4868F4A6-25E1-4125-AEBA-48F31C835875'),('cn=yr2014,ou=groups,ou=people,DC=blackmesa,DC=org','yr2014','8EAEFB82-1661-4714-AAE9-0B4277944527'),('cn=yr2015,ou=groups,ou=people,DC=blackmesa,DC=org','yr2015','E3F58180-B788-4B03-87A0-B552853D7E38'),('cn=yr2016,ou=groups,ou=people,DC=blackmesa,DC=org','yr2016','B1A39E41-E1B1-46DD-977A-CE333B510BE2'),('cn=yr2017,ou=groups,ou=people,DC=blackmesa,DC=org','yr2017','737961D4-20C1-43E9-B60A-33122CE32AD8'),('cn=yr2018,ou=groups,ou=people,DC=blackmesa,DC=org','yr2018','D9D6B42C-4F4D-43E7-9C84-41995B5E6682'),('cn=yr2019,ou=groups,ou=people,DC=blackmesa,DC=org','yr2019','2B6419CD-E627-4DC3-A1B1-A3F8C51527B9'),('cn=yr2020,ou=groups,ou=people,DC=blackmesa,DC=org','yr2020','33545533-3E77-4AA5-AF25-09DF93FE1162'),('cn=yr2021,ou=groups,ou=people,DC=blackmesa,DC=org','yr2021','DFBBC03C-CE7E-4DFF-8515-83AD526BD43A'),('cn=yr2022,ou=groups,ou=people,DC=blackmesa,DC=org','yr2022','D30A3D9C-553D-4611-AAB2-5F9FC1BCB831'),('cn=yr2023,ou=groups,ou=people,DC=blackmesa,DC=org','yr2023','93569E15-5A3D-4D26-A46C-FAE10C33E47E'),('cn=yr2024,ou=groups,ou=people,DC=blackmesa,DC=org','yr2024','F7231E19-E5D8-4DB6-8DDE-5C42A3A33910'),('cn=yr2025,ou=groups,ou=people,DC=blackmesa,DC=org','yr2025','C3465FCE-CD74-4931-B4FC-A762F75845A0'),('cn=yr2026,ou=groups,ou=people,DC=blackmesa,DC=org','yr2026','D9659AE7-325E-402E-9385-3FD0EC01F983'),('cn=yr2027,ou=groups,ou=people,DC=blackmesa,DC=org','yr2027','738C2F8D-8AF4-4EFF-B215-E292B929C51B'),('cn=yr2028,ou=groups,ou=people,DC=blackmesa,DC=org','yr2028','231D81A1-974A-44CC-845D-2D0A8945F1B9'),('cn=yr2029,ou=groups,ou=people,DC=blackmesa,DC=org','yr2029','089244DB-5E54-4F00-94F8-19E83562C712'),('cn=yr2030,ou=groups,ou=people,DC=blackmesa,DC=org','yr2030','95424FA3-FD47-459A-9DAA-089FA1A0C690'),('cn=yr2031,ou=groups,ou=people,DC=blackmesa,DC=org','yr2031','65023FFE-2403-49DB-8441-100597960A0C'),('cn=yr2032,ou=groups,ou=people,DC=blackmesa,DC=org','yr2032','050377F4-EB5B-4E16-A7FD-834C5B8B1C87'),('cn=yr2033,ou=groups,ou=people,DC=blackmesa,DC=org','yr2033','6729E0F6-2207-4EC2-97DA-29A4B2E5F2DE'),('cn=yr2034,ou=groups,ou=people,DC=blackmesa,DC=org','yr2034','352A0187-C735-4C29-9C87-3174BC2B05D0'),('cn=yr2035,ou=groups,ou=people,DC=blackmesa,DC=org','yr2035','88DFBA53-A237-4EF1-A50C-39A1EDD7D3D4'),('cn=yr2036,ou=groups,ou=people,DC=blackmesa,DC=org','yr2036','DDCBBCC6-CF47-46D2-9A57-73F3C0934D73'),('cn=yr2037,ou=groups,ou=people,DC=blackmesa,DC=org','yr2037','64D57BD2-0D7D-494C-BF67-6CB0305C158B'),('cn=yr2038,ou=groups,ou=people,DC=blackmesa,DC=org','yr2038','10F5E0B1-4B94-44E3-B689-3B2E3B721A94'),('cn=yr2039,ou=groups,ou=people,DC=blackmesa,DC=org','yr2039','30140BCA-F484-4999-A760-01950CAB11BE'),('cn=yr2040,ou=groups,ou=people,DC=blackmesa,DC=org','yr2040','FB8DE615-B0CF-4954-91E5-18EEE72F979B'),('cn=yr2041,ou=groups,ou=people,DC=blackmesa,DC=org','yr2041','1927289B-68A3-461F-BDC9-8028ECA5D23E'),('cn=yr2042,ou=groups,ou=people,DC=blackmesa,DC=org','yr2042','2A285E9F-5CD7-49CC-9937-7666BAD53A90'),('cn=yr2043,ou=groups,ou=people,DC=blackmesa,DC=org','yr2043','E8F8BD02-61DB-4EE9-AD1D-17FF595C48D8'),('cn=yr2044,ou=groups,ou=people,DC=blackmesa,DC=org','yr2044','4A58B0C5-E4E7-4E7A-A6EB-538B88229872'),('cn=yr2045,ou=groups,ou=people,DC=blackmesa,DC=org','yr2045','227F7A99-7E3E-4690-8B7B-58655C149B9E'),('cn=yr2046,ou=groups,ou=people,DC=blackmesa,DC=org','yr2046','37D1BF4E-0DEC-4E90-B2D8-F8E22E79D4B0'),('cn=yr2047,ou=groups,ou=people,DC=blackmesa,DC=org','yr2047','80469449-B3E7-4DE8-BE80-3A48164B4A3C'),('cn=yr2048,ou=groups,ou=people,DC=blackmesa,DC=org','yr2048','36A5EBC9-7CB0-42F2-852B-2E78E50E4299');
/*!40000 ALTER TABLE `oc_ldap_group_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_group_members`
--

DROP TABLE IF EXISTS `oc_ldap_group_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_members` (
  `owncloudname` varchar(255) NOT NULL DEFAULT '',
  `owncloudusers` longtext NOT NULL,
  UNIQUE KEY `ldap_group_members_index` (`owncloudname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_group_members`
--

LOCK TABLES `oc_ldap_group_members` WRITE;
/*!40000 ALTER TABLE `oc_ldap_group_members` DISABLE KEYS */;
INSERT INTO `oc_ldap_group_members` VALUES ('bursar','a:0:{}'),('exams','a:5:{i:0;s:36:\"01CB6403-A340-4689-B2B7-FA815D990701\";i:1;s:36:\"92B64C14-D4DB-4911-A17A-837D4E2D1AF8\";i:2;s:36:\"756114B3-8D05-43EB-805B-AF640CC895B5\";i:3;s:36:\"A2CCB104-4C4F-4E96-BB53-1C3F2CF60122\";i:4;s:36:\"C3B0355E-091C-40DD-B206-EB4D73D333D6\";}'),('governors','a:0:{}'),('guardians','a:0:{}'),('guestusers','a:10:{i:0;s:36:\"21F4D433-21AF-44B9-8D45-80E8B7B6A51D\";i:1;s:36:\"79B90102-13EC-4335-8970-519066438B90\";i:2;s:36:\"84C93032-4439-4033-AA1E-7073189E7F6F\";i:3;s:36:\"725A2A62-C9AD-48CA-85E4-F5CA53BE5BCD\";i:4;s:36:\"896F3DDA-460F-43FB-9C7A-0449B5EB1895\";i:5;s:36:\"C8CEFA2B-EA7D-4255-A58C-E0BD1DD2369B\";i:6;s:36:\"CB0B4991-1523-4043-A958-51825BA150D6\";i:7;s:36:\"D08AC3C9-709C-4154-9CAF-AF6E7D226AB9\";i:8;s:36:\"D5687733-F266-4FA8-9360-A6EF0D4B8148\";i:9;s:36:\"EA22A818-706D-46F2-8843-C298FFA4C663\";}'),('itadmin','a:1:{i:0;s:36:\"497F5FE5-1406-404C-A657-D8E3AF9BA909\";}'),('nonteachingstaff','a:0:{}'),('officestaff','a:0:{}'),('profilemanagement','a:1:{i:0;s:36:\"DB13489D-67F6-495F-B6D5-C2C4E13130E9\";}'),('smt','a:0:{}'),('staff','a:3:{i:0;s:36:\"5FD9724B-40C3-4E64-884D-262239D28128\";i:1;s:36:\"62502FA8-1105-4346-A829-218EA2A8B6B6\";i:2;s:36:\"C054B037-D4B3-47F5-BDA9-CC0C24CC64E3\";}'),('studentstaff','a:0:{}'),('tech','a:4:{i:0;s:36:\"08A466EA-01C7-413C-85B6-F2F222277F41\";i:1;s:36:\"A6E6EB88-1927-4A3E-A4A7-15AB0EE43194\";i:2;s:36:\"ADA7F265-5B9A-4596-AEB3-6D6F7C9A9AE1\";i:3;s:36:\"DB36E452-4820-462E-8DEB-97EBA2057443\";}'),('yr2001','a:0:{}'),('yr2002','a:0:{}'),('yr2003','a:0:{}'),('yr2004','a:0:{}'),('yr2005','a:0:{}'),('yr2006','a:0:{}'),('yr2007','a:0:{}'),('yr2008','a:2:{i:0;s:36:\"06DA06FC-21CB-4FEB-97E4-5CDE8D53156A\";i:1;s:36:\"1440C0E1-12B2-4D6E-9F0B-AE9D2EA9FB0C\";}'),('yr2009','a:2:{i:0;s:36:\"0C4914A1-1B15-4F8D-A354-E78573650A74\";i:1;s:36:\"F8D6051D-1521-432A-A25B-3B4E825E8514\";}'),('yr2010','a:0:{}'),('yr2011','a:0:{}'),('yr2012','a:0:{}'),('yr2013','a:0:{}'),('yr2014','a:0:{}'),('yr2015','a:0:{}'),('yr2016','a:0:{}'),('yr2017','a:0:{}'),('yr2018','a:0:{}'),('yr2019','a:0:{}'),('yr2020','a:0:{}'),('yr2021','a:0:{}'),('yr2022','a:0:{}'),('yr2023','a:0:{}'),('yr2024','a:0:{}'),('yr2025','a:0:{}'),('yr2026','a:0:{}'),('yr2027','a:0:{}'),('yr2028','a:0:{}'),('yr2029','a:0:{}'),('yr2030','a:0:{}'),('yr2031','a:0:{}'),('yr2032','a:0:{}'),('yr2033','a:0:{}'),('yr2034','a:0:{}'),('yr2035','a:0:{}'),('yr2036','a:0:{}'),('yr2037','a:0:{}'),('yr2038','a:0:{}'),('yr2039','a:0:{}'),('yr2040','a:0:{}'),('yr2041','a:0:{}'),('yr2042','a:0:{}'),('yr2043','a:0:{}'),('yr2044','a:0:{}'),('yr2045','a:0:{}'),('yr2046','a:0:{}'),('yr2047','a:0:{}'),('yr2048','a:0:{}');
/*!40000 ALTER TABLE `oc_ldap_group_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_user_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_user_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_user_mapping` (
  `ldap_dn` varchar(255) NOT NULL DEFAULT '',
  `owncloud_name` varchar(255) NOT NULL DEFAULT '',
  `directory_uuid` varchar(255) NOT NULL DEFAULT '',
  UNIQUE KEY `ldap_dn_users` (`ldap_dn`),
  UNIQUE KEY `owncloud_name_users` (`owncloud_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_user_mapping`
--

LOCK TABLES `oc_ldap_user_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_user_mapping` DISABLE KEYS */;
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=apalmer,ou=staff,ou=personnel,ou=people,DC=blackmesa,DC=org','5FD9724B-40C3-4E64-884D-262239D28128','5FD9724B-40C3-4E64-884D-262239D28128'),('cn=exam1,ou=exams,ou=other,ou=people,dc=blackmesa,dc=org','756114B3-8D05-43EB-805B-AF640CC895B5','756114B3-8D05-43EB-805B-AF640CC895B5'),('cn=exam2,ou=exams,ou=other,ou=people,dc=blackmesa,dc=org','01CB6403-A340-4689-B2B7-FA815D990701','01CB6403-A340-4689-B2B7-FA815D990701'),('cn=exam3,ou=exams,ou=other,ou=people,dc=blackmesa,dc=org','C3B0355E-091C-40DD-B206-EB4D73D333D6','C3B0355E-091C-40DD-B206-EB4D73D333D6'),('cn=exam4,ou=exams,ou=other,ou=people,dc=blackmesa,dc=org','92B64C14-D4DB-4911-A17A-837D4E2D1AF8','92B64C14-D4DB-4911-A17A-837D4E2D1AF8'),('cn=exam5,ou=exams,ou=other,ou=people,dc=blackmesa,dc=org','A2CCB104-4C4F-4E96-BB53-1C3F2CF60122','A2CCB104-4C4F-4E96-BB53-1C3F2CF60122'),('cn=guest1,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','84C93032-4439-4033-AA1E-7073189E7F6F','84C93032-4439-4033-AA1E-7073189E7F6F'),('cn=guest10,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','C8CEFA2B-EA7D-4255-A58C-E0BD1DD2369B','C8CEFA2B-EA7D-4255-A58C-E0BD1DD2369B'),('cn=guest2,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','EA22A818-706D-46F2-8843-C298FFA4C663','EA22A818-706D-46F2-8843-C298FFA4C663'),('cn=guest3,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','CB0B4991-1523-4043-A958-51825BA150D6','CB0B4991-1523-4043-A958-51825BA150D6'),('cn=guest4,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','D5687733-F266-4FA8-9360-A6EF0D4B8148','D5687733-F266-4FA8-9360-A6EF0D4B8148'),('cn=guest5,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','725A2A62-C9AD-48CA-85E4-F5CA53BE5BCD','725A2A62-C9AD-48CA-85E4-F5CA53BE5BCD'),('cn=guest6,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','896F3DDA-460F-43FB-9C7A-0449B5EB1895','896F3DDA-460F-43FB-9C7A-0449B5EB1895'),('cn=guest7,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','D08AC3C9-709C-4154-9CAF-AF6E7D226AB9','D08AC3C9-709C-4154-9CAF-AF6E7D226AB9'),('cn=guest8,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','79B90102-13EC-4335-8970-519066438B90','79B90102-13EC-4335-8970-519066438B90'),('cn=guest9,ou=guestusers,ou=other,ou=people,DC=blackmesa,DC=org','21F4D433-21AF-44B9-8D45-80E8B7B6A51D','21F4D433-21AF-44B9-8D45-80E8B7B6A51D'),('cn=ismith,ou=staff,ou=personnel,ou=people,DC=blackmesa,DC=org','62502FA8-1105-4346-A829-218EA2A8B6B6','62502FA8-1105-4346-A829-218EA2A8B6B6'),('cn=ismith08,ou=yr2008,ou=students,ou=people,DC=blackmesa,DC=org','06DA06FC-21CB-4FEB-97E4-5CDE8D53156A','06DA06FC-21CB-4FEB-97E4-5CDE8D53156A'),('cn=jdavies09,ou=yr2009,ou=students,ou=people,DC=blackmesa,DC=org','0C4914A1-1B15-4F8D-A354-E78573650A74','0C4914A1-1B15-4F8D-A354-E78573650A74'),('cn=jjones,ou=staff,ou=personnel,ou=people,DC=blackmesa,DC=org','C054B037-D4B3-47F5-BDA9-CC0C24CC64E3','C054B037-D4B3-47F5-BDA9-CC0C24CC64E3'),('cn=karoshi-krb5,ou=karoshi,ou=other,ou=people,DC=blackmesa,DC=org','DC0E640A-43C5-46FE-A7E9-B5C75B958F63','DC0E640A-43C5-46FE-A7E9-B5C75B958F63'),('cn=kbailey08,ou=yr2008,ou=students,ou=people,DC=blackmesa,DC=org','1440C0E1-12B2-4D6E-9F0B-AE9D2EA9FB0C','1440C0E1-12B2-4D6E-9F0B-AE9D2EA9FB0C'),('cn=mjones09,ou=yr2009,ou=students,ou=people,DC=blackmesa,DC=org','F8D6051D-1521-432A-A25B-3B4E825E8514','F8D6051D-1521-432A-A25B-3B4E825E8514'),('cn=profileuser,ou=other,ou=people,DC=blackmesa,DC=org','DB13489D-67F6-495F-B6D5-C2C4E13130E9','DB13489D-67F6-495F-B6D5-C2C4E13130E9'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,DC=blackmesa,DC=org','497F5FE5-1406-404C-A657-D8E3AF9BA909','497F5FE5-1406-404C-A657-D8E3AF9BA909'),('cn=tech1,ou=tech,ou=personnel,ou=people,DC=blackmesa,DC=org','DB36E452-4820-462E-8DEB-97EBA2057443','DB36E452-4820-462E-8DEB-97EBA2057443'),('cn=tech2,ou=tech,ou=personnel,ou=people,DC=blackmesa,DC=org','ADA7F265-5B9A-4596-AEB3-6D6F7C9A9AE1','ADA7F265-5B9A-4596-AEB3-6D6F7C9A9AE1'),('cn=tech3,ou=tech,ou=personnel,ou=people,DC=blackmesa,DC=org','A6E6EB88-1927-4A3E-A4A7-15AB0EE43194','A6E6EB88-1927-4A3E-A4A7-15AB0EE43194'),('cn=tech4,ou=tech,ou=personnel,ou=people,DC=blackmesa,DC=org','08A466EA-01C7-413C-85B6-F2F222277F41','08A466EA-01C7-413C-85B6-F2F222277F41');
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
  `userid` varchar(64) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `timeout` int(10) unsigned DEFAULT NULL,
  `created` bigint(20) DEFAULT NULL,
  `token` varchar(100) DEFAULT NULL,
  `scope` smallint(6) DEFAULT NULL,
  `depth` smallint(6) DEFAULT NULL,
  `uri` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_locks`
--

LOCK TABLES `oc_locks` WRITE;
/*!40000 ALTER TABLE `oc_locks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_locks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_lucene_status`
--

DROP TABLE IF EXISTS `oc_lucene_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_lucene_status` (
  `fileid` int(11) NOT NULL DEFAULT '0',
  `status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`fileid`),
  KEY `status_index` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_lucene_status`
--

LOCK TABLES `oc_lucene_status` WRITE;
/*!40000 ALTER TABLE `oc_lucene_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_lucene_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_media_albums`
--

DROP TABLE IF EXISTS `oc_media_albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_media_albums` (
  `album_id` int(11) NOT NULL AUTO_INCREMENT,
  `album_name` varchar(200) NOT NULL DEFAULT ' ',
  `album_artist` int(11) NOT NULL DEFAULT '0',
  `album_art` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`album_id`),
  KEY `album_name_index` (`album_name`),
  KEY `album_artist_index` (`album_artist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_albums`
--

LOCK TABLES `oc_media_albums` WRITE;
/*!40000 ALTER TABLE `oc_media_albums` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_media_albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_media_artists`
--

DROP TABLE IF EXISTS `oc_media_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_media_artists` (
  `artist_id` int(11) NOT NULL AUTO_INCREMENT,
  `artist_name` varchar(200) NOT NULL DEFAULT ' ',
  PRIMARY KEY (`artist_id`),
  UNIQUE KEY `artist_name` (`artist_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_artists`
--

LOCK TABLES `oc_media_artists` WRITE;
/*!40000 ALTER TABLE `oc_media_artists` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_media_artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_media_sessions`
--

DROP TABLE IF EXISTS `oc_media_sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_media_sessions` (
  `session_id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(64) NOT NULL DEFAULT ' ',
  `user_id` varchar(64) NOT NULL DEFAULT ' ',
  `start` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_sessions`
--

LOCK TABLES `oc_media_sessions` WRITE;
/*!40000 ALTER TABLE `oc_media_sessions` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_media_sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_media_songs`
--

DROP TABLE IF EXISTS `oc_media_songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_media_songs` (
  `song_id` int(11) NOT NULL AUTO_INCREMENT,
  `song_name` varchar(200) NOT NULL DEFAULT ' ',
  `song_artist` int(11) NOT NULL DEFAULT '0',
  `song_album` int(11) NOT NULL DEFAULT '0',
  `song_path` varchar(200) NOT NULL DEFAULT ' ',
  `song_user` varchar(64) NOT NULL DEFAULT '0',
  `song_length` int(11) NOT NULL DEFAULT '0',
  `song_track` int(11) NOT NULL DEFAULT '0',
  `song_size` int(11) NOT NULL DEFAULT '0',
  `song_playcount` int(11) NOT NULL DEFAULT '0',
  `song_lastplayed` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`song_id`),
  KEY `song_album_index` (`song_album`),
  KEY `song_artist_index` (`song_artist`),
  KEY `song_name_index` (`song_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_songs`
--

LOCK TABLES `oc_media_songs` WRITE;
/*!40000 ALTER TABLE `oc_media_songs` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_media_songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_media_users`
--

DROP TABLE IF EXISTS `oc_media_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_media_users` (
  `user_id` varchar(64) NOT NULL DEFAULT '0',
  `user_password_sha256` varchar(64) NOT NULL DEFAULT ' '
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_users`
--

LOCK TABLES `oc_media_users` WRITE;
/*!40000 ALTER TABLE `oc_media_users` DISABLE KEYS */;
INSERT INTO `oc_media_users` VALUES ('admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'),('62502FA8-1105-4346-A829-218EA2A8B6B6','2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824');
/*!40000 ALTER TABLE `oc_media_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_mimetypes`
--

DROP TABLE IF EXISTS `oc_mimetypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_mimetypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mimetype` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mimetype_id_index` (`mimetype`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (7,''),(3,'application'),(10,'application/octet-stream'),(5,'application/vnd.oasis.opendocument.spreadsheet'),(4,'application/vnd.oasis.opendocument.text'),(6,'application/x-empty'),(1,'httpd'),(2,'httpd/unix-directory'),(8,'text'),(9,'text/plain');
/*!40000 ALTER TABLE `oc_mimetypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_permissions`
--

DROP TABLE IF EXISTS `oc_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_permissions` (
  `fileid` int(11) NOT NULL DEFAULT '0',
  `user` varchar(64) DEFAULT NULL,
  `permissions` int(11) NOT NULL DEFAULT '0',
  KEY `id_user_index` (`fileid`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_permissions`
--

LOCK TABLES `oc_permissions` WRITE;
/*!40000 ALTER TABLE `oc_permissions` DISABLE KEYS */;
INSERT INTO `oc_permissions` VALUES (2,'admin',31),(12,'',27),(13,'',27),(14,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(15,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(16,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(17,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(18,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(19,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(20,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(21,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(22,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(23,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(24,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(27,'',27),(7,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(26,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(8,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(5,'62502FA8-1105-4346-A829-218EA2A8B6B6',31),(30,'admin',27);
/*!40000 ALTER TABLE `oc_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_pictures_images_cache`
--

DROP TABLE IF EXISTS `oc_pictures_images_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_pictures_images_cache` (
  `uid_owner` varchar(64) NOT NULL,
  `path` varchar(256) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_pictures_images_cache`
--

LOCK TABLES `oc_pictures_images_cache` WRITE;
/*!40000 ALTER TABLE `oc_pictures_images_cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_pictures_images_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_preferences`
--

DROP TABLE IF EXISTS `oc_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_preferences` (
  `userid` varchar(64) NOT NULL DEFAULT '',
  `appid` varchar(32) NOT NULL DEFAULT '',
  `configkey` varchar(64) NOT NULL DEFAULT '',
  `configvalue` longtext,
  PRIMARY KEY (`userid`,`appid`,`configkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_preferences`
--

LOCK TABLES `oc_preferences` WRITE;
/*!40000 ALTER TABLE `oc_preferences` DISABLE KEYS */;
INSERT INTO `oc_preferences` VALUES ('62502FA8-1105-4346-A829-218EA2A8B6B6','files','cache_version','5'),('62502FA8-1105-4346-A829-218EA2A8B6B6','firstrunwizard','show','0'),('62502FA8-1105-4346-A829-218EA2A8B6B6','user_ldap','firstLoginAccomplished','1'),('62502FA8-1105-4346-A829-218EA2A8B6B6','user_ldap','lastJpegPhotoLookup','1387461977'),('admin','files','cache_version','5'),('admin','firstrunwizard','show','0');
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
  `user` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `key` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `value` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`keyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  `userid` varchar(64) NOT NULL DEFAULT '',
  `propertypath` varchar(255) NOT NULL DEFAULT '',
  `propertyname` varchar(255) NOT NULL DEFAULT '',
  `propertyvalue` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `property_index` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_properties`
--

LOCK TABLES `oc_properties` WRITE;
/*!40000 ALTER TABLE `oc_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_queuedtasks`
--

DROP TABLE IF EXISTS `oc_queuedtasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_queuedtasks` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL DEFAULT ' ',
  `klass` varchar(255) NOT NULL DEFAULT ' ',
  `method` varchar(255) NOT NULL DEFAULT ' ',
  `parameters` varchar(255) NOT NULL DEFAULT ' ',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_queuedtasks`
--

LOCK TABLES `oc_queuedtasks` WRITE;
/*!40000 ALTER TABLE `oc_queuedtasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_queuedtasks` ENABLE KEYS */;
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
  `share_with` varchar(255) DEFAULT NULL,
  `uid_owner` varchar(255) NOT NULL DEFAULT '',
  `parent` int(11) DEFAULT NULL,
  `item_type` varchar(64) NOT NULL DEFAULT '',
  `item_source` varchar(255) DEFAULT NULL,
  `item_target` varchar(255) DEFAULT NULL,
  `file_source` int(11) DEFAULT NULL,
  `file_target` varchar(512) DEFAULT NULL,
  `permissions` smallint(6) NOT NULL DEFAULT '0',
  `stime` bigint(20) NOT NULL DEFAULT '0',
  `accepted` smallint(6) NOT NULL DEFAULT '0',
  `expiration` datetime DEFAULT NULL,
  `token` varchar(32) DEFAULT NULL,
  `mail_send` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `token_index` (`token`),
  KEY `item_share_type_index` (`item_type`,`share_type`),
  KEY `file_source_index` (`file_source`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_share`
--

LOCK TABLES `oc_share` WRITE;
/*!40000 ALTER TABLE `oc_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_share` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_storages`
--

DROP TABLE IF EXISTS `oc_storages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_storages` (
  `id` varchar(64) DEFAULT NULL,
  `numeric_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`numeric_id`),
  UNIQUE KEY `storages_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('home::62502FA8-1105-4346-A829-218EA2A8B6B6',2),('home::admin',1),('local::/home/owncloud/data/',3),('smb::ismith@//172.30.3.1/ismith//homefolder//',5),('smb::ismith@//172.30.3.1/ismith//root//',13),('smb::ismith@172.30.3.1//homefolder//',7),('smb::ismith@172.30.3.1//ismith//',9),('smb::ismith@172.30.3.1//ismith//ismith/',14),('smb::ismith@172.30.3.1/i//ismith//',8),('smb::ismith@172.30.3.1/ismith//homefolder//',6),('smb::ismith@172.30.3.1/ismith//root//',12),('smb::ismith@ismith@172.30.3.1//ismith//',11),('smb::ismith@smb://172.30.3.1/ismith//homefolder//',4),('smb::ismith@\\\\172.30.3.1\\ismith//ismith//',10);
/*!40000 ALTER TABLE `oc_storages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_users`
--

DROP TABLE IF EXISTS `oc_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_users` (
  `uid` varchar(64) NOT NULL DEFAULT '',
  `displayname` varchar(64) DEFAULT NULL,
  `password` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_users`
--

LOCK TABLES `oc_users` WRITE;
/*!40000 ALTER TABLE `oc_users` DISABLE KEYS */;
INSERT INTO `oc_users` VALUES ('admin',NULL,'$2a$08$wH8reufYCCm21ZMJYWQYtuSHssb57fuKzNfdZSPxlvqL75weCxFMK');
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
  `uid` varchar(64) NOT NULL DEFAULT '',
  `type` varchar(64) NOT NULL DEFAULT '',
  `category` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `uid_index` (`uid`),
  KEY `type_index` (`type`),
  KEY `category_index` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `type` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`categoryid`,`objid`,`type`),
  KEY `vcategory_objectd_index` (`objid`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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

-- Dump completed on 2013-12-19 14:10:45
