-- MySQL dump 10.13  Distrib 5.7.18, for Linux (x86_64)
--
-- Host: localhost    Database: nextcloud
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1

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
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `data` longtext COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_accounts`
--

LOCK TABLES `oc_accounts` WRITE;
/*!40000 ALTER TABLE `oc_accounts` DISABLE KEYS */;
INSERT INTO `oc_accounts` VALUES ('admin','{\"displayname\":{\"value\":\"admin\",\"scope\":\"contacts\",\"verified\":\"0\"},\"address\":{\"value\":\"\",\"scope\":\"private\",\"verified\":\"0\"},\"website\":{\"value\":\"\",\"scope\":\"private\",\"verified\":\"0\"},\"email\":{\"value\":null,\"scope\":\"contacts\",\"verified\":\"0\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\",\"verified\":\"0\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\",\"verified\":\"0\"}}');
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
  `type` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `user` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `affecteduser` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `app` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  `subject` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `subjectparams` longtext COLLATE utf8mb4_bin NOT NULL,
  `message` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `messageparams` longtext COLLATE utf8mb4_bin,
  `file` varchar(4000) COLLATE utf8mb4_bin DEFAULT NULL,
  `link` varchar(4000) COLLATE utf8mb4_bin DEFAULT NULL,
  `object_type` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `object_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`activity_id`),
  KEY `activity_time` (`timestamp`),
  KEY `activity_user_time` (`affecteduser`,`timestamp`),
  KEY `activity_filter_by` (`affecteduser`,`user`,`timestamp`),
  KEY `activity_filter_app` (`affecteduser`,`app`,`timestamp`),
  KEY `activity_object` (`object_type`,`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity`
--

LOCK TABLES `oc_activity` WRITE;
/*!40000 ALTER TABLE `oc_activity` DISABLE KEYS */;
INSERT INTO `oc_activity` VALUES (1,1497011838,30,'calendar','system','system','dav','calendar_add_self','[\"system\",\"Contact birthdays\"]','','[]','','','calendar',1);
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
  `amq_type` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `amq_affecteduser` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `amq_appid` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `amq_subject` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `amq_subjectparams` varchar(4000) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`mail_id`),
  KEY `amp_user` (`amq_affecteduser`),
  KEY `amp_latest_send_time` (`amq_latest_send`),
  KEY `amp_timestamp_time` (`amq_timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  `addressbookid` int(11) NOT NULL,
  `operation` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `addressbookid_synctoken` (`addressbookid`,`synctoken`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbookchanges`
--

LOCK TABLES `oc_addressbookchanges` WRITE;
/*!40000 ALTER TABLE `oc_addressbookchanges` DISABLE KEYS */;
INSERT INTO `oc_addressbookchanges` VALUES (1,'Database:admin.vcf',1,1,1);
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
  `principaluri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `displayname` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `description` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `addressbook_index` (`principaluri`,`uri`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbooks`
--

LOCK TABLES `oc_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_addressbooks` VALUES (1,'principals/system/system','system','system','System addressbook which holds all users of this instance',2);
/*!40000 ALTER TABLE `oc_addressbooks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_admin_sections`
--

DROP TABLE IF EXISTS `oc_admin_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_admin_sections` (
  `id` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `priority` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_sections_class` (`class`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_admin_sections`
--

LOCK TABLES `oc_admin_sections` WRITE;
/*!40000 ALTER TABLE `oc_admin_sections` DISABLE KEYS */;
INSERT INTO `oc_admin_sections` VALUES ('activity','OCA\\Activity\\Settings\\Section',55),('externalstorages','OCA\\Files_External\\Settings\\Section',10),('ldap','OCA\\User_LDAP\\Settings\\Section',25),('logging','OCA\\LogReader\\Settings\\Section',90),('richdocuments','OCA\\Richdocuments\\Settings\\Section',75),('serverinfo','OCA\\ServerInfo\\Settings\\AdminSection',0),('survey_client','OCA\\Survey_Client\\Settings\\AdminSection',80),('theming','OCA\\Theming\\Settings\\Section',30),('workflow','OCA\\WorkflowEngine\\Settings\\Section',55);
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
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `section` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `priority` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_settings_class` (`class`),
  KEY `admin_settings_section` (`section`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_admin_settings`
--

LOCK TABLES `oc_admin_settings` WRITE;
/*!40000 ALTER TABLE `oc_admin_settings` DISABLE KEYS */;
INSERT INTO `oc_admin_settings` VALUES (1,'OCA\\Theming\\Settings\\Admin','theming',5),(2,'OCA\\UpdateNotification\\Controller\\AdminController','server',1),(3,'OCA\\Survey_Client\\Settings\\AdminSettings','survey_client',50),(4,'OCA\\Files\\Settings\\Admin','additional',5),(5,'OCA\\Federation\\Settings\\Admin','sharing',30),(6,'OCA\\ServerInfo\\Settings\\AdminSettings','serverinfo',0),(7,'OCA\\Password_Policy\\Settings','security',50),(8,'OCA\\FederatedFileSharing\\Settings\\Admin','sharing',20),(9,'OCA\\OAuth2\\Settings\\Admin','security',0),(10,'OCA\\ShareByMail\\Settings\\Admin','sharing',40),(11,'OCA\\LogReader\\Settings\\Admin','logging',90),(12,'OCA\\Activity\\Settings\\Admin','activity',55),(13,'OCA\\NextcloudAnnouncements\\Settings\\Admin','additional',30),(14,'OCA\\SystemTags\\Settings\\Admin','workflow',70),(15,'OCA\\BruteForceSettings\\Settings\\IPWhitelist','security',50),(16,'OCA\\Files_External\\Settings\\Admin','externalstorages',40),(17,'OCA\\User_LDAP\\Settings\\Admin','ldap',5),(18,'OCA\\Richdocuments\\Settings\\Admin','richdocuments',0),(20,'OCA\\Drawio\\AdminSettings','server',60);
/*!40000 ALTER TABLE `oc_admin_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_appconfig`
--

DROP TABLE IF EXISTS `oc_appconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_appconfig` (
  `appid` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `configkey` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `configvalue` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`appid`,`configkey`),
  KEY `appconfig_config_key_index` (`configkey`),
  KEY `appconfig_appid_key` (`appid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_appconfig`
--

LOCK TABLES `oc_appconfig` WRITE;
/*!40000 ALTER TABLE `oc_appconfig` DISABLE KEYS */;
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.5.2'),('activity','types','filesystem'),('backgroundjob','lastjob','10'),('bookmarks','enabled','yes'),('bookmarks','installed_version','0.10.0'),('bookmarks','types',''),('bruteforcesettings','enabled','yes'),('bruteforcesettings','installed_version','1.0.2'),('bruteforcesettings','types',''),('calendar','enabled','yes'),('calendar','installed_version','1.5.3'),('calendar','types',''),('comments','enabled','yes'),('comments','installed_version','1.2.0'),('comments','types','logging'),('core','installed.bundles','[\"CoreBundle\"]'),('core','installedat','1497011141.6814'),('core','lastcron','1497017536'),('core','lastupdateResult','[]'),('core','lastupdatedat','1497015780'),('core','oc.integritycheck.checker','[]'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('core','scss.variables','3566bc1e0f55c1f422c50b3255478fd7'),('core','vendor','nextcloud'),('dav','enabled','yes'),('dav','installed_version','1.3.0'),('dav','types','filesystem'),('deck','enabled','yes'),('deck','installed_version','0.1.4'),('deck','types',''),('drawio','enabled','yes'),('drawio','installed_version','0.8.8'),('drawio','types','filesystem'),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','1.2.0'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','1.2.0'),('federation','types','authentication'),('files','cronjob_scan_files','500'),('files','enabled','yes'),('files','installed_version','1.7.2'),('files','types','filesystem'),('files_external','enabled','yes'),('files_external','installed_version','1.3.0'),('files_external','types','filesystem'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','1.1.1'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_reader','enabled','yes'),('files_reader','installed_version','1.0.4'),('files_reader','types','filesystem'),('files_sharing','enabled','yes'),('files_sharing','installed_version','1.4.0'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.4.1'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','1.2.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.5.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','1.1.0'),('files_videoplayer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','2.1'),('firstrunwizard','types','logging'),('gallery','enabled','yes'),('gallery','installed_version','17.0.0'),('gallery','types',''),('logreader','enabled','yes'),('logreader','installed_version','2.0.0'),('logreader','ocsid','170871'),('logreader','types',''),('lookup_server_connector','enabled','yes'),('lookup_server_connector','installed_version','1.0.0'),('lookup_server_connector','types','authentication'),('nextcloud_announcements','enabled','yes'),('nextcloud_announcements','installed_version','1.1'),('nextcloud_announcements','pub_date','Sat, 10 Dec 2016 00:00:00 +0100'),('nextcloud_announcements','types','logging'),('notes','enabled','yes'),('notes','installed_version','2.2.0'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','2.0.0'),('notifications','types','logging'),('oauth2','enabled','yes'),('oauth2','installed_version','1.0.5'),('oauth2','types','authentication'),('password_policy','enabled','yes'),('password_policy','installed_version','1.2.2'),('password_policy','types',''),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','1.2.0'),('provisioning_api','types','prevent_group_restriction'),('richdocuments','enabled','yes'),('richdocuments','installed_version','1.12.32'),('richdocuments','types','prevent_group_restriction'),('richdocuments','wopi_url','https://CHANGETHISREALM'),('serverinfo','enabled','yes'),('serverinfo','installed_version','1.2.0'),('serverinfo','types',''),('sharebymail','enabled','yes'),('sharebymail','installed_version','1.2.0'),('sharebymail','types','filesystem'),('spreed','enabled','no'),('spreed','installed_version','2.0.1'),('spreed','types','prevent_group_restriction'),('survey_client','enabled','yes'),('survey_client','installed_version','1.0.0'),('survey_client','types',''),('systemtags','enabled','yes'),('systemtags','installed_version','1.2.0'),('systemtags','types','logging'),('tasks','enabled','yes'),('tasks','installed_version','0.9.5'),('tasks','types',''),('theming','enabled','yes'),('theming','installed_version','1.3.0'),('theming','types','logging'),('twofactor_backupcodes','enabled','yes'),('twofactor_backupcodes','installed_version','1.1.1'),('twofactor_backupcodes','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','1.2.0'),('updatenotification','types',''),('user_ldap','cleanUpJobOffset','0'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','1.2.1'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,DC=constellations,DC=com'),('user_ldap','ldap_base_users','OU=People,DC=constellations,DC=com'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_default_ppolicy_dn',''),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr','sAMAccountName'),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_gid_number','gidNumber'),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter',''),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass',''),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=person)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_turn_on_pwd_change','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','person\nposixAccount'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=person)(objectclass=posixAccount)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1'),('workflowengine','enabled','yes'),('workflowengine','installed_version','1.2.0'),('workflowengine','types','filesystem');
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
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `login_name` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `password` longtext COLLATE utf8mb4_bin,
  `name` longtext COLLATE utf8mb4_bin NOT NULL,
  `token` varchar(200) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `type` smallint(5) unsigned NOT NULL DEFAULT '0',
  `remember` smallint(5) unsigned NOT NULL DEFAULT '0',
  `last_activity` int(10) unsigned NOT NULL DEFAULT '0',
  `last_check` int(10) unsigned NOT NULL DEFAULT '0',
  `scope` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authtoken_token_index` (`token`),
  KEY `authtoken_last_activity_index` (`last_activity`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_authtoken`
--

LOCK TABLES `oc_authtoken` WRITE;
/*!40000 ALTER TABLE `oc_authtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_authtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_bookmarks`
--

DROP TABLE IF EXISTS `oc_bookmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_bookmarks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(4096) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `title` varchar(4096) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `description` varchar(4096) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `public` smallint(6) DEFAULT '0',
  `added` int(10) unsigned DEFAULT '0',
  `lastmodified` int(10) unsigned DEFAULT '0',
  `clickcount` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `tag` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  UNIQUE KEY `bookmark_tag` (`bookmark_id`,`tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_bookmarks_tags`
--

LOCK TABLES `oc_bookmarks_tags` WRITE;
/*!40000 ALTER TABLE `oc_bookmarks_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_bookmarks_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_bruteforce_attempts`
--

DROP TABLE IF EXISTS `oc_bruteforce_attempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_bruteforce_attempts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `action` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `occurred` int(10) unsigned NOT NULL DEFAULT '0',
  `ip` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `subnet` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `metadata` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `bruteforce_attempts_ip` (`ip`),
  KEY `bruteforce_attempts_subnet` (`subnet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  `calendarid` int(11) NOT NULL,
  `operation` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `calendarid_synctoken` (`calendarid`,`synctoken`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `calendarid` int(10) unsigned NOT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  `componenttype` varchar(8) COLLATE utf8mb4_bin DEFAULT NULL,
  `firstoccurence` bigint(20) unsigned DEFAULT NULL,
  `lastoccurence` bigint(20) unsigned DEFAULT NULL,
  `uid` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `classification` int(11) DEFAULT '0' COMMENT '0 - public, 1 - private, 2 - confidential',
  PRIMARY KEY (`id`),
  UNIQUE KEY `calobjects_index` (`calendarid`,`uri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarobjects`
--

LOCK TABLES `oc_calendarobjects` WRITE;
/*!40000 ALTER TABLE `oc_calendarobjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendarobjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendarobjects_props`
--

DROP TABLE IF EXISTS `oc_calendarobjects_props`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendarobjects_props` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `calendarid` bigint(20) NOT NULL DEFAULT '0',
  `objectid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `name` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `parameter` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `value` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `calendarobject_index` (`objectid`),
  KEY `calendarobject_name_index` (`name`),
  KEY `calendarobject_value_index` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarobjects_props`
--

LOCK TABLES `oc_calendarobjects_props` WRITE;
/*!40000 ALTER TABLE `oc_calendarobjects_props` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_calendarobjects_props` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_calendars`
--

DROP TABLE IF EXISTS `oc_calendars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_calendars` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `principaluri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `displayname` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `synctoken` int(10) unsigned NOT NULL DEFAULT '1',
  `description` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `calendarorder` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarcolor` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `timezone` longtext COLLATE utf8mb4_bin,
  `components` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `transparent` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `calendars_index` (`principaluri`,`uri`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendars`
--

LOCK TABLES `oc_calendars` WRITE;
/*!40000 ALTER TABLE `oc_calendars` DISABLE KEYS */;
INSERT INTO `oc_calendars` VALUES (1,'principals/system/system','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0);
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
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `principaluri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `source` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `displayname` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `refreshrate` varchar(10) COLLATE utf8mb4_bin DEFAULT NULL,
  `calendarorder` int(10) unsigned NOT NULL DEFAULT '0',
  `calendarcolor` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `striptodos` smallint(6) DEFAULT NULL,
  `stripalarms` smallint(6) DEFAULT NULL,
  `stripattachments` smallint(6) DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `calsub_index` (`principaluri`,`uri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `lastmodified` bigint(20) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards`
--

LOCK TABLES `oc_cards` WRITE;
/*!40000 ALTER TABLE `oc_cards` DISABLE KEYS */;
INSERT INTO `oc_cards` VALUES (1,1,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 4.1.2//EN\r\nUID:admin\r\nFN:admin\r\nN:admin;;;;\r\nCLOUD:admin@www.constellations.com/nextcloud\r\nEND:VCARD\r\n','Database:admin.vcf',1497011838,'ededc66b442a55c9138b6b13e0ed938b',159);
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
  `name` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `value` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `preferred` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `card_contactid_index` (`cardid`),
  KEY `card_name_index` (`name`),
  KEY `card_value_index` (`value`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards_properties`
--

LOCK TABLES `oc_cards_properties` WRITE;
/*!40000 ALTER TABLE `oc_cards_properties` DISABLE KEYS */;
INSERT INTO `oc_cards_properties` VALUES (1,1,1,'UID','admin',0),(2,1,1,'FN','admin',0),(3,1,1,'N','admin;;;;',0),(4,1,1,'CLOUD','admin@www.constellations.com/nextcloud',0);
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
  `actor_type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `actor_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `message` longtext COLLATE utf8mb4_bin,
  `verb` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `creation_timestamp` datetime DEFAULT NULL,
  `latest_child_timestamp` datetime DEFAULT NULL,
  `object_type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `object_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `comments_parent_id_index` (`parent_id`),
  KEY `comments_topmost_parent_id_idx` (`topmost_parent_id`),
  KEY `comments_object_index` (`object_type`,`object_id`,`creation_timestamp`),
  KEY `comments_actor_index` (`actor_type`,`actor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `marker_datetime` datetime DEFAULT NULL,
  `object_type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `object_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  UNIQUE KEY `comments_marker_index` (`user_id`,`object_type`,`object_id`),
  KEY `comments_marker_object_index` (`object_type`,`object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `user` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `identifier` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `credentials` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`user`,`identifier`),
  KEY `credentials_user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `principaluri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `access` smallint(6) DEFAULT NULL,
  `resourceid` int(10) unsigned NOT NULL,
  `publicuri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dav_shares_index` (`principaluri`,`resourceid`,`type`,`publicuri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_dav_shares`
--

LOCK TABLES `oc_dav_shares` WRITE;
/*!40000 ALTER TABLE `oc_dav_shares` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_dav_shares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_assigned_labels`
--

DROP TABLE IF EXISTS `oc_deck_assigned_labels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_assigned_labels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label_id` int(11) NOT NULL DEFAULT '0',
  `card_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `deck_assigned_labels_label_id_index` (`label_id`),
  KEY `deck_assigned_labels_card_id_index` (`card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_assigned_labels`
--

LOCK TABLES `oc_deck_assigned_labels` WRITE;
/*!40000 ALTER TABLE `oc_deck_assigned_labels` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_assigned_labels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_attachment`
--

DROP TABLE IF EXISTS `oc_deck_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `card_id` bigint(20) NOT NULL,
  `type` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `data` longtext COLLATE utf8mb4_bin,
  `last_modified` bigint(20) unsigned DEFAULT '0',
  `created_at` bigint(20) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_attachment`
--

LOCK TABLES `oc_deck_attachment` WRITE;
/*!40000 ALTER TABLE `oc_deck_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_board_acl`
--

DROP TABLE IF EXISTS `oc_deck_board_acl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_board_acl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `board_id` bigint(20) NOT NULL,
  `type` int(11) NOT NULL,
  `participant` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `permission_edit` tinyint(1) DEFAULT '0',
  `permission_share` tinyint(1) DEFAULT '0',
  `permission_manage` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `UNIQ_F8F31A55D6E16D85A29A910A8F856BFF` (`board_id`,`type`,`participant`),
  KEY `deck_board_acl_board_id_index` (`board_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_board_acl`
--

LOCK TABLES `oc_deck_board_acl` WRITE;
/*!40000 ALTER TABLE `oc_deck_board_acl` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_board_acl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_boards`
--

DROP TABLE IF EXISTS `oc_deck_boards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_boards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `owner` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `color` varchar(6) COLLATE utf8mb4_bin DEFAULT NULL,
  `archived` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_boards`
--

LOCK TABLES `oc_deck_boards` WRITE;
/*!40000 ALTER TABLE `oc_deck_boards` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_boards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_cards`
--

DROP TABLE IF EXISTS `oc_deck_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_cards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `description` longtext COLLATE utf8mb4_bin,
  `stack_id` bigint(20) NOT NULL,
  `type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT 'plain',
  `last_modified` bigint(20) unsigned DEFAULT '0',
  `created_at` bigint(20) unsigned DEFAULT '0',
  `owner` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `order` bigint(20) DEFAULT NULL,
  `archived` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `deck_cards_stack_id_index` (`stack_id`),
  KEY `deck_cards_order_index` (`order`),
  KEY `deck_cards_archived_index` (`archived`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_cards`
--

LOCK TABLES `oc_deck_cards` WRITE;
/*!40000 ALTER TABLE `oc_deck_cards` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_labels`
--

DROP TABLE IF EXISTS `oc_deck_labels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_labels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `color` varchar(6) COLLATE utf8mb4_bin DEFAULT NULL,
  `board_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deck_labels_board_id_index` (`board_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_labels`
--

LOCK TABLES `oc_deck_labels` WRITE;
/*!40000 ALTER TABLE `oc_deck_labels` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_labels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_deck_stacks`
--

DROP TABLE IF EXISTS `oc_deck_stacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_deck_stacks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `board_id` bigint(20) NOT NULL,
  `order` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `deck_stacks_board_id_index` (`board_id`),
  KEY `deck_stacks_order_index` (`order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_deck_stacks`
--

LOCK TABLES `oc_deck_stacks` WRITE;
/*!40000 ALTER TABLE `oc_deck_stacks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_deck_stacks` ENABLE KEYS */;
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
  `value` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`applicable_id`),
  UNIQUE KEY `applicable_type_value_mount` (`type`,`value`,`mount_id`),
  KEY `applicable_mount` (`mount_id`),
  KEY `applicable_type_value` (`type`,`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `key` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `value` varchar(4096) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`config_id`),
  UNIQUE KEY `config_mount_key` (`mount_id`,`key`),
  KEY `config_mount` (`mount_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `mount_point` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `storage_backend` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `auth_backend` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `priority` int(11) NOT NULL DEFAULT '100',
  `type` int(11) NOT NULL,
  PRIMARY KEY (`mount_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `key` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `value` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`option_id`),
  UNIQUE KEY `option_mount_key` (`mount_id`,`key`),
  KEY `option_mount` (`mount_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `key` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `ttl` int(11) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `lock_key_index` (`key`),
  KEY `lock_ttl_index` (`ttl`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (5,0,'files/38f1a462ac005ca53e80d2b991446fcc',1497021042),(6,0,'files/94d6e57f87a95ab97190ea200c471d58',1497021042),(7,0,'files/76287b2f29364703dfd1d9b543a9b4ea',1497021042),(8,0,'files/6003c26f820e7dfb8cf1349b1eee4192',1497021042),(9,0,'files/169ecf9ce9d92154b2d8f3bb3ae0a844',1497021042),(10,0,'files/8d808264268ae2fe9bc1ba387ea3d422',1497021042),(11,0,'files/4462d021359874962ce01e459811fd2f',1497021042),(12,0,'files/3fc6c5255194229c8fe7207c019f799d',1497021042),(13,0,'files/96de6c364514d73c48c4d1bb07cb500e',1497021042),(14,0,'files/f9b7ca3604813ca018716be621bb7909',1497021042),(15,0,'files/ee32bae6d3c598e340831969e79c6340',1497021042),(16,0,'files/3e0af14d5271af42865bdaa6a9b668ef',1497021042),(17,0,'files/11c6efefe7042583d9bc33a4020aeb62',1497021042),(18,0,'files/6868cf08f134e4ecd9c67e38641df516',1497021042),(19,0,'files/2b472e2132c1f0e68c63cc5652e1ecff',1497021042),(20,0,'files/7107b3afb9d25db8c4c2c58e71e8c0ac',1497021042),(21,0,'files/b2e4494a9b232ace38f0844901b5b4ba',1497021042),(22,0,'files/228a47e1c54e7c56e1df5be52615f554',1497021042),(23,0,'files/aeb66e606de35cf9f9a90a92affda4ea',1497021043),(24,0,'files/ccd5867b110c51fe9b9df5956b9f22dd',1497021043),(25,0,'files/45e5e4c8b19c96fc636c08cac20d67ff',1497021043),(26,0,'files/c2a592af53bcc32c877c55c3397f3520',1497021043),(27,0,'files/90a7deb8600fbfa23023022e5837929d',1497021043),(28,0,'files/8526746e8561ee494303fe5516868760',1497021043),(29,0,'files/e0ab5ae5038b2e8094771d158b3ff28f',1497021043),(30,0,'files/bb166a694622fcc1e912d40218e27fb6',1497021043),(31,0,'files/c951a56970345a6ef9485b44b958d96a',1497021043),(32,0,'files/62106b3c9c93cb6201616390d72d6c18',1497021043),(33,0,'files/f69ef922556068be6b410fdad929dbf3',1497021043),(34,0,'files/05ca4d2ebc744e27d3816f5927324151',1497021043),(35,0,'files/ae5fa984d8d64b5bf0cacdab2950c08b',1497021043),(36,0,'files/1a5e469fc6e0f5606d5214ae00f09e4b',1497021043),(37,0,'files/0ac839f5f56bf15ef6734de860656114',1497021043),(38,0,'files/af3d1cd190ca4bbdf43f6129da9bd90f',1497021043),(39,0,'files/dbdfbd901dcc1fe63971eb6f304c1ffb',1497021043),(40,0,'files/74166daef647b6b8b80bb306691fccb1',1497021043),(41,0,'files/5c7f1675da37cffa2909ddfc424b34df',1497021043),(42,0,'files/1a3c3f93ca79c2ca62845777b136b4fe',1497021043),(43,0,'files/f77be4599c82c8f9c4a6a222705284a9',1497021043),(44,0,'files/488f4074bf8bbafabcfe2531b2de081e',1497021043),(45,0,'files/117734283db6fc2b7df28542840a143d',1497021043),(46,0,'files/d7639b8862753bb00bd95fcc197824ae',1497021043),(47,0,'files/e0bd635c6d81d13841803ca8d11167a0',1497021043),(48,0,'files/b6e959f26bf3ca22766f78c502f6bd4c',1497021043),(49,0,'files/219681c0c1f76776bca5080643ef5bbc',1497021043),(50,0,'files/9714630514ffd94bf0173dac5216fc01',1497021043);
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
  `path` varchar(4000) COLLATE utf8mb4_bin DEFAULT NULL,
  `path_hash` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `parent` int(11) NOT NULL DEFAULT '0',
  `name` varchar(250) COLLATE utf8mb4_bin DEFAULT NULL,
  `mimetype` int(11) NOT NULL DEFAULT '0',
  `mimepart` int(11) NOT NULL DEFAULT '0',
  `size` bigint(20) NOT NULL DEFAULT '0',
  `mtime` int(11) NOT NULL DEFAULT '0',
  `storage_mtime` int(11) NOT NULL DEFAULT '0',
  `encrypted` int(11) NOT NULL DEFAULT '0',
  `unencrypted_size` bigint(20) NOT NULL DEFAULT '0',
  `etag` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `permissions` int(11) DEFAULT '0',
  `checksum` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`fileid`),
  UNIQUE KEY `fs_storage_path_hash` (`storage`,`path_hash`),
  KEY `fs_parent_name_hash` (`parent`,`name`),
  KEY `fs_storage_mimetype` (`storage`,`mimetype`),
  KEY `fs_storage_mimepart` (`storage`,`mimepart`),
  KEY `fs_storage_size` (`storage`,`size`,`fileid`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1497017535,1497011203,0,0,'593aacbf8c1ec',23,''),(2,1,'appdata_octzcc66adb8','cc07fa4e97329332eff86064716c8276',1,'appdata_octzcc66adb8',2,1,2385168,1497017535,1497012008,0,0,'593aacbf8c1ec',31,''),(3,1,'appdata_octzcc66adb8/appstore','edf79733597b088282733d50f0255a5f',2,'appstore',2,1,297360,1497015621,1497011203,0,0,'593aa5453ce64',31,''),(4,1,'appdata_octzcc66adb8/appstore/apps.json','3d4c5b91dff0ceab92630bc93bbffd86',3,'apps.json',4,3,264827,1497015621,1497015621,0,0,'eec4552fa9662d590c81cca17f31ca81',27,''),(5,1,'appdata_octzcc66adb8/preview','dde34861366aceeeb313275e2b201260',2,'preview',2,1,0,1497011144,1497011144,0,0,'593a93c900a48',31,''),(6,2,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,6823068,1497011148,1497011148,0,0,'593a93ccb194b',23,''),(7,2,'files','45b963397aa40d4a0063e0d85e4fe7a1',6,'files',2,1,6823068,1497011148,1497011148,0,0,'593a93ccb194b',31,''),(8,2,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',7,'Photos',2,1,2360011,1497011148,1497011148,0,0,'593a93cc6106d',31,''),(9,2,'files/Photos/Hummingbird.jpg','e077463269c404ae0f6f8ea7f2d7a326',8,'Hummingbird.jpg',6,5,585219,1497011148,1497011148,0,0,'0074ab5c85e9e1ad36722f5bd3086c72',27,''),(10,2,'files/Photos/Nut.jpg','aa8daeb975e1d39412954fd5cd41adb4',8,'Nut.jpg',6,5,955026,1497011148,1497011148,0,0,'e01d3d9fe5fb9b5415a68052f18b6c9c',27,''),(11,2,'files/Photos/Coast.jpg','a6fe87299d78b207e9b7aba0f0cb8a0a',8,'Coast.jpg',6,5,819766,1497011148,1497011148,0,0,'3e3656544aee17d45dbeaf78360b9b53',27,''),(12,2,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',7,'Documents',2,1,78496,1497011148,1497011148,0,0,'593a93cc8b7af',31,''),(13,2,'files/Documents/About.txt','9da7b739e7a65d74793b2881da521169',12,'About.txt',8,7,1074,1497011148,1497011148,0,0,'2b4a21d1855a38a6e0bd64692175b5cc',27,''),(14,2,'files/Documents/About.odt','b2ee7d56df9f34a0195d4b611376e885',12,'About.odt',9,3,77422,1497011148,1497011148,0,0,'4150e78de88e6a46bb233fa525eafa40',27,''),(15,2,'files/Nextcloud.mp4','77a79c09b93e57cba23c11eb0e6048a6',7,'Nextcloud.mp4',11,10,462413,1497011148,1497011148,0,0,'d0bb565b6b1e6ebe9ad660893917e1fd',27,''),(16,2,'files/Nextcloud Manual.pdf','2bc58a43566a8edde804a4a97a9c7469',7,'Nextcloud Manual.pdf',12,3,3922148,1497011148,1497011148,0,0,'2e14dee66d120fec9765cdf3d8a3ccd0',27,''),(17,1,'appdata_octzcc66adb8/avatar','bab988a16c60f060b3c3890dfcd0acf0',2,'avatar',2,1,0,1497011168,1497011168,0,0,'593a93e08aff5',31,''),(18,1,'appdata_octzcc66adb8/avatar/admin','ece9ccdaa1700008df8055bae518c4cb',17,'admin',2,1,0,1497011168,1497011168,0,0,'593a93e08632b',31,''),(19,1,'appdata_octzcc66adb8/js','961977a55286d920a5afccd3ff9553d6',2,'js',2,1,1982162,1497017535,1497011171,0,0,'593aacbf8c1ec',31,''),(20,1,'appdata_octzcc66adb8/js/core','ba7d2c05e3516710a4d7d85283aaee14',19,'core',2,1,343719,1497017535,1497017535,0,0,'593aacbf8c1ec',31,''),(21,1,'appdata_octzcc66adb8/js/core/merged-template-prepend.js','57b47d76e88128f19b83129e815475d7',20,'merged-template-prepend.js',13,3,142144,1497011168,1497011168,0,0,'7423b075a319f9c469909b7fbfa6aa4b',27,''),(22,1,'appdata_octzcc66adb8/js/core/merged-template-prepend.js.deps','492292c54f00f96e6b9987912e5a4fe9',20,'merged-template-prepend.js.deps',14,3,1146,1497011168,1497011168,0,0,'ef312ea89651a54632ecba3bb34c5d27',27,''),(23,1,'appdata_octzcc66adb8/js/core/merged-template-prepend.js.gzip','099867b4e917fab78f2819120a451e64',20,'merged-template-prepend.js.gzip',15,3,39023,1497011168,1497011168,0,0,'f20e466fae17d541bd75e669a95c7da8',27,''),(24,1,'appdata_octzcc66adb8/js/core/merged-share-backend.js','539bb7c60d6032e32fb76f5c94e6695d',20,'merged-share-backend.js',13,3,104522,1497011169,1497011169,0,0,'ab5fb8aa72c2259d543ba64c509ce73b',27,''),(25,1,'appdata_octzcc66adb8/js/core/merged-share-backend.js.deps','d62838fcd4338e01a40e7d629ce26abe',20,'merged-share-backend.js.deps',14,3,752,1497011169,1497011169,0,0,'ce8f42196e75964666671413db9f91a3',27,''),(26,1,'appdata_octzcc66adb8/js/core/merged-share-backend.js.gzip','1d4e2c470607a6b71a0c4908942dd567',20,'merged-share-backend.js.gzip',15,3,22508,1497011169,1497011169,0,0,'3934b2e373d1ce1394bbd1e42f7a5afe',27,''),(27,1,'appdata_octzcc66adb8/js/notifications','4cc18bb438d3c69bc81e752f9720f0d2',19,'notifications',2,1,25514,1497011169,1497011169,0,0,'593a93e14e4b4',31,''),(28,1,'appdata_octzcc66adb8/js/notifications/merged.js','09741fca6916abb1ce7698e9d767b71e',27,'merged.js',13,3,20114,1497011169,1497011169,0,0,'a3b1197d69ecf55e12ab4189b90574fa',27,''),(29,1,'appdata_octzcc66adb8/js/notifications/merged.js.deps','097f640ccc813550d041b8de9c8d6735',27,'merged.js.deps',14,3,330,1497011169,1497011169,0,0,'49b4524794613261a2b8baeeed97d497',27,''),(30,1,'appdata_octzcc66adb8/js/notifications/merged.js.gzip','43c420791423827b5454e7e53e10294f',27,'merged.js.gzip',15,3,5070,1497011169,1497011169,0,0,'67489d130f9de45c1496afbf55852b52',27,''),(31,1,'appdata_octzcc66adb8/js/files','33e77b8557f88d9b48f3854c80cb155c',19,'files',2,1,398160,1497011169,1497011169,0,0,'593a93e198590',31,''),(32,1,'appdata_octzcc66adb8/js/files/merged-index.js','dff27f940958e70a80feb0a145fb7e98',31,'merged-index.js',13,3,319781,1497011169,1497011169,0,0,'769b2175ef3295584ea2a9df3b7870d2',27,''),(33,1,'appdata_octzcc66adb8/js/files/merged-index.js.deps','a1afc001f2f9219739b90191433f665a',31,'merged-index.js.deps',14,3,2125,1497011169,1497011169,0,0,'9fa5e93008564e6de1d5895f6eed7020',27,''),(34,1,'appdata_octzcc66adb8/js/files/merged-index.js.gzip','bf98387be0e19ca900c4fa04167f887a',31,'merged-index.js.gzip',15,3,76254,1497011169,1497011169,0,0,'0ad81d3a43efa6eac91b900eb75e5b51',27,''),(35,1,'appdata_octzcc66adb8/js/activity','0a816d9523776a40fb3798891fa28f9f',19,'activity',2,1,20399,1497011169,1497011169,0,0,'593a93e1c7177',31,''),(36,1,'appdata_octzcc66adb8/js/activity/activity-sidebar.js','867461b8c32dea0f453db2321631bfa7',35,'activity-sidebar.js',13,3,15755,1497011169,1497011169,0,0,'2e3a5d31d1d21c11c64cac0b5b012a05',27,''),(37,1,'appdata_octzcc66adb8/js/activity/activity-sidebar.js.deps','1cf3b183486f2562bb44f2dc62e1231f',35,'activity-sidebar.js.deps',14,3,494,1497011169,1497011169,0,0,'10d6674917526f29a07a64f43fb45963',27,''),(38,1,'appdata_octzcc66adb8/js/activity/activity-sidebar.js.gzip','18987698eab93a23a297359de2449200',35,'activity-sidebar.js.gzip',15,3,4150,1497011169,1497011169,0,0,'302d2a8933184afbf022d99ce8b5d88d',27,''),(39,1,'appdata_octzcc66adb8/js/comments','8c6b06d187c4b4066f143e942e23b11b',19,'comments',2,1,36996,1497011170,1497011169,0,0,'593a93e2097c5',31,''),(40,1,'appdata_octzcc66adb8/js/comments/merged.js','d41d96ab18edd582d0a5aa282319e222',39,'merged.js',13,3,28929,1497011169,1497011169,0,0,'af537cf779147d7b00a7151db75cf1a3',27,''),(41,1,'appdata_octzcc66adb8/js/comments/merged.js.deps','c6e85f401c9d086efb462f55ec1bbfa1',39,'merged.js.deps',14,3,635,1497011169,1497011169,0,0,'728d9a8fdcdf86de9a742500aa0f24cf',27,''),(42,1,'appdata_octzcc66adb8/js/comments/merged.js.gzip','1efa34bdd2c2a3ddf111d606cc1213b5',39,'merged.js.gzip',15,3,7432,1497011170,1497011170,0,0,'af637c0f55e938fd514af6e50dec8ce9',27,''),(43,1,'appdata_octzcc66adb8/js/files_sharing','f7238012f712db1e92036f1d369fd10a',19,'files_sharing',2,1,20226,1497011170,1497011170,0,0,'593a93e23dbdf',31,''),(44,1,'appdata_octzcc66adb8/js/files_sharing/additionalScripts.js','de8082bff7ecb76737364c8cb17abd6d',43,'additionalScripts.js',13,3,15161,1497011170,1497011170,0,0,'b43871a6b8e295f81b92337a5362d88d',27,''),(45,1,'appdata_octzcc66adb8/js/files_sharing/additionalScripts.js.deps','6e19b56b391729a7658e8a30cc7a8145',43,'additionalScripts.js.deps',14,3,340,1497011170,1497011170,0,0,'358429fe1849e345bad1a8778d0aead7',27,''),(46,1,'appdata_octzcc66adb8/js/files_sharing/additionalScripts.js.gzip','564bcbb63d38d4efefe7a5b65d18d3fe',43,'additionalScripts.js.gzip',15,3,4725,1497011170,1497011170,0,0,'697d0568fdf1d86c7d375eff93e3e5d6',27,''),(47,1,'appdata_octzcc66adb8/js/files_texteditor','8d8458f5a32a9f5cf8eca6f55fc6df6d',19,'files_texteditor',2,1,820097,1497011170,1497011170,0,0,'593a93e294736',31,''),(48,1,'appdata_octzcc66adb8/js/files_texteditor/merged.js','e8d7b504c351b9f74b5c0ec1e8d0a4c3',47,'merged.js',13,3,681977,1497011170,1497011170,0,0,'159fd4cb49d61eab0019b6bbacc14f9e',27,''),(49,1,'appdata_octzcc66adb8/js/files_texteditor/merged.js.deps','6e85808f275b4653924b3a646dbf0b6d',47,'merged.js.deps',14,3,370,1497011170,1497011170,0,0,'5f29036f359f67f89c65896911b32719',27,''),(50,1,'appdata_octzcc66adb8/js/files_texteditor/merged.js.gzip','d4280b3e41d37a52732043c0d492961c',47,'merged.js.gzip',15,3,137750,1497011170,1497011170,0,0,'2cd742d672f1ac59b24517bf48b198eb',27,''),(51,1,'appdata_octzcc66adb8/js/files_versions','03881a1ca402f57a9a7933f8a8e4bf37',19,'files_versions',2,1,16725,1497011170,1497011170,0,0,'593a93e2c3c31',31,''),(52,1,'appdata_octzcc66adb8/js/files_versions/merged.js','57de2ba4e046ca56e85727499bbd57ce',51,'merged.js',13,3,12719,1497011170,1497011170,0,0,'4460b4dbfacbb71277d6495d4d8ff99f',27,''),(53,1,'appdata_octzcc66adb8/js/files_versions/merged.js.deps','a3f31c173deb98f5e02310d3bc489602',51,'merged.js.deps',14,3,424,1497011170,1497011170,0,0,'6943aeb82aed958893e8a35d53b36594',27,''),(54,1,'appdata_octzcc66adb8/js/files_versions/merged.js.gzip','b508b99f7699b8d71a6df01f42d10f5f',51,'merged.js.gzip',15,3,3582,1497011170,1497011170,0,0,'d2df3d4e2bb06e18b1bf8acdbe735a8a',27,''),(55,1,'appdata_octzcc66adb8/js/gallery','adc5b6a433cc7bd915ab8c2f20451246',19,'gallery',2,1,280677,1497011171,1497011170,0,0,'593a93e324876',31,''),(56,1,'appdata_octzcc66adb8/js/gallery/scripts-for-file-app.js','57ddd43bfb1e1da6ce84b7923382b6f1',55,'scripts-for-file-app.js',13,3,225356,1497011171,1497011171,0,0,'1e74d4dc04c46601603850f8537d9852',27,''),(57,1,'appdata_octzcc66adb8/js/gallery/scripts-for-file-app.js.deps','07ba7e165b57b22a7fa11581923bd868',55,'scripts-for-file-app.js.deps',14,3,856,1497011171,1497011171,0,0,'a09ee1c3c9dcc2ea1a1a5841221b69db',27,''),(58,1,'appdata_octzcc66adb8/js/gallery/scripts-for-file-app.js.gzip','d6f916d310af4dfae496ffdc8463f363',55,'scripts-for-file-app.js.gzip',15,3,54465,1497011171,1497011171,0,0,'4a23281334960912feee4e8066ffddac',27,''),(59,1,'appdata_octzcc66adb8/js/core/merged.js','066ceec796c6300bb70818b7d3153b4c',20,'merged.js',13,3,20224,1497011171,1497011171,0,0,'136e5255688c756401aece0f081244d9',27,''),(60,1,'appdata_octzcc66adb8/js/core/merged.js.deps','df28aba9898c1947009c5e6db410fe5b',20,'merged.js.deps',14,3,508,1497011171,1497011171,0,0,'34d382db008ed29b888a625ac0ad63cd',27,''),(61,1,'appdata_octzcc66adb8/js/core/merged.js.gzip','2a97ce206f4e398a403e169d34584aa1',20,'merged.js.gzip',15,3,5365,1497011171,1497011171,0,0,'db3b0e12dee530bc705930fa55521be2',27,''),(62,1,'appdata_octzcc66adb8/js/systemtags','fa6977ad875faf78052ebc2dcaedc3ca',19,'systemtags',2,1,19649,1497011171,1497011171,0,0,'593a93e396da2',31,''),(63,1,'appdata_octzcc66adb8/js/systemtags/merged.js','6a5faea00dd422c38e16417170a7d47f',62,'merged.js',13,3,14902,1497011171,1497011171,0,0,'b46092edb982e48f9b8e4efc8b990ed1',27,''),(64,1,'appdata_octzcc66adb8/js/systemtags/merged.js.deps','53bd0d97ef168c8afc8d24c7b0407b87',62,'merged.js.deps',14,3,399,1497011171,1497011171,0,0,'77c879146e395cd4d6448a20e66735e7',27,''),(65,1,'appdata_octzcc66adb8/js/systemtags/merged.js.gzip','09145feabbded049188b58dd8976e7f5',62,'merged.js.gzip',15,3,4348,1497011171,1497011171,0,0,'2c1b5781be88f5330d7e231fd7f39276',27,''),(66,1,'appdata_octzcc66adb8/css','01c0c30169856fe07e9e3c3d7f4b143a',2,'css',2,1,103529,1497012090,1497011177,0,0,'593a977a48538',31,''),(67,1,'appdata_octzcc66adb8/css/core','7f692f721e85895e98e49260589fd7d3',66,'core',2,1,95937,1497012088,1497012088,0,0,'593a977856887',31,''),(68,1,'appdata_octzcc66adb8/theming','c8e8812d80ef2f531024f06d8a5d9652',2,'theming',2,1,2117,1497011183,1497011182,0,0,'593a93ef4f547',31,''),(71,1,'appdata_octzcc66adb8/css/core/server.css.gzip','27e45555d07578f6d50eaa7e690c5dc4',67,'server.css.gzip',15,3,13409,1497012088,1497012088,0,0,'7bc8be125d11d14c5a549632da7f5eef',27,''),(74,1,'appdata_octzcc66adb8/css/core/share.css.gzip','70f4764a9dd48d3c6239c06513c05abd',67,'share.css.gzip',15,3,994,1497012088,1497012088,0,0,'312b8db1eb8044ae7999fbd25797b232',27,''),(75,1,'appdata_octzcc66adb8/css/files','6d1ebc654e1ce30421f04572cfc9ed5b',66,'files',2,1,4283,1497012084,1497012084,0,0,'593a9774c8deb',31,''),(78,1,'appdata_octzcc66adb8/css/files/merged.css.gzip','1975dd85b288bb4309031c0b53d96f54',75,'merged.css.gzip',15,3,4283,1497011174,1497011174,0,0,'c6f4d090c81c54640bd37bbc93e7c572',27,''),(79,1,'appdata_octzcc66adb8/css/files_sharing','a3d6f76210e64bac57eda6e5a9205d63',66,'files_sharing',2,1,878,1497012084,1497012084,0,0,'593a9774dc1f2',31,''),(82,1,'appdata_octzcc66adb8/css/files_sharing/mergedAdditionalStyles.css.gzip','965ffec1d4dc955ae5c160471942a656',79,'mergedAdditionalStyles.css.gzip',15,3,878,1497011175,1497011175,0,0,'01e609744192c7c7419e2981427b7749',27,''),(83,1,'appdata_octzcc66adb8/css/files_texteditor','3035b1610c882c7aad9d14f84f90369b',66,'files_texteditor',2,1,1184,1497012084,1497012084,0,0,'593a9774eea50',31,''),(86,1,'appdata_octzcc66adb8/css/files_texteditor/merged.css.gzip','12d5c704841458cc247d04eef3c07c95',83,'merged.css.gzip',15,3,1184,1497011175,1497011175,0,0,'28b190daafa7211ca24e46eb0efd83e7',27,''),(89,1,'appdata_octzcc66adb8/css/core/systemtags.css.gzip','b4ef2bf731e2cc663144271173300e06',67,'systemtags.css.gzip',15,3,389,1497011175,1497011175,0,0,'06eed61fdd4e3d9ff83e2323c4ac2748',27,''),(90,1,'appdata_octzcc66adb8/css/theming','d7163d8d49124770872c2b0e1b0ccb6d',66,'theming',2,1,1247,1497012090,1497012090,0,0,'593a977a48538',31,''),(93,1,'appdata_octzcc66adb8/css/theming/theming.css.gzip','a727a8a9b2e20c860471cf2e07687814',90,'theming.css.gzip',15,3,313,1497012090,1497012090,0,0,'c3fc4966a818225a5923ca40684cb9bb',27,''),(94,1,'appdata_octzcc66adb8/theming/0','08125e0aefca96a8d76c886d56becda0',68,'0',2,1,2117,1497011183,1497011183,0,0,'593a93ef4f547',31,''),(95,1,'appdata_octzcc66adb8/theming/0/icon-core-filetypes_folder.svg','b622b10a421799a7e4b1be2fb9862fa7',94,'icon-core-filetypes_folder.svg',17,5,254,1497011182,1497011182,0,0,'1934d84574d1d5b863bae9ebcac38bbc',27,''),(96,1,'appdata_octzcc66adb8/theming/0/icon-core-filetypes_video.svg','15917711b36a9f37d82445889bb868ca',94,'icon-core-filetypes_video.svg',17,5,328,1497011183,1497011183,0,0,'5141a7aad95aebfc82b3ebe410575e57',27,''),(97,1,'appdata_octzcc66adb8/theming/0/icon-core-filetypes_application-pdf.svg','4aae32db4dfe808313dab6c86c718af0',94,'icon-core-filetypes_application-pdf.svg',17,5,1535,1497011183,1497011183,0,0,'9891ef69f601ea32ffa013049faf3bc6',27,''),(98,1,'appdata_octzcc66adb8/appstore/categories.json','7ae02f360bcc19db588bf0f354bffc51',3,'categories.json',4,3,32533,1497015621,1497015621,0,0,'8c0545b2c272385271becb8138785443',27,''),(99,1,'files_external','c270928b685e7946199afdfb898d27ea',1,'files_external',2,1,0,1497011203,1497011203,0,0,'593a94036e746',31,''),(100,1,'appdata_octzcc66adb8/richdocuments','21c4bff10ef8c6fe719385358da74ff8',2,'richdocuments',2,1,0,1497012008,1497012008,0,0,'593a9728c398e',31,''),(101,1,'appdata_octzcc66adb8/richdocuments/richdocuments','7079eb2749f8b182057ae9e955b7f14d',100,'richdocuments',2,1,0,1497012008,1497012008,0,0,'593a9728c019d',31,''),(102,1,'appdata_octzcc66adb8/css/core/server.css','fe232c6d0046f01d08757eb6ddb445ec',67,'server.css',16,7,77314,1497012087,1497012087,0,0,'6f014f0ee58f5d48022d99961c08ff38',27,''),(103,1,'appdata_octzcc66adb8/css/core/server.css.deps','c33ed9c7dd1a413d2792b0939ca0c0c8',67,'server.css.deps',14,3,850,1497012088,1497012088,0,0,'30fccfb0f5a02cc6d0f3debfa3ca571c',27,''),(104,1,'appdata_octzcc66adb8/css/core/share.css','8e26de9c1e8d8a16fdf60ead5db78faa',67,'share.css',16,7,2848,1497012088,1497012088,0,0,'0afd04745416898164815fc4f0e878f5',27,''),(105,1,'appdata_octzcc66adb8/css/core/share.css.deps','0a109896a40d6d311141640e4e5b1460',67,'share.css.deps',14,3,133,1497012088,1497012088,0,0,'10826c0ef8dfea141f4c824174fdfc06',27,''),(106,1,'appdata_octzcc66adb8/css/theming/theming.css','dd257982758cb4a94c1288970b2f190f',90,'theming.css',16,7,790,1497012090,1497012090,0,0,'9fa91ea33f8ec7386e7c7ba22ee7a983',27,''),(107,1,'appdata_octzcc66adb8/css/theming/theming.css.deps','85c2d7e9634fafd4037be6bd6a589251',90,'theming.css.deps',14,3,144,1497012090,1497012090,0,0,'63c2a8c2c23b4857ea41834363567823',27,''),(108,1,'appdata_octzcc66adb8/js/core/merged-login.js','fcccdd09b95b7b9bd3286a387d70a42e',20,'merged-login.js',13,3,5389,1497017535,1497017535,0,0,'459cfb60a947ef05b6ff8bafac84cc5d',27,''),(109,1,'appdata_octzcc66adb8/js/core/merged-login.js.deps','d412ddb4875501891814c49083101168',20,'merged-login.js.deps',14,3,271,1497017535,1497017535,0,0,'8effc41afcb31460ae566b07a26576f7',27,''),(110,1,'appdata_octzcc66adb8/js/core/merged-login.js.gzip','9d083f05ff3fc2b05182abb141ef5b56',20,'merged-login.js.gzip',15,3,1867,1497017535,1497017535,0,0,'2fcddf423f4f4d7ae821342485482aac',27,'');
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
  `id` varchar(250) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `user` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `timestamp` varchar(12) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `location` varchar(512) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `type` varchar(4) COLLATE utf8mb4_bin DEFAULT NULL,
  `mime` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`auto_id`),
  KEY `id_index` (`id`),
  KEY `timestamp_index` (`timestamp`),
  KEY `user_index` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `class` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `operator` varchar(16) COLLATE utf8mb4_bin NOT NULL,
  `value` longtext COLLATE utf8mb4_bin,
  `hash` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flow_unique_hash` (`hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `class` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `checks` longtext COLLATE utf8mb4_bin,
  `operation` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `gid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`,`uid`),
  KEY `group_admin_uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `gid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`,`uid`),
  KEY `gu_uid_index` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `gid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `argument` varchar(4000) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `last_run` int(11) DEFAULT '0',
  `last_checked` int(11) DEFAULT '0',
  `reserved_at` int(11) DEFAULT '0',
  `execution_duration` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `job_class_index` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1497015807,1497015807,0,0),(2,'OCA\\Files_Sharing\\DeleteOrphanedSharesJob','null',1497015960,1497015960,0,0),(3,'OCA\\Files_Sharing\\ExpireSharesJob','null',1497011297,1497016771,0,0),(4,'OCA\\UpdateNotification\\Notification\\BackgroundJob','null',1497011773,1497017075,0,2),(6,'OCA\\DAV\\CardDAV\\SyncJob','null',1497011838,1497017090,0,0),(7,'OCA\\Files\\BackgroundJob\\ScanFiles','null',1497017441,1497017441,0,2),(8,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',1497017523,1497017522,0,0),(9,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',1497017527,1497017527,0,0),(10,'OCA\\Federation\\SyncJob','null',1497015606,1497017536,0,0),(11,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1497015620,1497015620,0,0),(12,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1497015625,1497015625,0,0),(13,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1497015782,1497015782,0,0),(14,'OCA\\NextcloudAnnouncements\\Cron\\Crawler','null',1497015785,1497015785,0,2),(15,'\\OC\\Authentication\\Token\\DefaultTokenCleanupJob','null',1497015792,1497015792,0,0),(17,'OCA\\User_LDAP\\Jobs\\UpdateGroups','null',1497015969,1497015969,0,0),(18,'OCA\\User_LDAP\\Jobs\\CleanUp','null',1497016763,1497016763,0,0);
/*!40000 ALTER TABLE `oc_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_ldap_group_mapping`
--

DROP TABLE IF EXISTS `oc_ldap_group_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_ldap_group_mapping` (
  `ldap_dn` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `owncloud_name` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `directory_uuid` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`ldap_dn`),
  UNIQUE KEY `owncloud_name_groups` (`owncloud_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `owncloudname` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `owncloudusers` longtext COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`owncloudname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `ldap_dn` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `owncloud_name` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `directory_uuid` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`owncloud_name`),
  UNIQUE KEY `ldap_dn_users` (`ldap_dn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_ldap_user_mapping`
--

LOCK TABLES `oc_ldap_user_mapping` WRITE;
/*!40000 ALTER TABLE `oc_ldap_user_mapping` DISABLE KEYS */;
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=exam1,ou=exams,ou=other,ou=people,dc=constellations,dc=com','exam1','5FC79BED-1BB5-4616-9377-A03BF2D227AB'),('cn=exam2,ou=exams,ou=other,ou=people,dc=constellations,dc=com','exam2','70D8B173-63B1-4CD1-86BC-DE5DB3495898'),('cn=exam3,ou=exams,ou=other,ou=people,dc=constellations,dc=com','exam3','3138ACBC-3168-4DF4-8003-700C2962D709'),('cn=exam4,ou=exams,ou=other,ou=people,dc=constellations,dc=com','exam4','E8D2A365-F1C7-4F6B-B089-C289CF4AF70D'),('cn=exam5,ou=exams,ou=other,ou=people,dc=constellations,dc=com','exam5','F5FE513C-08C8-46DD-9517-CBDA70AE1D6F'),('cn=guest1,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest1','F2189C45-4403-46D5-8309-598FE34ED7DB'),('cn=guest10,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest10','33952766-1307-4046-BED6-0A164103FF6A'),('cn=guest2,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest2','B2979F51-0A25-4CCD-9848-DE6113898C47'),('cn=guest3,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest3','B7D07A03-F0FD-489D-A339-037A454DC81E'),('cn=guest4,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest4','AAFDD98A-6FEA-4AD0-B535-6BB2A36548CD'),('cn=guest5,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest5','5EDD2BF0-5410-4B98-9759-F9D5255071E8'),('cn=guest6,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest6','404B3DF1-00B3-44B8-9AFA-AAC426F8F8A7'),('cn=guest7,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest7','E6C15BA1-9DAF-4D9A-B374-93786FE09F99'),('cn=guest8,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest8','429F8C72-9D03-4FDD-B53C-749E2E13CDF4'),('cn=guest9,ou=guestusers,ou=other,ou=people,dc=constellations,dc=com','guest9','DA6651DA-E7CE-453C-A17E-C53322F01DA7'),('cn=ismith,ou=staff,ou=personnel,ou=people,dc=constellations,dc=com','ismith','ED66F05E-6B14-4D80-B5B1-802AA33A2E77'),('cn=jjones,ou=staff,ou=personnel,ou=people,dc=constellations,dc=com','jjones','4AD7B379-D0FA-4ED0-A1E9-5A8150522DC9'),('cn=profileuser,ou=other,ou=people,dc=constellations,dc=com','profileuser','53994F0F-BCF0-4FFC-B099-11391C1AE82C'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,dc=constellations,dc=com','sysadmin','971BF1AC-5F48-401B-B653-7BF833649CCF'),('cn=tech1,ou=tech,ou=personnel,ou=people,dc=constellations,dc=com','tech1','766B6AEB-5BF9-446D-ACEE-815E1BE52463'),('cn=tech2,ou=tech,ou=personnel,ou=people,dc=constellations,dc=com','tech2','2A22818E-3C4D-4CF1-802D-D6D3C2DFCB35'),('cn=tech3,ou=tech,ou=personnel,ou=people,dc=constellations,dc=com','tech3','F4C8C638-6C45-4E76-A940-7AE326F360D2'),('cn=tech4,ou=tech,ou=personnel,ou=people,dc=constellations,dc=com','tech4','BB2CA7E7-4DF6-4E1B-AA3A-01D8600B987B');
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
  `mimetype` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mimetype_id_index` (`mimetype`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (3,'application'),(13,'application/javascript'),(4,'application/json'),(14,'application/octet-stream'),(12,'application/pdf'),(9,'application/vnd.oasis.opendocument.text'),(15,'application/x-gzip'),(1,'httpd'),(2,'httpd/unix-directory'),(5,'image'),(6,'image/jpeg'),(17,'image/svg+xml'),(7,'text'),(16,'text/css'),(8,'text/plain'),(10,'video'),(11,'video/mp4');
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
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `mount_point` varchar(4000) COLLATE utf8mb4_bin NOT NULL,
  `mount_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mounts_user_root_index` (`user_id`,`root_id`),
  KEY `mounts_user_index` (`user_id`),
  KEY `mounts_storage_index` (`storage_id`),
  KEY `mounts_root_index` (`root_id`),
  KEY `mounts_mount_id_index` (`mount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mounts`
--

LOCK TABLES `oc_mounts` WRITE;
/*!40000 ALTER TABLE `oc_mounts` DISABLE KEYS */;
INSERT INTO `oc_mounts` VALUES (1,2,6,'admin','/admin/',NULL);
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
  `app` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  `user` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `timestamp` int(11) NOT NULL DEFAULT '0',
  `object_type` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `object_id` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `subject` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `subject_parameters` longtext COLLATE utf8mb4_bin,
  `message` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `message_parameters` longtext COLLATE utf8mb4_bin,
  `link` varchar(4000) COLLATE utf8mb4_bin DEFAULT NULL,
  `icon` varchar(4000) COLLATE utf8mb4_bin DEFAULT NULL,
  `actions` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`notification_id`),
  KEY `oc_notifications_app` (`app`),
  KEY `oc_notifications_user` (`user`),
  KEY `oc_notifications_timestamp` (`timestamp`),
  KEY `oc_notifications_object` (`object_type`,`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_notifications`
--

LOCK TABLES `oc_notifications` WRITE;
/*!40000 ALTER TABLE `oc_notifications` DISABLE KEYS */;
INSERT INTO `oc_notifications` VALUES (1,'survey_client','admin',1497011784,'dummy','23','updated','[]','','[]','','','[{\"label\":\"enable\",\"link\":\"http:\\/\\/www.constellations.com\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"POST\",\"primary\":true},{\"label\":\"disable\",\"link\":\"http:\\/\\/www.constellations.com\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"DELETE\",\"primary\":false}]'),(2,'firstrunwizard','admin',1497015802,'user','admin','profile','[]','','[]','','','[]');
/*!40000 ALTER TABLE `oc_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_notifications_pushtokens`
--

DROP TABLE IF EXISTS `oc_notifications_pushtokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_notifications_pushtokens` (
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `token` int(11) NOT NULL DEFAULT '0',
  `deviceidentifier` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `devicepublickey` varchar(512) COLLATE utf8mb4_bin NOT NULL,
  `devicepublickeyhash` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `pushtokenhash` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `proxyserver` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  UNIQUE KEY `oc_notifpushtoken` (`uid`,`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_notifications_pushtokens`
--

LOCK TABLES `oc_notifications_pushtokens` WRITE;
/*!40000 ALTER TABLE `oc_notifications_pushtokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_notifications_pushtokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_oauth2_access_tokens`
--

DROP TABLE IF EXISTS `oc_oauth2_access_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_oauth2_access_tokens` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `token_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `hashed_code` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `encrypted_token` varchar(786) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_access_hash_idx` (`hashed_code`),
  KEY `oauth2_access_client_id_idx` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_oauth2_access_tokens`
--

LOCK TABLES `oc_oauth2_access_tokens` WRITE;
/*!40000 ALTER TABLE `oc_oauth2_access_tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_oauth2_access_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_oauth2_clients`
--

DROP TABLE IF EXISTS `oc_oauth2_clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_oauth2_clients` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `redirect_uri` varchar(2000) COLLATE utf8mb4_bin NOT NULL,
  `client_identifier` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `secret` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oauth2_client_id_idx` (`client_identifier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_oauth2_clients`
--

LOCK TABLES `oc_oauth2_clients` WRITE;
/*!40000 ALTER TABLE `oc_oauth2_clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_oauth2_clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_preferences`
--

DROP TABLE IF EXISTS `oc_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_preferences` (
  `userid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `appid` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `configkey` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `configvalue` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`userid`,`appid`,`configkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_preferences`
--

LOCK TABLES `oc_preferences` WRITE;
/*!40000 ALTER TABLE `oc_preferences` DISABLE KEYS */;
INSERT INTO `oc_preferences` VALUES ('admin','core','lang','en'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1497011147'),('exam1','files_external','config_version','0.5.0'),('exam1','user_ldap','displayName','Exam 1'),('exam1','user_ldap','homePath',''),('exam1','user_ldap','lastFeatureRefresh','1497017442'),('exam1','user_ldap','uid','exam1'),('exam2','files_external','config_version','0.5.0'),('exam2','user_ldap','displayName','Exam 2'),('exam2','user_ldap','homePath',''),('exam2','user_ldap','lastFeatureRefresh','1497017442'),('exam2','user_ldap','uid','exam2'),('exam3','files_external','config_version','0.5.0'),('exam3','user_ldap','displayName','Exam 3'),('exam3','user_ldap','homePath',''),('exam3','user_ldap','lastFeatureRefresh','1497017442'),('exam3','user_ldap','uid','exam3'),('exam4','files_external','config_version','0.5.0'),('exam4','user_ldap','displayName','Exam 4'),('exam4','user_ldap','homePath',''),('exam4','user_ldap','lastFeatureRefresh','1497017442'),('exam4','user_ldap','uid','exam4'),('exam5','files_external','config_version','0.5.0'),('exam5','user_ldap','displayName','Exam 5'),('exam5','user_ldap','homePath',''),('exam5','user_ldap','lastFeatureRefresh','1497017442'),('exam5','user_ldap','uid','exam5'),('guest1','files_external','config_version','0.5.0'),('guest1','user_ldap','displayName','Guest 1'),('guest1','user_ldap','homePath',''),('guest1','user_ldap','lastFeatureRefresh','1497017442'),('guest1','user_ldap','uid','guest1'),('guest10','files_external','config_version','0.5.0'),('guest10','user_ldap','displayName','Guest 10'),('guest10','user_ldap','homePath',''),('guest10','user_ldap','lastFeatureRefresh','1497017442'),('guest10','user_ldap','uid','guest10'),('guest2','files_external','config_version','0.5.0'),('guest2','user_ldap','displayName','Guest 2'),('guest2','user_ldap','homePath',''),('guest2','user_ldap','lastFeatureRefresh','1497017442'),('guest2','user_ldap','uid','guest2'),('guest3','files_external','config_version','0.5.0'),('guest3','user_ldap','displayName','Guest 3'),('guest3','user_ldap','homePath',''),('guest3','user_ldap','lastFeatureRefresh','1497017442'),('guest3','user_ldap','uid','guest3'),('guest4','files_external','config_version','0.5.0'),('guest4','user_ldap','displayName','Guest 4'),('guest4','user_ldap','homePath',''),('guest4','user_ldap','lastFeatureRefresh','1497017442'),('guest4','user_ldap','uid','guest4'),('guest5','files_external','config_version','0.5.0'),('guest5','user_ldap','displayName','Guest 5'),('guest5','user_ldap','homePath',''),('guest5','user_ldap','lastFeatureRefresh','1497017442'),('guest5','user_ldap','uid','guest5'),('guest6','files_external','config_version','0.5.0'),('guest6','user_ldap','displayName','Guest 6'),('guest6','user_ldap','homePath',''),('guest6','user_ldap','lastFeatureRefresh','1497017442'),('guest6','user_ldap','uid','guest6'),('guest7','files_external','config_version','0.5.0'),('guest7','user_ldap','displayName','Guest 7'),('guest7','user_ldap','homePath',''),('guest7','user_ldap','lastFeatureRefresh','1497017442'),('guest7','user_ldap','uid','guest7'),('guest8','files_external','config_version','0.5.0'),('guest8','user_ldap','displayName','Guest 8'),('guest8','user_ldap','homePath',''),('guest8','user_ldap','lastFeatureRefresh','1497017442'),('guest8','user_ldap','uid','guest8'),('guest9','files_external','config_version','0.5.0'),('guest9','user_ldap','displayName','Guest 9'),('guest9','user_ldap','homePath',''),('guest9','user_ldap','lastFeatureRefresh','1497017442'),('guest9','user_ldap','uid','guest9'),('ismith','files_external','config_version','0.5.0'),('ismith','user_ldap','displayName','Ian Smith'),('ismith','user_ldap','homePath',''),('ismith','user_ldap','lastFeatureRefresh','1497017442'),('ismith','user_ldap','uid','ismith'),('jjones','files_external','config_version','0.5.0'),('jjones','user_ldap','displayName','John Jones'),('jjones','user_ldap','homePath',''),('jjones','user_ldap','lastFeatureRefresh','1497017442'),('jjones','user_ldap','uid','jjones'),('profileuser','files_external','config_version','0.5.0'),('profileuser','user_ldap','displayName','Profile User'),('profileuser','user_ldap','homePath',''),('profileuser','user_ldap','lastFeatureRefresh','1497017442'),('profileuser','user_ldap','uid','profileuser'),('sysadmin','files_external','config_version','0.5.0'),('sysadmin','user_ldap','displayName','Sysadmin User'),('sysadmin','user_ldap','homePath',''),('sysadmin','user_ldap','lastFeatureRefresh','1497017442'),('sysadmin','user_ldap','uid','sysadmin'),('tech1','files_external','config_version','0.5.0'),('tech1','user_ldap','displayName','Tech 1'),('tech1','user_ldap','homePath',''),('tech1','user_ldap','lastFeatureRefresh','1497017442'),('tech1','user_ldap','uid','tech1'),('tech2','files_external','config_version','0.5.0'),('tech2','user_ldap','displayName','Tech 2'),('tech2','user_ldap','homePath',''),('tech2','user_ldap','lastFeatureRefresh','1497017442'),('tech2','user_ldap','uid','tech2'),('tech3','files_external','config_version','0.5.0'),('tech3','user_ldap','displayName','Tech 3'),('tech3','user_ldap','homePath',''),('tech3','user_ldap','lastFeatureRefresh','1497017442'),('tech3','user_ldap','uid','tech3'),('tech4','files_external','config_version','0.5.0'),('tech4','user_ldap','displayName','Tech 4'),('tech4','user_ldap','homePath',''),('tech4','user_ldap','lastFeatureRefresh','1497017442'),('tech4','user_ldap','uid','tech4');
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
  `user` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `app` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `key` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `value` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`keyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `userid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `propertypath` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `propertyname` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `propertyvalue` longtext COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_index` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_properties`
--

LOCK TABLES `oc_properties` WRITE;
/*!40000 ALTER TABLE `oc_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_reader_bookmarks`
--

DROP TABLE IF EXISTS `oc_reader_bookmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_reader_bookmarks` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `file_id` bigint(20) unsigned NOT NULL,
  `type` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `name` varchar(512) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `value` varchar(512) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `content` varchar(4096) COLLATE utf8mb4_bin DEFAULT NULL,
  `last_modified` bigint(20) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `reader_bookmarks_file_id_index` (`file_id`),
  KEY `reader_bookmarks_user_id_index` (`user_id`),
  KEY `reader_bookmarks_name_index` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_reader_bookmarks`
--

LOCK TABLES `oc_reader_bookmarks` WRITE;
/*!40000 ALTER TABLE `oc_reader_bookmarks` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_reader_bookmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_reader_preferences`
--

DROP TABLE IF EXISTS `oc_reader_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_reader_preferences` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `file_id` bigint(20) unsigned NOT NULL,
  `scope` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `name` varchar(128) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `value` varchar(4096) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `last_modified` bigint(20) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `reader_preferences_file_id_index` (`file_id`),
  KEY `reader_preferences_user_id_index` (`user_id`),
  KEY `reader_preferences_scope_index` (`scope`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_reader_preferences`
--

LOCK TABLES `oc_reader_preferences` WRITE;
/*!40000 ALTER TABLE `oc_reader_preferences` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_reader_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_richdocuments_member`
--

DROP TABLE IF EXISTS `oc_richdocuments_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_richdocuments_member` (
  `member_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Unique per user and session',
  `uid` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `color` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `last_activity` int(10) unsigned DEFAULT NULL,
  `is_guest` smallint(5) unsigned NOT NULL DEFAULT '0',
  `token` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `status` smallint(5) unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `owner_uid` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `editor_uid` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `fileid` int(11) NOT NULL,
  `version` int(11) NOT NULL DEFAULT '0',
  `canwrite` tinyint(1) NOT NULL DEFAULT '0',
  `server_host` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT 'localhost',
  `token` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `expiry` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rd_wopi_token_idx` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `principaluri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `calendardata` longblob,
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `lastmodified` int(10) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `share_with` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `uid_owner` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `uid_initiator` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `parent` int(11) DEFAULT NULL,
  `item_type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `item_source` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `item_target` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `file_source` int(11) DEFAULT NULL,
  `file_target` varchar(512) COLLATE utf8mb4_bin DEFAULT NULL,
  `permissions` smallint(6) NOT NULL DEFAULT '0',
  `stime` bigint(20) NOT NULL DEFAULT '0',
  `accepted` smallint(6) NOT NULL DEFAULT '0',
  `expiration` datetime DEFAULT NULL,
  `token` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `mail_send` smallint(6) NOT NULL DEFAULT '0',
  `share_name` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `item_share_type_index` (`item_type`,`share_type`),
  KEY `file_source_index` (`file_source`),
  KEY `token_index` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `remote` varchar(512) COLLATE utf8mb4_bin NOT NULL COMMENT 'Url of the remove owncloud instance',
  `remote_id` int(11) NOT NULL DEFAULT '-1',
  `share_token` varchar(64) COLLATE utf8mb4_bin NOT NULL COMMENT 'Public share token',
  `password` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'Optional password for the public share',
  `name` varchar(64) COLLATE utf8mb4_bin NOT NULL COMMENT 'Original name on the remote server',
  `owner` varchar(64) COLLATE utf8mb4_bin NOT NULL COMMENT 'User that owns the public share on the remote server',
  `user` varchar(64) COLLATE utf8mb4_bin NOT NULL COMMENT 'Local user which added the external share',
  `mountpoint` varchar(4000) COLLATE utf8mb4_bin NOT NULL COMMENT 'Full path where the share is mounted',
  `mountpoint_hash` varchar(32) COLLATE utf8mb4_bin NOT NULL COMMENT 'md5 hash of the mountpoint',
  `accepted` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `sh_external_mp` (`user`,`mountpoint_hash`),
  KEY `sh_external_user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_share_external`
--

LOCK TABLES `oc_share_external` WRITE;
/*!40000 ALTER TABLE `oc_share_external` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_share_external` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_spreedme_messages`
--

DROP TABLE IF EXISTS `oc_spreedme_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_spreedme_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `recipient` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `sessionId` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `object` longtext COLLATE utf8mb4_bin NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_spreedme_messages`
--

LOCK TABLES `oc_spreedme_messages` WRITE;
/*!40000 ALTER TABLE `oc_spreedme_messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_spreedme_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_spreedme_room_participants`
--

DROP TABLE IF EXISTS `oc_spreedme_room_participants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_spreedme_room_participants` (
  `userId` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `roomId` int(11) NOT NULL,
  `lastPing` int(11) NOT NULL,
  `sessionId` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_spreedme_room_participants`
--

LOCK TABLES `oc_spreedme_room_participants` WRITE;
/*!40000 ALTER TABLE `oc_spreedme_room_participants` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_spreedme_room_participants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_spreedme_rooms`
--

DROP TABLE IF EXISTS `oc_spreedme_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_spreedme_rooms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `token` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `type` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `unique_token` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_spreedme_rooms`
--

LOCK TABLES `oc_spreedme_rooms` WRITE;
/*!40000 ALTER TABLE `oc_spreedme_rooms` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_spreedme_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_storages`
--

DROP TABLE IF EXISTS `oc_storages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_storages` (
  `id` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `numeric_id` int(11) NOT NULL AUTO_INCREMENT,
  `available` int(11) NOT NULL DEFAULT '1',
  `last_checked` int(11) DEFAULT NULL,
  PRIMARY KEY (`numeric_id`),
  UNIQUE KEY `storages_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('local::/home/nextcloud/data/',1,1,NULL),('home::admin',2,1,NULL),('home::exam1',3,1,NULL),('home::exam2',4,1,NULL),('home::exam3',5,1,NULL),('home::exam4',6,1,NULL),('home::exam5',7,1,NULL),('home::guest1',8,1,NULL),('home::guest10',9,1,NULL),('home::guest2',10,1,NULL),('home::guest3',11,1,NULL),('home::guest4',12,1,NULL),('home::guest5',13,1,NULL),('home::guest6',14,1,NULL),('home::guest7',15,1,NULL),('home::guest8',16,1,NULL),('home::guest9',17,1,NULL),('home::ismith',18,1,NULL),('home::jjones',19,1,NULL),('home::profileuser',20,1,NULL),('home::sysadmin',21,1,NULL),('home::tech1',22,1,NULL),('home::tech2',23,1,NULL),('home::tech3',24,1,NULL),('home::tech4',25,1,NULL);
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
  `name` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `visibility` smallint(6) NOT NULL DEFAULT '1',
  `editable` smallint(6) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_ident` (`name`,`visibility`,`editable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `gid` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`gid`,`systemtagid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `objectid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `objecttype` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `systemtagid` int(10) unsigned NOT NULL DEFAULT '0',
  UNIQUE KEY `mapping` (`objecttype`,`objectid`,`systemtagid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `url` varchar(512) COLLATE utf8mb4_bin NOT NULL COMMENT 'Url of trusted server',
  `url_hash` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '' COMMENT 'sha1 hash of the url without the protocol',
  `token` varchar(128) COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'token used to exchange the shared secret',
  `shared_secret` varchar(256) COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'shared secret used to authenticate',
  `status` int(11) NOT NULL DEFAULT '2' COMMENT 'current status of the connection',
  `sync_token` varchar(512) COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'cardDav sync token',
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_hash` (`url_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_trusted_servers`
--

LOCK TABLES `oc_trusted_servers` WRITE;
/*!40000 ALTER TABLE `oc_trusted_servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_trusted_servers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_twofactor_backupcodes`
--

DROP TABLE IF EXISTS `oc_twofactor_backupcodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_twofactor_backupcodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `code` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `used` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `twofactor_backupcodes_uid` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_twofactor_backupcodes`
--

LOCK TABLES `oc_twofactor_backupcodes` WRITE;
/*!40000 ALTER TABLE `oc_twofactor_backupcodes` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_twofactor_backupcodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_users`
--

DROP TABLE IF EXISTS `oc_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_users` (
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `displayname` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_users`
--

LOCK TABLES `oc_users` WRITE;
/*!40000 ALTER TABLE `oc_users` DISABLE KEYS */;
INSERT INTO `oc_users` VALUES ('admin',NULL,'1|$2y$10$U4LDR9StQbqMPijYHT.ET.ywIb.0XkdGbhzxCR7xp/UKhc1g.U/Vq');
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
  `uid` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `category` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `uid_index` (`uid`),
  KEY `type_index` (`type`),
  KEY `category_index` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`categoryid`,`objid`,`type`),
  KEY `vcategory_objectd_index` (`objid`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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

-- Dump completed on 2017-06-09 15:18:58
