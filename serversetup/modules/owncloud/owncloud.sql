-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: owncloud
-- ------------------------------------------------------
-- Server version	5.5.35-0ubuntu0.12.04.2

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
INSERT INTO `oc_appconfig` VALUES ('admin_migrate','enabled','no'),('admin_migrate','installed_version','0.1'),('admin_migrate','types',NULL),('backgroundjob','lastjob','1'),('calendar','enabled','no'),('calendar','installed_version','0.6.3'),('calendar','types',NULL),('contacts','enabled','no'),('contacts','installed_version','0.3'),('contacts','types',''),('core','backgroundjobs_step','regular_tasks'),('core','backgroundjobs_task',''),('core','global_cache_gc_lastrun','1395916083'),('core','installedat','1386078554.6398'),('core','lastupdatedat','1395916077'),('core','lastupdateResult','{\"version\":{},\"versionstring\":{},\"url\":{},\"web\":{}}'),('core','public_caldav','calendar/share.php'),('core','public_calendar','calendar/share.php'),('core','public_files','files_sharing/public.php'),('core','public_gallery','gallery/public.php'),('core','public_webdav','files_sharing/public.php'),('core','remote_ampache','media/remote.php'),('core','remote_caldav','calendar/appinfo/remote.php'),('core','remote_calendar','calendar/appinfo/remote.php'),('core','remote_carddav','contacts/appinfo/remote.php'),('core','remote_contacts','contacts/appinfo/remote.php'),('core','remote_contactthumbnail','contacts/thumbnail.php'),('core','remote_core.css','/core/minimizer.php'),('core','remote_core.js','/core/minimizer.php'),('core','remote_files','files/appinfo/remote.php'),('core','remote_filesync','files/appinfo/filesync.php'),('core','remote_webdav','files/appinfo/remote.php'),('core','shareapi_allow_links','no'),('core','shareapi_allow_resharing','no'),('files','backgroundwatcher_previous_file','18'),('files','backgroundwatcher_previous_folder','29'),('files','default_quota','50 GB'),('files','enabled','yes'),('files','installed_version','1.1.7'),('files','types','filesystem'),('files_encryption','enabled','no'),('files_encryption','installed_version','0.5'),('files_encryption','publicShareKeyId','pubShare_df7de1ac'),('files_encryption','types','filesystem'),('files_external','allow_user_mounting','no'),('files_external','enabled','yes'),('files_external','installed_version','0.2'),('files_external','types','filesystem'),('files_imageviewer','enabled','no'),('files_imageviewer','installed_version','1.0'),('files_imageviewer','types',NULL),('files_odfviewer','enabled','no'),('files_odfviewer','installed_version','0.1'),('files_odfviewer','types',NULL),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','0.2'),('files_pdfviewer','types',NULL),('files_sharing','enabled','yes'),('files_sharing','installed_version','0.3.5'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','0.3'),('files_texteditor','types',NULL),('files_trashbin','enabled','no'),('files_trashbin','installed_version','0.5'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.0.3'),('files_versions','types','filesystem'),('files_videoviewer','enabled','yes'),('files_videoviewer','installed_version','0.1.2'),('files_videoviewer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','1.0'),('firstrunwizard','types',NULL),('gallery','enabled','yes'),('gallery','installed_version','0.5.3'),('gallery','types','filesystem'),('media','enabled','no'),('media','installed_version','0.4.3'),('media','types',NULL),('search_lucene','enabled','yes'),('search_lucene','installed_version','0.5.2'),('search_lucene','types','filesystem'),('tasks','enabled','no'),('tasks','installed_version','0.1'),('tasks','types',''),('updater','enabled','yes'),('updater','installed_version','0.3'),('updater','types',NULL),('user_ldap','bgjUpdateGroupsLastRun','1387461455'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','0.4.1'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port','389'),('user_ldap','ldap_base','DC=testdomain,DC=com'),('user_ldap','ldap_base_groups','OU=Groups,OU=People,DC=testdomain,DC=com'),('user_ldap','ldap_base_users','OU=People,DC=testdomain,DC=com'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayname'),('user_ldap','ldap_dn',''),('user_ldap','ldap_email_attr','mail'),('user_ldap','ldap_expert_username_attr','cn'),('user_ldap','ldap_expert_uuid_attr',''),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','group'),('user_ldap','ldap_group_display_name','displayname'),('user_ldap','ldap_group_filter','(&(|(objectclass=group)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','member'),('user_ldap','ldap_host','ldap://127.0.0.1'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=user)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_nocase','0'),('user_ldap','ldap_override_main_server','0'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls',''),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','user'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=user)))'),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_uuid_attribute','objectguid'),('user_ldap','ldap_uuid_group_attribute','objectguid'),('user_ldap','ldap_uuid_user_attribute','objectguid'),('user_ldap','types','authentication'),('user_migrate','enabled','no'),('user_migrate','installed_version','0.1'),('user_migrate','types',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
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
INSERT INTO `oc_encryption` VALUES ('admin','server-side',0,0),('62502FA8-1105-4346-A829-218EA2A8B6B6','server-side',0,0),('89400D1A-371D-4B34-B5FB-CAE34482DBA4','server-side',0,0);
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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,6043957,1387462010,0,0,'52b2fd7a76ab4',0),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,6038713,1395916075,0,0,'5333fd2ce8e08',1395916075),(3,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1387205082,0,0,'52b2fd4d2b37e',1387205082),(4,2,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,1386079307,0,0,'529de46467266',0),(5,2,'files','45b963397aa40d4a0063e0d85e4fe7a1',4,'files',2,1,54840,1387205084,0,0,'52b2fd5a2d270',1387205084),(6,2,'files/test1','76f319578995011a1b66bff4f2495d37',5,'test1',2,1,0,1387205082,0,0,'52b2fd5a3064c',1387205082),(7,2,'files/pseudocode.odt','a3ca53892eb4ec4f73f7b1cbb08e9c83',5,'pseudocode.odt',4,3,25576,1386085875,1,19110,'529de7093c13b',0),(8,2,'files/Year 9 Computing Grades.ods','d1d5a96fd55710daf33aac64900e466d',5,'Year 9 Computing Grades.ods',5,3,29264,1386085876,1,21874,'529de748ba783',0),(9,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1395916086,0,0,'5333fd38b4b0c',1395916086),(14,4,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df22d20a27',0),(15,5,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df2bf24873',0),(16,6,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,0,0,0,'529df2e38aa42',0),(17,7,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df3186a100',0),(18,8,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df3b3b8dbd',0),(19,9,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,1385562213,0,0,'529df3cb82798',0),(20,10,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df44f0b70b',0),(21,11,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df643104fb',0),(22,12,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,0,0,0,'529df677c0030',0),(23,13,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',6,3,0,0,0,0,'529df6911715c',0),(24,14,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',7,7,0,0,0,0,'529df70008439',0),(26,2,'files/test2','83a97dfef853db52113c0ca6cfb15c5e',5,'test2',10,3,0,1386675240,0,0,'52a6fc4e9a24b',0),(28,1,'files_trashbin','fb66dca5f27af6f15c1d1d81e6f8d28b',1,'files_trashbin',2,1,856,1387462010,0,0,'52b2fd7ad850c',1387462010),(29,1,'files_trashbin/files','3014a771cbe30761f2e9ff3272110dbf',28,'files',2,1,100,1387462010,0,0,'52b2fd7ad7f1b',1387462010),(30,1,'files_trashbin/files/karoshi_setup.d1387462010','1252b45ba026d930c5e39ed5f08ee2ea',29,'karoshi_setup.d1387462010',10,3,100,1386086046,0,0,'52b2fd7adb4c0',1386086046),(31,1,'files_trashbin/share-keys','efadb182f5229706b54ec20d20e8c46d',28,'share-keys',2,1,512,1387462010,0,0,'52b2fdde55e7d',1387462010),(32,1,'files_trashbin/versions','c639d144d3f1014051e14a98beac5705',28,'versions',2,1,0,1387462010,0,0,'52b2fdde56d9e',1387462010),(33,1,'files_trashbin/keyfiles','728c7d8454e585e21166e28b78be8546',28,'keyfiles',2,1,244,1387462010,0,0,'52b2fdde57c3d',1387462010),(34,1,'files_trashbin/share-keys/karoshi_setup.admin.shareKey.d1387462010','0c550040f13d13ffb4586f62c75ea352',31,'karoshi_setup.admin.shareKey.d1387462010',10,3,512,1386086046,0,0,'52b2fdde5dc69',1386086046),(35,1,'files_trashbin/keyfiles/karoshi_setup.key.d1387462010','dff155fe346fa55f6ad214bf9e56a527',33,'karoshi_setup.key.d1387462010',10,3,244,1386086046,0,0,'52b2fdde63046',1386086046),(36,15,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1395914575,0,0,'5333f753dae04',1395914575),(37,15,'files','45b963397aa40d4a0063e0d85e4fe7a1',36,'files',2,1,8075360,1395914579,0,0,'5333f753d95fc',1395914579),(38,15,'files/documents','2d30f25cef1a92db784bc537e8bf128d',37,'documents',2,1,31276,1395914578,0,23383,'5333f75269840',1395914578),(39,15,'files/documents/example.odt','f51311bd6910ec7356d79286dcb24dec',38,'example.odt',4,3,31276,1395914575,1,23383,'5333f751e3df1',1395914575),(40,15,'files/music','1f8cfec283cd675038bb95b599fdc75a',37,'music',2,1,5034500,1395914578,0,3764804,'5333f752c8752',1395914578),(41,15,'files/music/projekteva-letitrain.mp3','da7d05a957a2bbbf0e74b12c1b5fcfee',40,'projekteva-letitrain.mp3',12,11,5034500,1395914575,1,3764804,'5333f751ed000',1395914575),(42,15,'files/photos','923e51351db3e8726f22ba0fa1c04d5a',37,'photos',2,1,907456,1395914579,0,678556,'5333f7539333c',1395914579),(43,15,'files/photos/squirrel.jpg','e462c24fc17cb1a3fa3bca86d7f89593',42,'squirrel.jpg',14,13,312568,1395914575,1,233724,'5333f75219dd7',1395914575),(44,15,'files/photos/paris.jpg','65154b90b985bff20d4923f224ca1c33',42,'paris.jpg',14,13,305928,1395914575,1,228761,'5333f752200c4',1395914575),(45,15,'files/photos/san francisco.jpg','e86e87a4ecd557753734e1d34fbeecec',42,'san francisco.jpg',14,13,288960,1395914575,1,216071,'5333f7522483f',1395914575),(46,15,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',37,'ownCloudUserManual.pdf',15,3,2102128,1395914575,1,1571970,'5333f75229323',1395914575),(47,1,'files/documents','2d30f25cef1a92db784bc537e8bf128d',2,'documents',2,1,23383,1395916075,0,0,'5333fd2cebb91',1395916075),(48,1,'files/music','1f8cfec283cd675038bb95b599fdc75a',2,'music',2,1,3764804,1395916075,0,0,'5333fd2cec696',1395916075),(49,1,'files/photos','923e51351db3e8726f22ba0fa1c04d5a',2,'photos',2,1,678556,1395916075,0,0,'5333fd2ced035',1395916075),(50,1,'files/ownCloudUserManual.pdf','c8edba2d1b8eb651c107b43532c34445',2,'ownCloudUserManual.pdf',15,3,1571970,1395916075,0,0,'5333fd2cedca4',1395916075),(51,1,'files/photos/squirrel.jpg','e462c24fc17cb1a3fa3bca86d7f89593',49,'squirrel.jpg',14,13,233724,1395916075,0,0,'5333fd34c329b',1395916075),(52,1,'files/photos/paris.jpg','65154b90b985bff20d4923f224ca1c33',49,'paris.jpg',14,13,228761,1395916075,0,0,'5333fd34c4ba4',1395916075),(53,1,'files/photos/san francisco.jpg','e86e87a4ecd557753734e1d34fbeecec',49,'san francisco.jpg',14,13,216071,1395916075,0,0,'5333fd34c5888',1395916075),(54,1,'files/music/projekteva-letitrain.mp3','da7d05a957a2bbbf0e74b12c1b5fcfee',48,'projekteva-letitrain.mp3',12,11,3764804,1395916075,0,0,'5333fd34ced85',1395916075),(55,1,'files/documents/example.odt','f51311bd6910ec7356d79286dcb24dec',47,'example.odt',4,3,23383,1395916075,0,0,'5333fd34d6290',1395916075),(56,3,'owncloud_private_key','c2dcccd485df969dab921e05beb09cf8',9,'owncloud_private_key',2,1,-1,1395914577,0,0,'5333fd38b755e',1395914577),(57,3,'public-keys','de78051f8af6f61dc704af4f82cd2067',9,'public-keys',2,1,-1,1395916076,0,0,'5333fd38b8e14',1395916076),(58,3,'admin','21232f297a57a5a743894a0e4a801fc3',9,'admin',2,1,-1,1395916076,0,0,'5333fd38b9809',1395916076),(59,3,'owncloud.log','9703bd00121351aafcb85ff51784acc5',9,'owncloud.log',10,3,16448,1395916088,0,0,'5333fd38ba83c',1395916088),(60,3,'89400D1A-371D-4B34-B5FB-CAE34482DBA4','d0d0ae3cf12a2c989768d12b29c442e6',9,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',2,1,-1,1395914579,0,0,'5333fd38bb9e5',1395914579),(61,1,'files_encryption','171a8829416be21834bef1b79079dde8',1,'files_encryption',2,1,4388,1395916076,0,0,'5333fe4654e5c',1395916076),(62,1,'files_encryption/keyfiles','5a9277b1926b6770100b193add9a5825',61,'keyfiles',2,1,0,1395916076,0,0,'5333fe4654aee',1395916076),(63,1,'files_encryption/share-keys','b8104bb9e905689c4a5a9b99dfa0084b',61,'share-keys',2,1,0,1395916076,0,0,'5333fe485ecfe',1395916076),(64,1,'files_encryption/admin.private.key','b59e3ececa75169a37ec537ee1853b18',61,'admin.private.key',10,3,4388,1395916076,0,0,'5333fe485f948',1395916076);
/*!40000 ALTER TABLE `oc_filecache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_files_trash`
--

DROP TABLE IF EXISTS `oc_files_trash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_files_trash` (
  `id` varchar(250) NOT NULL DEFAULT '',
  `user` varchar(64) NOT NULL DEFAULT '',
  `timestamp` varchar(12) NOT NULL DEFAULT '',
  `location` varchar(512) NOT NULL DEFAULT '',
  `type` varchar(4) NOT NULL DEFAULT '',
  `mime` varchar(255) NOT NULL DEFAULT '',
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
  `user` varchar(64) NOT NULL DEFAULT '',
  `size` varchar(50) NOT NULL DEFAULT ''
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OC\\BackgroundJob\\Legacy\\RegularJob','[\"\\\\OC\\\\Files\\\\Cache\\\\BackgroundWatcher\",\"checkNext\"]',1395916374),(2,'OCA\\user_ldap\\lib\\Jobs','null',1395916073),(3,'OC\\Cache\\FileGlobalGC','null',1395916367);
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
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=bursar,ou=groups,ou=people,dc=testdomain,dc=com','bursar','12F56AC9-585E-4109-AB66-9EB56CCEE1AE'),('cn=exams,ou=groups,ou=people,dc=testdomain,dc=com','exams','0D385F27-7541-4BCF-8795-313029D06E7C'),('cn=governors,ou=groups,ou=people,dc=testdomain,dc=com','governors','87BF83F4-4363-4FD5-B030-7AC513E9476B'),('cn=guardians,ou=groups,ou=people,dc=testdomain,dc=com','guardians','8F01B8B3-0570-4C73-BDE6-D2A434871EA0'),('cn=guestusers,ou=groups,ou=people,dc=testdomain,dc=com','guestusers','DCD94BEA-2297-4940-9E1E-9852433E073B'),('cn=itadmin,ou=groups,ou=people,dc=testdomain,dc=com','itadmin','6063B812-03E6-4A40-9A36-745C9148767C'),('cn=nonteachingstaff,ou=groups,ou=people,dc=testdomain,dc=com','nonteachingstaff','BA553D70-2A8B-48E4-AFD0-88697F262CE5'),('cn=officestaff,ou=groups,ou=people,dc=testdomain,dc=com','officestaff','4986BA89-0401-486D-BD78-7FDB3557BEFF'),('cn=profilemanagement,ou=groups,ou=people,dc=testdomain,dc=com','profilemanagement','F15FB4F2-9FE1-4F18-AAB6-079DF741CBB0'),('cn=smt,ou=groups,ou=people,dc=testdomain,dc=com','smt','A20B8C40-4123-4E56-A660-A85A0A3D26CD'),('cn=staff,ou=groups,ou=people,dc=testdomain,dc=com','staff','6CBE2807-03C9-4F3A-AA25-024E4478DD16'),('cn=studentstaff,ou=groups,ou=people,dc=testdomain,dc=com','studentstaff','BC13795A-B69D-4B7B-97CF-93597B307454'),('cn=tech,ou=groups,ou=people,dc=testdomain,dc=com','tech','206FB86A-6616-40FF-9168-7BEF21DC10B6'),('cn=yr2004,ou=groups,ou=people,dc=testdomain,dc=com','yr2004','14672C68-3F3B-44B3-8731-F7EE89B6DAFE'),('cn=yr2005,ou=groups,ou=people,dc=testdomain,dc=com','yr2005','A7EA803D-69A9-4EAD-B552-8CF7234B5370'),('cn=yr2006,ou=groups,ou=people,dc=testdomain,dc=com','yr2006','25A30E08-9D27-4F24-8995-F7ECC40326AC'),('cn=yr2007,ou=groups,ou=people,dc=testdomain,dc=com','yr2007','15B9125D-6E28-4B56-850C-6A60B75E3181'),('cn=yr2008,ou=groups,ou=people,dc=testdomain,dc=com','yr2008','8787910A-1C77-466E-AB15-F64EA1FA475C'),('cn=yr2009,ou=groups,ou=people,dc=testdomain,dc=com','yr2009','2FF2D48F-F975-4B2D-8ED2-E4B4408E5A62'),('cn=yr2010,ou=groups,ou=people,dc=testdomain,dc=com','yr2010','96BF5C32-A567-4B5C-BF74-E51F37863876'),('cn=yr2011,ou=groups,ou=people,dc=testdomain,dc=com','yr2011','6A72FA79-F3F2-405F-9AD1-9ED31A753995'),('cn=yr2012,ou=groups,ou=people,dc=testdomain,dc=com','yr2012','E0277B98-BC68-4816-B371-13520C6E2B1F'),('cn=yr2013,ou=groups,ou=people,dc=testdomain,dc=com','yr2013','A7F936A9-92EA-462A-B617-DF43FF0E873B'),('cn=yr2014,ou=groups,ou=people,dc=testdomain,dc=com','yr2014','49FAED2F-B081-4C9E-A7CF-79158F19A816'),('cn=yr2015,ou=groups,ou=people,dc=testdomain,dc=com','yr2015','934BA4A5-C69C-42A8-A21B-90259EF05D10'),('cn=yr2016,ou=groups,ou=people,dc=testdomain,dc=com','yr2016','9DACAE64-516E-403F-9CF3-37386C353B46'),('cn=yr2017,ou=groups,ou=people,dc=testdomain,dc=com','yr2017','6712B629-9071-4DD4-A9DE-7CE270AAC8F4'),('cn=yr2018,ou=groups,ou=people,dc=testdomain,dc=com','yr2018','2F5D7B49-D82A-49E4-A75A-D3BD700E3836'),('cn=yr2019,ou=groups,ou=people,dc=testdomain,dc=com','yr2019','F6942942-85DD-45A3-BFF8-7B4D860D628A'),('cn=yr2020,ou=groups,ou=people,dc=testdomain,dc=com','yr2020','E47879B7-28DA-4A22-98CF-485D414C7106'),('cn=yr2021,ou=groups,ou=people,dc=testdomain,dc=com','yr2021','0E4F8F2D-1A1E-4E7A-A98D-5DB2F95EA22D'),('cn=yr2022,ou=groups,ou=people,dc=testdomain,dc=com','yr2022','67C56F9B-CF8E-4E3D-BD46-DA34946A7605'),('cn=yr2023,ou=groups,ou=people,dc=testdomain,dc=com','yr2023','4BB1C7F0-CDF8-4E17-AD12-41BACF7A8461'),('cn=yr2024,ou=groups,ou=people,dc=testdomain,dc=com','yr2024','F65D901A-47E2-4629-AD93-52C2167429E7'),('cn=yr2025,ou=groups,ou=people,dc=testdomain,dc=com','yr2025','E784C30F-7479-4B86-BFA4-8931F7BB16D4'),('cn=yr2026,ou=groups,ou=people,dc=testdomain,dc=com','yr2026','076D66D1-EF5E-4472-A276-2628665CE398'),('cn=yr2027,ou=groups,ou=people,dc=testdomain,dc=com','yr2027','FEEC7F56-596A-4E89-A555-4CD1D7663389'),('cn=yr2028,ou=groups,ou=people,dc=testdomain,dc=com','yr2028','B2DB7A73-4BEA-4BFB-9D9D-CAEF283F8363'),('cn=yr2029,ou=groups,ou=people,dc=testdomain,dc=com','yr2029','9162D4B7-4AE6-4F10-A296-2C3280E11CDE'),('cn=yr2030,ou=groups,ou=people,dc=testdomain,dc=com','yr2030','FAB6BCDD-B312-40B7-B4D7-9B0230ECA92F'),('cn=yr2031,ou=groups,ou=people,dc=testdomain,dc=com','yr2031','CCCD3267-0ABE-4991-9600-1CA47712A059'),('cn=yr2032,ou=groups,ou=people,dc=testdomain,dc=com','yr2032','CC55075B-2BA2-41BA-89A2-9C3644371560'),('cn=yr2033,ou=groups,ou=people,dc=testdomain,dc=com','yr2033','4CBC3F10-9B9C-4209-A988-87692F7A5DE2'),('cn=yr2034,ou=groups,ou=people,dc=testdomain,dc=com','yr2034','00AEB112-3DD9-417B-9142-399ED6EE4DC8'),('cn=yr2035,ou=groups,ou=people,dc=testdomain,dc=com','yr2035','E036FA53-292F-4ED6-AEEF-A33598BB424C'),('cn=yr2036,ou=groups,ou=people,dc=testdomain,dc=com','yr2036','F13DE640-6BB2-4F41-8689-A90A2ED7F388'),('cn=yr2037,ou=groups,ou=people,dc=testdomain,dc=com','yr2037','86FFBB15-CA56-4ECA-91EC-1A435A87F841'),('cn=yr2038,ou=groups,ou=people,dc=testdomain,dc=com','yr2038','474E2432-9DCB-4CC0-8B15-BB593F71FDAF'),('cn=yr2039,ou=groups,ou=people,dc=testdomain,dc=com','yr2039','AE747F7B-00D5-4C8A-8E5F-555BBCEE31DA'),('cn=yr2040,ou=groups,ou=people,dc=testdomain,dc=com','yr2040','811CD46C-C9F9-4E48-BF57-A7585DC712ED'),('cn=yr2041,ou=groups,ou=people,dc=testdomain,dc=com','yr2041','38C2C3FC-5C82-4461-B90A-959563A9574D'),('cn=yr2042,ou=groups,ou=people,dc=testdomain,dc=com','yr2042','99FE60F1-34D7-49AD-8274-441C4B6ACDE7'),('cn=yr2043,ou=groups,ou=people,dc=testdomain,dc=com','yr2043','DE27BD6B-9527-4738-9792-EEC2D707B1C2'),('cn=yr2044,ou=groups,ou=people,dc=testdomain,dc=com','yr2044','7D5B7E8E-72F8-4B10-B96B-A4495409B6DC'),('cn=yr2045,ou=groups,ou=people,dc=testdomain,dc=com','yr2045','BD137839-1CE1-42AE-A770-070D38498958'),('cn=yr2046,ou=groups,ou=people,dc=testdomain,dc=com','yr2046','76F2EE7C-F898-46BD-8E01-73415C9393FD'),('cn=yr2047,ou=groups,ou=people,dc=testdomain,dc=com','yr2047','D4D21D13-8B74-4EC1-BD1C-7084E36EC11F'),('cn=yr2048,ou=groups,ou=people,dc=testdomain,dc=com','yr2048','305BDE86-18DE-4974-A3B4-921A715A189E');
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
INSERT INTO `oc_ldap_group_members` VALUES ('bursar','a:0:{}'),('exams','a:0:{}'),('governors','a:0:{}'),('guardians','a:0:{}'),('guestusers','a:0:{}'),('itadmin','a:0:{}'),('nonteachingstaff','a:0:{}'),('officestaff','a:0:{}'),('profilemanagement','a:0:{}'),('smt','a:0:{}'),('staff','a:4:{i:0;s:36:\"47FF6C62-953F-40DC-ADCA-499A96E21143\";i:1;s:36:\"773B3111-3783-4CFE-A085-E14287B64046\";i:2;s:36:\"89400D1A-371D-4B34-B5FB-CAE34482DBA4\";i:3;s:36:\"F79D13A3-55B3-4D52-83C2-5E1DD51FFCA1\";}'),('studentstaff','a:0:{}'),('tech','a:0:{}'),('yr2004','a:0:{}'),('yr2005','a:0:{}'),('yr2006','a:0:{}'),('yr2007','a:0:{}'),('yr2008','a:0:{}'),('yr2009','a:0:{}'),('yr2010','a:0:{}'),('yr2011','a:0:{}'),('yr2012','a:0:{}'),('yr2013','a:0:{}'),('yr2014','a:0:{}'),('yr2015','a:0:{}'),('yr2016','a:0:{}'),('yr2017','a:0:{}'),('yr2018','a:0:{}'),('yr2019','a:0:{}'),('yr2020','a:0:{}'),('yr2021','a:0:{}'),('yr2022','a:0:{}'),('yr2023','a:0:{}'),('yr2024','a:0:{}'),('yr2025','a:0:{}'),('yr2026','a:0:{}'),('yr2027','a:0:{}'),('yr2028','a:0:{}'),('yr2029','a:0:{}'),('yr2030','a:0:{}'),('yr2031','a:0:{}'),('yr2032','a:0:{}'),('yr2033','a:0:{}'),('yr2034','a:0:{}'),('yr2035','a:0:{}'),('yr2036','a:0:{}'),('yr2037','a:0:{}'),('yr2038','a:0:{}'),('yr2039','a:0:{}'),('yr2040','a:0:{}'),('yr2041','a:0:{}'),('yr2042','a:0:{}'),('yr2043','a:0:{}'),('yr2044','a:0:{}'),('yr2045','a:0:{}'),('yr2046','a:0:{}'),('yr2047','a:0:{}'),('yr2048','a:0:{}');
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
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=aball,ou=itadmin,ou=personnel,ou=people,dc=testdomain,dc=com','773B3111-3783-4CFE-A085-E14287B64046','773B3111-3783-4CFE-A085-E14287B64046'),('cn=guest1,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','BAD47347-B3B2-4DB3-A37B-EF18F57B77E6','BAD47347-B3B2-4DB3-A37B-EF18F57B77E6'),('cn=guest10,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','BEF95D2F-8CC5-4F9F-A1DA-D2F7DA78E70B','BEF95D2F-8CC5-4F9F-A1DA-D2F7DA78E70B'),('cn=guest2,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','D40E4E5C-3A0A-419D-B04F-7F5317993B79','D40E4E5C-3A0A-419D-B04F-7F5317993B79'),('cn=guest3,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','5D1E6B37-54B7-4D8A-87FE-E8E4374D05C2','5D1E6B37-54B7-4D8A-87FE-E8E4374D05C2'),('cn=guest4,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','EC6DA102-1B30-4996-97E7-DD95AA20C287','EC6DA102-1B30-4996-97E7-DD95AA20C287'),('cn=guest5,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','DB97E2FA-BBBC-4570-B7D1-6AB6B3E33223','DB97E2FA-BBBC-4570-B7D1-6AB6B3E33223'),('cn=guest6,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','779765B2-1CB5-4516-AE75-B45FF332D4A3','779765B2-1CB5-4516-AE75-B45FF332D4A3'),('cn=guest7,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','AA8BCC46-1190-43D9-B864-53106FAD9D85','AA8BCC46-1190-43D9-B864-53106FAD9D85'),('cn=guest8,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','FD8CCCC9-810F-4848-AD07-CD3A8E08E5D8','FD8CCCC9-810F-4848-AD07-CD3A8E08E5D8'),('cn=guest9,ou=guestusers,ou=other,ou=people,dc=testdomain,dc=com','4AFC5FF1-F4B1-479D-A602-185FE1B7B8EE','4AFC5FF1-F4B1-479D-A602-185FE1B7B8EE'),('cn=ismith,ou=staff,ou=personnel,ou=people,dc=testdomain,dc=com','89400D1A-371D-4B34-B5FB-CAE34482DBA4','89400D1A-371D-4B34-B5FB-CAE34482DBA4'),('cn=jjones,ou=staff,ou=personnel,ou=people,dc=testdomain,dc=com','F79D13A3-55B3-4D52-83C2-5E1DD51FFCA1','F79D13A3-55B3-4D52-83C2-5E1DD51FFCA1'),('cn=karoshi-krb5,ou=karoshi,ou=other,ou=people,dc=testdomain,dc=com','AB35663D-EB83-49E7-8E23-2919E84F84BA','AB35663D-EB83-49E7-8E23-2919E84F84BA'),('cn=profileuser,ou=other,ou=people,dc=testdomain,dc=com','28F71D18-3928-46EA-AA8A-8544CDC946E9','28F71D18-3928-46EA-AA8A-8544CDC946E9'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,dc=testdomain,dc=com','2CDD8880-62CF-4F41-89CE-1EB73CEA2E7C','2CDD8880-62CF-4F41-89CE-1EB73CEA2E7C'),('cn=tech1,ou=tech,ou=personnel,ou=people,dc=testdomain,dc=com','FB29D1A2-124D-419D-A032-ED884DBE0FD6','FB29D1A2-124D-419D-A032-ED884DBE0FD6'),('cn=tech2,ou=tech,ou=personnel,ou=people,dc=testdomain,dc=com','5B611953-69D8-4EB6-87EC-9F1B4DC04C5B','5B611953-69D8-4EB6-87EC-9F1B4DC04C5B'),('cn=tech3,ou=tech,ou=personnel,ou=people,dc=testdomain,dc=com','5F9C86C6-1D5A-492F-BDE7-CC824B64322D','5F9C86C6-1D5A-492F-BDE7-CC824B64322D'),('cn=tech4,ou=tech,ou=personnel,ou=people,dc=testdomain,dc=com','019A6CBC-DB5B-422D-B709-35439FA88E52','019A6CBC-DB5B-422D-B709-35439FA88E52'),('cn=tguy10,ou=yr2010,ou=students,ou=people,dc=testdomain,dc=com','69815D2E-6338-4DDB-8039-247AB61D3BC5','69815D2E-6338-4DDB-8039-247AB61D3BC5'),('cn=tstudent09,ou=yr2009,ou=students,ou=people,dc=testdomain,dc=com','80BBABD2-86DA-4324-91DE-B03E23F65410','80BBABD2-86DA-4324-91DE-B03E23F65410'),('cn=ttest,ou=staff,ou=personnel,ou=people,dc=testdomain,dc=com','47FF6C62-953F-40DC-ADCA-499A96E21143','47FF6C62-953F-40DC-ADCA-499A96E21143');
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (7,''),(3,'application'),(10,'application/octet-stream'),(15,'application/pdf'),(5,'application/vnd.oasis.opendocument.spreadsheet'),(4,'application/vnd.oasis.opendocument.text'),(6,'application/x-empty'),(11,'audio'),(12,'audio/mpeg'),(1,'httpd'),(2,'httpd/unix-directory'),(13,'image'),(14,'image/jpeg'),(8,'text'),(9,'text/plain');
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
INSERT INTO `oc_permissions` VALUES (14,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(15,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(16,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(17,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(18,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(19,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(20,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(21,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(22,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(23,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(24,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(7,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(26,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(8,'62502FA8-1105-4346-A829-218EA2A8B6B6',27),(5,'62502FA8-1105-4346-A829-218EA2A8B6B6',31),(30,'admin',27),(37,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',31),(38,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',31),(40,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',31),(46,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',27),(42,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',31),(44,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',27),(45,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',27),(43,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',27),(41,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',27),(39,'89400D1A-371D-4B34-B5FB-CAE34482DBA4',27),(50,'admin',27),(2,'admin',31),(47,'admin',31),(48,'admin',31),(49,'admin',31);
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
INSERT INTO `oc_preferences` VALUES ('62502FA8-1105-4346-A829-218EA2A8B6B6','files','cache_version','5'),('62502FA8-1105-4346-A829-218EA2A8B6B6','firstrunwizard','show','0'),('62502FA8-1105-4346-A829-218EA2A8B6B6','user_ldap','firstLoginAccomplished','1'),('62502FA8-1105-4346-A829-218EA2A8B6B6','user_ldap','lastJpegPhotoLookup','1387461977'),('89400D1A-371D-4B34-B5FB-CAE34482DBA4','settings','email','ismith@testdomain.com'),('89400D1A-371D-4B34-B5FB-CAE34482DBA4','user_ldap','firstLoginAccomplished','1'),('89400D1A-371D-4B34-B5FB-CAE34482DBA4','user_ldap','lastJpegPhotoLookup','1395914575'),('admin','files','cache_version','5'),('admin','firstrunwizard','show','0');
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('home::62502FA8-1105-4346-A829-218EA2A8B6B6',2),('home::89400D1A-371D-4B34-B5FB-CAE34482DBA4',15),('home::admin',1),('local::/home/owncloud/data/',3),('smb::ismith@//172.30.3.1/ismith//homefolder//',5),('smb::ismith@//172.30.3.1/ismith//root//',13),('smb::ismith@172.30.3.1//homefolder//',7),('smb::ismith@172.30.3.1//ismith//',9),('smb::ismith@172.30.3.1//ismith//ismith/',14),('smb::ismith@172.30.3.1/i//ismith//',8),('smb::ismith@172.30.3.1/ismith//homefolder//',6),('smb::ismith@172.30.3.1/ismith//root//',12),('smb::ismith@ismith@172.30.3.1//ismith//',11),('smb::ismith@smb://172.30.3.1/ismith//homefolder//',4),('smb::ismith@\\\\172.30.3.1\\ismith//ismith//',10);
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

-- Dump completed on 2014-03-27 12:56:29
