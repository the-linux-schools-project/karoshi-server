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
  KEY `activity_filter_app` (`affecteduser`,`app`,`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity`
--

LOCK TABLES `oc_activity` WRITE;
/*!40000 ALTER TABLE `oc_activity` DISABLE KEYS */;
INSERT INTO `oc_activity` VALUES (1,1456918805,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[false]','','[]','','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=','files',12),(2,1456918805,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/ownCloud_User_Manual.pdf\"]','','[]','/ownCloud_User_Manual.pdf','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2F','files',13),(3,1456918805,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Documents\"]','','[]','/Documents','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2F','files',14),(4,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Documents\\/Example.odt\"]','','[]','/Documents/Example.odt','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FDocuments','files',15),(5,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\"]','','[]','/Photos','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2F','files',16),(6,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\\/Squirrel.jpg\"]','','[]','/Photos/Squirrel.jpg','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',17),(7,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\\/San Francisco.jpg\"]','','[]','/Photos/San Francisco.jpg','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',18),(8,1456918806,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/Photos\\/Paris.jpg\"]','','[]','/Photos/Paris.jpg','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2FPhotos','files',19),(9,1456920501,30,'file_created','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483','files','created_self','[\"\\/home\\/test.txt\"]','','[]','/home/test.txt','https://mycloud.karoshi.testing.com/owncloud/index.php/apps/files?dir=%2Fhome','files',22);
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.1.3'),('activity','types','filesystem'),('backgroundjob','lastjob','5'),('core','installedat','1456918136.5882'),('core','lastcron','1456920943'),('core','lastupdateResult','{\"version\":{},\"versionstring\":{},\"url\":{},\"web\":{}}'),('core','lastupdatedat','1456920654'),('core','public_files','files_sharing/public.php'),('core','public_webdav','files_sharing/publicwebdav.php'),('core','remote_files','files/appinfo/remote.php'),('core','remote_webdav','files/appinfo/remote.php'),('core','shareapi_allow_resharing','no'),('files','enabled','yes'),('files','installed_version','1.2.0'),('files','types','filesystem'),('files_external','allow_user_mounting','no'),('files_external','enabled','yes'),('files_external','installed_version','0.3.0'),('files_external','ocsid','166048'),('files_external','types','filesystem'),('files_external','user_mounting_backends','ftp,dav,owncloud,sftp,amazons3,dropbox,googledrive,swift,smb,\\OC\\Files\\Storage\\SFTP_Key,\\OC\\Files\\Storage\\SMB_OC'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','0.7'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','0.7.0'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.0'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','0.7.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.1.0'),('files_versions','types','filesystem'),('files_videoviewer','enabled','yes'),('files_videoviewer','installed_version','0.1.3'),('files_videoviewer','ocsid','166054'),('files_videoviewer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','1.1'),('firstrunwizard','ocsid','166055'),('firstrunwizard','types',''),('gallery','enabled','yes'),('gallery','installed_version','14.2.0'),('gallery','types',''),('notifications','enabled','yes'),('notifications','installed_version','0.1.0'),('notifications','types','filesystem'),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','0.3.0'),('provisioning_api','types','filesystem'),('templateeditor','enabled','yes'),('templateeditor','installed_version','0.1'),('templateeditor','types',''),('updater','enabled','yes'),('updater','installed_version','0.6'),('updater','types',''),('user_ldap','cleanUpJobOffset','0'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','0.7.1'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr',''),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=organizationalPerson)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','1'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_user_filter_mode','1'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','organizationalPerson'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=organizationalPerson)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1');
/*!40000 ALTER TABLE `oc_appconfig` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (1,0,'files/a3594fd4eca7119cb937772e1f8f5415',1456921740),(2,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1456921740),(3,0,'files/a36e4eb9c7358bd02497aa960b1151a9',1456921740),(4,0,'files/2c7eaecb9090bd89cef1dcd4d0d5881a',1456921739),(5,0,'files/3513aba8aa4305d3ad33fc7122d4af30',1456921739),(6,0,'files/47b35dd91a203e06efeb4436117e4def',1456921739),(7,0,'files/37c85de42508b164a7d7f502df40796e',1456921739),(8,0,'files/173a67328b2dceac7a89367cdcc7b1b6',1456921739),(9,0,'files/7f472eca153e78ea7caaa6d969440cba',1456921739),(10,0,'files/0e69da27f6883fa212e7d953fcc0076c',1456922405),(11,0,'files/405085325cd22c61ce43a16697e7b900',1456922406),(12,0,'files/2265a7864cbb01fd760398e786dc9eee',1456922405),(13,0,'files/0a20e8bb7fca64b825f630f296210deb',1456922405),(14,0,'files/23aa47b4383e20346c5edd148bead939',1456922406),(15,0,'files/df0ede9cf6b602bb23bca0d3696b3858',1456922406),(16,0,'files/0d6e884bdb13e9a88889ca37284d55ca',1456922406),(17,0,'files/d12b2490f7a320727aed25c8f99a2626',1456922406),(18,0,'files/7557d79c922cee68bc4d4044420de676',1456922406),(19,0,'files/6d129869366263b5c55d27073db979a5',1456922406),(20,0,'files/7bdb4ac2fec2256440ebc76ae8ba44ba',1456922406),(21,0,'files/af844dd7d9509ac12ed00fc34d7cbc55',1456924101),(22,0,'files/bf59726a488dfa1c71cf9297b0490e28',1456924101);
/*!40000 ALTER TABLE `oc_file_locks` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,3259772,1456918822,1456918822,0,0,'56d6d12656f9f',23),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,3259772,1456918140,1456917896,0,0,'56d6ce7c1ae8a',31),(3,1,'files/ownCloud_User_Manual.pdf','fbaae4021d9c766fc309c54e81133013',2,'ownCloud_User_Manual.pdf',4,3,2544989,1456917896,1456917896,0,0,'c78980ae278b90e6110eda6a4dc6f295',27),(4,1,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',2,'Documents',2,1,36227,1456918140,1456917896,0,0,'56d6ce7c1cb79',31),(5,1,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',2,'Photos',2,1,678556,1456918140,1456917896,0,0,'56d6ce7c1bd7a',31),(6,1,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',5,'Squirrel.jpg',6,5,233724,1456917896,1456917896,0,0,'37f15b01feb4cedec8dbc52123cf2ba3',27),(7,1,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',5,'San Francisco.jpg',6,5,216071,1456917896,1456917896,0,0,'8960a33c741512a996988a308a14f3f7',27),(8,1,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',5,'Paris.jpg',6,5,228761,1456917896,1456917896,0,0,'77c3b5c61999e81299ffdc62539acc7d',27),(9,1,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',4,'Example.odt',7,3,36227,1456917896,1456917896,0,0,'80cd944a14ec31518ea2ac156902e706',27),(10,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,3259772,1456918806,1456918805,0,0,'56d6d11666336',23),(11,3,'cache','0fea6a13c52b4d4725368f24b045ca84',10,'cache',2,1,0,1456918805,1456918805,0,0,'56d6d1157c00d',31),(12,3,'files','45b963397aa40d4a0063e0d85e4fe7a1',10,'files',2,1,3259772,1456920501,1456918806,0,0,'56d6d7b5510f3',31),(13,3,'files/ownCloud_User_Manual.pdf','fbaae4021d9c766fc309c54e81133013',12,'ownCloud_User_Manual.pdf',4,3,2544989,1456918805,1456918805,0,0,'8af623094069ea4d8ac3224c53e45087',27),(14,3,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',12,'Documents',2,1,36227,1456918805,1456918805,0,0,'56d6d115f0a2e',31),(15,3,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',14,'Example.odt',7,3,36227,1456918806,1456918806,0,0,'b859bcb5612690ce134572e1fd540b62',27),(16,3,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',12,'Photos',2,1,678556,1456918806,1456918806,0,0,'56d6d116682f7',31),(17,3,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',16,'Squirrel.jpg',6,5,233724,1456918806,1456918806,0,0,'959059e80e056225ecde63b1668ea456',27),(18,3,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',16,'San Francisco.jpg',6,5,216071,1456918806,1456918806,0,0,'6c253191799e50a282124d1aba2a0a02',27),(19,3,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',16,'Paris.jpg',6,5,228761,1456918806,1456918806,0,0,'84b53d7c493a7bdfa3f3a9550db976e0',27),(20,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1456918822,1456918822,0,0,'56d6d12646338',31),(21,5,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,1456920501,1456920501,0,0,'56d6d7b553492',23),(22,5,'test.txt','dd18bf3a8e0a2a3e53e2661c7fb53534',21,'test.txt',9,8,0,1456920501,1456920501,0,0,'56d6d7b53aa6e',27);
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Files_sharing\\Lib\\DeleteOrphanedSharesJob','null',1456920472),(2,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1456920507),(3,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1456920656),(4,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1456918292),(5,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1456920943),(6,'OCA\\user_ldap\\lib\\Jobs','null',1456918808),(7,'\\OCA\\User_LDAP\\Jobs\\CleanUp','null',1456918818);
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
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=staff,ou=groups,ou=people,dc=karoshi,dc=testing,dc=com','staff','400C85D5-B809-4682-92E7-4E86B189037F');
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
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=guest7,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','0FBB66F4-04AC-4F70-99FB-FF01EE5C2396'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','332D3193-25CA-4137-9AE1-9DD6032E99D5','332D3193-25CA-4137-9AE1-9DD6032E99D5'),('cn=guest4,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','3683285D-531B-4AF9-97ED-F2194AF031DF','3683285D-531B-4AF9-97ED-F2194AF031DF'),('cn=guest10,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','36DD0503-E46E-403B-8D89-3AED69A27632','36DD0503-E46E-403B-8D89-3AED69A27632'),('cn=ismith,ou=staff,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','482DEFA3-C1CF-4348-9C1C-571396011483','482DEFA3-C1CF-4348-9C1C-571396011483'),('cn=tech3,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','4C68AA9A-0952-4200-98C1-7C43E7DFE8A1'),('cn=guest2,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','67B1FC51-5555-4297-ACD2-72E1EF6CF797','67B1FC51-5555-4297-ACD2-72E1EF6CF797'),('cn=tech2,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','711F7896-EB66-42BE-AD5C-DB5121693431','711F7896-EB66-42BE-AD5C-DB5121693431'),('cn=profileuser,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15'),('cn=tech4,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','BA79ED58-C2CD-4330-954A-FEC72FE230F5','BA79ED58-C2CD-4330-954A-FEC72FE230F5'),('cn=guest5,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','C713E05B-6633-4723-89C7-94F070C39D5B','C713E05B-6633-4723-89C7-94F070C39D5B'),('cn=tech1,ou=tech,ou=personnel,ou=people,dc=karoshi,dc=testing,dc=com','CBC82A9B-9A83-4232-A7E5-81C1C56B3822','CBC82A9B-9A83-4232-A7E5-81C1C56B3822'),('cn=guest1,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E'),('cn=guest6,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','E6EACADC-22BF-4349-B8D2-D41848C179B1','E6EACADC-22BF-4349-B8D2-D41848C179B1'),('cn=guest9,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','EF3BCD6A-1994-4091-8410-62DC8C7115C8','EF3BCD6A-1994-4091-8410-62DC8C7115C8'),('cn=guest3,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','F0E986F5-1066-42E4-A34F-7DD9D7C216F4','F0E986F5-1066-42E4-A34F-7DD9D7C216F4'),('cn=guest8,ou=guestusers,ou=other,ou=people,dc=karoshi,dc=testing,dc=com','FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','FE6FAF10-D0F4-4807-A73F-E91712CCBA0D');
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (3,'application'),(4,'application/pdf'),(7,'application/vnd.oasis.opendocument.text'),(1,'httpd'),(2,'httpd/unix-directory'),(5,'image'),(6,'image/jpeg'),(8,'text'),(9,'text/plain');
/*!40000 ALTER TABLE `oc_mimetypes` ENABLE KEYS */;
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
  `object_id` int(11) NOT NULL DEFAULT '0',
  `subject` varchar(64) COLLATE utf8_bin NOT NULL,
  `subject_parameters` longtext COLLATE utf8_bin,
  `message` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `message_parameters` longtext COLLATE utf8_bin,
  `link` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `icon` varchar(64) COLLATE utf8_bin DEFAULT NULL,
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
INSERT INTO `oc_preferences` VALUES ('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','displayName','Guest 7'),('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','lastFeatureRefresh','1456919491'),('0FBB66F4-04AC-4F70-99FB-FF01EE5C2396','user_ldap','uid','guest7'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','displayName','Sysadmin User'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','lastFeatureRefresh','1456919491'),('332D3193-25CA-4137-9AE1-9DD6032E99D5','user_ldap','uid','sysadmin'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','displayName','Guest 4'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','lastFeatureRefresh','1456919491'),('3683285D-531B-4AF9-97ED-F2194AF031DF','user_ldap','uid','guest4'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','displayName','Guest 10'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','lastFeatureRefresh','1456919491'),('36DD0503-E46E-403B-8D89-3AED69A27632','user_ldap','uid','guest10'),('482DEFA3-C1CF-4348-9C1C-571396011483','core','lang','en'),('482DEFA3-C1CF-4348-9C1C-571396011483','core','timezone','Europe/London'),('482DEFA3-C1CF-4348-9C1C-571396011483','firstrunwizard','show','0'),('482DEFA3-C1CF-4348-9C1C-571396011483','login','lastLogin','1456920470'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','displayName','Ian Smith'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','firstLoginAccomplished','1'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','homePath',''),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','lastFeatureRefresh','1456920470'),('482DEFA3-C1CF-4348-9C1C-571396011483','user_ldap','uid','ismith'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','displayName','Tech 3'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','lastFeatureRefresh','1456919491'),('4C68AA9A-0952-4200-98C1-7C43E7DFE8A1','user_ldap','uid','tech3'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','displayName','Guest 2'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','lastFeatureRefresh','1456919491'),('67B1FC51-5555-4297-ACD2-72E1EF6CF797','user_ldap','uid','guest2'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','displayName','Tech 2'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','lastFeatureRefresh','1456919491'),('711F7896-EB66-42BE-AD5C-DB5121693431','user_ldap','uid','tech2'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','displayName','Profile User'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','lastFeatureRefresh','1456919491'),('AD9E6ED5-26FA-4861-B3A0-5F1209FCAC15','user_ldap','uid','profileuser'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','displayName','Tech 4'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','lastFeatureRefresh','1456919491'),('BA79ED58-C2CD-4330-954A-FEC72FE230F5','user_ldap','uid','tech4'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','displayName','Guest 5'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','lastFeatureRefresh','1456919491'),('C713E05B-6633-4723-89C7-94F070C39D5B','user_ldap','uid','guest5'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','displayName','Tech 1'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','lastFeatureRefresh','1456919491'),('CBC82A9B-9A83-4232-A7E5-81C1C56B3822','user_ldap','uid','tech1'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','displayName','Guest 1'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','lastFeatureRefresh','1456919491'),('DBF8E78B-993F-45A3-8DCE-38E93FBD9C4E','user_ldap','uid','guest1'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','displayName','Guest 6'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','lastFeatureRefresh','1456919491'),('E6EACADC-22BF-4349-B8D2-D41848C179B1','user_ldap','uid','guest6'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','displayName','Guest 9'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','lastFeatureRefresh','1456919491'),('EF3BCD6A-1994-4091-8410-62DC8C7115C8','user_ldap','uid','guest9'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','displayName','Guest 3'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','lastFeatureRefresh','1456919491'),('F0E986F5-1066-42E4-A34F-7DD9D7C216F4','user_ldap','uid','guest3'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','displayName','Guest 8'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','lastFeatureRefresh','1456919491'),('FE6FAF10-D0F4-4807-A73F-E91712CCBA0D','user_ldap','uid','guest8'),('admin','core','lang','en'),('admin','core','timezone','Europe/London'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1456920654');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('home::admin',1,1,NULL),('local::/home/owncloud/data/',2,1,NULL),('home::482DEFA3-C1CF-4348-9C1C-571396011483',3,1,NULL),('smb::admin@bertie.karoshi.testing.com//admin//',4,0,1456920665),('smb::ismith@bertie.karoshi.testing.com//ismith//',5,1,NULL);
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

-- Dump completed on 2016-03-02 12:17:54
