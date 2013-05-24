-- MySQL dump 10.13  Distrib 5.5.22, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: owncloud
-- ------------------------------------------------------
-- Server version	5.5.22-0ubuntu1

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
  `appid` varchar(32) NOT NULL DEFAULT ' ',
  `configkey` varchar(64) NOT NULL DEFAULT ' ',
  `configvalue` longtext NOT NULL,
  KEY `appconfig_appid_key_index` (`appid`,`configkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_appconfig`
--

LOCK TABLES `oc_appconfig` WRITE;
/*!40000 ALTER TABLE `oc_appconfig` DISABLE KEYS */;
INSERT INTO `oc_appconfig` VALUES ('core','installedat','1350821436.7674'),('core','lastupdatedat','1350829471.5552'),('contacts','installed_version','0.2.4'),('core','remote_contacts','contacts/appinfo/remote.php'),('core','remote_carddav','contacts/appinfo/remote.php'),('contacts','enabled','yes'),('files_imageviewer','installed_version','1.0'),('files_imageviewer','enabled','yes'),('calendar','installed_version','0.6.1'),('core','remote_calendar','calendar/appinfo/remote.php'),('core','remote_caldav','calendar/appinfo/remote.php'),('core','public_calendar','calendar/share.php'),('core','public_caldav','calendar/share.php'),('calendar','enabled','yes'),('files_sharing','installed_version','0.3.3'),('core','public_files','files_sharing/public.php'),('core','public_webdav','files_sharing/public.php'),('files_sharing','types','filesystem'),('files_sharing','enabled','yes'),('media','installed_version','0.4.3'),('core','remote_ampache','media/remote.php'),('media','enabled','no'),('files_odfviewer','installed_version','0.1'),('files_odfviewer','enabled','yes'),('user_migrate','installed_version','0.1'),('user_migrate','enabled','yes'),('files_texteditor','installed_version','0.3'),('files_texteditor','enabled','yes'),('gallery','installed_version','0.5.1'),('core','public_gallery','gallery/sharing.php'),('gallery','enabled','yes'),('files_pdfviewer','installed_version','0.1'),('files_pdfviewer','enabled','yes'),('admin_migrate','installed_version','0.1'),('admin_migrate','enabled','yes'),('files_versions','installed_version','1.0.2'),('files_versions','types','filesystem'),('files_versions','enabled','yes'),('files','installed_version','1.1.6'),('core','remote_files','files/appinfo/remote.php'),('core','remote_webdav','files/appinfo/remote.php'),('core','remote_filesync','files/appinfo/filesync.php'),('files','types','filesystem'),('files','enabled','yes'),('core','remote_core.css','/core/minimizer.php'),('core','remote_core.js','/core/minimizer.php'),('core','backgroundjobs_task','OC_Cache_FileGlobal-gc'),('core','global_cache_gc_lastrun','1350831928'),('core','backgroundjobs_step','queued_tasks'),('user_ldap','installed_version','0.3.0.0'),('user_ldap','types','authentication'),('user_ldap','enabled','yes'),('user_ldap','bgjUpdateGroupsLastRun','1350829695'),('user_ldap','ldap_host','ldap://127.0.0.1/'),('user_ldap','ldap_port','389'),('user_ldap','ldap_dn',''),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_base','ou=People,dc=karoshi,dc=local'),('user_ldap','ldap_base_users',''),('user_ldap','ldap_base_groups',''),('user_ldap','ldap_userlist_filter','objectClass=posixAccount'),('user_ldap','ldap_login_filter','uid=%uid'),('user_ldap','ldap_group_filter','objectClass=posixGroup'),('user_ldap','ldap_display_name','uid'),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_tls','1'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_nocase','0'),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','home_folder_naming_rule','opt:username'),('impress','installed_version','1.0'),('impress','types',''),('impress','enabled','yes'),('files_videoviewer','installed_version','0.1'),('files_videoviewer','types',''),('files_videoviewer','enabled','yes'),('files_archive','installed_version','0.2'),('files_archive','types','filesystem'),('files_archive','enabled','yes'),('bookmarks','installed_version','0.2'),('bookmarks','types',''),('bookmarks','enabled','yes'),('files_external','installed_version','0.2'),('files_external','types','filesystem'),('files_external','enabled','no'),('tasks','installed_version','0.1'),('tasks','types',''),('tasks','enabled','yes');
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
  `url` varchar(4096) NOT NULL DEFAULT ' ',
  `title` varchar(140) NOT NULL DEFAULT ' ',
  `user_id` varchar(64) NOT NULL DEFAULT ' ',
  `public` tinyint(4) DEFAULT '0',
  `added` int(10) unsigned DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  `clickcount` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_bookmarks`
--

LOCK TABLES `oc_bookmarks` WRITE;
/*!40000 ALTER TABLE `oc_bookmarks` DISABLE KEYS */;
INSERT INTO `oc_bookmarks` VALUES (1,'http://192.168.0.200/owncloud/?app=bookmarks','ownCloud','jsmith',0,1350830188,1350830188,0),(2,'http://192.168.0.200/owncloud/?app=bookmarks','ownCloud','jsmith',0,1350830237,1350830237,0),(3,'http://192.168.0.200/owncloud/?app=bookmarks','ownCloud','jsmith',0,1350830273,1350830273,0),(4,'http://192.168.0.200/owncloud/?app=bookmarks','ownCloud','jsmith',0,1350830281,1350830281,0);
/*!40000 ALTER TABLE `oc_bookmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_bookmarks_tags`
--

DROP TABLE IF EXISTS `oc_bookmarks_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_bookmarks_tags` (
  `bookmark_id` bigint(20) DEFAULT '0',
  `tag` varchar(255) NOT NULL DEFAULT ' ',
  UNIQUE KEY `bookmark_tag` (`bookmark_id`,`tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_bookmarks_tags`
--

LOCK TABLES `oc_bookmarks_tags` WRITE;
/*!40000 ALTER TABLE `oc_bookmarks_tags` DISABLE KEYS */;
INSERT INTO `oc_bookmarks_tags` VALUES (1,'Read-Later'),(2,'Read-Later'),(3,'Read-Later'),(4,'Read-Later');
/*!40000 ALTER TABLE `oc_bookmarks_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendar_calendars`
--

DROP TABLE IF EXISTS `oc_calendar_calendars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendar_calendars` (
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendar_calendars`
--

