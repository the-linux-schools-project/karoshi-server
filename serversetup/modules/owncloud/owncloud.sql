-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: owncloud
-- ------------------------------------------------------
-- Server version	5.6.28-1ubuntu2

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
  `type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `user` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `affecteduser` varchar(64) COLLATE utf8_bin NOT NULL,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `subject` varchar(255) COLLATE utf8_bin NOT NULL,
  `subjectparams` varchar(4000) COLLATE utf8_bin NOT NULL,
  `message` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `messageparams` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `file` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `link` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `object_type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `object_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`activity_id`),
  KEY `activity_user_time` (`affecteduser`,`timestamp`),
  KEY `activity_filter_by` (`affecteduser`,`user`,`timestamp`),
  KEY `activity_filter_app` (`affecteduser`,`app`,`timestamp`),
  KEY `activity_time` (`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity`
--

LOCK TABLES `oc_activity` WRITE;
/*!40000 ALTER TABLE `oc_activity` DISABLE KEYS */;
INSERT INTO `oc_activity` VALUES (1,1456918805,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[false]','','[]','','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=','files',12),(2,1456918805,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/ownCloud_User_Manual.pdf\"]','','[]','/ownCloud_User_Manual.pdf','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2F','files',13),(3,1456918805,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Documents\"]','','[]','/Documents','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2F','files',14),(4,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Documents\\/Example.odt\"]','','[]','/Documents/Example.odt','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FDocuments','files',15),(5,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\"]','','[]','/Photos','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2F','files',16),(6,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\\/Squirrel.jpg\"]','','[]','/Photos/Squirrel.jpg','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',17),(7,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\\/San Francisco.jpg\"]','','[]','/Photos/San Francisco.jpg','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',18),(8,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\\/Paris.jpg\"]','','[]','/Photos/Paris.jpg','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',19),(9,1456920501,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/home\\/test.txt\"]','','[]','/home/test.txt','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2Fhome','files',22),(10,1457516557,30,'file_created','admin','admin','files','created_self','[false]','','[]','','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=','files',2),(11,1457516557,30,'file_created','admin','admin','files','created_self','[\"\\/Documents\"]','','[]','/Documents','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2F','files',23),(12,1457516558,30,'file_created','admin','admin','files','created_self','[\"\\/Documents\\/Example.odt\"]','','[]','/Documents/Example.odt','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2FDocuments','files',24),(13,1457516558,30,'file_created','admin','admin','files','created_self','[\"\\/ownCloud_User_Manual.pdf\"]','','[]','/ownCloud_User_Manual.pdf','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2F','files',25),(14,1457516558,30,'file_created','admin','admin','files','created_self','[\"\\/Photos\"]','','[]','/Photos','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2F','files',26),(15,1457516558,30,'file_created','admin','admin','files','created_self','[\"\\/Photos\\/San Francisco.jpg\"]','','[]','/Photos/San Francisco.jpg','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',27),(16,1457516558,30,'file_created','admin','admin','files','created_self','[\"\\/Photos\\/Paris.jpg\"]','','[]','/Photos/Paris.jpg','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',28),(17,1457516558,30,'file_created','admin','admin','files','created_self','[\"\\/Photos\\/Squirrel.jpg\"]','','[]','/Photos/Squirrel.jpg','https://mycloud.just.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',29),(18,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"34\":false}]','','[]','','https://mycloud.just.testing.com/owncloud/files/index.php?dir=','files',34),(19,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"35\":\"\\/Documents\"}]','','[]','/Documents','https://mycloud.just.testing.com/owncloud/files/index.php?dir=%2F','files',35),(20,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"36\":\"\\/Documents\\/Example.odt\"}]','','[]','/Documents/Example.odt','https://mycloud.just.testing.com/owncloud/files/index.php?dir=%2FDocuments','files',36),(21,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"37\":\"\\/Photos\"}]','','[]','/Photos','https://mycloud.just.testing.com/owncloud/files/index.php?dir=%2F','files',37),(22,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"38\":\"\\/Photos\\/San Francisco.jpg\"}]','','[]','/Photos/San Francisco.jpg','https://mycloud.just.testing.com/owncloud/files/index.php?dir=%2FPhotos','files',38),(23,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"39\":\"\\/Photos\\/Paris.jpg\"}]','','[]','/Photos/Paris.jpg','https://mycloud.just.testing.com/owncloud/files/index.php?dir=%2FPhotos','files',39),(24,1457519003,30,'file_created','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0','files','created_self','[{\"40\":\"\\/Photos\\/Squirrel.jpg\"}]','','[]','/Photos/Squirrel.jpg','https://mycloud.just.testing.com/owncloud/files/index.php?dir=%2FPhotos','files',40);
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
  `amq_subjectparams` varchar(4000) COLLATE utf8_bin NOT NULL,
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
-- Table structure for table `oc_addressbookchanges`
--

DROP TABLE IF EXISTS `oc_addressbookchanges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_addressbookchanges` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  `addressbookid` int(11) NOT NULL,
  `operation` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `addressbookid_synctoken` (`addressbookid`,`synctoken`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbookchanges`
--

