-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: nextcloud
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.1

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
-- Table structure for table `oc_accounts`
--

DROP TABLE IF EXISTS `oc_accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_accounts` (
  `uid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `data` longtext COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_accounts`
--

LOCK TABLES `oc_accounts` WRITE;
/*!40000 ALTER TABLE `oc_accounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_accounts` ENABLE KEYS */;
UNLOCK TABLES;

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
  `app` varchar(32) COLLATE utf8_bin NOT NULL,
  `subject` varchar(255) COLLATE utf8_bin NOT NULL,
  `subjectparams` longtext COLLATE utf8_bin NOT NULL,
  `message` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `messageparams` longtext COLLATE utf8_bin,
  `file` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `link` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `object_type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `object_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`activity_id`),
  KEY `activity_time` (`timestamp`),
  KEY `activity_user_time` (`affecteduser`,`timestamp`),
  KEY `activity_filter_by` (`affecteduser`,`user`,`timestamp`),
  KEY `activity_filter_app` (`affecteduser`,`app`,`timestamp`),
  KEY `activity_object` (`object_type`,`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity`
--

LOCK TABLES `oc_activity` WRITE;
/*!40000 ALTER TABLE `oc_activity` DISABLE KEYS */;
INSERT INTO `oc_activity` VALUES (1,1485536381,30,'file_created','admin','admin','files','created_self','[{\"2\":\"\"}]','','[]','','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=','files',2),(2,1485536381,30,'file_created','admin','admin','files','created_self','[{\"3\":\"\\/Nextcloud.mp4\"}]','','[]','/Nextcloud.mp4','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',3),(3,1485536381,30,'file_created','admin','admin','files','created_self','[{\"7\":\"\\/Photos\"}]','','[]','/Photos','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',7),(4,1485536381,30,'file_created','admin','admin','files','created_self','[{\"8\":\"\\/Photos\\/Nut.jpg\"}]','','[]','/Photos/Nut.jpg','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Photos','files',8),(5,1485536381,30,'file_created','admin','admin','files','created_self','[{\"9\":\"\\/Photos\\/Hummingbird.jpg\"}]','','[]','/Photos/Hummingbird.jpg','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Photos','files',9),(6,1485536381,30,'file_created','admin','admin','files','created_self','[{\"10\":\"\\/Photos\\/Coast.jpg\"}]','','[]','/Photos/Coast.jpg','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Photos','files',10),(7,1485536382,30,'file_created','admin','admin','files','created_self','[{\"11\":\"\\/Documents\"}]','','[]','/Documents','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',11),(8,1485536382,30,'file_created','admin','admin','files','created_self','[{\"12\":\"\\/Documents\\/About.txt\"}]','','[]','/Documents/About.txt','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Documents','files',12),(9,1485536382,30,'file_created','admin','admin','files','created_self','[{\"13\":\"\\/Documents\\/About.odt\"}]','','[]','/Documents/About.odt','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Documents','files',13),(10,1485536382,30,'file_created','admin','admin','files','created_self','[{\"14\":\"\\/Nextcloud Manual.pdf\"}]','','[]','/Nextcloud Manual.pdf','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',14),(11,1485536382,30,'calendar','admin','admin','dav','calendar_add_self','[\"admin\",\"Personal\"]','','[]','','','calendar',1);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbookchanges`
--

LOCK TABLES `oc_addressbookchanges` WRITE;
/*!40000 ALTER TABLE `oc_addressbookchanges` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbooks`
--

LOCK TABLES `oc_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_addressbooks` VALUES (1,'principals/users/admin','Contacts','contacts',NULL,1);
/*!40000 ALTER TABLE `oc_addressbooks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_admin_sections`
--

DROP TABLE IF EXISTS `oc_admin_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_admin_sections` (
  `id` varchar(64) COLLATE utf8_bin NOT NULL,
  `class` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `priority` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_sections_class` (`class`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_admin_sections`
--

LOCK TABLES `oc_admin_sections` WRITE;
/*!40000 ALTER TABLE `oc_admin_sections` DISABLE KEYS */;
INSERT INTO `oc_admin_sections` VALUES ('externalstorages','OCA\\Files_External\\Settings\\Section',10),('ldap','OCA\\User_LDAP\\Settings\\Section',25),('logging','OCA\\LogReader\\Settings\\Section',90),('richdocuments','OCA\\Richdocuments\\Settings\\Section',75),('serverinfo','OCA\\ServerInfo\\Settings\\AdminSection',0),('survey_client','OCA\\Survey_Client\\Settings\\AdminSection',80),('theming','OCA\\Theming\\Settings\\Section',30),('workflow','OCA\\WorkflowEngine\\Settings\\Section',55);
/*!40000 ALTER TABLE `oc_admin_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_admin_settings`
--

DROP TABLE IF EXISTS `oc_admin_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_admin_settings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `section` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `priority` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_settings_class` (`class`),
  KEY `admin_settings_section` (`section`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_admin_settings`
--

LOCK TABLES `oc_admin_settings` WRITE;
/*!40000 ALTER TABLE `oc_admin_settings` DISABLE KEYS */;
INSERT INTO `oc_admin_settings` VALUES (1,'OCA\\Federation\\Settings\\Admin','sharing',30),(2,'OCA\\ServerInfo\\Settings\\AdminSettings','serverinfo',0),(3,'OCA\\LogReader\\Settings\\Admin','logging',90),(4,'OCA\\FederatedFileSharing\\Settings\\Admin','sharing',20),(5,'OCA\\Theming\\Settings\\Admin','theming',5),(6,'OCA\\Survey_Client\\Settings\\AdminSettings','survey_client',50),(7,'OCA\\UpdateNotification\\Controller\\AdminController','server',1),(8,'OCA\\NextcloudAnnouncements\\Settings\\Admin','additional',30),(9,'OCA\\SystemTags\\Settings\\Admin','workflow',70),(10,'OCA\\Files\\Settings\\Admin','additional',5),(11,'OCA\\User_LDAP\\Settings\\Admin','ldap',5),(12,'OCA\\Files_External\\Settings\\Admin','externalstorages',40),(13,'OCA\\Richdocuments\\Settings\\Admin','richdocuments',0);
/*!40000 ALTER TABLE `oc_admin_settings` ENABLE KEYS */;
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.4.1'),('activity','types','filesystem'),('backgroundjob','lastjob','7'),('comments','enabled','yes'),('comments','installed_version','1.1.0'),('comments','types','logging'),('core','installedat','1485536380.8184'),('core','lastcron','1485597009'),('core','lastupdateResult','[]'),('core','lastupdatedat','1485596890'),('core','oc.integritycheck.checker','[]'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('dav','enabled','yes'),('dav','installed_version','1.1.1'),('dav','types','filesystem'),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','1.1.1'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','1.1.1'),('federation','types','authentication'),('files','enabled','yes'),('files','installed_version','1.6.1'),('files','types','filesystem'),('files_external','enabled','yes'),('files_external','installed_version','1.1.2'),('files_external','types','filesystem'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','1.0.1'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_reader','enabled','yes'),('files_reader','installed_version','0.8.1'),('files_reader','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','1.1.1'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.2'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','1.1.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.4.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','1.0.0'),('files_videoplayer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','2.0'),('firstrunwizard','types','logging'),('gallery','enabled','yes'),('gallery','installed_version','16.0.0'),('gallery','types',''),('logreader','enabled','yes'),('logreader','installed_version','2.0.0'),('logreader','ocsid','170871'),('logreader','types',''),('lookup_server_connector','enabled','yes'),('lookup_server_connector','installed_version','1.0.0'),('lookup_server_connector','types','authentication'),('nextcloud_announcements','enabled','yes'),('nextcloud_announcements','installed_version','1.0'),('nextcloud_announcements','types','logging'),('notes','enabled','yes'),('notes','installed_version','2.2.0'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','1.0.1'),('notifications','types','logging'),('password_policy','enabled','yes'),('password_policy','installed_version','1.1.0'),('password_policy','types',''),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','1.1.0'),('provisioning_api','types','prevent_group_restriction'),('richdocuments','enabled','yes'),('richdocuments','installed_version','1.1.25'),('richdocuments','types','prevent_group_restriction'),('richdocuments','wopi_url','https://CHANGETHISREALM'),('serverinfo','enabled','yes'),('serverinfo','installed_version','1.1.1'),('serverinfo','types',''),('sharebymail','enabled','yes'),('sharebymail','installed_version','1.0.1'),('sharebymail','types','filesystem'),('survey_client','enabled','yes'),('survey_client','installed_version','0.1.5'),('survey_client','types',''),('systemtags','enabled','yes'),('systemtags','installed_version','1.1.3'),('systemtags','types','logging'),('theming','enabled','yes'),('theming','installed_version','1.1.1'),('theming','types','logging'),('twofactor_backupcodes','enabled','yes'),('twofactor_backupcodes','installed_version','1.0.0'),('twofactor_backupcodes','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','1.1.1'),('updatenotification','types',''),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','1.1.1'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr','sAMAccountName'),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=person)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_turn_on_pwd_change','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','posixAccount'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=posixAccount)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1'),('workflowengine','enabled','yes'),('workflowengine','installed_version','1.1.1'),('workflowengine','types','filesystem');
/*!40000 ALTER TABLE `oc_appconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_authtoken`
--

DROP TABLE IF EXISTS `oc_authtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_authtoken` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `login_name` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `password` longtext COLLATE utf8_bin,
  `name` longtext COLLATE utf8_bin NOT NULL,
  `token` varchar(200) COLLATE utf8_bin NOT NULL DEFAULT '',
  `type` smallint(5) unsigned NOT NULL DEFAULT '0',
  `remember` smallint(5) unsigned NOT NULL DEFAULT '0',
  `last_activity` int(10) unsigned NOT NULL DEFAULT '0',
  `last_check` int(10) unsigned NOT NULL DEFAULT '0',
  `scope` longtext COLLATE utf8_bin,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authtoken_token_index` (`token`),
  KEY `authtoken_last_activity_index` (`last_activity`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_authtoken`
--

LOCK TABLES `oc_authtoken` WRITE;
/*!40000 ALTER TABLE `oc_authtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_authtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_bruteforce_attempts`
--

DROP TABLE IF EXISTS `oc_bruteforce_attempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_bruteforce_attempts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `action` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `occurred` int(10) unsigned NOT NULL DEFAULT '0',
  `ip` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `subnet` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `metadata` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `bruteforce_attempts_ip` (`ip`),
  KEY `bruteforce_attempts_subnet` (`subnet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_bruteforce_attempts`
--

LOCK TABLES `oc_bruteforce_attempts` WRITE;
/*!40000 ALTER TABLE `oc_bruteforce_attempts` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_bruteforce_attempts` ENABLE KEYS */;
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
  `componenttype` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  `firstoccurence` bigint(20) unsigned DEFAULT NULL,
  `lastoccurence` bigint(20) unsigned DEFAULT NULL,
  `uid` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `classification` int(11) DEFAULT '0' COMMENT '0 - public, 1 - private, 2 - confidential',
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
  `components` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `transparent` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `calendars_index` (`principaluri`,`uri`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendars`
--

LOCK TABLES `oc_calendars` WRITE;
/*!40000 ALTER TABLE `oc_calendars` DISABLE KEYS */;
INSERT INTO `oc_calendars` VALUES (1,'principals/users/admin','Personal','personal',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards`
--

LOCK TABLES `oc_cards` WRITE;
/*!40000 ALTER TABLE `oc_cards` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards_properties`
--

LOCK TABLES `oc_cards_properties` WRITE;
/*!40000 ALTER TABLE `oc_cards_properties` DISABLE KEYS */;
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
  `publicuri` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dav_shares_index` (`principaluri`,`resourceid`,`type`,`publicuri`)
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_applicable`
--

LOCK TABLES `oc_external_applicable` WRITE;
/*!40000 ALTER TABLE `oc_external_applicable` DISABLE KEYS */;
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
  `value` varchar(4096) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`config_id`),
  UNIQUE KEY `config_mount_key` (`mount_id`,`key`),
  KEY `config_mount` (`mount_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_config`
--

LOCK TABLES `oc_external_config` WRITE;
/*!40000 ALTER TABLE `oc_external_config` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_mounts`
--

LOCK TABLES `oc_external_mounts` WRITE;
/*!40000 ALTER TABLE `oc_external_mounts` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_options`
--

LOCK TABLES `oc_external_options` WRITE;
/*!40000 ALTER TABLE `oc_external_options` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_external_options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_federated_reshares`
--

DROP TABLE IF EXISTS `oc_federated_reshares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_federated_reshares` (
  `share_id` int(11) NOT NULL,
  `remote_id` int(11) NOT NULL COMMENT 'share ID at the remote server',
  UNIQUE KEY `share_id_index` (`share_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_federated_reshares`
--

LOCK TABLES `oc_federated_reshares` WRITE;
/*!40000 ALTER TABLE `oc_federated_reshares` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_federated_reshares` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (1,0,'files/468c740695b998c9b920835b3af18225',1485539986),(2,0,'files/3ef927705e35f104f5c8825610e550db',1485539999),(3,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1485539986),(4,0,'files/bc76dde1a029b9698a1164dc9d6f4422',1485539999);
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,7074735,1485536382,1485536381,0,0,'588b7c7e1fca3',23,''),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,7074735,1485536382,1485536382,0,0,'588b7c7e1c615',31,''),(3,1,'files/Nextcloud.mp4','77a79c09b93e57cba23c11eb0e6048a6',2,'Nextcloud.mp4',4,3,462413,1485536381,1485536381,0,0,'2e0c6f035652f7ec29d5958b4d90fde1',27,''),(4,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1485596908,1485536399,0,0,'588c68ecc2bdf',23,''),(5,3,'appdata_ocll5awmjb7q','e7a8a61323a5dca2ede2cbe9c5cb7bbc',4,'appdata_ocll5awmjb7q',2,1,183135,1485596908,1485536412,0,0,'588c68ecc2bdf',31,''),(6,3,'appdata_ocll5awmjb7q/preview','2cea38b94d1285578586b5cc14b5a347',5,'preview',2,1,0,1485536381,1485536381,0,0,'588b7c7dcac41',31,''),(7,1,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',2,'Photos',2,1,2360011,1485536381,1485536381,0,0,'588b7c7df1166',31,''),(8,1,'files/Photos/Nut.jpg','aa8daeb975e1d39412954fd5cd41adb4',7,'Nut.jpg',6,5,955026,1485536381,1485536381,0,0,'1ed8bdc1f6c252ec7919cd0f3cd9a2f6',27,''),(9,1,'files/Photos/Hummingbird.jpg','e077463269c404ae0f6f8ea7f2d7a326',7,'Hummingbird.jpg',6,5,585219,1485536381,1485536381,0,0,'7d97a07608c81805c42b0a073b7c870e',27,''),(10,1,'files/Photos/Coast.jpg','a6fe87299d78b207e9b7aba0f0cb8a0a',7,'Coast.jpg',6,5,819766,1485536382,1485536382,0,0,'96570532ff5c2c31c2a19894f2100869',27,''),(11,1,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',2,'Documents',2,1,78496,1485536382,1485536382,0,0,'588b7c7e14bf5',31,''),(12,1,'files/Documents/About.txt','9da7b739e7a65d74793b2881da521169',11,'About.txt',8,7,1074,1485536382,1485536382,0,0,'81f0f098ceab77b31b34ae011daa7edb',27,''),(13,1,'files/Documents/About.odt','b2ee7d56df9f34a0195d4b611376e885',11,'About.odt',10,9,77422,1485536382,1485536382,0,0,'483a2ec102c031cc5ee0f1cbca1fc9f0',27,''),(14,1,'files/Nextcloud Manual.pdf','2bc58a43566a8edde804a4a97a9c7469',2,'Nextcloud Manual.pdf',11,9,4173815,1485536382,1485536382,0,0,'77f87781841d789a7de2e7fceeaba571',27,''),(15,3,'appdata_ocll5awmjb7q/avatar','3ba2a1f8dae2d92bb188e5f04d81f384',5,'avatar',2,1,0,1485536384,1485536384,0,0,'588b7c809c846',31,''),(16,3,'appdata_ocll5awmjb7q/avatar/admin','f814e8679325f67adbe104542afb0d51',15,'admin',2,1,0,1485536384,1485536384,0,0,'588b7c809aa0f',31,''),(17,3,'appdata_ocll5awmjb7q/theming','3e18ef4914086f27159792884373e207',5,'theming',2,1,2117,1485536388,1485536388,0,0,'588b7c84a926b',31,''),(18,3,'appdata_ocll5awmjb7q/theming/0','344e998ce0e8878359748028a1db4ae6',17,'0',2,1,2117,1485536388,1485536388,0,0,'588b7c84a926b',31,''),(19,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_folder.svg','34598e545dd2228f6b91a229c698d807',18,'icon-core-filetypes_folder.svg',12,5,254,1485536388,1485536388,0,0,'5367e1366ec8cacaca54a3b2c4e82c55',27,''),(20,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_video.svg','98d9e39165989a3d076a962b447c8bb7',18,'icon-core-filetypes_video.svg',12,5,328,1485536388,1485536388,0,0,'d6952fced18acbb9df9d2e4325a6259b',27,''),(21,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_application-pdf.svg','ab4efc1fac68882bbceadde19af542df',18,'icon-core-filetypes_application-pdf.svg',12,5,1535,1485536388,1485536388,0,0,'e872d2b15ec22c71eb95bdc1b0cb963d',27,''),(22,3,'files_external','c270928b685e7946199afdfb898d27ea',4,'files_external',2,1,0,1485536399,1485536399,0,0,'588b7c8f76148',31,''),(23,3,'appdata_ocll5awmjb7q/appstore','a50221ec28c7669b947e8a7c718800f8',5,'appstore',2,1,181018,1485596908,1485536413,0,0,'588c68ecc2bdf',31,''),(24,3,'appdata_ocll5awmjb7q/appstore/apps.json','0ddc045c916e17c7cae94638e0fd98fb',23,'apps.json',13,9,156803,1485596908,1485596908,0,0,'3e763404747f8de72d4f1a6c0032a892',27,''),(25,3,'appdata_ocll5awmjb7q/appstore/categories.json','b213cc26ba8b8058df581e5d83c5b6ec',23,'categories.json',13,9,24215,1485596908,1485596908,0,0,'d83b19a6557c0bfb0838cf9c68965183',27,'');
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
-- Table structure for table `oc_flow_checks`
--

DROP TABLE IF EXISTS `oc_flow_checks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_flow_checks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(256) COLLATE utf8_bin NOT NULL,
  `operator` varchar(16) COLLATE utf8_bin NOT NULL,
  `value` longtext COLLATE utf8_bin,
  `hash` varchar(32) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flow_unique_hash` (`hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_flow_checks`
--

LOCK TABLES `oc_flow_checks` WRITE;
/*!40000 ALTER TABLE `oc_flow_checks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_flow_checks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_flow_operations`
--

DROP TABLE IF EXISTS `oc_flow_operations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_flow_operations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(256) COLLATE utf8_bin NOT NULL,
  `name` varchar(256) COLLATE utf8_bin NOT NULL,
  `checks` longtext COLLATE utf8_bin,
  `operation` longtext COLLATE utf8_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_flow_operations`
--

LOCK TABLES `oc_flow_operations` WRITE;
/*!40000 ALTER TABLE `oc_flow_operations` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_flow_operations` ENABLE KEYS */;
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
  `last_checked` int(11) DEFAULT '0',
  `reserved_at` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `job_class_index` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Federation\\SyncJob','null',1485536386,1485536386,0),(2,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1485536399,1485536399,0),(4,'OCA\\UpdateNotification\\Notification\\BackgroundJob','null',1485536497,1485536497,0),(5,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1485536500,1485536500,0),(6,'OCA\\Files_Sharing\\DeleteOrphanedSharesJob','null',1485596907,1485596907,0),(7,'OCA\\Files_Sharing\\ExpireSharesJob','null',1485597009,1485597009,0),(8,'OCA\\NextcloudAnnouncements\\Cron\\Crawler','null',0,1485536381,0),(9,'OCA\\DAV\\CardDAV\\SyncJob','null',0,1485536381,0),(10,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',0,1485536381,0),(11,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',0,1485536381,0),(12,'OCA\\Files\\BackgroundJob\\ScanFiles','null',0,1485536381,0),(13,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',0,1485536381,0),(14,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',0,1485536381,0),(15,'\\OC\\Authentication\\Token\\DefaultTokenCleanupJob','null',0,1485536381,0),(16,'OCA\\FirstRunWizard\\Notification\\BackgroundJob','{\"uid\":\"admin\"}',0,1485536384,0),(17,'OCA\\User_LDAP\\Jobs\\UpdateGroups','null',0,1485536435,0),(18,'OCA\\User_LDAP\\Jobs\\CleanUp','null',0,1485536435,0);
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
INSERT INTO `oc_mimetypes` VALUES (9,'application'),(13,'application/json'),(11,'application/pdf'),(10,'application/vnd.oasis.opendocument.text'),(1,'httpd'),(2,'httpd/unix-directory'),(5,'image'),(6,'image/jpeg'),(12,'image/svg+xml'),(7,'text'),(8,'text/plain'),(3,'video'),(4,'video/mp4');
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
  `mount_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mounts_user_root_index` (`user_id`,`root_id`),
  KEY `mounts_user_index` (`user_id`),
  KEY `mounts_storage_index` (`storage_id`),
  KEY `mounts_root_index` (`root_id`),
  KEY `mounts_mount_id_index` (`mount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mounts`
--

LOCK TABLES `oc_mounts` WRITE;
/*!40000 ALTER TABLE `oc_mounts` DISABLE KEYS */;
INSERT INTO `oc_mounts` VALUES (1,1,1,'admin','/admin/',NULL);
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
  `icon` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `actions` longtext COLLATE utf8_bin,
  PRIMARY KEY (`notification_id`),
  KEY `oc_notifications_app` (`app`),
  KEY `oc_notifications_user` (`user`),
  KEY `oc_notifications_timestamp` (`timestamp`),
  KEY `oc_notifications_object` (`object_type`,`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_notifications`
--

LOCK TABLES `oc_notifications` WRITE;
/*!40000 ALTER TABLE `oc_notifications` DISABLE KEYS */;
INSERT INTO `oc_notifications` VALUES (1,'survey_client','admin',1485536412,'dummy','23','updated','[]','','[]','','','[{\"label\":\"enable\",\"link\":\"https:\\/\\/www.constellations.com\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"POST\",\"primary\":true},{\"label\":\"disable\",\"link\":\"https:\\/\\/www.constellations.com\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"DELETE\",\"primary\":false}]');
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
INSERT INTO `oc_preferences` VALUES ('admin','core','lang','en'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1485536381');
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
-- Table structure for table `oc_richdocuments_member`
--

DROP TABLE IF EXISTS `oc_richdocuments_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_richdocuments_member` (
  `member_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Unique per user and session',
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
-- Dumping data for table `oc_richdocuments_member`
--

LOCK TABLES `oc_richdocuments_member` WRITE;
/*!40000 ALTER TABLE `oc_richdocuments_member` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_richdocuments_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_richdocuments_wopi`
--

DROP TABLE IF EXISTS `oc_richdocuments_wopi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_richdocuments_wopi` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `owner_uid` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `editor_uid` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `fileid` int(11) NOT NULL,
  `version` int(11) NOT NULL DEFAULT '0',
  `canwrite` tinyint(1) NOT NULL DEFAULT '0',
  `server_host` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT 'localhost',
  `token` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `expiry` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `richdocuments_wopi_token_idx` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_richdocuments_wopi`
--

LOCK TABLES `oc_richdocuments_wopi` WRITE;
/*!40000 ALTER TABLE `oc_richdocuments_wopi` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_richdocuments_wopi` ENABLE KEYS */;
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
  `uid_initiator` varchar(64) COLLATE utf8_bin DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('home::admin',1,1,NULL),('1',2,1,NULL),('local::/home/nextcloud/data/',3,1,NULL);
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
-- Table structure for table `oc_systemtag_group`
--

DROP TABLE IF EXISTS `oc_systemtag_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_systemtag_group` (
  `systemtagid` int(10) unsigned NOT NULL DEFAULT '0',
  `gid` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`gid`,`systemtagid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_systemtag_group`
--

LOCK TABLES `oc_systemtag_group` WRITE;
/*!40000 ALTER TABLE `oc_systemtag_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_systemtag_group` ENABLE KEYS */;
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
-- Table structure for table `oc_twofactor_backup_codes`
--

DROP TABLE IF EXISTS `oc_twofactor_backup_codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_twofactor_backup_codes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `code` varchar(64) COLLATE utf8_bin NOT NULL,
  `used` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `two_factor_backupcodes_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_twofactor_backup_codes`
--

LOCK TABLES `oc_twofactor_backup_codes` WRITE;
/*!40000 ALTER TABLE `oc_twofactor_backup_codes` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_twofactor_backup_codes` ENABLE KEYS */;
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
INSERT INTO `oc_users` VALUES ('admin',NULL,'1|$2y$10$mPB/dWaNshvvpAUyuV8QYOmQiM0N.l9xY.R3IFgNtcv8qArSWhUBC');
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

-- Dump completed on 2017-01-28  9:53:57