LOCK TABLES `oc_calendar_calendars` WRITE;
/*!40000 ALTER TABLE `oc_calendar_calendars` DISABLE KEYS */;
INSERT INTO `oc_calendar_calendars` VALUES (1,'ismith','Default calendar','defaultcalendar',1,1,0,NULL,NULL,'VEVENT,VTODO,VJOURNAL'),(2,'jsmith','Default calendar','defaultcalendar',1,3,0,NULL,NULL,'VEVENT,VTODO,VJOURNAL');
/*!40000 ALTER TABLE `oc_calendar_calendars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendar_objects`
--

DROP TABLE IF EXISTS `oc_calendar_objects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendar_objects` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `calendarid` int(10) unsigned NOT NULL DEFAULT '0',
  `objecttype` varchar(40) NOT NULL DEFAULT ' ',
  `startdate` datetime DEFAULT '0000-00-00 00:00:00',
  `enddate` datetime DEFAULT '0000-00-00 00:00:00',
  `repeating` int(11) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `calendardata` longtext,
  `uri` varchar(255) DEFAULT NULL,
  `lastmodified` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendar_objects`
--

LOCK TABLES `oc_calendar_objects` WRITE;
/*!40000 ALTER TABLE `oc_calendar_objects` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendar_objects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendar_repeat`
--

DROP TABLE IF EXISTS `oc_calendar_repeat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendar_repeat` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `eventid` int(10) unsigned NOT NULL DEFAULT '0',
  `calid` int(10) unsigned NOT NULL DEFAULT '0',
  `startdate` datetime DEFAULT '0000-00-00 00:00:00',
  `enddate` datetime DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendar_repeat`
--

LOCK TABLES `oc_calendar_repeat` WRITE;
/*!40000 ALTER TABLE `oc_calendar_repeat` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendar_repeat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendar_share_calendar`
--

DROP TABLE IF EXISTS `oc_calendar_share_calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendar_share_calendar` (
  `owner` varchar(255) NOT NULL DEFAULT ' ',
  `share` varchar(255) NOT NULL DEFAULT ' ',
  `sharetype` varchar(6) NOT NULL DEFAULT ' ',
  `calendarid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `permissions` tinyint(4) NOT NULL DEFAULT '0',
  `active` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendar_share_calendar`
--

LOCK TABLES `oc_calendar_share_calendar` WRITE;
/*!40000 ALTER TABLE `oc_calendar_share_calendar` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendar_share_calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendar_share_event`
--

DROP TABLE IF EXISTS `oc_calendar_share_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendar_share_event` (
  `owner` varchar(255) NOT NULL DEFAULT ' ',
  `share` varchar(255) NOT NULL DEFAULT ' ',
  `sharetype` varchar(6) NOT NULL DEFAULT ' ',
  `eventid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `permissions` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendar_share_event`
--

LOCK TABLES `oc_calendar_share_event` WRITE;
/*!40000 ALTER TABLE `oc_calendar_share_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendar_share_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_contacts_addressbooks`
--

DROP TABLE IF EXISTS `oc_contacts_addressbooks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_contacts_addressbooks` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) NOT NULL DEFAULT ' ',
  `displayname` varchar(255) DEFAULT NULL,
  `uri` varchar(200) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `ctag` int(10) unsigned NOT NULL DEFAULT '1',
  `active` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_contacts_addressbooks`
--

LOCK TABLES `oc_contacts_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_contacts_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_contacts_addressbooks` VALUES (1,'admin','Contacts','contacts','Default Address Book',1,1),(2,'ismith','Contacts','contacts','Default Address Book',1,1),(3,'jsmith','Contacts','contacts','Default Address Book',1,1);
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
-- Table structure for table `oc_fscache`
--

DROP TABLE IF EXISTS `oc_fscache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_fscache` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(512) NOT NULL DEFAULT ' ',
  `path_hash` varchar(32) NOT NULL DEFAULT ' ',
  `parent` bigint(20) NOT NULL DEFAULT '0',
  `name` varchar(300) NOT NULL DEFAULT ' ',
  `user` varchar(64) NOT NULL DEFAULT ' ',
  `size` bigint(20) NOT NULL DEFAULT '0',
  `ctime` bigint(20) NOT NULL DEFAULT '0',
  `mtime` bigint(20) NOT NULL DEFAULT '0',
  `mimetype` varchar(96) NOT NULL DEFAULT ' ',
  `mimepart` varchar(32) NOT NULL DEFAULT ' ',
  `encrypted` tinyint(4) NOT NULL DEFAULT '0',
  `versioned` tinyint(4) NOT NULL DEFAULT '0',
  `writable` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fscache_path_hash_index` (`path_hash`),
  KEY `parent_index` (`parent`),
  KEY `name_index` (`name`(255)),
  KEY `parent_name_index` (`parent`,`name`(255))
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_fscache`
--

LOCK TABLES `oc_fscache` WRITE;
/*!40000 ALTER TABLE `oc_fscache` DISABLE KEYS */;
INSERT INTO `oc_fscache` VALUES (1,'/admin/files','dbb5f96946862a55abb65ee90e3cf566',-1,'files','admin',0,1350821436,1350821436,'httpd/unix-directory','httpd',0,0,1),(2,'/ismith/files','4f3bd4751dfadc352e820211137badbf',-1,'files','ismith',-14424566,1350827723,1350827723,'httpd/unix-directory','httpd',0,0,1),(4,'/ismith/files/ismith','3f2663aeb98b212b5df78ee36a6782d7',2,'ismith','ismith',7212283,1350828300,1350831422,'httpd/unix-directory','httpd',0,0,1),(10,'/ismith/files_versions/ismith/achievements.odt.v1350824284','9eb4d9c55fb281e4fa2c5f7c4f591096',-1,'achievements.odt.v1350824284','ismith',21217,1350824284,1350824284,'application/vnd.oasis.opendocument.text','application',0,0,1),(12,'/ismith/files_versions/ismith/300words.odt.v1350824284','0c8547b940bdd3f7abd1a7588ec82635',-1,'300words.odt.v1350824284','ismith',20984,1350824285,1350824285,'application/vnd.oasis.opendocument.text','application',0,0,1),(14,'/ismith/files_versions/background.jpg.v1350824321','5aea4b74dedb1f971c91123b4a939000',-1,'background.jpg.v1350824321','ismith',35029,1350824321,1350824321,'image/jpeg','image',0,0,1),(15,'/ismith/files/background.jpg','e67ecc68a950d478afea94b3f823f45b',2,'background.jpg','ismith',35029,1350824321,1350824321,'image/jpeg','image',0,0,1),(16,'/ismith/files_versions/ismith/2_raid_teams.ods.v1350824429','fd9084e335ec71b10d564907f1fcfd68',-1,'2_raid_teams.ods.v1350824429','ismith',11593,1350824429,1350824429,'','',0,0,1),(18,'/ismith/files_versions/ismith/koha.odp.v1350824430','663f1882973728da044dc5f2e019a059',-1,'koha.odp.v1350824430','ismith',47245,1350824430,1350824430,'','',0,0,1),(22,'/ismith/files/03 Dont Tell Me.mp3','c55843fd8e519add5ec958333a86df7c',2,'03 Dont Tell Me.mp3','ismith',4853427,1350827596,1350827596,'audio/mpeg','audio',0,0,1),(23,'/ismith/files/08 Forgotten.mp3','f1e42d19b2afd28219871ca0e7eb064a',2,'08 Forgotten.mp3','ismith',4742459,1350827629,1350827629,'audio/mpeg','audio',0,0,1),(24,'/ismith/files/dragnet.ogg','72975d08b47b9567ac21c37d141f4c6e',2,'dragnet.ogg','ismith',3830428,1350827723,1350827723,'audio/ogg','audio',0,0,1),(25,'/ismith/files_versions/ismith/achievements.odt.v1350827872','d5be48d61d9d9f5c59925e129b422927',-1,'achievements.odt.v1350827872','ismith',21217,1350827872,1350827872,'application/vnd.oasis.opendocument.text','application',0,0,1),(26,'/ismith/files/ismith/achievements.odt','2234aa36cb3f7314b6fe609c8860f653',4,'achievements.odt','ismith',21217,1343400453,1343400453,'application/vnd.oasis.opendocument.text','application',0,0,1),(27,'/ismith/files_versions/ismith/.mailboxlist.v1350827873','e562cfbb7a1b8f2d57cf0c501518e27e',-1,'.mailboxlist.v1350827873','ismith',36,1350827873,1350827873,'text/plain','text',0,0,1),(28,'/ismith/files/ismith/.mailboxlist','ddadd8671c0c1310d1cecb38963fd466',4,'.mailboxlist','ismith',36,1347863483,1347863483,'text/plain','text',0,0,1),(29,'/ismith/files_versions/ismith/Mail/INBOX.Drafts.v1350827873','b86523c2a734f842ded615f734ca8fb3',-1,'INBOX.Drafts.v1350827873','ismith',476,1350827874,1350827874,'text/plain','text',0,0,1),(30,'/ismith/files/ismith/Mail/INBOX.Drafts','06df7fbaa98cd90bbe4755897d258ab7',-1,'INBOX.Drafts','ismith',476,1347863483,1347863483,'text/plain','text',0,0,1),(31,'/ismith/files_versions/ismith/Mail/INBOX.Sent.v1350827874','20e0864e413cb26e795af8dbce0be369',-1,'INBOX.Sent.v1350827874','ismith',476,1350827874,1350827874,'text/plain','text',0,0,1),(32,'/ismith/files/ismith/Mail/INBOX.Sent','8d31ff659bbbe97b11db5c4b2aaf839f',-1,'INBOX.Sent','ismith',476,1347863483,1347863483,'text/plain','text',0,0,1),(33,'/ismith/files_versions/ismith/Mail/INBOX.Trash.v1350827875','8e675fd208dc5cf082b4e77d3ec8bd98',-1,'INBOX.Trash.v1350827875','ismith',476,1350827875,1350827875,'text/plain','text',0,0,1),(34,'/ismith/files/ismith/Mail/INBOX.Trash','d40fbfe25f2297b2bee5434c3f09790f',-1,'INBOX.Trash','ismith',476,1347863483,1347863483,'text/plain','text',0,0,1),(35,'/ismith/files/ismith/Mail','f2740f8bfc610be0635afee3433a0a40',4,'Mail','ismith',1428,1347863483,1347863483,'httpd/unix-directory','httpd',0,0,1),(36,'/ismith/files/ismith/ismith','ed9a7c8b826df03fcfbaf7dcc2407a05',4,'ismith','ismith',0,1350831422,1350831422,'httpd/unix-directory','httpd',0,0,1),(37,'/ismith/files_versions/ismith/300words.odt.v1350827876','484b1572a0d8d24fd8abe603d33b9780',-1,'300words.odt.v1350827876','ismith',20984,1350827876,1350827876,'application/vnd.oasis.opendocument.text','application',0,0,1),(38,'/ismith/files/ismith/300words.odt','4785d580cdc11457e467ceac2f94ea69',4,'300words.odt','ismith',20984,1321124854,1321124854,'application/vnd.oasis.opendocument.text','application',0,0,1),(39,'/ismith/files_versions/ismith/2_raid_teams.ods.v1350827877','22a95349cfe00436ac3f32fe8ae88060',-1,'2_raid_teams.ods.v1350827877','ismith',11593,1350827877,1350827877,'','',0,0,1),(40,'/ismith/files/ismith/2_raid_teams.ods','e6e923cb17cae969b90f6edeeb4f39e4',4,'2_raid_teams.ods','ismith',11593,1321125045,1321125045,'application/vnd.oasis.opendocument.spreadsheet','application',0,0,1),(41,'/jsmith/files','4332710d5d58b99e810534819b3ed04a',-1,'files','jsmith',7468426,1350829550,1350829550,'httpd/unix-directory','httpd',0,0,1),(42,'/ismith/files/ismith/02_sharp_dressed_man.ogg','8e76dd4f7bfd21c70c06b0c85c533070',4,'02_sharp_dressed_man.ogg','ismith',3529130,1321121401,1321121401,'audio/ogg','audio',0,0,1),(43,'/ismith/files_versions/ismith/koha.odp.v1350828097','7e9dfdc7e3b056a4123c4c2aa0ada61a',-1,'koha.odp.v1350828097','ismith',47245,1350828098,1350828098,'','',0,0,1),(44,'/ismith/files/ismith/koha.odp','18a76eee5bb8de17cd2134d9433b20a3',4,'koha.odp','ismith',47245,1321125048,1321125048,'application/vnd.oasis.opendocument.presentation','application',0,0,1),(45,'/jsmith/files/jsmith','f2129d0c46df862c6ff3b05e155b5eb3',41,'jsmith','jsmith',3723196,1350830383,1350833753,'httpd/unix-directory','httpd',0,0,1),(46,'/ismith/files/ismith/01_gimme_all_your_lovin.ogg','cf9142fd7a5aec6c290712fc6f4c00c5',4,'01_gimme_all_your_lovin.ogg','ismith',3580650,1321121401,1321121401,'audio/ogg','audio',0,0,1),(47,'/jsmith/files/jsmith/.mailboxlist','789dc45c4dcb0a7a240f96962ca18e44',45,'.mailboxlist','jsmith',36,1347864088,1347864088,'text/plain','text',0,0,1),(48,'/jsmith/files/jsmith/Mail/INBOX.Drafts','de940014b81d65be76a1f24925f9743b',-1,'INBOX.Drafts','jsmith',476,1347864088,1347864088,'text/plain','text',0,0,1),(49,'/jsmith/files/jsmith/Mail/INBOX.Sent','58bd7da2a5a720bd6ab5e4b8fbb196ad',-1,'INBOX.Sent','jsmith',476,1347864088,1347864088,'text/plain','text',0,0,1),(50,'/jsmith/files/jsmith/Mail/INBOX.Trash','809b3d56dbf935e8bfd7f313e64b88da',-1,'INBOX.Trash','jsmith',476,1347864088,1347864088,'text/plain','text',0,0,1),(51,'/jsmith/files/jsmith/Mail','6b0242b64b7aaa2201017b4960c30e72',45,'Mail','jsmith',1428,1347864088,1347864088,'httpd/unix-directory','httpd',0,0,1),(52,'/jsmith/files/music','c92e9db71e6dba5402a4f5b824623df8',41,'music','jsmith',26203557,1350829873,1350829873,'httpd/unix-directory','httpd',0,0,1),(53,'/jsmith/files/music/04_the_diary_of_horace_wimp.ogg','da7a5aa83ca6bd92a0b6846b23778ab6',52,'04_the_diary_of_horace_wimp.ogg','jsmith',3734213,1350829578,1350829578,'audio/ogg','audio',0,0,1),(54,'/jsmith/files/music/07_on_the_run.ogg','bbae760531d7a7712c5b96017cb88ac2',52,'07_on_the_run.ogg','jsmith',3658337,1350829852,1350829852,'audio/ogg','audio',0,0,1),(55,'/jsmith/files/music/04_the_diary_of_horace_wimp (2).ogg','9c44fdf89d78869f5c6ff354b4377aef',52,'04_the_diary_of_horace_wimp (2).ogg','jsmith',3734213,1350829859,1350829859,'audio/ogg','audio',0,0,1),(56,'/jsmith/files/music/07_on_the_run (2).ogg','bd010ceae8b1164a042f6a2d0ed22813',52,'07_on_the_run (2).ogg','jsmith',3658337,1350829859,1350829859,'audio/ogg','audio',0,0,1),(57,'/jsmith/files/music/06_midnight_blue.ogg','00147bf8f745d8e98b6c6ad1de013391',52,'06_midnight_blue.ogg','jsmith',3886991,1350829860,1350829860,'audio/ogg','audio',0,0,1),(58,'/jsmith/files/music/05_last_train_to_london.ogg','e199ade53fd64141e73017e8e7135601',52,'05_last_train_to_london.ogg','jsmith',4207685,1350829860,1350829860,'audio/ogg','audio',0,0,1),(59,'/jsmith/files/music/11_second_time_around.ogg','41691702b850efbb8a02fe1cbe6c2ace',52,'11_second_time_around.ogg','jsmith',648952,1350829873,1350829873,'audio/ogg','audio',0,0,1),(60,'/jsmith/files/music/12_little_town_flirt.ogg','9934bf54ea3947af8a1c194cdeedc34f',52,'12_little_town_flirt.ogg','jsmith',2674829,1350829873,1350829873,'audio/ogg','audio',0,0,1),(61,'/jsmith/files/jsmith/07_on_the_run.ogg','2e62a1fded1166f9f52f28b1e7623a79',45,'07_on_the_run.ogg','jsmith',3658337,1350833515,1350833515,'audio/ogg','audio',0,0,1),(62,'/jsmith/files/jsmith/logout.png','5d0c871fee9c8f42f85369cfcf15baab',45,'logout.png','jsmith',63395,1350833753,1350833753,'image/png','image',0,0,1);
/*!40000 ALTER TABLE `oc_fscache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_gallery_sharing`
--

DROP TABLE IF EXISTS `oc_gallery_sharing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_gallery_sharing` (
  `token` varchar(64) NOT NULL DEFAULT ' ',
  `gallery_id` int(11) NOT NULL DEFAULT '0',
  `recursive` tinyint(4) NOT NULL DEFAULT '0'
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
  `gid` varchar(64) NOT NULL DEFAULT ' ',
  `uid` varchar(64) NOT NULL DEFAULT ' '
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
  `gid` varchar(64) NOT NULL DEFAULT ' ',
  `uid` varchar(64) NOT NULL DEFAULT ' '
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
  `gid` varchar(64) NOT NULL DEFAULT ' ',
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
-- Table structure for table `oc_ldap_group_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_group_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_mapping` (
  `ldap_dn` varchar(255) NOT NULL DEFAULT ' ',
  `owncloud_name` varchar(255) NOT NULL DEFAULT ' ',
  `directory_uuid` varchar(255) NOT NULL DEFAULT ' ',
  UNIQUE KEY `ldap_dn_groups` (`ldap_dn`),
  UNIQUE KEY `owncloud_name_groups` (`owncloud_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_group_mapping`
--

LOCK TABLES `oc_ldap_group_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_group_mapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_ldap_group_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_group_members`
--

DROP TABLE IF EXISTS `oc_ldap_group_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_members` (
  `owncloudname` varchar(255) NOT NULL DEFAULT ' ',
  `owncloudusers` longtext NOT NULL,
  UNIQUE KEY `ldap_group_members` (`owncloudname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_group_members`
--

LOCK TABLES `oc_ldap_group_members` WRITE;
/*!40000 ALTER TABLE `oc_ldap_group_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_ldap_group_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_user_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_user_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_user_mapping` (
  `ldap_dn` varchar(255) NOT NULL DEFAULT ' ',
  `owncloud_name` varchar(255) NOT NULL DEFAULT ' ',
  `directory_uuid` varchar(255) NOT NULL DEFAULT ' ',
  UNIQUE KEY `ldap_dn_users` (`ldap_dn`),
  UNIQUE KEY `owncloud_name_users` (`owncloud_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_user_mapping`
--

LOCK TABLES `oc_ldap_user_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_user_mapping` DISABLE KEYS */;
INSERT INTO `oc_ldap_user_mapping` VALUES ('uid=abaker,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=local','abaker','4a5a63e2-94d6-1031-8a93-47cfc9fabe28'),('uid=exam1,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam1','5c215d9e-94d4-1031-97fd-81c11c92648b'),('uid=exam10,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam10','5c23ccdc-94d4-1031-97fe-81c11c92648b'),('uid=exam11,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam11','5c263d8c-94d4-1031-97ff-81c11c92648b'),('uid=exam12,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam12','5c28cafc-94d4-1031-9800-81c11c92648b'),('uid=exam13,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam13','5c2b1c4e-94d4-1031-9801-81c11c92648b'),('uid=exam14,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam14','5c2d8dee-94d4-1031-9802-81c11c92648b'),('uid=exam15,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam15','5c39c08c-94d4-1031-9803-81c11c92648b'),('uid=exam16,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam16','5c3c53b0-94d4-1031-9804-81c11c92648b'),('uid=exam17,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam17','5c3ebdbc-94d4-1031-9805-81c11c92648b'),('uid=exam18,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam18','5c412c96-94d4-1031-9806-81c11c92648b'),('uid=exam19,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam19','5c43a0de-94d4-1031-9807-81c11c92648b'),('uid=exam2,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam2','5c460fe0-94d4-1031-9808-81c11c92648b'),('uid=exam20,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam20','5c487e1a-94d4-1031-9809-81c11c92648b'),('uid=exam21,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam21','5c4aedf8-94d4-1031-980a-81c11c92648b'),('uid=exam22,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam22','5c4d5f84-94d4-1031-980b-81c11c92648b'),('uid=exam23,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam23','5c4fcdaa-94d4-1031-980c-81c11c92648b'),('uid=exam24,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam24','5c523dba-94d4-1031-980d-81c11c92648b'),('uid=exam25,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam25','5c54ae7e-94d4-1031-980e-81c11c92648b'),('uid=exam26,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam26','5c571d1c-94d4-1031-980f-81c11c92648b'),('uid=exam27,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam27','5c59ae4c-94d4-1031-9810-81c11c92648b'),('uid=exam28,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam28','5c5bfd3c-94d4-1031-9811-81c11c92648b'),('uid=exam29,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam29','5c5e6d2e-94d4-1031-9812-81c11c92648b'),('uid=exam3,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam3','5c60de1a-94d4-1031-9813-81c11c92648b'),('uid=exam30,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam30','5c634d12-94d4-1031-9814-81c11c92648b'),('uid=exam31,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam31','5c65bd54-94d4-1031-9815-81c11c92648b'),('uid=exam32,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam32','5c6833ea-94d4-1031-9816-81c11c92648b'),('uid=exam33,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam33','5c6aa260-94d4-1031-9817-81c11c92648b'),('uid=exam34,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam34','5c6d1356-94d4-1031-9818-81c11c92648b'),('uid=exam35,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam35','5c6f8294-94d4-1031-9819-81c11c92648b'),('uid=exam36,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam36','5c71f3da-94d4-1031-981a-81c11c92648b'),('uid=exam37,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam37','5c747420-94d4-1031-981b-81c11c92648b'),('uid=exam38,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam38','5c76d31e-94d4-1031-981c-81c11c92648b'),('uid=exam39,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam39','5c79562a-94d4-1031-981d-81c11c92648b'),('uid=exam4,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam4','5c7bb3ac-94d4-1031-981e-81c11c92648b'),('uid=exam40,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam40','5c7e2448-94d4-1031-981f-81c11c92648b'),('uid=exam5,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam5','5c8093fe-94d4-1031-9820-81c11c92648b'),('uid=exam6,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam6','5c8304d6-94d4-1031-9821-81c11c92648b'),('uid=exam7,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam7','5c8574dc-94d4-1031-9822-81c11c92648b'),('uid=exam8,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam8','5c87e49c-94d4-1031-9823-81c11c92648b'),('uid=exam9,ou=exams,ou=other,ou=people,dc=karoshi,dc=local','exam9','5c8a55d8-94d4-1031-9824-81c11c92648b'),('uid=guest1,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest1','5c8e0070-94d4-1031-9826-81c11c92648b'),('uid=guest10,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest10','5c9071e8-94d4-1031-9827-81c11c92648b'),('uid=guest11,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest11','5c92e6e4-94d4-1031-9828-81c11c92648b'),('uid=guest12,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest12','5c955136-94d4-1031-9829-81c11c92648b'),('uid=guest13,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest13','5c97c1f0-94d4-1031-982a-81c11c92648b'),('uid=guest14,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest14','5c9a314c-94d4-1031-982b-81c11c92648b'),('uid=guest15,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest15','5c9ca468-94d4-1031-982c-81c11c92648b'),('uid=guest16,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest16','5c9f2b66-94d4-1031-982d-81c11c92648b'),('uid=guest17,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest17','5ca188de-94d4-1031-982e-81c11c92648b'),('uid=guest18,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest18','5ca400fa-94d4-1031-982f-81c11c92648b'),('uid=guest19,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest19','5ca66a48-94d4-1031-9830-81c11c92648b'),('uid=guest2,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest2','5ca8df08-94d4-1031-9831-81c11c92648b'),('uid=guest20,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest20','5cab49f0-94d4-1031-9832-81c11c92648b'),('uid=guest21,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest21','5cadbcbc-94d4-1031-9833-81c11c92648b'),('uid=guest22,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest22','5cb02cb8-94d4-1031-9834-81c11c92648b'),('uid=guest23,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest23','5cb29ab6-94d4-1031-9835-81c11c92648b'),('uid=guest24,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest24','5cbb2460-94d4-1031-9836-81c11c92648b'),('uid=guest25,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest25','5cbd9916-94d4-1031-9837-81c11c92648b'),('uid=guest26,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest26','5cc00ef8-94d4-1031-9838-81c11c92648b'),('uid=guest27,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest27','5cc274ae-94d4-1031-9839-81c11c92648b'),('uid=guest28,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest28','5cc4e798-94d4-1031-983a-81c11c92648b'),('uid=guest29,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest29','5cc754b0-94d4-1031-983b-81c11c92648b'),('uid=guest3,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest3','5cc9c33a-94d4-1031-983c-81c11c92648b'),('uid=guest30,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest30','5ccc353e-94d4-1031-983d-81c11c92648b'),('uid=guest4,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest4','5ccea5da-94d4-1031-983e-81c11c92648b'),('uid=guest5,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest5','5cd11554-94d4-1031-983f-81c11c92648b'),('uid=guest6,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest6','5cd3865e-94d4-1031-9840-81c11c92648b'),('uid=guest7,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest7','5cd5fb28-94d4-1031-9841-81c11c92648b'),('uid=guest8,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest8','5cd86bb0-94d4-1031-9842-81c11c92648b'),('uid=guest9,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','guest9','5cdadc2e-94d4-1031-9843-81c11c92648b'),('uid=ismith,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=local','ismith','a9b0b3d4-94d4-1031-9a68-859fa79a497b'),('uid=jjones,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=local','jjones','8c7cf7a4-94d5-1031-9e92-cf23003d4784'),('uid=jsmith,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=local','jsmith','12058b20-94d6-1031-9e96-cf23003d4784'),('uid=karoshi,ou=karoshi,ou=other,ou=people,dc=karoshi,dc=local','karoshi','5d2abb90-94d4-1031-9863-81c11c92648b'),('uid=kmay,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=local','kmay','ce73ec4e-94d5-1031-9e94-cf23003d4784'),('uid=nobody,ou=people,dc=karoshi,dc=local','nobody','59be6baa-94d4-1031-9584-691c0ada23e6'),('uid=profileuser,ou=profileuser,ou=other,ou=people,dc=karoshi,dc=local','profileuser','5d2f9d5e-94d4-1031-9866-81c11c92648b'),('uid=psharrad,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=local','psharrad','5db81112-959b-1031-8bd5-53bb3d5c3bce'),('uid=root,ou=people,dc=karoshi,dc=local','root','59a6007e-94d4-1031-9583-691c0ada23e6'),('uid=tech1,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=local','tech1','5b8be94e-94d4-1031-98cf-f98a72417f40'),('uid=tech2,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=local','tech2','5b8e5dbe-94d4-1031-98d0-f98a72417f40'),('uid=tech3,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=local','tech3','5b98bac0-94d4-1031-98d1-f98a72417f40'),('uid=tech4,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=local','tech4','5b9b343a-94d4-1031-98d2-f98a72417f40'),('uid=training1,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training1','5cdd6fa2-94d4-1031-9844-81c11c92648b'),('uid=training10,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training10','5cdfbdac-94d4-1031-9845-81c11c92648b'),('uid=training11,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training11','5ce22f06-94d4-1031-9846-81c11c92648b'),('uid=training12,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training12','5ce49c64-94d4-1031-9847-81c11c92648b'),('uid=training13,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training13','5ce70ff8-94d4-1031-9848-81c11c92648b'),('uid=training14,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training14','5ce98b98-94d4-1031-9849-81c11c92648b'),('uid=training15,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training15','5cebf446-94d4-1031-984a-81c11c92648b'),('uid=training16,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training16','5cee5dd0-94d4-1031-984b-81c11c92648b'),('uid=training17,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training17','5cf0cf48-94d4-1031-984c-81c11c92648b'),('uid=training18,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training18','5cf33fc6-94d4-1031-984d-81c11c92648b'),('uid=training19,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training19','5cf5aee6-94d4-1031-984e-81c11c92648b'),('uid=training2,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training2','5cf82068-94d4-1031-984f-81c11c92648b'),('uid=training20,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training20','5cfda1be-94d4-1031-9850-81c11c92648b'),('uid=training21,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training21','5d000fbc-94d4-1031-9851-81c11c92648b'),('uid=training22,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training22','5d02809e-94d4-1031-9852-81c11c92648b'),('uid=training23,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training23','5d0506f2-94d4-1031-9853-81c11c92648b'),('uid=training24,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training24','5d07605a-94d4-1031-9854-81c11c92648b'),('uid=training25,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training25','5d09df7e-94d4-1031-9855-81c11c92648b'),('uid=training26,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training26','5d0c3fbc-94d4-1031-9856-81c11c92648b'),('uid=training27,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training27','5d0eb314-94d4-1031-9857-81c11c92648b'),('uid=training28,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training28','5d111f64-94d4-1031-9858-81c11c92648b'),('uid=training29,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training29','5d1392d0-94d4-1031-9859-81c11c92648b'),('uid=training3,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training3','5d160772-94d4-1031-985a-81c11c92648b'),('uid=training30,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training30','5d1878a4-94d4-1031-985b-81c11c92648b'),('uid=training4,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training4','5d1ae9f4-94d4-1031-985c-81c11c92648b'),('uid=training5,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training5','5d1d5784-94d4-1031-985d-81c11c92648b'),('uid=training6,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training6','5d1fc4ce-94d4-1031-985e-81c11c92648b'),('uid=training7,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training7','5d2234ca-94d4-1031-985f-81c11c92648b'),('uid=training8,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training8','5d24b6c8-94d4-1031-9860-81c11c92648b'),('uid=training9,ou=guests,ou=other,ou=people,dc=karoshi,dc=local','training9','5d271530-94d4-1031-9861-81c11c92648b');
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
  `timeout` int(10) unsigned DEFAULT '0',
  `created` bigint(20) DEFAULT '0',
  `token` varchar(100) DEFAULT NULL,
  `scope` tinyint(4) DEFAULT '0',
  `depth` tinyint(4) DEFAULT '0',
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_albums`
--

LOCK TABLES `oc_media_albums` WRITE;
/*!40000 ALTER TABLE `oc_media_albums` DISABLE KEYS */;
INSERT INTO `oc_media_albums` VALUES (1,'Greatest Hits',1,NULL),(2,'Under my skin',2,NULL),(3,'Discovery',3,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_artists`
--