LOCK TABLES `oc_addressbookchanges` WRITE;
/*!40000 ALTER TABLE `oc_addressbookchanges` DISABLE KEYS */;
INSERT INTO `oc_addressbookchanges` VALUES (1,'Database:admin.vcf',1,3,1),(2,'LDAP:04D07B2F-AA52-4864-A503-F44609812371.vcf',2,3,1),(3,'LDAP:FB1373F1-0797-4830-AF84-BC7A2E133ED6.vcf',3,3,1),(4,'LDAP:306935A2-117F-4CF2-9881-C6B593D7A9C9.vcf',4,3,1),(5,'LDAP:0539132B-286D-4DB1-8C17-24A301199ADB.vcf',5,3,1),(6,'LDAP:FDE96242-A375-4C1B-B272-29191FE2D4B0.vcf',6,3,1),(7,'LDAP:C9C3BC45-1887-4747-BC73-556901C92A0E.vcf',7,3,1),(8,'LDAP:B62478F9-E071-41AF-84B6-E755C2ADE9C6.vcf',8,3,1),(9,'LDAP:3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6.vcf',9,3,1);
/*!40000 ALTER TABLE `oc_addressbookchanges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_addressbooks`
--

DROP TABLE IF EXISTS `oc_addressbooks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_addressbooks` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `principaluri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `displayname` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `addressbook_index` (`principaluri`,`uri`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbooks`
--

LOCK TABLES `oc_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_addressbooks` VALUES (1,'principals/users/FDE96242-A375-4C1B-B272-29191FE2D4B0','default','default',NULL,1),(2,'principals/users/admin','default','default',NULL,1),(3,'principals/system/system','system','system','System addressbook which holds all users of this instance',10);
/*!40000 ALTER TABLE `oc_addressbooks` ENABLE KEYS */;
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.2.1'),('activity','types','filesystem'),('backgroundjob','lastjob','1'),('comments','enabled','yes'),('comments','installed_version','0.2'),('comments','types','logging'),('core','OC_Channel','daily'),('core','installedat','1456918136.5882'),('core','lastcron','1457519138'),('core','lastupdateResult','{\"version\":\"100.0.0.0\",\"versionstring\":\"ownCloud daily\",\"url\":\"https:\\/\\/download.owncloud.org\\/community\\/owncloud-daily-stable9.tar.bz2\",\"web\":\"https:\\/\\/doc.owncloud.org\\/server\\/8.2\\/admin_manual\\/maintenance\\/upgrade.html\"}'),('core','lastupdatedat','1457518952'),('core','oc.integritycheck.checker','[]'),('core','public_documents','documents/public.php'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('core','remote_caldav','dav/appinfo/v1/caldav.php'),('core','remote_calendar','dav/appinfo/v1/caldav.php'),('core','remote_carddav','dav/appinfo/v1/carddav.php'),('core','remote_contacts','dav/appinfo/v1/carddav.php'),('core','remote_dav','dav/appinfo/v2/remote.php'),('core','remote_files','dav/appinfo/v1/webdav.php'),('core','remote_webdav','dav/appinfo/v1/webdav.php'),('core','repairlegacystoragesdone','yes'),('core','shareapi_allow_resharing','no'),('dav','enabled','yes'),('dav','installed_version','0.1.5'),('dav','types','filesystem'),('documents','enabled','yes'),('documents','installed_version','0.12.0'),('documents','ocsid','168711'),('documents','types',''),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','0.1.0'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','0.0.4'),('federation','types','authentication'),('files','cronjob_scan_files','500'),('files','enabled','yes'),('files','installed_version','1.4.4'),('files','types','filesystem'),('files_external','allow_user_mounting','no'),('files_external','enabled','yes'),('files_external','installed_version','0.5.2'),('files_external','ocsid','166048'),('files_external','types','filesystem'),('files_external','user_mounting_backends','ftp,dav,owncloud,sftp,amazons3,dropbox,googledrive,swift,smb,\\OC\\Files\\Storage\\SFTP_Key,\\OC\\Files\\Storage\\SMB_OC'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','0.8'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','0.9.1'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.1'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','0.8.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.2.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','0.9.8'),('files_videoplayer','types',''),('files_videoviewer','enabled','no'),('files_videoviewer','installed_version','0.1.3'),('files_videoviewer','ocsid','166054'),('files_videoviewer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','1.1'),('firstrunwizard','ocsid','166055'),('firstrunwizard','types',''),('gallery','enabled','yes'),('gallery','installed_version','14.5.0'),('gallery','types',''),('notes','enabled','yes'),('notes','installed_version','2.0.0'),('notes','ocsid','174554'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','0.2.3'),('notifications','types','logging'),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','0.4.1'),('provisioning_api','types','prevent_group_restriction'),('systemtags','enabled','yes'),('systemtags','installed_version','0.2'),('systemtags','types','logging'),('templateeditor','enabled','yes'),('templateeditor','installed_version','0.1'),('templateeditor','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','0.1.0'),('updatenotification','types',''),('updater','enabled','no'),('updater','installed_version','0.6'),('updater','types',''),('user_ldap','cleanUpJobOffset','0'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','0.8.0'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr',''),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=organizationalPerson)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','1'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','1'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','organizationalPerson'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=organizationalPerson)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1');
/*!40000 ALTER TABLE `oc_appconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendarchanges`
--

DROP TABLE IF EXISTS `oc_calendarchanges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendarchanges` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  `calendarid` int(11) NOT NULL,
  `operation` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `calendarid_synctoken` (`calendarid`,`synctoken`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarchanges`
--

LOCK TABLES `oc_calendarchanges` WRITE;
/*!40000 ALTER TABLE `oc_calendarchanges` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendarchanges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendarobjects`
--

DROP TABLE IF EXISTS `oc_calendarobjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendarobjects` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `calendardata` longblob,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `calendarid` int(10) unsigned NOT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  `componenttype` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `firstoccurence` int(10) unsigned DEFAULT NULL,
  `lastoccurence` int(10) unsigned DEFAULT NULL,
  `uid` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `calobjects_index` (`calendarid`,`uri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarobjects`
--

LOCK TABLES `oc_calendarobjects` WRITE;
/*!40000 ALTER TABLE `oc_calendarobjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendarobjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendars`
--

DROP TABLE IF EXISTS `oc_calendars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendars` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `principaluri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `displayname` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  `description` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `calendarorder` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarcolor` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `timezone` longtext COLLATE utf8_bin,
  `components` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `transparent` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `calendars_index` (`principaluri`,`uri`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendars`
--

LOCK TABLES `oc_calendars` WRITE;
/*!40000 ALTER TABLE `oc_calendars` DISABLE KEYS */;
INSERT INTO `oc_calendars` VALUES (1,'principals/users/FDE96242-A375-4C1B-B272-29191FE2D4B0','default','default',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(2,'principals/users/admin','default','default',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(3,'principals/system/system','contact_birthdays','contact_birthdays',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0);
/*!40000 ALTER TABLE `oc_calendars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendarsubscriptions`
--

DROP TABLE IF EXISTS `oc_calendarsubscriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendarsubscriptions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `principaluri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `source` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `displayname` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `refreshrate` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `calendarorder` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarcolor` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `striptodos` smallint(6) DEFAULT NULL,
  `stripalarms` smallint(6) DEFAULT NULL,
  `stripattachments` smallint(6) DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `calsub_index` (`principaluri`,`uri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarsubscriptions`
--

LOCK TABLES `oc_calendarsubscriptions` WRITE;
/*!40000 ALTER TABLE `oc_calendarsubscriptions` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendarsubscriptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_cards`
--

DROP TABLE IF EXISTS `oc_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_cards` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `addressbookid` int(11) NOT NULL DEFAULT '0',
  `carddata` longblob,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `lastmodified` bigint(20) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards`
--

LOCK TABLES `oc_cards` WRITE;
/*!40000 ALTER TABLE `oc_cards` DISABLE KEYS */;
INSERT INTO `oc_cards` VALUES (1,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:admin\r\nFN:admin\r\nN:admin;;;;\r\nCLOUD:admin@mycloud.just.testing.com/owncloud\r\nEND:VCARD\r\n','Database:admin.vcf',1457519113,'58d616a8b447f11afa684a7be2f81b56',160),(2,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:04D07B2F-AA52-4864-A503-F44609812371\r\nFN:Guest 1\r\nN:1;Guest;;;\r\nCLOUD:04D07B2F-AA52-4864-A503-F44609812371@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:04D07B2F-AA52-4864-A503-F44609812371.vcf',1457519113,'4885cb802352fbdcc899530b17959ec8',228),(3,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:FB1373F1-0797-4830-AF84-BC7A2E133ED6\r\nFN:Guest 2\r\nN:2;Guest;;;\r\nCLOUD:FB1373F1-0797-4830-AF84-BC7A2E133ED6@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:FB1373F1-0797-4830-AF84-BC7A2E133ED6.vcf',1457519113,'9ec36e95e8d87599576256d6492031ce',228),(4,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:306935A2-117F-4CF2-9881-C6B593D7A9C9\r\nFN:Guest 3\r\nN:3;Guest;;;\r\nCLOUD:306935A2-117F-4CF2-9881-C6B593D7A9C9@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:306935A2-117F-4CF2-9881-C6B593D7A9C9.vcf',1457519114,'3fef7cb04b7c58db7226f56ec2a89fe1',228),(5,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:0539132B-286D-4DB1-8C17-24A301199ADB\r\nFN:Guest 4\r\nN:4;Guest;;;\r\nCLOUD:0539132B-286D-4DB1-8C17-24A301199ADB@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:0539132B-286D-4DB1-8C17-24A301199ADB.vcf',1457519114,'4caace5b6766d89d1d0086f6a4496f34',228),(6,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:FDE96242-A375-4C1B-B272-29191FE2D4B0\r\nFN:Ian Smith\r\nN:Smith;Ian;;;\r\nCLOUD:FDE96242-A375-4C1B-B272-29191FE2D4B0@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:FDE96242-A375-4C1B-B272-29191FE2D4B0.vcf',1457519114,'d5baf5cc25a0c1b8dfb96e637e746fea',232),(7,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:C9C3BC45-1887-4747-BC73-556901C92A0E\r\nFN:John Jones\r\nN:Jones;John;;;\r\nCLOUD:C9C3BC45-1887-4747-BC73-556901C92A0E@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:C9C3BC45-1887-4747-BC73-556901C92A0E.vcf',1457519114,'2bd33b226e4b837d9c0699df389175a7',234),(8,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:B62478F9-E071-41AF-84B6-E755C2ADE9C6\r\nFN:Profile User\r\nN:User;Profile;;;\r\nCLOUD:B62478F9-E071-41AF-84B6-E755C2ADE9C6@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:B62478F9-E071-41AF-84B6-E755C2ADE9C6.vcf',1457519114,'b0e2c5722eecf80614ce3d743b3964ae',238),(9,3,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 3.5.0//EN\r\nUID:3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6\r\nFN:Sysadmin User\r\nN:User;Sysadmin;;;\r\nCLOUD:3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6@mycloud.just.testing.com/ownclou\r\n d\r\nEND:VCARD\r\n','LDAP:3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6.vcf',1457519114,'86fd4938e3c5d2a0ec60d601871511fd',240);
/*!40000 ALTER TABLE `oc_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_cards_properties`
--

DROP TABLE IF EXISTS `oc_cards_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_cards_properties` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `addressbookid` bigint(20) NOT NULL DEFAULT '0',
  `cardid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `name` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `value` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `preferred` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `card_contactid_index` (`cardid`),
  KEY `card_name_index` (`name`),
  KEY `card_value_index` (`value`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards_properties`
--

LOCK TABLES `oc_cards_properties` WRITE;
/*!40000 ALTER TABLE `oc_cards_properties` DISABLE KEYS */;
INSERT INTO `oc_cards_properties` VALUES (1,3,1,'UID','admin',0),(2,3,1,'FN','admin',0),(3,3,1,'N','admin;;;;',0),(4,3,1,'CLOUD','admin@mycloud.just.testing.com/owncloud',0),(5,3,2,'UID','04D07B2F-AA52-4864-A503-F44609812371',0),(6,3,2,'FN','Guest 1',0),(7,3,2,'N','1;Guest;;;',0),(8,3,2,'CLOUD','04D07B2F-AA52-4864-A503-F44609812371@mycloud.just.testing.com/owncloud',0),(9,3,3,'UID','FB1373F1-0797-4830-AF84-BC7A2E133ED6',0),(10,3,3,'FN','Guest 2',0),(11,3,3,'N','2;Guest;;;',0),(12,3,3,'CLOUD','FB1373F1-0797-4830-AF84-BC7A2E133ED6@mycloud.just.testing.com/owncloud',0),(13,3,4,'UID','306935A2-117F-4CF2-9881-C6B593D7A9C9',0),(14,3,4,'FN','Guest 3',0),(15,3,4,'N','3;Guest;;;',0),(16,3,4,'CLOUD','306935A2-117F-4CF2-9881-C6B593D7A9C9@mycloud.just.testing.com/owncloud',0),(17,3,5,'UID','0539132B-286D-4DB1-8C17-24A301199ADB',0),(18,3,5,'FN','Guest 4',0),(19,3,5,'N','4;Guest;;;',0),(20,3,5,'CLOUD','0539132B-286D-4DB1-8C17-24A301199ADB@mycloud.just.testing.com/owncloud',0),(21,3,6,'UID','FDE96242-A375-4C1B-B272-29191FE2D4B0',0),(22,3,6,'FN','Ian Smith',0),(23,3,6,'N','Smith;Ian;;;',0),(24,3,6,'CLOUD','FDE96242-A375-4C1B-B272-29191FE2D4B0@mycloud.just.testing.com/owncloud',0),(25,3,7,'UID','C9C3BC45-1887-4747-BC73-556901C92A0E',0),(26,3,7,'FN','John Jones',0),(27,3,7,'N','Jones;John;;;',0),(28,3,7,'CLOUD','C9C3BC45-1887-4747-BC73-556901C92A0E@mycloud.just.testing.com/owncloud',0),(29,3,8,'UID','B62478F9-E071-41AF-84B6-E755C2ADE9C6',0),(30,3,8,'FN','Profile User',0),(31,3,8,'N','User;Profile;;;',0),(32,3,8,'CLOUD','B62478F9-E071-41AF-84B6-E755C2ADE9C6@mycloud.just.testing.com/owncloud',0),(33,3,9,'UID','3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6',0),(34,3,9,'FN','Sysadmin User',0),(35,3,9,'N','User;Sysadmin;;;',0),(36,3,9,'CLOUD','3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6@mycloud.just.testing.com/owncloud',0);
/*!40000 ALTER TABLE `oc_cards_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_comments`
--

DROP TABLE IF EXISTS `oc_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_comments` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `parent_id` int(10) unsigned NOT NULL DEFAULT '0',
  `topmost_parent_id` int(10) unsigned NOT NULL DEFAULT '0',
  `children_count` int(10) unsigned NOT NULL DEFAULT '0',
  `actor_type` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `actor_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `message` longtext COLLATE utf8_bin,
  `verb` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `creation_timestamp` datetime DEFAULT NULL,
  `latest_child_timestamp` datetime DEFAULT NULL,
  `object_type` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `object_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `comments_parent_id_index` (`parent_id`),
  KEY `comments_topmost_parent_id_idx` (`topmost_parent_id`),
  KEY `comments_object_index` (`object_type`,`object_id`,`creation_timestamp`),
  KEY `comments_actor_index` (`actor_type`,`actor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_comments`
--

LOCK TABLES `oc_comments` WRITE;
/*!40000 ALTER TABLE `oc_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_comments_read_markers`
--

DROP TABLE IF EXISTS `oc_comments_read_markers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_comments_read_markers` (
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `marker_datetime` datetime DEFAULT NULL,
  `object_type` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `object_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  UNIQUE KEY `comments_marker_index` (`user_id`,`object_type`,`object_id`),
  KEY `comments_marker_object_index` (`object_type`,`object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_comments_read_markers`
--

LOCK TABLES `oc_comments_read_markers` WRITE;
/*!40000 ALTER TABLE `oc_comments_read_markers` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_comments_read_markers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_credentials`
--

DROP TABLE IF EXISTS `oc_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_credentials` (
  `user` varchar(64) COLLATE utf8_bin NOT NULL,
  `identifier` varchar(64) COLLATE utf8_bin NOT NULL,
  `credentials` longtext COLLATE utf8_bin,
  PRIMARY KEY (`user`,`identifier`),
  KEY `credentials_user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_credentials`
--

LOCK TABLES `oc_credentials` WRITE;
/*!40000 ALTER TABLE `oc_credentials` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_dav_shares`
--

DROP TABLE IF EXISTS `oc_dav_shares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_dav_shares` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `principaluri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `access` smallint(6) DEFAULT NULL,
  `resourceid` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dav_shares_index` (`principaluri`,`resourceid`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_dav_shares`
--

LOCK TABLES `oc_dav_shares` WRITE;
/*!40000 ALTER TABLE `oc_dav_shares` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_dav_shares` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_member`
--

LOCK TABLES `oc_documents_member` WRITE;
/*!40000 ALTER TABLE `oc_documents_member` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_documents_op`
--

LOCK TABLES `oc_documents_op` WRITE;
/*!40000 ALTER TABLE `oc_documents_op` DISABLE KEYS */;
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
/*!40000 ALTER TABLE `oc_documents_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_external_applicable`
--

DROP TABLE IF EXISTS `oc_external_applicable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_external_applicable` (
  `applicable_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mount_id` bigint(20) NOT NULL,
  `type` int(11) NOT NULL,
  `value` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`applicable_id`),
  UNIQUE KEY `applicable_type_value_mount` (`type`,`value`,`mount_id`),
  KEY `applicable_mount` (`mount_id`),
  KEY `applicable_type_value` (`type`,`value`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_applicable`
--

LOCK TABLES `oc_external_applicable` WRITE;
/*!40000 ALTER TABLE `oc_external_applicable` DISABLE KEYS */;
INSERT INTO `oc_external_applicable` VALUES (1,1,2,'adults'),(2,1,2,'children'),(3,1,2,'guestusers'),(4,1,2,'itadmin'),(5,1,2,'profilemanagement'),(6,1,2,'teenagers');
/*!40000 ALTER TABLE `oc_external_applicable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_external_config`
--

DROP TABLE IF EXISTS `oc_external_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_external_config` (
  `config_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mount_id` bigint(20) NOT NULL,
  `key` varchar(64) COLLATE utf8_bin NOT NULL,
  `value` varchar(4096) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`config_id`),
  UNIQUE KEY `config_mount_key` (`mount_id`,`key`),
  KEY `config_mount` (`mount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_config`
--

LOCK TABLES `oc_external_config` WRITE;
/*!40000 ALTER TABLE `oc_external_config` DISABLE KEYS */;
INSERT INTO `oc_external_config` VALUES (1,1,'host','bertie.just.testing.com'),(2,1,'username_as_share','1'),(3,1,'share',''),(4,1,'root','');
/*!40000 ALTER TABLE `oc_external_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_external_mounts`
--

DROP TABLE IF EXISTS `oc_external_mounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_external_mounts` (
  `mount_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mount_point` varchar(128) COLLATE utf8_bin NOT NULL,
  `storage_backend` varchar(64) COLLATE utf8_bin NOT NULL,
  `auth_backend` varchar(64) COLLATE utf8_bin NOT NULL,
  `priority` int(11) NOT NULL DEFAULT '100',
  `type` int(11) NOT NULL,
  PRIMARY KEY (`mount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_mounts`
--

LOCK TABLES `oc_external_mounts` WRITE;
/*!40000 ALTER TABLE `oc_external_mounts` DISABLE KEYS */;
INSERT INTO `oc_external_mounts` VALUES (1,'/home','\\OC\\Files\\Storage\\SMB_OC','password::sessioncredentials',90,1);
/*!40000 ALTER TABLE `oc_external_mounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_external_options`
--

DROP TABLE IF EXISTS `oc_external_options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_external_options` (
  `option_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mount_id` bigint(20) NOT NULL,
  `key` varchar(64) COLLATE utf8_bin NOT NULL,
  `value` varchar(256) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`option_id`),
  UNIQUE KEY `option_mount_key` (`mount_id`,`key`),
  KEY `option_mount` (`mount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_options`
--

LOCK TABLES `oc_external_options` WRITE;
/*!40000 ALTER TABLE `oc_external_options` DISABLE KEYS */;
INSERT INTO `oc_external_options` VALUES (1,1,'encrypt','true'),(2,1,'previews','true'),(3,1,'filesystem_check_changes','1'),(4,1,'enable_sharing','true');
/*!40000 ALTER TABLE `oc_external_options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_file_locks`
--

DROP TABLE IF EXISTS `oc_file_locks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_file_locks` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `lock` int(11) NOT NULL DEFAULT '0',
  `key` varchar(64) COLLATE utf8_bin NOT NULL,
  `ttl` int(11) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `lock_key_index` (`key`),
  KEY `lock_ttl_index` (`ttl`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (23,0,'files/2c7eaecb9090bd89cef1dcd4d0d5881a',1457520157),(24,0,'files/2265a7864cbb01fd760398e786dc9eee',1457522603),(25,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1457520157),(26,0,'files/7f472eca153e78ea7caaa6d969440cba',1457520158),(27,0,'files/a36e4eb9c7358bd02497aa960b1151a9',1457520158),(28,0,'files/3513aba8aa4305d3ad33fc7122d4af30',1457520158),(29,0,'files/37c85de42508b164a7d7f502df40796e',1457520158),(30,0,'files/173a67328b2dceac7a89367cdcc7b1b6',1457520158),(31,0,'files/47b35dd91a203e06efeb4436117e4def',1457520158),(32,0,'files/a3594fd4eca7119cb937772e1f8f5415',1457520158),(33,0,'files/4d0a5085369fc0554c67b8420144d947',1457520158),(34,0,'files/b90e2f3adbfcaaa9507228281d9f15e7',1457522534),(35,0,'files/15a1cdafe5281ab2f4e41a302b7a0e42',1457522602),(36,0,'files/45085a96c31cc432a39f45e722812ece',1457522603),(37,0,'files/88c14b07dd5f8ab6c4e49468e1844458',1457522603),(38,0,'files/637c3a0737b64356c85d9cb57efdc653',1457522603),(39,0,'files/0797907065b840cb77ea681a8e2df42c',1457522603),(40,0,'files/750959f274b25dd0f8ff7ef82303e599',1457522603),(41,0,'files/d01f6efbef520f61ca0129e432769690',1457522603),(42,0,'files/577c44c9289f67b786404c935930a54f',1457522603),(43,0,'files/077c541ed764c2fc41dfe17be42652c7',1457522603),(44,0,'files/ed5e4d37e9361837b0f2e657f8ae76f4',1457522606);
/*!40000 ALTER TABLE `oc_file_locks` ENABLE KEYS */;
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
  `checksum` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`fileid`),
  UNIQUE KEY `fs_storage_path_hash` (`storage`,`path_hash`),
  KEY `fs_parent_name_hash` (`parent`,`name`),
  KEY `fs_storage_mimetype` (`storage`,`mimetype`),
  KEY `fs_storage_mimepart` (`storage`,`mimepart`),
  KEY `fs_storage_size` (`storage`,`size`,`fileid`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,3259772,1457516558,1457516557,0,0,'56dff00ed63cd',23,NULL),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,3259772,1457516558,1457516558,0,0,'56dff00ed739e',31,NULL),(10,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,3259772,1456918806,1456918805,0,0,'56d6d11666336',23,NULL),(11,3,'cache','0fea6a13c52b4d4725368f24b045ca84',10,'cache',2,1,0,1456918805,1456918805,0,0,'56d6d1157c00d',31,NULL),(12,3,'files','45b963397aa40d4a0063e0d85e4fe7a1',10,'files',2,1,3259772,1456920501,1456918806,0,0,'56d6d7b5510f3',31,NULL),(13,3,'files/ownCloud_User_Manual.pdf','fbaae4021d9c766fc309c54e81133013',12,'ownCloud_User_Manual.pdf',4,3,2544989,1456918805,1456918805,0,0,'8af623094069ea4d8ac3224c53e45087',27,NULL),(14,3,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',12,'Documents',2,1,36227,1456918805,1456918805,0,0,'56d6d115f0a2e',31,NULL),(15,3,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',14,'Example.odt',7,3,36227,1456918806,1456918806,0,0,'b859bcb5612690ce134572e1fd540b62',27,NULL),(16,3,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',12,'Photos',2,1,678556,1456918806,1456918806,0,0,'56d6d116682f7',31,NULL),(17,3,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',16,'Squirrel.jpg',6,5,233724,1456918806,1456918806,0,0,'959059e80e056225ecde63b1668ea456',27,NULL),(18,3,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',16,'San Francisco.jpg',6,5,216071,1456918806,1456918806,0,0,'6c253191799e50a282124d1aba2a0a02',27,NULL),(19,3,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',16,'Paris.jpg',6,5,228761,1456918806,1456918806,0,0,'84b53d7c493a7bdfa3f3a9550db976e0',27,NULL),(20,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1457516557,1457516557,0,0,'56dff00d7af3f',31,NULL),(21,5,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,1456920501,1456920501,0,0,'56d6d7b553492',23,NULL),(22,5,'test.txt','dd18bf3a8e0a2a3e53e2661c7fb53534',21,'test.txt',9,8,0,1456920501,1456920501,0,0,'56d6d7b53aa6e',27,NULL),(23,1,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',2,'Documents',2,1,36227,1457516557,1457516557,0,0,'56dff00de86b4',31,NULL),(24,1,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',23,'Example.odt',7,3,36227,1457516558,1457516558,0,0,'ec8aa877ee070ddc7a6e85050199a600',27,NULL),(25,1,'files/ownCloud_User_Manual.pdf','fbaae4021d9c766fc309c54e81133013',2,'ownCloud_User_Manual.pdf',4,3,2544989,1457516558,1457516558,0,0,'e897730ed8d693b343d07871d9192549',27,NULL),(26,1,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',2,'Photos',2,1,678556,1457516558,1457516558,0,0,'56dff00ed88e8',31,NULL),(27,1,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',26,'San Francisco.jpg',6,5,216071,1457516558,1457516558,0,0,'eda6805ba5a61d2708857a763726d503',27,NULL),(28,1,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',26,'Paris.jpg',6,5,228761,1457516558,1457516558,0,0,'0e61d068b0a507710db7b15dc540b3eb',27,NULL),(29,1,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',26,'Squirrel.jpg',6,5,233724,1457516558,1457516558,0,0,'a2fd50d566664c764d638817666a73b9',27,NULL),(30,2,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1457518934,1457518934,0,0,'56dff956d9d51',23,NULL),(31,2,'files_external','c270928b685e7946199afdfb898d27ea',30,'files_external',2,1,0,1457518934,1457518934,0,0,'56dff956ca18f',31,NULL),(32,8,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,714783,1457519003,1457519003,0,0,'56dff99b9afff',23,NULL),(33,8,'cache','0fea6a13c52b4d4725368f24b045ca84',32,'cache',2,1,0,1457519002,1457519002,0,0,'56dff99ae728c',31,NULL),(34,8,'files','45b963397aa40d4a0063e0d85e4fe7a1',32,'files',2,1,714783,1457519003,1457519003,0,0,'56dff99b9a159',31,NULL),(35,8,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',34,'Documents',2,1,36227,1457519003,1457519003,0,0,'56dff99b37d25',31,NULL),(36,8,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',35,'Example.odt',7,3,36227,1457519003,1457519003,0,0,'af71ca06a8a6c580a99c02344900def9',27,NULL),(37,8,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',34,'Photos',2,1,678556,1457519003,1457519003,0,0,'56dff99b9914e',31,NULL),(38,8,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',37,'San Francisco.jpg',6,5,216071,1457519003,1457519003,0,0,'d91c7378999aefdd564f6ea8687579b7',27,NULL),(39,8,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',37,'Paris.jpg',6,5,228761,1457519003,1457519003,0,0,'80becc70c276c68c858ba043e2bc9056',27,NULL),(40,8,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',37,'Squirrel.jpg',6,5,233724,1457519003,1457519003,0,0,'ac4372d06b18bb242c6f5e5f435a58f1',27,NULL),(41,7,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1457515990,1457515990,0,0,'56dff99f3ef83',23,NULL);
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
  PRIMARY KEY (`gid`,`uid`),
  KEY `gu_uid_index` (`uid`)
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
  `argument` varchar(4000) COLLATE utf8_bin NOT NULL DEFAULT '',
  `last_run` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `job_class_index` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Files_sharing\\Lib\\DeleteOrphanedSharesJob','null',1457519138),(2,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1457518681),(3,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1457518955),(4,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1457518972),(5,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1457518979),(6,'OCA\\user_ldap\\lib\\Jobs','null',1457516553),(7,'\\OCA\\User_LDAP\\Jobs\\CleanUp','null',1457516562),(8,'OCA\\Files\\BackgroundJob\\ScanFiles','null',1457519018),(9,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',1457519023),(10,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',1457519033),(11,'OCA\\Files_sharing\\ExpireSharesJob','null',1457519105),(12,'OCA\\DAV\\CardDAV\\SyncJob','null',1457519112),(13,'OCA\\Federation\\SyncJob','null',1457519123);
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
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=adults,ou=groups,ou=people,dc=just,dc=testing,dc=com','adults','99622F71-36E6-44A7-9951-63FAE2B4DDBF'),('cn=children,ou=groups,ou=people,dc=just,dc=testing,dc=com','children','4456C654-8E55-4B05-8833-4A8899F876B9'),('cn=guestusers,ou=groups,ou=people,dc=just,dc=testing,dc=com','guestusers','7DAD21BA-56D4-4D72-A5B9-9E0B04B90FF8'),('cn=itadmin,ou=groups,ou=people,dc=just,dc=testing,dc=com','itadmin','EEE4018D-87C0-4883-B800-3875B4F1A018'),('cn=multimedia,ou=groups,ou=people,dc=just,dc=testing,dc=com','multimedia','57F34649-89CC-4A58-AB55-9C42C6F0E593'),('cn=profilemanagement,ou=groups,ou=people,dc=just,dc=testing,dc=com','profilemanagement','7BDEC7C6-395F-4B8C-8A3A-E2BBF96A2B6C'),('cn=staff,ou=groups,ou=people,dc=karoshi,dc=testing,dc=com','staff','400C85D5-B809-4682-92E7-4E86B189037F'),('cn=tech,ou=groups,ou=people,dc=just,dc=testing,dc=com','tech','B39B30B8-6F8D-4F58-9E57-8063E9C9B412'),('cn=teenagers,ou=groups,ou=people,dc=just,dc=testing,dc=com','teenagers','038B4842-FE97-41BF-A2A4-ABAFC0476CC6');
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
INSERT INTO `oc_ldap_group_members` VALUES ('adults','a:0:{}'),('children','a:0:{}'),('guestusers','a:0:{}'),('itadmin','a:0:{}'),('multimedia','a:0:{}'),('profilemanagement','a:0:{}'),('tech','a:0:{}'),('teenagers','a:0:{}');
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
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=guest1,ou=guestusers,ou=other,ou=people,dc=just,dc=testing,dc=com','04D07B2F-AA52-4864-A503-F44609812371','04D07B2F-AA52-4864-A503-F44609812371'),('cn=guest4,ou=guestusers,ou=other,ou=people,dc=just,dc=testing,dc=com','0539132B-286D-4DB1-8C17-24A301199ADB','0539132B-286D-4DB1-8C17-24A301199ADB'),('cn=guest7,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','0FBB66F4-04AC-4F70-99FB-FF01EE5C2396'),('cn=guest3,ou=guestusers,ou=other,ou=people,dc=just,dc=testing,dc=com','306935A2-117F-4CF2-9881-C6B593D7A9C9','306935A2-117F-4CF2-9881-C6B593D7A9C9'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','332D3193-25CA-4137-9AE1-9DD6032E99D5','332D3193-25CA-4137-9AE1-9DD6032E99D5'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,dc=just,dc=testing,dc=com','3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6','3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6'),('cn=guest4,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','3683285D-531B-4AF9-97ED-F2194AF031DF','3683285D-531B-4AF9-97ED-F2194AF031DF'),('cn=guest10,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','36DD0503-E46E-403B-8D89-3AED69A27632','36DD0503-E46E-403B-8D89-3AED69A27632'),('cn=ismith,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483'),('cn=tech3,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','4C68AA9A-0952-4200-98C1-7C43E7DFE8A1'),('cn=guest2,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','67B1FC51-5555-4297-ACD2-72E1EF6CF797','67B1FC51-5555-4297-ACD2-72E1EF6CF797'),('cn=tech2,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','711F7896-EB66-42BE-AD5C-DB5121693431','711F7896-EB66-42BE-AD5C-DB5121693431'),('cn=profileuser,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15'),('cn=profileuser,ou=other,ou=people,dc=just,dc=testing,dc=com','B62478F9-E071-41AF-84B6-E755C2ADE9C6','B62478F9-E071-41AF-84B6-E755C2ADE9C6'),('cn=tech4,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','BA79ED58-C2CD-4330-954A-FEC72FE230F5','BA79ED58-C2CD-4330-954A-FEC72FE230F5'),('cn=guest5,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','C713E05B-6633-4723-89C7-94F070C39D5B','C713E05B-6633-4723-89C7-94F070C39D5B'),('cn=jjones,ou=adults,ou=family,ou=people,dc=just,dc=testing,dc=com','C9C3BC45-1887-4747-BC73-556901C92A0E','C9C3BC45-1887-4747-BC73-556901C92A0E'),('cn=tech1,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','CBC82A9B-9A83-4232-A7E5-81C1C56B3822','CBC82A9B-9A83-4232-A7E5-81C1C56B3822'),('cn=guest1,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E'),('cn=guest6,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','E6EACADC-22BF-4349-B8D2-D41848C179B1','E6EACADC-22BF-4349-B8D2-D41848C179B1'),('cn=guest9,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','EF3BCD6A-1994-4091-8410-62DC8C7115C8','EF3BCD6A-1994-4091-8410-62DC8C7115C8'),('cn=guest3,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','F0E986F5-1066-42E4-A34F-7DD9D7C216F4','F0E986F5-1066-42E4-A34F-7DD9D7C216F4'),('cn=guest2,ou=guestusers,ou=other,ou=people,dc=just,dc=testing,dc=com','FB1373F1-0797-4830-AF84-BC7A2E133ED6','FB1373F1-0797-4830-AF84-BC7A2E133ED6'),('cn=ismith,ou=adults,ou=family,ou=people,dc=just,dc=testing,dc=com','FDE96242-A375-4C1B-B272-29191FE2D4B0','FDE96242-A375-4C1B-B272-29191FE2D4B0'),('cn=guest8,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','FE6FAF10-D0F4-4807-A73F-E91712CCBA0D');
/*!40000 ALTER TABLE `oc_ldap_user_mapping` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (3,'application'),(11,'application/msonenote'),(4,'application/pdf'),(10,'application/vnd.lotus-wordpro'),(7,'application/vnd.oasis.opendocument.text'),(12,'application/vnd.visio'),(13,'application/vnd.wordperfect'),(1,'httpd'),(2,'httpd/unix-directory'),(5,'image'),(6,'image/jpeg'),(8,'text'),(9,'text/plain');
/*!40000 ALTER TABLE `oc_mimetypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_mounts`
--

DROP TABLE IF EXISTS `oc_mounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_mounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_id` int(11) NOT NULL,
  `root_id` int(11) NOT NULL,
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL,
  `mount_point` varchar(4000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mounts_user_root_index` (`user_id`,`root_id`),
  KEY `mounts_user_index` (`user_id`),
  KEY `mounts_storage_index` (`storage_id`),
  KEY `mounts_root_index` (`root_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mounts`
--

LOCK TABLES `oc_mounts` WRITE;
/*!40000 ALTER TABLE `oc_mounts` DISABLE KEYS */;
INSERT INTO `oc_mounts` VALUES (1,1,1,'admin','/admin/'),(2,8,32,'FDE96242-A375-4C1B-B272-29191FE2D4B0','/FDE96242-A375-4C1B-B272-29191FE2D4B0/');
/*!40000 ALTER TABLE `oc_mounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_notifications`
--

DROP TABLE IF EXISTS `oc_notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_notifications` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(32) COLLATE utf8_bin NOT NULL,
  `user` varchar(64) COLLATE utf8_bin NOT NULL,
  `timestamp` int(11) NOT NULL DEFAULT '0',
  `object_type` varchar(64) COLLATE utf8_bin NOT NULL,
  `object_id` varchar(64) COLLATE utf8_bin NOT NULL,
  `subject` varchar(64) COLLATE utf8_bin NOT NULL,
  `subject_parameters` longtext COLLATE utf8_bin,
  `message` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `message_parameters` longtext COLLATE utf8_bin,
  `link` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `actions` longtext COLLATE utf8_bin,
  PRIMARY KEY (`notification_id`),
  KEY `oc_notifications_app` (`app`),
  KEY `oc_notifications_user` (`user`),
  KEY `oc_notifications_timestamp` (`timestamp`),
  KEY `oc_notifications_object` (`object_type`,`object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_notifications`
--

LOCK TABLES `oc_notifications` WRITE;
/*!40000 ALTER TABLE `oc_notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_notifications` ENABLE KEYS */;
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
INSERT INTO `oc_preferences` VALUES ('04D07B2F-AA52-4864-A503-F44609812371','files_external','config_version','0.5.0'),('04D07B2F-AA52-4864-A503-F44609812371','user_ldap','displayName','Guest 1'),('04D07B2F-AA52-4864-A503-F44609812371','user_ldap','homePath',''),('04D07B2F-AA52-4864-A503-F44609812371','user_ldap','lastFeatureRefresh','1457519113'),('04D07B2F-AA52-4864-A503-F44609812371','user_ldap','uid','guest1'),('0539132B-286D-4DB1-8C17-24A301199ADB','files_external','config_version','0.5.0'),('0539132B-286D-4DB1-8C17-24A301199ADB','user_ldap','displayName','Guest 4'),('0539132B-286D-4DB1-8C17-24A301199ADB','user_ldap','homePath',''),('0539132B-286D-4DB1-8C17-24A301199ADB','user_ldap','lastFeatureRefresh','1457519113'),('0539132B-286D-4DB1-8C17-24A301199ADB','user_ldap','uid','guest4'),('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','displayName','Guest 7'),('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','isDeleted','1'),('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','lastFeatureRefresh','1456919491'),('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','uid','guest7'),('306935A2-117F-4CF2-9881-C6B593D7A9C9','files_external','config_version','0.5.0'),('306935A2-117F-4CF2-9881-C6B593D7A9C9','user_ldap','displayName','Guest 3'),('306935A2-117F-4CF2-9881-C6B593D7A9C9','user_ldap','homePath',''),('306935A2-117F-4CF2-9881-C6B593D7A9C9','user_ldap','lastFeatureRefresh','1457519113'),('306935A2-117F-4CF2-9881-C6B593D7A9C9','user_ldap','uid','guest3'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','displayName','Sysadmin User'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','isDeleted','1'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','lastFeatureRefresh','1456919491'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','uid','sysadmin'),('3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6','files_external','config_version','0.5.0'),('3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6','user_ldap','displayName','Sysadmin User'),('3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6','user_ldap','homePath',''),('3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6','user_ldap','lastFeatureRefresh','1457519113'),('3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6','user_ldap','uid','sysadmin'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','displayName','Guest 4'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','isDeleted','1'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','lastFeatureRefresh','1456919491'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','uid','guest4'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','displayName','Guest 10'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','isDeleted','1'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','lastFeatureRefresh','1456919491'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','uid','guest10'),('482DEFA3-C1CF-4348-9C1C-571396011483','core','lang','en'),('482DEFA3-C1CF-4348-9C1C-571396011483','core','timezone','Europe/London'),('482DEFA3-C1CF-4348-9C1C-571396011483','firstrunwizard','show','0'),('482DEFA3-C1CF-4348-9C1C-571396011483','login','lastLogin','1456920470'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','displayName','Ian Smith'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','firstLoginAccomplished','1'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','homePath',''),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','isDeleted','1'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','lastFeatureRefresh','1456920470'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','uid','ismith'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','displayName','Tech 3'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','isDeleted','1'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','lastFeatureRefresh','1456919491'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','uid','tech3'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','displayName','Guest 2'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','isDeleted','1'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','lastFeatureRefresh','1456919491'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','uid','guest2'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','displayName','Tech 2'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','isDeleted','1'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','lastFeatureRefresh','1456919491'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','uid','tech2'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','displayName','Profile User'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','isDeleted','1'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','lastFeatureRefresh','1456919491'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','uid','profileuser'),('B62478F9-E071-41AF-84B6-E755C2ADE9C6','files_external','config_version','0.5.0'),('B62478F9-E071-41AF-84B6-E755C2ADE9C6','user_ldap','displayName','Profile User'),('B62478F9-E071-41AF-84B6-E755C2ADE9C6','user_ldap','homePath',''),('B62478F9-E071-41AF-84B6-E755C2ADE9C6','user_ldap','lastFeatureRefresh','1457519113'),('B62478F9-E071-41AF-84B6-E755C2ADE9C6','user_ldap','uid','profileuser'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','displayName','Tech 4'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','isDeleted','1'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','lastFeatureRefresh','1456919491'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','uid','tech4'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','displayName','Guest 5'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','isDeleted','1'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','lastFeatureRefresh','1456919491'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','uid','guest5'),('C9C3BC45-1887-4747-BC73-556901C92A0E','files_external','config_version','0.5.0'),('C9C3BC45-1887-4747-BC73-556901C92A0E','user_ldap','displayName','John Jones'),('C9C3BC45-1887-4747-BC73-556901C92A0E','user_ldap','homePath',''),('C9C3BC45-1887-4747-BC73-556901C92A0E','user_ldap','lastFeatureRefresh','1457519113'),('C9C3BC45-1887-4747-BC73-556901C92A0E','user_ldap','uid','jjones'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','displayName','Tech 1'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','isDeleted','1'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','lastFeatureRefresh','1456919491'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','uid','tech1'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','displayName','Guest 1'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','isDeleted','1'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','lastFeatureRefresh','1456919491'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','uid','guest1'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','displayName','Guest 6'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','isDeleted','1'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','lastFeatureRefresh','1456919491'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','uid','guest6'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','displayName','Guest 9'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','isDeleted','1'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','lastFeatureRefresh','1456919491'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','uid','guest9'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','displayName','Guest 3'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','isDeleted','1'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','lastFeatureRefresh','1456919491'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','uid','guest3'),('FB1373F1-0797-4830-AF84-BC7A2E133ED6','files_external','config_version','0.5.0'),('FB1373F1-0797-4830-AF84-BC7A2E133ED6','user_ldap','displayName','Guest 2'),('FB1373F1-0797-4830-AF84-BC7A2E133ED6','user_ldap','homePath',''),('FB1373F1-0797-4830-AF84-BC7A2E133ED6','user_ldap','lastFeatureRefresh','1457519113'),('FB1373F1-0797-4830-AF84-BC7A2E133ED6','user_ldap','uid','guest2'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','core','lang','en'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','core','timezone','Europe/London'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','files_external','config_version','0.5.0'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','firstrunwizard','show','0'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','login','lastLogin','1457519002'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','user_ldap','displayName','Ian Smith'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','user_ldap','firstLoginAccomplished','1'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','user_ldap','homePath',''),('FDE96242-A375-4C1B-B272-29191FE2D4B0','user_ldap','lastFeatureRefresh','1457519113'),('FDE96242-A375-4C1B-B272-29191FE2D4B0','user_ldap','uid','ismith'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','displayName','Guest 8'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','isDeleted','1'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','lastFeatureRefresh','1456919491'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','uid','guest8'),('admin','core','lang','en'),('admin','core','timezone','Europe/London'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1457519110');
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
-- Table structure for table `oc_schedulingobjects`
--

DROP TABLE IF EXISTS `oc_schedulingobjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_schedulingobjects` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `principaluri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `calendardata` longblob,
  `uri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_schedulingobjects`
--

LOCK TABLES `oc_schedulingobjects` WRITE;
/*!40000 ALTER TABLE `oc_schedulingobjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_schedulingobjects` ENABLE KEYS */;
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
  `uid_initiator` varchar(64) COLLATE utf8_bin DEFAULT NULL,
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
  `remote_id` int(11) NOT NULL DEFAULT '-1',
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
  `available` int(11) NOT NULL DEFAULT '1',
  `last_checked` int(11) DEFAULT NULL,
  PRIMARY KEY (`numeric_id`),
  UNIQUE KEY `storages_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('home::admin',1,1,NULL),('local::/home/owncloud/data/',2,1,NULL),('home::482DEFA3-C1CF-4348-9C1C-571396011483',3,1,NULL),('smb::admin@bertie.karoshi.testing.com//admin//',4,0,1456920665),('smb::ismith@bertie.karoshi.testing.com//ismith//',5,1,NULL),('smb::admin@bertie.just.testing.com//admin//',6,0,1457519127),('smb::ismith@bertie.just.testing.com//ismith//',7,1,1457519008),('home::FDE96242-A375-4C1B-B272-29191FE2D4B0',8,1,NULL),('home::04D07B2F-AA52-4864-A503-F44609812371',9,1,NULL),('failedstorage',10,1,NULL),('home::0539132B-286D-4DB1-8C17-24A301199ADB',11,1,NULL),('home::306935A2-117F-4CF2-9881-C6B593D7A9C9',12,1,NULL),('home::3570E5FF-9250-4D3A-BF80-0CDA44C5C5A6',13,1,NULL),('home::B62478F9-E071-41AF-84B6-E755C2ADE9C6',14,1,NULL),('home::C9C3BC45-1887-4747-BC73-556901C92A0E',15,1,NULL),('home::FB1373F1-0797-4830-AF84-BC7A2E133ED6',16,1,NULL);
/*!40000 ALTER TABLE `oc_storages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_systemtag`
--

DROP TABLE IF EXISTS `oc_systemtag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_systemtag` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `visibility` smallint(6) NOT NULL DEFAULT '1',
  `editable` smallint(6) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_ident` (`name`,`visibility`,`editable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_systemtag`
--

LOCK TABLES `oc_systemtag` WRITE;
/*!40000 ALTER TABLE `oc_systemtag` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_systemtag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_systemtag_object_mapping`
--

DROP TABLE IF EXISTS `oc_systemtag_object_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_systemtag_object_mapping` (
  `objectid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `objecttype` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `systemtagid` int(10) unsigned NOT NULL DEFAULT '0',
  UNIQUE KEY `mapping` (`objecttype`,`objectid`,`systemtagid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_systemtag_object_mapping`
--

LOCK TABLES `oc_systemtag_object_mapping` WRITE;
/*!40000 ALTER TABLE `oc_systemtag_object_mapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_systemtag_object_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_trusted_servers`
--

DROP TABLE IF EXISTS `oc_trusted_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_trusted_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(512) COLLATE utf8_bin NOT NULL COMMENT 'Url of trusted server',
  `url_hash` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT 'sha1 hash of the url without the protocol',
  `token` varchar(128) COLLATE utf8_bin DEFAULT NULL COMMENT 'token used to exchange the shared secret',
  `shared_secret` varchar(256) COLLATE utf8_bin DEFAULT NULL COMMENT 'shared secret used to authenticate',
  `status` int(11) NOT NULL DEFAULT '2' COMMENT 'current status of the connection',
  `sync_token` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT 'cardDav sync token',
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_hash` (`url_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_trusted_servers`
--

LOCK TABLES `oc_trusted_servers` WRITE;
/*!40000 ALTER TABLE `oc_trusted_servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_trusted_servers` ENABLE KEYS */;
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
INSERT INTO `oc_users` VALUES ('admin',NULL,'1|$2y$10$4C7YumRjpzzG.lGcNFu80egS2PYSPhvHTakmUdht.ZveaBVOb5i6i');
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

-- Dump completed on 2016-03-09 10:26:56