LOCK TABLES `oc_media_artists` WRITE;
/*!40000 ALTER TABLE `oc_media_artists` DISABLE KEYS */;
INSERT INTO `oc_media_artists` VALUES (2,'Avril Lavigne'),(3,'ELO'),(1,'ZZ Top');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_media_songs`
--

LOCK TABLES `oc_media_songs` WRITE;
/*!40000 ALTER TABLE `oc_media_songs` DISABLE KEYS */;
INSERT INTO `oc_media_songs` VALUES (3,'Dont Tell Me',2,2,'/03 Dont Tell Me.mp3','ismith',202,3,4853427,1,1350827636),(4,'Forgotten',2,2,'/08 Forgotten.mp3','ismith',197,8,4742459,1,1350827643),(5,'Sharp Dressed Man',1,1,'/ismith/02_sharp_dressed_man.ogg','ismith',255,0,3529130,0,0),(6,'Gimme All Your Lovin&#039;',1,1,'/ismith/01_gimme_all_your_lovin.ogg','ismith',240,0,3580650,0,0),(7,'The diary of Horace Wimp',3,3,'/music/04_the_diary_of_horace_wimp.ogg','jsmith',258,0,3734213,1,1350829581),(8,'On the run',3,3,'/jsmith/07_on_the_run.ogg','jsmith',236,0,3658337,0,0),(9,'Midnight blue',3,3,'/music/06_midnight_blue.ogg','jsmith',259,0,3886991,1,1350829895),(10,'Last train to London',3,3,'/music/05_last_train_to_london.ogg','jsmith',271,0,4207685,0,0),(11,'Second time around',3,3,'/music/11_second_time_around.ogg','jsmith',43,0,648952,0,0),(12,'Little town flirt',3,3,'/music/12_little_town_flirt.ogg','jsmith',174,0,2674829,1,1350829886);
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
INSERT INTO `oc_media_users` VALUES ('admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'),('ismith','2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'),('jsmith','280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02');
/*!40000 ALTER TABLE `oc_media_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_pictures_images_cache`
--

DROP TABLE IF EXISTS `oc_pictures_images_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_pictures_images_cache` (
  `uid_owner` varchar(64) NOT NULL DEFAULT ' ',
  `path` varchar(256) NOT NULL DEFAULT ' ',
  `width` int(11) NOT NULL DEFAULT '0',
  `height` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_pictures_images_cache`
--

LOCK TABLES `oc_pictures_images_cache` WRITE;
/*!40000 ALTER TABLE `oc_pictures_images_cache` DISABLE KEYS */;
INSERT INTO `oc_pictures_images_cache` VALUES ('jsmith','/jsmith/logout.png',181,150),('jsmith','/jsmith/logout.png',181,150),('jsmith','/var/www/html/owncloud/data/jsmith/gallery/jsmith/logout.png',181,150);
/*!40000 ALTER TABLE `oc_pictures_images_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_preferences`
--

DROP TABLE IF EXISTS `oc_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_preferences` (
  `userid` varchar(64) NOT NULL DEFAULT ' ',
  `appid` varchar(32) NOT NULL DEFAULT ' ',
  `configkey` varchar(64) NOT NULL DEFAULT ' ',
  `configvalue` longtext,
  KEY `pref_userid_appid_key_index` (`userid`,`appid`,`configkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_preferences`
--

LOCK TABLES `oc_preferences` WRITE;
/*!40000 ALTER TABLE `oc_preferences` DISABLE KEYS */;
INSERT INTO `oc_preferences` VALUES ('ismith','user_ldap','homedir','/var/www/html/owncloud/data/ismith'),('ismith','files','mountconfigmtime','1350827867'),('jsmith','user_ldap','homedir','/var/www/html/owncloud/data/jsmith'),('jsmith','files','mountconfigmtime','1350828501');
/*!40000 ALTER TABLE `oc_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_properties`
--

DROP TABLE IF EXISTS `oc_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_properties` (
  `userid` varchar(64) NOT NULL DEFAULT ' ',
  `propertypath` varchar(255) NOT NULL DEFAULT ' ',
  `propertyname` varchar(255) NOT NULL DEFAULT ' ',
  `propertyvalue` varchar(255) NOT NULL DEFAULT ' '
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
  `share_type` tinyint(4) NOT NULL DEFAULT '0',
  `share_with` varchar(255) DEFAULT NULL,
  `uid_owner` varchar(255) NOT NULL DEFAULT ' ',
  `parent` int(11) DEFAULT '0',
  `item_type` varchar(64) NOT NULL DEFAULT ' ',
  `item_source` varchar(255) DEFAULT NULL,
  `item_target` varchar(255) DEFAULT NULL,
  `file_source` int(11) DEFAULT '0',
  `file_target` varchar(512) DEFAULT NULL,
  `permissions` tinyint(4) NOT NULL DEFAULT '0',
  `stime` bigint(20) NOT NULL DEFAULT '0',
  `accepted` tinyint(4) NOT NULL DEFAULT '0',
  `expiration` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
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
-- Table structure for table `oc_users`
--

DROP TABLE IF EXISTS `oc_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_users` (
  `uid` varchar(64) NOT NULL DEFAULT ' ',
  `password` varchar(255) NOT NULL DEFAULT ' ',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_users`
--

LOCK TABLES `oc_users` WRITE;
/*!40000 ALTER TABLE `oc_users` DISABLE KEYS */;
INSERT INTO `oc_users` VALUES ('admin','$2a$08$wvy2sfd7wzLGSBmY2/k4U..plB1NyJIcEZjNdPGpSdtEtlXRdizUO');
/*!40000 ALTER TABLE `oc_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-10-21 16:10:31
