-- MySQL dump 10.15  Distrib 10.0.33-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: nextcloud
-- ------------------------------------------------------
-- Server version	10.0.31-MariaDB-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
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
INSERT INTO `oc_activity` VALUES (1,1497074828,30,'calendar','system','system','dav','calendar_add_self','[\"system\",\"Contact birthdays\"]','','[]','','','calendar',1);
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
  `addressbookid` bigint(20) NOT NULL,
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
INSERT INTO `oc_admin_sections` VALUES ('activity','OCA\\Activity\\Settings\\Section',55),('externalstorages','OCA\\Files_External\\Settings\\Section',10),('ldap','OCA\\User_LDAP\\Settings\\Section',25),('logging','OCA\\LogReader\\Settings\\Section',90),('richdocuments','OCA\\Richdocuments\\Settings\\Section',75),('serverinfo','OCA\\ServerInfo\\Settings\\AdminSection',0),('survey_client','OCA\\Survey_Client\\Settings\\AdminSection',80),('talk','OCA\\Spreed\\Settings\\Admin\\Section',70),('theming','OCA\\Theming\\Settings\\Section',30),('workflow','OCA\\WorkflowEngine\\Settings\\Section',55);
/*!40000 ALTER TABLE `oc_admin_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_admin_settings`
--

DROP TABLE IF EXISTS `oc_admin_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_admin_settings` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `section` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `priority` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_settings_class` (`class`),
  KEY `admin_settings_section` (`section`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_admin_settings`
--

LOCK TABLES `oc_admin_settings` WRITE;
/*!40000 ALTER TABLE `oc_admin_settings` DISABLE KEYS */;
INSERT INTO `oc_admin_settings` VALUES (1,'OCA\\FederatedFileSharing\\Settings\\Admin','sharing',20),(2,'OCA\\Activity\\Settings\\Admin','activity',55),(3,'OCA\\Password_Policy\\Settings','security',50),(4,'OCA\\SystemTags\\Settings\\Admin','workflow',70),(5,'OCA\\LogReader\\Settings\\Admin','logging',90),(6,'OCA\\ShareByMail\\Settings\\Admin','sharing',40),(7,'OCA\\NextcloudAnnouncements\\Settings\\Admin','additional',30),(8,'OCA\\Theming\\Settings\\Admin','theming',5),(9,'OCA\\ServerInfo\\Settings\\AdminSettings','serverinfo',0),(10,'OCA\\UpdateNotification\\Controller\\AdminController','server',1),(11,'OCA\\Survey_Client\\Settings\\AdminSettings','survey_client',50),(12,'OCA\\OAuth2\\Settings\\Admin','security',0),(13,'OCA\\Files\\Settings\\Admin','additional',5),(14,'OCA\\Federation\\Settings\\Admin','sharing',30),(16,'OCA\\Files_External\\Settings\\Admin','externalstorages',40),(17,'OCA\\User_LDAP\\Settings\\Admin','ldap',5),(19,'OCA\\DAV\\Settings\\CalDAVSettings','additional',20),(20,'OCA\\Richdocuments\\Settings\\Admin','richdocuments',0),(21,'OCA\\BruteForceSettings\\Settings\\IPWhitelist','security',50),(22,'OCA\\Spreed\\Settings\\Admin\\TurnServer','talk',70),(23,'OCA\\Spreed\\Settings\\Admin\\StunServer','talk',65),(24,'OCA\\Spreed\\Settings\\Admin\\SignalingServer','talk',75);
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.6.1'),('activity','types','filesystem'),('backgroundjob','lastjob','5'),('bruteforcesettings','enabled','yes'),('bruteforcesettings','installed_version','1.0.3'),('bruteforcesettings','types',''),('comments','enabled','yes'),('comments','installed_version','1.3.0'),('comments','types','logging'),('core','installed.bundles','[\"CoreBundle\"]'),('core','installedat','1497074451.3496'),('core','lastcron','1519457736'),('core','lastupdateResult','{\"version\":\"13.0.0.14\",\"versionstring\":\"Nextcloud 13.0.0\",\"url\":\"https:\\/\\/download.nextcloud.com\\/server\\/releases\\/nextcloud-13.0.0.zip\",\"web\":\"https:\\/\\/docs.nextcloud.com\\/server\\/12\\/admin_manual\\/maintenance\\/upgrade.html\",\"autoupdater\":\"1\",\"signature\":\"q5bqFR15JaWW6oGM+iNtC7JoDsRHPXAkySJ5TMgcbAfajheMUwgQtytK2S1vpJd7\\nUbhO5CfWStBQKFNR6\\/tV6R++xLbIBZgXhvjLtpciug+dNBMANZNUiqEbdYLZSWEp\\nY3HOk087s3o0wazQ\\/kLDmFmCzW8bngpcI1rRDJTXCS6uf\\/0BVatOaIoByJRkArnw\\nir+Hd8swyREt3jrngeePu6\\/ZrB+5toGcEHaSCmTNwJ7ipKnwi3mPP0XcGWJVswzY\\nWpeJUBR9OkzLQ8Y6sKIEOZrDBsoSjFp0YN6Adgbxgbd4UPwgaJVOFdfuW18RNWWw\\nTx\\/vStIU+zA9\\/Yan\\/RotKg==\"}'),('core','lastupdatedat','0'),('core','moveavatarsdone','yes'),('core','oc.integritycheck.checker','[]'),('core','previewsCleanedUp','1'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('core','scss.variables','0bb3ffaff208485903890df6887dce03'),('core','updater.secret.created','1519457069'),('core','vendor','nextcloud'),('dav','buildCalendarSearchIndex','yes'),('dav','enabled','yes'),('dav','installed_version','1.4.6'),('dav','types','filesystem'),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','1.3.1'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','1.3.0'),('federation','types','authentication'),('files','cronjob_scan_files','500'),('files','enabled','yes'),('files','installed_version','1.8.0'),('files','types','filesystem'),('files_external','enabled','yes'),('files_external','installed_version','1.4.1'),('files_external','ocsid','166048'),('files_external','types','filesystem'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','1.2.0'),('files_pdfviewer','types',''),('files_reader','enabled','yes'),('files_reader','installed_version','1.2.2'),('files_reader','ocsid','167127'),('files_reader','types','filesystem'),('files_sharing','enabled','yes'),('files_sharing','installed_version','1.5.0'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.5.1'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','1.3.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.6.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','1.2.0'),('files_videoplayer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','2.2.1'),('firstrunwizard','types','logging'),('gallery','enabled','yes'),('gallery','installed_version','18.0.0'),('gallery','types',''),('logreader','enabled','yes'),('logreader','installed_version','2.0.0'),('logreader','ocsid','170871'),('logreader','types',''),('lookup_server_connector','enabled','yes'),('lookup_server_connector','installed_version','1.1.0'),('lookup_server_connector','types','authentication'),('nextcloud_announcements','enabled','yes'),('nextcloud_announcements','installed_version','1.2.0'),('nextcloud_announcements','pub_date','Sat, 10 Dec 2016 00:00:00 +0100'),('nextcloud_announcements','types','logging'),('notes','enabled','yes'),('notes','installed_version','2.3.2'),('notes','ocsid','174554'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','2.1.2'),('notifications','types','logging'),('oauth2','enabled','yes'),('oauth2','installed_version','1.1.0'),('oauth2','types','authentication'),('password_policy','enabled','yes'),('password_policy','installed_version','1.3.0'),('password_policy','types',''),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','1.3.0'),('provisioning_api','types','prevent_group_restriction'),('richdocuments','enabled','yes'),('richdocuments','installed_version','2.0.3'),('richdocuments','types','prevent_group_restriction'),('richdocuments','wopi_url','https://CHANGETHISREALM'),('serverinfo','enabled','yes'),('serverinfo','installed_version','1.3.0'),('serverinfo','types',''),('sharebymail','enabled','yes'),('sharebymail','installed_version','1.3.0'),('sharebymail','types','filesystem'),('spreed','enabled','yes'),('spreed','installed_version','3.1.0'),('spreed','stun_servers','[\"stun.nextcloud.com:443\"]'),('spreed','types','prevent_group_restriction'),('survey_client','enabled','yes'),('survey_client','installed_version','1.1.0'),('survey_client','types',''),('systemtags','enabled','yes'),('systemtags','installed_version','1.3.0'),('systemtags','types','logging'),('tasks','enabled','yes'),('tasks','installed_version','0.9.6'),('tasks','ocsid','164356'),('tasks','types',''),('theming','enabled','yes'),('theming','installed_version','1.4.1'),('theming','types','logging'),('twofactor_backupcodes','enabled','yes'),('twofactor_backupcodes','installed_version','1.2.3'),('twofactor_backupcodes','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','1.3.0'),('updatenotification','types',''),('user_ldap','_lastChange','1519457715'),('user_ldap','cleanUpJobOffset','0'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','0'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','1.3.1'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_default_ppolicy_dn',''),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr','sAMAccountName'),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_gid_number','gidNumber'),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(|(objectclass=posixAccount))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_turn_on_pwd_change','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','posixAccount'),('user_ldap','ldap_userlist_filter','(|(objectclass=posixAccount))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1'),('workflowengine','enabled','yes'),('workflowengine','installed_version','1.3.0'),('workflowengine','types','filesystem');
/*!40000 ALTER TABLE `oc_appconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_authtoken`
--

DROP TABLE IF EXISTS `oc_authtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_authtoken` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
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
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
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
  `calendarid` bigint(20) NOT NULL,
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
  `calendarid` bigint(20) unsigned NOT NULL,
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
INSERT INTO `oc_calendars` VALUES (1,'principals/system/system','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT',0);
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
  `addressbookid` bigint(20) NOT NULL DEFAULT '0',
  `carddata` longblob,
  `uri` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `lastmodified` bigint(20) unsigned DEFAULT NULL,
  `etag` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `size` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_E98F2EC48B26C2E9` (`addressbookid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_cards`
--

LOCK TABLES `oc_cards` WRITE;
/*!40000 ALTER TABLE `oc_cards` DISABLE KEYS */;
INSERT INTO `oc_cards` VALUES (1,1,'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:-//Sabre//Sabre VObject 4.1.2//EN\r\nUID:admin\r\nFN:admin\r\nN:admin;;;;\r\nCLOUD:admin@www.constellations.com/nextcloud\r\nEND:VCARD\r\n','Database:admin.vcf',1497074828,'ededc66b442a55c9138b6b13e0ed938b',159);
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
  KEY `card_value_index` (`value`),
  KEY `IDX_811F5CFA8B26C2E9` (`addressbookid`)
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
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `parent_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `topmost_parent_id` bigint(20) unsigned NOT NULL DEFAULT '0',
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
INSERT INTO `oc_credentials` VALUES ('admin','password::logincredentials/credentials','11f4057ed7b4458d8704975b7c797c982f9b8f36a1e08958f678ae53f159ebc2df13c7de9a5aa448c89f864e49d0cdd4|wfooBjBKrKXpgnck|b91471e55c056de2397141ec3ff88a5cd520ae32b3c6afc5e350bab69ade0660b7c1d13f9d006d212111696db6b3d67f1eeb86f84ab68352d0ecf8fe7843fca7');
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
  `resourceid` bigint(20) unsigned NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_applicable`
--

LOCK TABLES `oc_external_applicable` WRITE;
/*!40000 ALTER TABLE `oc_external_applicable` DISABLE KEYS */;
INSERT INTO `oc_external_applicable` VALUES (2,2,1,NULL),(8,8,1,NULL),(1,1,2,'itadmin'),(3,3,2,'itadmin'),(5,5,2,'itadmin'),(4,4,2,'officestaff'),(6,6,2,'officestaff'),(7,7,2,'staff');
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_config`
--

LOCK TABLES `oc_external_config` WRITE;
/*!40000 ALTER TABLE `oc_external_config` DISABLE KEYS */;
INSERT INTO `oc_external_config` VALUES (1,1,'host','CHANGETHISREALM'),(2,1,'share','dfs/applications'),(3,1,'root',''),(4,1,'domain',''),(5,2,'host','CHANGETHISREALM'),(6,2,'share','dfs/homes/$user'),(7,2,'root',''),(8,2,'domain',''),(9,3,'host','CHANGETHISREALM'),(10,3,'share','dfs/itadminshare'),(11,3,'root',''),(12,3,'domain',''),(13,4,'host','CHANGETHISREALM'),(14,4,'share','dfs/officeshare'),(15,4,'root',''),(16,4,'domain',''),(17,5,'host','CHANGETHISREALM'),(18,5,'share','dfs/staffshare'),(19,5,'root',''),(20,5,'domain',''),(21,6,'host','CHANGETHISREALM'),(22,6,'share','dfs/staffshare'),(23,6,'root',''),(24,6,'domain',''),(25,7,'host','CHANGETHISREALM'),(26,7,'share','dfs/staffshare'),(27,7,'root',''),(28,7,'domain',''),(29,8,'host','CHANGETHISREALM'),(30,8,'share','dfs/subjects'),(31,8,'root',''),(32,8,'domain','');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_mounts`
--

LOCK TABLES `oc_external_mounts` WRITE;
/*!40000 ALTER TABLE `oc_external_mounts` DISABLE KEYS */;
INSERT INTO `oc_external_mounts` VALUES (1,'/applications','smb','password::logincredentials',100,1),(2,'/home','smb','password::logincredentials',100,1),(3,'/itadminshare','smb','password::logincredentials',100,1),(4,'/officeshare','smb','password::logincredentials',100,1),(5,'/staffshare','smb','password::logincredentials',100,1),(6,'/staffshare','smb','password::logincredentials',100,1),(7,'/staffshare','smb','password::logincredentials',100,1),(8,'/subjects','smb','password::logincredentials',100,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_options`
--

LOCK TABLES `oc_external_options` WRITE;
/*!40000 ALTER TABLE `oc_external_options` DISABLE KEYS */;
INSERT INTO `oc_external_options` VALUES (1,1,'encrypt','true'),(2,1,'previews','true'),(3,1,'filesystem_check_changes','1'),(4,1,'enable_sharing','false'),(5,2,'encrypt','true'),(6,2,'previews','true'),(7,2,'filesystem_check_changes','1'),(8,2,'enable_sharing','false'),(9,3,'encrypt','true'),(10,3,'previews','true'),(11,3,'filesystem_check_changes','1'),(12,3,'enable_sharing','false'),(13,4,'encrypt','true'),(14,4,'previews','true'),(15,4,'filesystem_check_changes','1'),(16,4,'enable_sharing','false'),(17,5,'encrypt','true'),(18,5,'previews','true'),(19,5,'filesystem_check_changes','1'),(20,5,'enable_sharing','false'),(21,6,'encrypt','true'),(22,6,'previews','true'),(23,6,'filesystem_check_changes','1'),(24,6,'enable_sharing','false'),(25,7,'encrypt','true'),(26,7,'previews','true'),(27,7,'filesystem_check_changes','1'),(28,7,'enable_sharing','false'),(29,8,'encrypt','true'),(30,8,'previews','true'),(31,8,'filesystem_check_changes','1'),(32,8,'enable_sharing','false');
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
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `lock` int(11) NOT NULL DEFAULT '0',
  `key` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `ttl` int(11) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `lock_key_index` (`key`),
  KEY `lock_ttl_index` (`ttl`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (1,0,'files/468c740695b998c9b920835b3af18225',1497078064),(2,0,'files/3ef927705e35f104f5c8825610e550db',1497078078),(3,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1497078064),(4,0,'files/bc76dde1a029b9698a1164dc9d6f4422',1497078078);
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
) ENGINE=InnoDB AUTO_INCREMENT=253 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,5836327,1519457735,1519457055,0,0,'5a9115c7185d7',23,''),(2,1,'appdata_ocodxjl8m9zm','af28c0efe18fdfef2e06334b355ac0c3',1,'appdata_ocodxjl8m9zm',2,1,2414872,1497075930,1497074926,0,0,'593b90da5c1ac',31,''),(3,1,'appdata_ocodxjl8m9zm/appstore','13f6fffdda1e7869da5e8defd4388455',2,'appstore',2,1,297568,1497075912,1497074510,0,0,'593b90c856e92',31,''),(4,1,'appdata_ocodxjl8m9zm/appstore/apps.json','31d77b83f9ae89a75bcd5ba7601b4073',3,'apps.json',4,3,265035,1497075912,1497075912,0,0,'0acf91d4492ea240f6ef034390f5c80a',27,''),(5,1,'appdata_ocodxjl8m9zm/preview','e2b08cfb1dca6e3be51c9dbc05efd711',2,'preview',2,1,0,1497074452,1497074452,0,0,'593b8b1432920',31,''),(6,2,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,6823068,1519457013,1519457013,0,0,'5a9112f5d9f14',23,''),(7,2,'files','45b963397aa40d4a0063e0d85e4fe7a1',6,'files',2,1,6823068,1497074453,1497074453,0,0,'593b8b158adab',31,''),(8,2,'files/Nextcloud.mp4','77a79c09b93e57cba23c11eb0e6048a6',7,'Nextcloud.mp4',6,5,462413,1497074453,1497074453,0,0,'ee76fd244d6d96c2643fd0471ec079a3',27,''),(9,2,'files/Nextcloud Manual.pdf','2bc58a43566a8edde804a4a97a9c7469',7,'Nextcloud Manual.pdf',7,3,3922148,1497074453,1497074453,0,0,'9c26dac40150d7f017831573768845ea',27,''),(10,2,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',7,'Photos',2,1,2360011,1497074453,1497074453,0,0,'593b8b1578a41',31,''),(11,2,'files/Photos/Nut.jpg','aa8daeb975e1d39412954fd5cd41adb4',10,'Nut.jpg',9,8,955026,1497074453,1497074453,0,0,'b1619da0f6d425288960b707ca0c13f0',27,''),(12,2,'files/Photos/Coast.jpg','a6fe87299d78b207e9b7aba0f0cb8a0a',10,'Coast.jpg',9,8,819766,1497074453,1497074453,0,0,'c539e8fcb7aa699da1812143b44ee05a',27,''),(13,2,'files/Photos/Hummingbird.jpg','e077463269c404ae0f6f8ea7f2d7a326',10,'Hummingbird.jpg',9,8,585219,1497074453,1497074453,0,0,'60b51fdebcc25944d49dbe60877d4ad9',27,''),(14,2,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',7,'Documents',2,1,78496,1497074453,1497074453,0,0,'593b8b158adab',31,''),(15,2,'files/Documents/About.odt','b2ee7d56df9f34a0195d4b611376e885',14,'About.odt',10,3,77422,1497074453,1497074453,0,0,'1eecc1b90f3edb37bc5c5f1569ab2bec',27,''),(16,2,'files/Documents/About.txt','9da7b739e7a65d74793b2881da521169',14,'About.txt',12,11,1074,1497074453,1497074453,0,0,'a896adca31a8ee83790d719b50867a36',27,''),(17,1,'appdata_ocodxjl8m9zm/avatar','2550859f0f997571133517a9d5a8aff4',2,'avatar',2,1,0,1497074455,1497074455,0,0,'593b8b17c9b68',31,''),(18,1,'appdata_ocodxjl8m9zm/avatar/admin','ae9f573ef95031e3427b926e7c68d743',17,'admin',2,1,0,1497074455,1497074455,0,0,'593b8b17c7e33',31,''),(19,1,'appdata_ocodxjl8m9zm/js','b5be92c25d77cf1222d9f90df8abb942',2,'js',2,1,1982162,1497075930,1497074457,0,0,'593b90da5c1ac',31,''),(20,1,'appdata_ocodxjl8m9zm/js/core','15ec51c9de49fcccc4bcc58051750f6c',19,'core',2,1,343719,1497075930,1497075930,0,0,'593b90da5c1ac',31,''),(21,1,'appdata_ocodxjl8m9zm/js/core/merged-template-prepend.js','45a94153084e313d7f06575df59ff660',20,'merged-template-prepend.js',13,3,142144,1497074455,1497074455,0,0,'8e6cc39f7e0962c4a189d7993cc82d62',27,''),(22,1,'appdata_ocodxjl8m9zm/js/core/merged-template-prepend.js.deps','d7404b1f0bf6c8ca1506b3f65ad6c33c',20,'merged-template-prepend.js.deps',14,3,1146,1497074455,1497074455,0,0,'16554de800530912c1a31cd577dd3b82',27,''),(23,1,'appdata_ocodxjl8m9zm/js/core/merged-template-prepend.js.gzip','bfc6435a164159e869f8bcc3dbcfc245',20,'merged-template-prepend.js.gzip',15,3,39023,1497074455,1497074455,0,0,'78efb7f5b9ae4a00310a6c5a4f65b04e',27,''),(24,1,'appdata_ocodxjl8m9zm/js/core/merged-share-backend.js','73a9986212d0bed04bb429ae82ed1e4b',20,'merged-share-backend.js',13,3,104522,1497074456,1497074456,0,0,'af04b93fcb54dd72177c7af0a7bed0d8',27,''),(25,1,'appdata_ocodxjl8m9zm/js/core/merged-share-backend.js.deps','79093b9b8e23efe1d43624e15b8c4910',20,'merged-share-backend.js.deps',14,3,752,1497074456,1497074456,0,0,'19e923272ae1a1b7e7af160597af91bb',27,''),(26,1,'appdata_ocodxjl8m9zm/js/core/merged-share-backend.js.gzip','ef1f137ce626b99d9c92dc8781054846',20,'merged-share-backend.js.gzip',15,3,22508,1497074456,1497074456,0,0,'560eaa45554adaa4c2cbf6b815d6d0b7',27,''),(27,1,'appdata_ocodxjl8m9zm/js/notifications','38070b0809a974cb284107cc1d62beb4',19,'notifications',2,1,25514,1497074456,1497074456,0,0,'593b8b184781e',31,''),(28,1,'appdata_ocodxjl8m9zm/js/notifications/merged.js','bb548eae525d91fe93177c2ed446e69e',27,'merged.js',13,3,20114,1497074456,1497074456,0,0,'0fed4578044d442f5d8ce453053481bd',27,''),(29,1,'appdata_ocodxjl8m9zm/js/notifications/merged.js.deps','0fb4382c59586c54e4cd013d381c95b8',27,'merged.js.deps',14,3,330,1497074456,1497074456,0,0,'9e217119d8c3d18a373f2f27866f4485',27,''),(30,1,'appdata_ocodxjl8m9zm/js/notifications/merged.js.gzip','4d7b919e31c315211167cfc4581eb693',27,'merged.js.gzip',15,3,5070,1497074456,1497074456,0,0,'4dd24adc29b3b8d7ab4c7b93f4553f0a',27,''),(31,1,'appdata_ocodxjl8m9zm/js/files','a7fa0d0186a47dbd52df2d8f131d1115',19,'files',2,1,398160,1497074456,1497074456,0,0,'593b8b1870572',31,''),(32,1,'appdata_ocodxjl8m9zm/js/files/merged-index.js','8a9eb608fdcee6a035e977013bb5f2c1',31,'merged-index.js',13,3,319781,1497074456,1497074456,0,0,'0733fa64b45fd1fe226b3752354a8c03',27,''),(33,1,'appdata_ocodxjl8m9zm/js/files/merged-index.js.deps','1999a5de76b47fd7fc833fbeecb9bf47',31,'merged-index.js.deps',14,3,2125,1497074456,1497074456,0,0,'5408701ff7bf9a3ffd50ba567a6547ca',27,''),(34,1,'appdata_ocodxjl8m9zm/js/files/merged-index.js.gzip','ee5d7e98f2845a627c459faa57cdcf0a',31,'merged-index.js.gzip',15,3,76254,1497074456,1497074456,0,0,'3980d6d0066f32179e0b3ff6ad920087',27,''),(35,1,'appdata_ocodxjl8m9zm/js/activity','8a68d70f11ac024771dd1ea5a8e12a5c',19,'activity',2,1,20399,1497074456,1497074456,0,0,'593b8b1888bfd',31,''),(36,1,'appdata_ocodxjl8m9zm/js/activity/activity-sidebar.js','115614c9c63f1be034bc8ac55d3b5f61',35,'activity-sidebar.js',13,3,15755,1497074456,1497074456,0,0,'5c6ea08b1b981d8d11c647e38b0dc842',27,''),(37,1,'appdata_ocodxjl8m9zm/js/activity/activity-sidebar.js.deps','0604d6a3bb01b7a9ceea1c732cde5f57',35,'activity-sidebar.js.deps',14,3,494,1497074456,1497074456,0,0,'8c623c7f13243441f4348eed5b5fcb5c',27,''),(38,1,'appdata_ocodxjl8m9zm/js/activity/activity-sidebar.js.gzip','1bf96c12bf1a5a16eb6252341e3d8273',35,'activity-sidebar.js.gzip',15,3,4150,1497074456,1497074456,0,0,'702ef9fba485232c1151dd69b308e380',27,''),(39,1,'appdata_ocodxjl8m9zm/js/comments','ed7c2bf1b87c78dee976f363c469fb1f',19,'comments',2,1,36996,1497074456,1497074456,0,0,'593b8b18a2303',31,''),(40,1,'appdata_ocodxjl8m9zm/js/comments/merged.js','a3cfc504e9a15f857169c4a467ef5ab0',39,'merged.js',13,3,28929,1497074456,1497074456,0,0,'dde0c699486af072084800af9827c618',27,''),(41,1,'appdata_ocodxjl8m9zm/js/comments/merged.js.deps','0afc98eb1ad7129c3dfeea07da84914e',39,'merged.js.deps',14,3,635,1497074456,1497074456,0,0,'49d06f0f4bb27cba9af504db3b53bbd3',27,''),(42,1,'appdata_ocodxjl8m9zm/js/comments/merged.js.gzip','149ba55a2ab0af81446d032488e08723',39,'merged.js.gzip',15,3,7432,1497074456,1497074456,0,0,'4719779dc0944a055719aceca0b39ec7',27,''),(43,1,'appdata_ocodxjl8m9zm/js/files_sharing','fd0126d6edb2eb6271a578a1e444dded',19,'files_sharing',2,1,20226,1497074456,1497074456,0,0,'593b8b18ba7ae',31,''),(44,1,'appdata_ocodxjl8m9zm/js/files_sharing/additionalScripts.js','59e5ffcffec01e6dae21b7bb12abacea',43,'additionalScripts.js',13,3,15161,1497074456,1497074456,0,0,'1ea093394a504ca2fa3e86a33e462e98',27,''),(45,1,'appdata_ocodxjl8m9zm/js/files_sharing/additionalScripts.js.deps','51a51398bcd28a494d0a1c5a5904a97d',43,'additionalScripts.js.deps',14,3,340,1497074456,1497074456,0,0,'2c03610b7f11b85ee04ff472eb881d6f',27,''),(46,1,'appdata_ocodxjl8m9zm/js/files_sharing/additionalScripts.js.gzip','5aa57465d14139ad4e74d0de5d509cd7',43,'additionalScripts.js.gzip',15,3,4725,1497074456,1497074456,0,0,'04d09c2a4a4bc2d859ebe509c8284780',27,''),(47,1,'appdata_ocodxjl8m9zm/js/files_texteditor','49ec1cc3261cfe576cf9bdbaac849469',19,'files_texteditor',2,1,820097,1497074456,1497074456,0,0,'593b8b18ecd9b',31,''),(48,1,'appdata_ocodxjl8m9zm/js/files_texteditor/merged.js','34cf9c40438c3177ee57a95f01672cff',47,'merged.js',13,3,681977,1497074456,1497074456,0,0,'c37cd1c3830cad1b41692f995bada09f',27,''),(49,1,'appdata_ocodxjl8m9zm/js/files_texteditor/merged.js.deps','04b124150ffffc36cfea62e7fceaa043',47,'merged.js.deps',14,3,370,1497074456,1497074456,0,0,'edc8b89096f8789f5db25a7f12330749',27,''),(50,1,'appdata_ocodxjl8m9zm/js/files_texteditor/merged.js.gzip','e86e98b67c487f49fa469c014158c3b6',47,'merged.js.gzip',15,3,137750,1497074456,1497074456,0,0,'9217ebb40a5313a3d6a6de4975f4c9bd',27,''),(51,1,'appdata_ocodxjl8m9zm/js/files_versions','060c654bff518e2984884d51cfd5bfc2',19,'files_versions',2,1,16725,1497074457,1497074457,0,0,'593b8b19139c1',31,''),(52,1,'appdata_ocodxjl8m9zm/js/files_versions/merged.js','a52dbdd5cdf827bc6c3ae8ee3e1916da',51,'merged.js',13,3,12719,1497074457,1497074457,0,0,'6db4d53ad7f41376aa816233064c66b0',27,''),(53,1,'appdata_ocodxjl8m9zm/js/files_versions/merged.js.deps','82194777580a9ff2aa32f9b3a43df766',51,'merged.js.deps',14,3,424,1497074457,1497074457,0,0,'dda1c91104a49ca43448ce029816393e',27,''),(54,1,'appdata_ocodxjl8m9zm/js/files_versions/merged.js.gzip','ab092dd428d4e8812d058402269582df',51,'merged.js.gzip',15,3,3582,1497074457,1497074457,0,0,'92279f9be00b43c77d3b0d42a9caa743',27,''),(55,1,'appdata_ocodxjl8m9zm/js/gallery','27f4d8de45f26c08ba1faef43e480e48',19,'gallery',2,1,280677,1497074457,1497074457,0,0,'593b8b19327d8',31,''),(56,1,'appdata_ocodxjl8m9zm/js/gallery/scripts-for-file-app.js','ab67c88d44046739434437465fe71af5',55,'scripts-for-file-app.js',13,3,225356,1497074457,1497074457,0,0,'223f15d81624a8e7095bd88baa635e44',27,''),(57,1,'appdata_ocodxjl8m9zm/js/gallery/scripts-for-file-app.js.deps','0e85e8fc0bebf931edebd94cb2f27cd1',55,'scripts-for-file-app.js.deps',14,3,856,1497074457,1497074457,0,0,'88b99ebe7160162e28b03b4b66d25588',27,''),(58,1,'appdata_ocodxjl8m9zm/js/gallery/scripts-for-file-app.js.gzip','d676c72c2798e404c46e4156a1df6f56',55,'scripts-for-file-app.js.gzip',15,3,54465,1497074457,1497074457,0,0,'2db0ee37f8bf29a6d3ebf9f424ba8c11',27,''),(59,1,'appdata_ocodxjl8m9zm/js/core/merged.js','31eb454f9fa80ba1a7603f3a91493c02',20,'merged.js',13,3,20224,1497074457,1497074457,0,0,'c5821dfd2e5a970a460bf99dc7034624',27,''),(60,1,'appdata_ocodxjl8m9zm/js/core/merged.js.deps','3289506c1992d2541e3867aa2596b6da',20,'merged.js.deps',14,3,508,1497074457,1497074457,0,0,'d75673023c13e9989fdb803379083675',27,''),(61,1,'appdata_ocodxjl8m9zm/js/core/merged.js.gzip','d04f319c85302e5ef89d672f589c33b5',20,'merged.js.gzip',15,3,5365,1497074457,1497074457,0,0,'78cea943ec3d18d9456ada47f40172ab',27,''),(62,1,'appdata_ocodxjl8m9zm/js/systemtags','ef33fdc3ed52957c2c855a9446a620d1',19,'systemtags',2,1,19649,1497074457,1497074457,0,0,'593b8b195d4d1',31,''),(63,1,'appdata_ocodxjl8m9zm/js/systemtags/merged.js','765b62ecae0527096455cdd1baa85129',62,'merged.js',13,3,14902,1497074457,1497074457,0,0,'44640a7f4439308d035136c2bf5d204a',27,''),(64,1,'appdata_ocodxjl8m9zm/js/systemtags/merged.js.deps','a9da170131dde08a8f88f1b9bfd48f46',62,'merged.js.deps',14,3,399,1497074457,1497074457,0,0,'06851c091044d826f36c66cdfcd9104d',27,''),(65,1,'appdata_ocodxjl8m9zm/js/systemtags/merged.js.gzip','1ee4687d4619ed9b89adfa1e8b1a6443',62,'merged.js.gzip',15,3,4348,1497074457,1497074457,0,0,'49f450a3263508f397ffb1097c82188d',27,''),(66,1,'appdata_ocodxjl8m9zm/css','da11e512d782a7e0ae43d5555c2a2d2f',2,'css',2,1,133025,1497074462,1497074462,0,0,'593b8b1e27ff4',31,''),(67,1,'appdata_ocodxjl8m9zm/css/core','9553d40e3b982cab8a1785768284c6fd',66,'core',2,1,97490,1497074460,1497074460,0,0,'593b8b1ca1e04',31,''),(68,1,'appdata_ocodxjl8m9zm/theming','16dba59ed234d8929bb71b7dc1380687',2,'theming',2,1,2117,1497074466,1497074465,0,0,'593b8b22362a4',31,''),(69,1,'appdata_ocodxjl8m9zm/css/core/server.css','1c85f585acc7a1e87e50ff3b1a59b433',67,'server.css',16,11,77314,1497074459,1497074459,0,0,'6ad2529f2364880f09934ec506f94d45',27,''),(70,1,'appdata_ocodxjl8m9zm/css/core/server.css.deps','c95b953de16f6cebcc215e6b0a6534a4',67,'server.css.deps',14,3,850,1497074459,1497074459,0,0,'4e520222016118f2a22dc357c85cc46a',27,''),(71,1,'appdata_ocodxjl8m9zm/css/core/server.css.gzip','853bb24be275bee95508bd1ac1e0172b',67,'server.css.gzip',15,3,13409,1497074459,1497074459,0,0,'b953059b218d35d06d59731a1c1f13a7',27,''),(72,1,'appdata_ocodxjl8m9zm/css/core/share.css','3386eed89b6691f2575f18af3ee32f61',67,'share.css',16,11,2848,1497074459,1497074459,0,0,'b3b00ea62c99af6f87837defe95c2a05',27,''),(73,1,'appdata_ocodxjl8m9zm/css/core/share.css.deps','086a8469d19ecee4f094a68f43b96889',67,'share.css.deps',14,3,133,1497074459,1497074459,0,0,'a342cd8bea9f69a4949f00168c9c4da5',27,''),(74,1,'appdata_ocodxjl8m9zm/css/core/share.css.gzip','23ba05f2e06adca4dfc2a10c1c6a8fb4',67,'share.css.gzip',15,3,994,1497074459,1497074459,0,0,'b9be933cd43a3eaecac539ccc462a3b9',27,''),(75,1,'appdata_ocodxjl8m9zm/css/files','9af9f883e4748b18ce0cd9883f514b87',66,'files',2,1,24966,1497074460,1497074460,0,0,'593b8b1c42c9c',31,''),(76,1,'appdata_ocodxjl8m9zm/css/files/merged.css','f1444c43b271a0193e21178f95500896',75,'merged.css',16,11,20250,1497074460,1497074460,0,0,'4b4cc62a6443d389823acb84db18b65f',27,''),(77,1,'appdata_ocodxjl8m9zm/css/files/merged.css.deps','6e0453f3c37f356175250a1376088fd1',75,'merged.css.deps',14,3,433,1497074460,1497074460,0,0,'f1e1a173649acb6156ad169a720178b1',27,''),(78,1,'appdata_ocodxjl8m9zm/css/files/merged.css.gzip','cf490948a62deabfa71ba165979dae51',75,'merged.css.gzip',15,3,4283,1497074460,1497074460,0,0,'f665908f545a4ca36fe4e4c683d36067',27,''),(79,1,'appdata_ocodxjl8m9zm/css/files_sharing','7744fa8c03b60f6f43773ee5623bdd6f',66,'files_sharing',2,1,3945,1497074460,1497074460,0,0,'593b8b1c6187d',31,''),(80,1,'appdata_ocodxjl8m9zm/css/files_sharing/mergedAdditionalStyles.css','63e8e7ece4590d1de3dcf4fb67a96fcd',79,'mergedAdditionalStyles.css',16,11,2727,1497074460,1497074460,0,0,'156b2018a9a682740832cf95dcf29b77',27,''),(81,1,'appdata_ocodxjl8m9zm/css/files_sharing/mergedAdditionalStyles.css.deps','22ce29def05a980a49309b34df988c92',79,'mergedAdditionalStyles.css.deps',14,3,340,1497074460,1497074460,0,0,'b719f4e30db80f25f10e4caddfe4f3af',27,''),(82,1,'appdata_ocodxjl8m9zm/css/files_sharing/mergedAdditionalStyles.css.gzip','f9457adc8b5b8cbfd0414272fed2facc',79,'mergedAdditionalStyles.css.gzip',15,3,878,1497074460,1497074460,0,0,'c6fb5ece6e005cd46eeeba1d15f2b028',27,''),(83,1,'appdata_ocodxjl8m9zm/css/files_texteditor','f604bbd421e1b8d0f3a62ccecd41869d',66,'files_texteditor',2,1,5377,1497074460,1497074460,0,0,'593b8b1c826c2',31,''),(84,1,'appdata_ocodxjl8m9zm/css/files_texteditor/merged.css','010f9a499b02f208c3ed743fde9aeab0',83,'merged.css',16,11,3774,1497074460,1497074460,0,0,'66caf5dd1b76993600bbeea6f578a169',27,''),(85,1,'appdata_ocodxjl8m9zm/css/files_texteditor/merged.css.deps','3366fd96cea3aa77a4178c65dd72d8f5',83,'merged.css.deps',14,3,419,1497074460,1497074460,0,0,'8ea5a638eaee5febf361e8a06241cde1',27,''),(86,1,'appdata_ocodxjl8m9zm/css/files_texteditor/merged.css.gzip','4da6060a35c77d512207c2e7b08cdfae',83,'merged.css.gzip',15,3,1184,1497074460,1497074460,0,0,'ca10985394f7bb6db6d1440ac3eff0c8',27,''),(87,1,'appdata_ocodxjl8m9zm/css/core/systemtags.css','755ed54f58990f210a863ce49c10cff4',67,'systemtags.css',16,11,1415,1497074460,1497074460,0,0,'e23fa533be71a5de3ba6b2a4213e114d',27,''),(88,1,'appdata_ocodxjl8m9zm/css/core/systemtags.css.deps','ad3afbad08d5fdf5cc1bab967d960b31',67,'systemtags.css.deps',14,3,138,1497074460,1497074460,0,0,'e438dc6dfb48499cee6b6fa5ebeb1a34',27,''),(89,1,'appdata_ocodxjl8m9zm/css/core/systemtags.css.gzip','fe05f988c5c17c5c81c07fdddf23764d',67,'systemtags.css.gzip',15,3,389,1497074460,1497074460,0,0,'03cef305259788b070f3fb016985b26b',27,''),(90,1,'appdata_ocodxjl8m9zm/css/theming','6c1f5cfc17b38608533be293516aacd7',66,'theming',2,1,1247,1497074462,1497074462,0,0,'593b8b1e27ff4',31,''),(91,1,'appdata_ocodxjl8m9zm/css/theming/theming.css','41bada8ebbfff4c836ba99771ef1902e',90,'theming.css',16,11,790,1497074462,1497074462,0,0,'8d7c8bebd294039d137aa09ba0c0d970',27,''),(92,1,'appdata_ocodxjl8m9zm/css/theming/theming.css.deps','eb8311da36b80c26b54f42c690367516',90,'theming.css.deps',14,3,144,1497074462,1497074462,0,0,'0305e87b30d7c0dd84203e77789fa2d4',27,''),(93,1,'appdata_ocodxjl8m9zm/css/theming/theming.css.gzip','ce7272a8e544bf3ef3927e09e9cdec8f',90,'theming.css.gzip',15,3,313,1497074462,1497074462,0,0,'48e3d6e8d042d8ddbcad4400ca04caf1',27,''),(94,1,'appdata_ocodxjl8m9zm/theming/0','c4fd072e5e869dd05c8f8c42083db935',68,'0',2,1,2117,1497074466,1497074466,0,0,'593b8b22362a4',31,''),(95,1,'appdata_ocodxjl8m9zm/theming/0/icon-core-filetypes_folder.svg','f06ca289a56995fda3c9b74f4877c60c',94,'icon-core-filetypes_folder.svg',17,8,254,1497074465,1497074465,0,0,'8338c7a5edcdcab73f1c245291e3af9a',27,''),(96,1,'appdata_ocodxjl8m9zm/theming/0/icon-core-filetypes_video.svg','5d695dd5262faee78d43afd18510b012',94,'icon-core-filetypes_video.svg',17,8,328,1497074465,1497074465,0,0,'0d146f90a5f2e527e670a645d27f5cae',27,''),(97,1,'appdata_ocodxjl8m9zm/theming/0/icon-core-filetypes_application-pdf.svg','cd78f9bdfe32bc05f2e7cc397add296a',94,'icon-core-filetypes_application-pdf.svg',17,8,1535,1497074466,1497074466,0,0,'50c89a3acbae65d13cc5f637d9927ee2',27,''),(98,1,'files_external','c270928b685e7946199afdfb898d27ea',1,'files_external',2,1,0,1519457243,1519457243,0,0,'5a9113db988d0',31,''),(99,1,'appdata_ocodxjl8m9zm/appstore/categories.json','6f576af292a22fbf4378e6e40d93ff96',3,'categories.json',4,3,32533,1497074511,1497074511,0,0,'0098080687626184f9dbc3d3d05b7d1a',27,''),(100,1,'appdata_ocodxjl8m9zm/richdocuments','9346c20e7049d192f1c0c21990153933',2,'richdocuments',2,1,0,1497074926,1497074926,0,0,'593b8ceec6d52',31,''),(101,1,'appdata_ocodxjl8m9zm/richdocuments/richdocuments','74136bbec942e1a2f9cf447e872eb6ab',100,'richdocuments',2,1,0,1497074926,1497074926,0,0,'593b8ceec58b4',31,''),(102,1,'appdata_ocodxjl8m9zm/js/core/merged-login.js','e7c272ad7c4ba9f80c06736bfd729adc',20,'merged-login.js',13,3,5389,1497075930,1497075930,0,0,'0378b1935fa2eea8f772d619dc15e438',27,''),(103,1,'appdata_ocodxjl8m9zm/js/core/merged-login.js.deps','b2d30e7fda641dea0e2fd3c80b6a356b',20,'merged-login.js.deps',14,3,271,1497075930,1497075930,0,0,'004ca08f6fab61f3e83a50e1c81da500',27,''),(104,1,'appdata_ocodxjl8m9zm/js/core/merged-login.js.gzip','356ad6cf015dd63528515cbeac831479',20,'merged-login.js.gzip',15,3,1867,1497075930,1497075930,0,0,'132fd3f134cd846bcc030176b9b2af6d',27,''),(105,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF','f73e431afd112dd389591520095f80c2',1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF',2,1,3421455,1519457735,1519457244,0,0,'5a9115c7185d7',31,''),(106,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js','f7f902fe73e47235e606b1b0453bd5f3',105,'js',2,1,2658729,1519457735,1519457015,0,0,'5a9115c7185d7',31,''),(107,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core','bf6139f82da83b53eb0358157d1a649c',106,'core',2,1,355778,1519457735,1519457015,0,0,'5a9115c7185d7',31,''),(108,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-template-prepend.js','0fd4bb5d73f30249dd031c225ca81f1b',107,'merged-template-prepend.js',13,3,148342,1519457224,1519457224,0,0,'4d63c362611b56e07881e1abdd363bff',27,''),(109,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/preview','305d612aefc0378ecc511bcb8b260777',105,'preview',2,1,0,1519457277,1519457277,0,0,'5a9113fd935d5',31,''),(110,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-template-prepend.js.deps','88799db37b811c08901187426329ca7b',107,'merged-template-prepend.js.deps',14,3,1294,1519457224,1519457224,0,0,'6eb662d8f9ae27c3706440791a494e7e',27,''),(111,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-template-prepend.js.gzip','3c1620d02bec64920c23cf5d86738241',107,'merged-template-prepend.js.gzip',15,3,40587,1519457224,1519457224,0,0,'de12db5fac3e127463241f7525e0a140',27,''),(112,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-share-backend.js','829f2087d704a5570ce9fb0e10bc110d',107,'merged-share-backend.js',13,3,105819,1519457258,1519457258,0,0,'bceba54016a853478f8b2dcfb4042316',27,''),(113,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-share-backend.js.deps','907d40d250442603c7974622f6fc4431',107,'merged-share-backend.js.deps',14,3,752,1519457258,1519457258,0,0,'dea9a20f032bcb4cd8a1a5969b538ff6',27,''),(114,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-share-backend.js.gzip','3646c433d15737badb145949b35d4bc1',107,'merged-share-backend.js.gzip',15,3,22777,1519457258,1519457258,0,0,'bee5fc3ac0b498c3a4f737bb1cfcf412',27,''),(115,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-login.js','7927fbccea6e02f6274042159f44d30e',107,'merged-login.js',13,3,7563,1519457735,1519457735,0,0,'c3b8d0b3c063e24939c2b87952574e34',27,''),(116,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-login.js.deps','4e838076800171f6c0d1306f8addcf00',107,'merged-login.js.deps',14,3,271,1519457735,1519457735,0,0,'3ab2809f4e2da1576cc23baf8c7b3fc8',27,''),(117,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged-login.js.gzip','5076064acb792accaa4dc7ee6a696f7b',107,'merged-login.js.gzip',15,3,2276,1519457735,1519457735,0,0,'ce576f6a6712eb99ab05e056df798424',27,''),(118,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css','c3905074530f40bba84d599fa672b6b8',105,'css',2,1,214886,1519457288,1519457287,0,0,'5a9114088f4bd',31,''),(119,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/theming','09fc932e02eda888f0491838d8c93db6',118,'theming',2,1,1673,1519457265,1519457265,0,0,'5a9113f1f030c',31,''),(120,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming','0cbd9c88caa9fdb94dd4a019d04ef6b0',105,'theming',2,1,2977,1519457277,1519457243,0,0,'5a9113fdc4964',31,''),(123,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/theming/theming.css.gzip','3a170347d762d5487043e88347f0ebbe',119,'theming.css.gzip',15,3,311,1519457003,1519457003,0,0,'c02bdffcf5776673f61e547c81c72c44',27,''),(124,2,'cache','0fea6a13c52b4d4725368f24b045ca84',6,'cache',2,1,0,1519457013,1519457013,0,0,'5a9112f5d8b06',31,''),(125,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/avatar','cb3ea6020659e187300b614cac89cd23',105,'avatar',2,1,16832,1519457712,1519457014,0,0,'5a9115b0ddbfa',31,''),(126,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/avatar/admin','8293fd1e3e4acc888a8bb94106130900',125,'admin',2,1,16832,1519457712,1519457712,0,0,'5a9115b0ddbfa',31,''),(127,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/notifications','7398a4910ed165fe584a4a4f7f03b999',106,'notifications',2,1,26472,1519457258,1519457014,0,0,'5a9113eb010b3',31,''),(128,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/notifications/merged.js','55c53b9a6304695e47b343ca3a735d66',127,'merged.js',13,3,20888,1519457258,1519457258,0,0,'fc526ee9a79c8d650e3d489195dfc1ba',27,''),(129,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/notifications/merged.js.deps','b38641a1905e929d6fa3cb2df6e2d3ee',127,'merged.js.deps',14,3,330,1519457258,1519457258,0,0,'8b772d5ba68fd2491d31a42dab6e925a',27,''),(130,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/notifications/merged.js.gzip','802b6060a566e336f75e0d0aebc19955',127,'merged.js.gzip',15,3,5254,1519457258,1519457258,0,0,'5923650d9d8dc64eeec1dac8a4a150da',27,''),(131,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files','6339de69758111fac03ce89fdc64aeb7',106,'files',2,1,418112,1519457259,1519457014,0,0,'5a9113eb166b1',31,''),(132,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files/merged-index.js','f2a57889b612f423dd264a8b5cff8d61',131,'merged-index.js',13,3,336296,1519457259,1519457259,0,0,'056e29ca4c23e707b9deebbef44891ee',27,''),(133,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files/merged-index.js.deps','28b055df20819058d2f98cf9c4c1905f',131,'merged-index.js.deps',14,3,2125,1519457259,1519457259,0,0,'d393dd36971d2e9da4ddbb15b4c1adf1',27,''),(134,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files/merged-index.js.gzip','74962728ea9d36b2917fa32f55aed36a',131,'merged-index.js.gzip',15,3,79691,1519457259,1519457259,0,0,'940d86b87ac2059be09197060b389fb5',27,''),(135,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/activity','e05a5dd5498c0540fc4a8c272f4d2f18',106,'activity',2,1,20779,1519457259,1519457014,0,0,'5a9113eb1c6b2',31,''),(136,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/activity/activity-sidebar.js','17b156218fc6ad6e67fd706d3cec7461',135,'activity-sidebar.js',13,3,16068,1519457259,1519457259,0,0,'ff5659cfa60a2e49147388b2601fca22',27,''),(137,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/activity/activity-sidebar.js.deps','f06b44f7715fc9d64bef4793466e6e2f',135,'activity-sidebar.js.deps',14,3,494,1519457259,1519457259,0,0,'c28476916addb5d527e65e4aabc1275c',27,''),(138,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/activity/activity-sidebar.js.gzip','377a9e957a016daceec0583a30fc159f',135,'activity-sidebar.js.gzip',15,3,4217,1519457259,1519457259,0,0,'110fb27d196613810c14e91d3dc30ccc',27,''),(139,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/comments','d343e3b9a412c17f52a3316e6e98c3cf',106,'comments',2,1,80536,1519457259,1519457014,0,0,'5a9113eb2444c',31,''),(140,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/comments/merged.js','71c4f7f665069f10800481a4883abece',139,'merged.js',13,3,62511,1519457259,1519457259,0,0,'395cb5fcbe0bc14eb79d3ddc1ae75ce4',27,''),(141,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/comments/merged.js.deps','918bb29e72e527cda914df9aee1fc6fa',139,'merged.js.deps',14,3,848,1519457259,1519457259,0,0,'b329a669fcbdb45b8f09713a8f4cbc23',27,''),(142,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/comments/merged.js.gzip','6c1335a74a5ed2f008d3e1bfa4de97d4',139,'merged.js.gzip',15,3,17177,1519457259,1519457259,0,0,'c1a601d5d732b7aecce91e0894f32b2c',27,''),(143,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_sharing','abdfb93e925a9c82ab1ecac7cf1703ce',106,'files_sharing',2,1,19406,1519457259,1519457014,0,0,'5a9113eb2b33e',31,''),(144,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_sharing/additionalScripts.js','ee05131234a87aab29360fad5ca4ac5b',143,'additionalScripts.js',13,3,14539,1519457259,1519457259,0,0,'e780c3aa4c666cb74a2d57d84a65f414',27,''),(145,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_sharing/additionalScripts.js.deps','5622cfdb6fe215c3d23660f0d63b56e5',143,'additionalScripts.js.deps',14,3,340,1519457259,1519457259,0,0,'097a6ec92f8a4e366ae28d4c71d7f831',27,''),(146,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_sharing/additionalScripts.js.gzip','17f272bf4911b1b3c8ca7911165e4723',143,'additionalScripts.js.gzip',15,3,4527,1519457259,1519457259,0,0,'abe262035197065a50ea4de7d05092cd',27,''),(147,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_versions','3143953d4f10a1532c3b3c9ec9c3a267',106,'files_versions',2,1,16725,1519457259,1519457014,0,0,'5a9113eb5d637',31,''),(148,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_versions/merged.js','d94c8fc11edf0a6bbd7ca4d6f116fbd3',147,'merged.js',13,3,12719,1519457259,1519457259,0,0,'1755da73b37b2ac652aa5de4a1231bb0',27,''),(149,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_versions/merged.js.deps','8b83b350dade3804cc03a45eee2e6016',147,'merged.js.deps',14,3,424,1519457259,1519457259,0,0,'0617f665a7430ab9652f2dcb3d39ee64',27,''),(150,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_versions/merged.js.gzip','4c5e6915472208f76a30d25a95e35756',147,'merged.js.gzip',15,3,3582,1519457259,1519457259,0,0,'f2dfd1a1d4b8d4b55d3e600bd9d1cb97',27,''),(151,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_texteditor','c07c5fa9d8603275efe0aa263c07ee6a',106,'files_texteditor',2,1,839126,1519457259,1519457014,0,0,'5a9113eb57315',31,''),(152,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_texteditor/merged.js','b4147ef3906648cde01c3ab7469548bb',151,'merged.js',13,3,699652,1519457259,1519457259,0,0,'a21c5b633da1147fc3b7eaecb2c47a01',27,''),(153,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_texteditor/merged.js.deps','4185417dfeadad0b41475d4f952c5932',151,'merged.js.deps',14,3,370,1519457259,1519457259,0,0,'3e0fea54a0667078de479f898c77aaf0',27,''),(154,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/files_texteditor/merged.js.gzip','0048be8aa1a894db67b506233e95b56c',151,'merged.js.gzip',15,3,139104,1519457259,1519457259,0,0,'f7badcaf0cb4b85358b5ebde4fab2831',27,''),(155,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery','c73af6c2f18d1b2a8194f0d658f621b0',106,'gallery',2,1,857749,1519457275,1519457275,0,0,'5a9113fb5bf1a',31,''),(156,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery/scripts-for-file-app.js','afd4d2ee0f6a06412047bc64b86d28b9',155,'scripts-for-file-app.js',13,3,226060,1519457259,1519457259,0,0,'d94c9e6602bde79448cc91d7b0c443b1',27,''),(157,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery/scripts-for-file-app.js.deps','c771131153983650e99e1b7860b52f84',155,'scripts-for-file-app.js.deps',14,3,856,1519457259,1519457259,0,0,'d4bc1b916e273294b66919315c24ff3b',27,''),(158,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery/scripts-for-file-app.js.gzip','3749b789356d0bab4ff5149205367711',155,'scripts-for-file-app.js.gzip',15,3,54487,1519457259,1519457259,0,0,'8c90cf3618161819c55dc62957b3a79d',27,''),(159,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged.js','79e454db171c8f78a19f93935be92d02',107,'merged.js',13,3,20224,1519457259,1519457259,0,0,'3424f3bd4e94162f11dd35fe4ae36e6c',27,''),(160,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged.js.deps','c2a3d3cda9a899b5917c919198bbc62a',107,'merged.js.deps',14,3,508,1519457259,1519457259,0,0,'158554308e2e28956069d0caef46279e',27,''),(161,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/core/merged.js.gzip','205e88b37fba9bdfcb7e4e3e1fa50269',107,'merged.js.gzip',15,3,5365,1519457259,1519457259,0,0,'91750ec36cd74958890f6395a9831fdd',27,''),(162,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/systemtags','4f3ef1556d480932840a2aa5f7d4356c',106,'systemtags',2,1,24046,1519457259,1519457015,0,0,'5a9113eb80ec9',31,''),(163,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/systemtags/merged.js','df6475f8c4fe8b22588ef8df54161e18',162,'merged.js',13,3,18223,1519457259,1519457259,0,0,'5194d7208699d736a82f16d0604fc1a0',27,''),(164,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/systemtags/merged.js.deps','eca0062cadbe8bfef68e104a320f2972',162,'merged.js.deps',14,3,495,1519457259,1519457259,0,0,'04ce906dbcf293369ac5162474ce5921',27,''),(165,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/systemtags/merged.js.gzip','dec4b790d7ed04ff0ac82be880ff9a2f',162,'merged.js.gzip',15,3,5328,1519457259,1519457259,0,0,'e9f727dcd1357662dd3d6d835d538434',27,''),(166,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core','1e87c2054727df2f362b72a7e9b5aebf',118,'core',2,1,145618,1519457264,1519457264,0,0,'5a9113f04911d',31,''),(169,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/server.css.gzip','a0132924b9c70dea4c70f1ed69617f59',166,'server.css.gzip',15,3,13406,1519457017,1519457017,0,0,'f1874d900f362be49122f7a69a5c565f',27,''),(172,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/share.css.gzip','c0efa6a3845b184ed012972f44467150',166,'share.css.gzip',15,3,994,1519457017,1519457017,0,0,'a8f1e19015ff6150d8aa2765378bbce2',27,''),(173,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files','d517897c6d257bf7f6b4806fd6e5b266',118,'files',2,1,33863,1519457275,1519457275,0,0,'5a9113fb7a501',31,''),(176,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/merged.css.gzip','752e9b8e120d683fec101c7df291e329',173,'merged.css.gzip',15,3,4283,1519457018,1519457018,0,0,'8eb1ac4f1cc47ace78e137a0a6ebd7c3',27,''),(177,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_sharing','54775a1fca3e4481d5d63c3bf504b329',118,'files_sharing',2,1,4314,1519457264,1519457264,0,0,'5a9113f01ed4b',31,''),(180,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_sharing/mergedAdditionalStyles.css.gzip','d3dd5e056356af7063e005668ffe81ef',177,'mergedAdditionalStyles.css.gzip',15,3,878,1519457018,1519457018,0,0,'fd1f5af07365910de4583f4c07f2f6c8',27,''),(181,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_texteditor','0de1885d3d25ee51f85f9e3c9cb37e57',118,'files_texteditor',2,1,7049,1519457264,1519457264,0,0,'5a9113f038f09',31,''),(184,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_texteditor/merged.css.gzip','454f6c265bec096e6f55bd107740cb11',181,'merged.css.gzip',15,3,1184,1519457018,1519457018,0,0,'873ff854e71b1a085894e1e4053a9e7a',27,''),(187,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/systemtags.css.gzip','bbbc809f22b2e8083a9e22c925e20124',166,'systemtags.css.gzip',15,3,389,1519457018,1519457018,0,0,'4bed4ebf2314a8dfdf3722ab981f70b4',27,''),(188,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/richdocuments','05eab11d4aed9ae97feb9ab812d1580e',105,'richdocuments',2,1,0,1519457023,1519457023,0,0,'5a9112ffc273c',31,''),(189,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/richdocuments/richdocuments','8c8cd1c2d44e31a00c0391d4333545ce',188,'richdocuments',2,1,0,1519457023,1519457023,0,0,'5a9112ffc0605',31,''),(190,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/0','b579e0aed47ad6dc8e786ee3ae26b1d4',120,'0',2,1,2977,1519457277,1519457277,0,0,'5a9113fdc4964',31,''),(191,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/0/icon-core-filetypes_folder.svg','45b3b36ae673f0bf2f8f306b8b83839b',190,'icon-core-filetypes_folder.svg',17,8,254,1519457025,1519457025,0,0,'967e9ae30af4d800f26cbc544ff38dd5',27,''),(192,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/0/icon-core-filetypes_video.svg','30ddd19385b5bfde708da1c6d789fc8a',190,'icon-core-filetypes_video.svg',17,8,328,1519457026,1519457026,0,0,'896a99c498c8bd7adc1afa0e4d4c95f5',27,''),(193,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/0/icon-core-filetypes_application-pdf.svg','0bd42bdd9a9298a0ff3e80478f4bd70e',190,'icon-core-filetypes_application-pdf.svg',17,8,1535,1519457026,1519457026,0,0,'7f1becc7f248b16ef9c52ea4b1dc587c',27,''),(194,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/images','f393d7a23a5442a7f9801f10fe549d37',120,'images',2,1,0,1519457243,1519457243,0,0,'5a9113db859f4',31,''),(195,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/appstore','4e9fa3f6be4193019ca394ccfbbad033',105,'appstore',2,1,528031,1519457550,1519457289,0,0,'5a91150e12249',31,''),(196,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/appstore/apps.json','0841795917de721d46324840182c804d',195,'apps.json',4,3,418911,1519457550,1519457550,0,0,'179560d9425d4d01e43760a73a538f80',27,''),(197,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/identityproof','8e7cbd34a0deb244b0277cb7a6fd5871',105,'identityproof',2,1,0,1519457244,1519457244,0,0,'5a9113dc519a7',31,''),(198,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-jquery-ui-fixes.css','f2514cbd12af60c8cc518355605e42b4',166,'bcc83ffd-jquery-ui-fixes.css',16,11,4159,1519457259,1519457259,0,0,'17d1c4926a9a073493a49055da15be01',27,''),(199,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-jquery-ui-fixes.css.deps','7f5a31d5027e6fbb61d0038518928d8e',166,'bcc83ffd-jquery-ui-fixes.css.deps',14,3,143,1519457259,1519457259,0,0,'56d2d99e384c17401e25b05dddf8b694',27,''),(200,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-jquery-ui-fixes.css.gzip','09200d30573423046126d26435ad7047',166,'bcc83ffd-jquery-ui-fixes.css.gzip',15,3,859,1519457259,1519457259,0,0,'fe3648d20ef2e514d08719028b6a6846',27,''),(201,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-server.css','6ec1ebbeb98800fd7325c17e8b276081',166,'bcc83ffd-server.css',16,11,101249,1519457262,1519457262,0,0,'c7188d65a0aab7fca8a06ae545d14f83',27,''),(202,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-server.css.deps','185960d2cd36064abb39339988375419',166,'bcc83ffd-server.css.deps',14,3,850,1519457262,1519457262,0,0,'58892758c781b7396318c4dd3c37c222',27,''),(203,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-server.css.gzip','0d241c53df49e79f30002c23600a9304',166,'bcc83ffd-server.css.gzip',15,3,15914,1519457262,1519457262,0,0,'a693fc224300a780ade126af8d7bf347',27,''),(204,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-share.css','c4e8b284c5f1cdcb56ed01996614a58a',166,'bcc83ffd-share.css',16,11,2685,1519457262,1519457262,0,0,'255aee105054a05b44429f876334da77',27,''),(205,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-share.css.deps','dc08a4c1ce355c4164104a75b8d00066',166,'bcc83ffd-share.css.deps',14,3,133,1519457262,1519457262,0,0,'44e05c7c2af3b82c13d8a3beee60dce6',27,''),(206,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-share.css.gzip','ecf31b6efe6355730e37d07f3cad6979',166,'bcc83ffd-share.css.gzip',15,3,957,1519457262,1519457262,0,0,'12f0f3456bb3cb562a2d5a2f77c94818',27,''),(207,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-jquery.ocdialog.css','2b7471354a844075534e4a269105094b',166,'bcc83ffd-jquery.ocdialog.css',16,11,1263,1519457262,1519457262,0,0,'a642dab71980ccc331588f5b8f67c7cd',27,''),(208,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-jquery.ocdialog.css.deps','ee6e04ff9efa53f09b9c4feb6323a946',166,'bcc83ffd-jquery.ocdialog.css.deps',14,3,143,1519457262,1519457262,0,0,'78e266aeccb7c6478675b8d4ed89b72a',27,''),(209,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-jquery.ocdialog.css.gzip','300f075d75d7155381797565d90314c4',166,'bcc83ffd-jquery.ocdialog.css.gzip',15,3,567,1519457262,1519457262,0,0,'7a976c901d40f5d670e3e05e8c306d17',27,''),(210,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/bcc83ffd-merged.css','b680083a8d33ebb15868df17a6e5f808',173,'bcc83ffd-merged.css',16,11,19994,1519457263,1519457263,0,0,'6322b93fb5f680b7db98c560069c98e9',27,''),(211,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/bcc83ffd-merged.css.deps','42fbdb4f779e98f04866ac2c7e04e4ca',173,'bcc83ffd-merged.css.deps',14,3,433,1519457263,1519457263,0,0,'21fa7e702bab457e27a8cfb769fecf6e',27,''),(212,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/bcc83ffd-merged.css.gzip','359c430cd9aadce54d711e720da6464d',173,'bcc83ffd-merged.css.gzip',15,3,4344,1519457263,1519457263,0,0,'c54b2ebb6a820e04d9d9d4608f1b515d',27,''),(213,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_trashbin','0528f7178efd4cf478ea4027f7d0f664',118,'files_trashbin',2,1,654,1519457263,1519457263,0,0,'5a9113efe6c17',31,''),(214,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_trashbin/bcc83ffd-trash.css','8b437d3b37409c19b8567d5d656544c9',213,'bcc83ffd-trash.css',16,11,344,1519457263,1519457263,0,0,'512811167966c84c6b5604086b39a023',27,''),(215,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_trashbin/bcc83ffd-trash.css.deps','97d35fb9950d73b1971e6cc2b42bc311',213,'bcc83ffd-trash.css.deps',14,3,149,1519457263,1519457263,0,0,'0064a3b6e8153bc621e2c934e82fb0ca',27,''),(216,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_trashbin/bcc83ffd-trash.css.gzip','813b7e5d45b60849e13c10e943618173',213,'bcc83ffd-trash.css.gzip',15,3,161,1519457263,1519457263,0,0,'5b7829152260081b171560a0075dd44d',27,''),(217,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/comments','f4637919659b1cb0098a0aa36060c0a3',118,'comments',2,1,1541,1519457264,1519457264,0,0,'5a9113f00b244',31,''),(218,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/comments/bcc83ffd-autocomplete.css','82980f42b511ac7ae77d038911f2d2c8',217,'bcc83ffd-autocomplete.css',16,11,967,1519457264,1519457264,0,0,'1986f1f511e94e7e5c12ec38c1b137c4',27,''),(219,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/comments/bcc83ffd-autocomplete.css.deps','5499b9d55637f9ccdae3e196f435df86',217,'bcc83ffd-autocomplete.css.deps',14,3,150,1519457264,1519457264,0,0,'480957bde4bb9bafd029f228d71035f7',27,''),(220,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/comments/bcc83ffd-autocomplete.css.gzip','c2a2a6f7c3fa5d6795a82358efe81f53',217,'bcc83ffd-autocomplete.css.gzip',15,3,424,1519457264,1519457264,0,0,'362129441c83a48f678f43d7fea1214f',27,''),(221,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_sharing/bcc83ffd-mergedAdditionalStyles.css','7b70e5139bf6754624923d5e17c04533',177,'bcc83ffd-mergedAdditionalStyles.css',16,11,2303,1519457264,1519457264,0,0,'8fc648d8576ac2a95e165854486b10ca',27,''),(222,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_sharing/bcc83ffd-mergedAdditionalStyles.css.deps','01205086385622321b2140a5859ee5ab',177,'bcc83ffd-mergedAdditionalStyles.css.deps',14,3,340,1519457264,1519457264,0,0,'118dbdfccb9d7d7b4a34b934ed373648',27,''),(223,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_sharing/bcc83ffd-mergedAdditionalStyles.css.gzip','dbf9da1d0e2ca2a59c990145d4025aa7',177,'bcc83ffd-mergedAdditionalStyles.css.gzip',15,3,793,1519457264,1519457264,0,0,'8d0e75f1ff5682080acfb679c61a5742',27,''),(224,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_texteditor/bcc83ffd-merged.css','1ae4f2aae9b685a687732a54c2b4f94e',181,'bcc83ffd-merged.css',16,11,4178,1519457264,1519457264,0,0,'2e40473c20f0358b17e2de24bd0bc357',27,''),(225,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_texteditor/bcc83ffd-merged.css.deps','247541984b8114549c0386e4a057d13a',181,'bcc83ffd-merged.css.deps',14,3,419,1519457264,1519457264,0,0,'7f0567680178ee459c908d0df955a10b',27,''),(226,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files_texteditor/bcc83ffd-merged.css.gzip','528a3448d5ea402fe3f9f87ce422dbbe',181,'bcc83ffd-merged.css.gzip',15,3,1268,1519457264,1519457264,0,0,'23eff5c0316b30c0b555d58e0152904c',27,''),(227,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-systemtags.css','54af812eb39902ae7270b50726b2f0b2',166,'bcc83ffd-systemtags.css',16,11,1391,1519457264,1519457264,0,0,'79f90173aa5e2f44727af32a66b19dbc',27,''),(228,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-systemtags.css.deps','e162a533c8d2aeaa2701e20d5f0c8398',166,'bcc83ffd-systemtags.css.deps',14,3,138,1519457264,1519457264,0,0,'d72e0bf832cd1798b7874e26b2a62a99',27,''),(229,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/core/bcc83ffd-systemtags.css.gzip','2ea6f77b73932855509e440d4e747c06',166,'bcc83ffd-systemtags.css.gzip',15,3,378,1519457264,1519457264,0,0,'984f0ba011d9abf9922588036c78c2c1',27,''),(230,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/theming/bcc83ffd-theming.css','e816d38a27e71cbe7700a4727bcbbd43',119,'bcc83ffd-theming.css',16,11,866,1519457265,1519457265,0,0,'8aa8eaf904bc1de2e77ee3a90fb2f8bf',27,''),(231,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/theming/bcc83ffd-theming.css.deps','54611f5a29691266c2fef62099ff60e8',119,'bcc83ffd-theming.css.deps',14,3,144,1519457265,1519457265,0,0,'dd1b2631bd367e214bf0514f55939c0f',27,''),(232,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/theming/bcc83ffd-theming.css.gzip','6c62e63feb23b97a11b1c4020001c62e',119,'bcc83ffd-theming.css.gzip',15,3,352,1519457265,1519457265,0,0,'7af737bd69997973c9c4d808ec154dd0',27,''),(233,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/0/icon-core-filetypes_folder-external.svg','a7b6b9b63dee0dfcfb427314156934f1',190,'icon-core-filetypes_folder-external.svg',17,8,508,1519457269,1519457269,0,0,'50a246bae3ee5ec688c483bb3eb44f5c',27,''),(234,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery/merged.js','81485b283b9d8b9ae18c666b09dfe535',155,'merged.js',13,3,450591,1519457275,1519457275,0,0,'c5b82ac53d50a09eec8df41b0b89cd76',27,''),(235,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery/merged.js.deps','93283c03996f4b2636d9e19bee5e58cd',155,'merged.js.deps',14,3,2225,1519457275,1519457275,0,0,'7c1314ed8d178b9159d09a0f50d7e768',27,''),(236,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/js/gallery/merged.js.gzip','ad252c391551a252e12fd6eaeb642157',155,'merged.js.gzip',15,3,123530,1519457275,1519457275,0,0,'81a643674fa5193c7bc73c481e3e56b3',27,''),(237,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/bcc83ffd-upload.css','7dadf7e8b7f5b797a9a814f0c4142ea5',173,'bcc83ffd-upload.css',16,11,3646,1519457275,1519457275,0,0,'d863528dc625d29350bd9af138c930db',27,''),(238,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/bcc83ffd-upload.css.deps','9d583ee7fe763e7d4cd421234891a1ea',173,'bcc83ffd-upload.css.deps',14,3,141,1519457275,1519457275,0,0,'a8913dbfa7166ffb0c1b2097a7d3fbe8',27,''),(239,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/files/bcc83ffd-upload.css.gzip','c0ec45e21d3d7e3eeab4a961b86a573a',173,'bcc83ffd-upload.css.gzip',15,3,1022,1519457275,1519457275,0,0,'ae4350ff9755fd8edc0e4472810881d7',27,''),(240,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/preview/12','e51f5413539afb892e0295dbcc7ca10e',109,'12',2,1,0,1519457277,1519457277,0,0,'5a9113fd88f67',31,''),(241,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/preview/13','d5e48cd8109b59dba7af771d34a7bcad',109,'13',2,1,0,1519457277,1519457277,0,0,'5a9113fd8e257',31,''),(242,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/preview/11','e5bde64658cafc23af97a55152e7d132',109,'11',2,1,0,1519457277,1519457277,0,0,'5a9113fd9218c',31,''),(243,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/theming/0/icon-core-filetypes_image.svg','0543c79591972f0dbbf8c66812756705',190,'icon-core-filetypes_image.svg',17,8,352,1519457277,1519457277,0,0,'63f226ff19bef89bd06914d454ed2d4b',27,''),(244,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/settings','c242527208e88b5241ac58a1e8571d2b',118,'settings',2,1,20174,1519457288,1519457288,0,0,'5a9114088f4bd',31,''),(245,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/settings/bcc83ffd-settings.css','5a7c20f3a3cdb3303396508e7e125f86',244,'bcc83ffd-settings.css',16,11,15682,1519457288,1519457288,0,0,'223dfe9c5af18c83ef2a1756bc29d282',27,''),(246,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/settings/bcc83ffd-settings.css.deps','98b6e5c0bd5e05cd9921dc4e6bc7a8c9',244,'bcc83ffd-settings.css.deps',14,3,140,1519457288,1519457288,0,0,'5c440c2a4f3b3c0abf45587d54aa07ff',27,''),(247,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/css/settings/bcc83ffd-settings.css.gzip','2f2bb6629b96916e79d3a1e3316e40a7',244,'bcc83ffd-settings.css.gzip',15,3,4352,1519457288,1519457288,0,0,'3d48ac56f19e7353d92dceaaa908b9c7',27,''),(248,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/appstore/categories.json','9596c1e86610e3d7c8149426814f7672',195,'categories.json',4,3,109120,1519457290,1519457290,0,0,'dcacc95ecc0b8f533260d5b39a2a277c',27,''),(249,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/avatar/admin/avatar.png','136fa0f11539806d7c6458c3ed4ac677',126,'avatar.png',25,8,14981,1519457706,1519457706,0,0,'5d4338745291176c81f942ecad81b2d1',27,''),(250,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/avatar/admin/generated','e57f25153f10e70cb79d6fd828977695',126,'generated',14,3,0,1519457706,1519457706,0,0,'ba2dbcc39d96b6378b72365e960cb861',27,''),(251,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/avatar/admin/avatar.145.png','f32d9a0c9b34a6c1ec7acdb11d6889d3',126,'avatar.145.png',25,8,1473,1519457706,1519457706,0,0,'14cfb2a6acc80a4f2686fb4f3b0d2551',27,''),(252,1,'appdata_ZWQ2MDM2MDMyNGRjOTg2NDlmYjZkMWJkMjF/avatar/admin/avatar.32.png','a293a8d6ba05ee0e1e81afce82c63526',126,'avatar.32.png',25,8,378,1519457712,1519457712,0,0,'dd160cc6e9e1129d231f6d637e42d2ed',27,'');
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
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `argument` varchar(4000) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `last_run` int(11) DEFAULT '0',
  `last_checked` int(11) DEFAULT '0',
  `reserved_at` int(11) DEFAULT '0',
  `execution_duration` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `job_class_index` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1519457289,1519457289,0,0),(2,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1519457385,1519457385,0,0),(3,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1519457705,1519457705,0,0),(4,'OCA\\DAV\\CardDAV\\SyncJob','null',1497074828,1519457735,1519457735,0),(5,'OCA\\NextcloudAnnouncements\\Cron\\Crawler','null',1519457735,1519457735,0,1),(6,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1497075018,1497075018,0,0),(7,'OCA\\UpdateNotification\\Notification\\BackgroundJob','null',1497075912,1497075911,0,0),(9,'OCA\\Files_Sharing\\DeleteOrphanedSharesJob','null',1497075926,1497075926,0,0),(10,'OCA\\Files_Sharing\\ExpireSharesJob','null',1497075931,1497075931,0,0),(11,'OCA\\Files\\BackgroundJob\\ScanFiles','null',1519457004,1519457004,0,1),(12,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',1519457022,1519457022,0,0),(13,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',1519457057,1519457057,0,0),(14,'OCA\\Federation\\SyncJob','null',1519457267,1519457267,0,0),(15,'\\OC\\Authentication\\Token\\DefaultTokenCleanupJob','null',1519457276,1519457276,0,0),(17,'OCA\\User_LDAP\\Jobs\\UpdateGroups','null',1519457713,1519457713,0,1),(18,'OCA\\User_LDAP\\Jobs\\CleanUp','null',1519457721,1519457721,0,0),(19,'OCA\\UpdateNotification\\ResetTokenBackgroundJob','null',0,1519457069,0,0),(20,'OC\\Authentication\\Token\\DefaultTokenCleanupJob','null',0,1519457235,0,0),(21,'OC\\Log\\Rotate','null',0,1519457235,0,0),(22,'OC\\Settings\\RemoveOrphaned','null',0,1519457235,0,0),(23,'OCA\\Survey_Client\\BackgroundJobs\\AdminNotification','null',0,1519457237,0,0),(24,'OCA\\User_LDAP\\Jobs\\Sync','null',0,1519457239,0,0),(25,'OCA\\DAV\\Migration\\BuildCalendarSearchIndexBackgroundJob','{\"offset\":0,\"stopAt\":0}',0,1519457241,0,0),(26,'OC\\Repair\\NC11\\MoveAvatarsBackgroundJob','null',0,1519457244,0,0),(27,'OC\\Repair\\NC11\\CleanPreviewsBackgroundJob','{\"uid\":\"admin\"}',0,1519457244,0,0),(28,'OCA\\Spreed\\BackgroundJob\\ExpireSignalingMessage','null',0,1519457529,0,0);
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
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=exams,ou=groups,ou=people,CHANGETHISLDAPBASE','exams','F0D61CD0-E32D-48B7-A3B8-0B6FA78CDFDB'),('cn=governors,ou=groups,ou=people,CHANGETHISLDAPBASE','governors','9ED60CE1-4E75-4593-86EB-481EEDF1E64F'),('cn=guardians,ou=groups,ou=people,CHANGETHISLDAPBASE','guardians','25E428CC-042F-4FEA-A1D8-5C540F8B00FE'),('cn=guestusers,ou=groups,ou=people,CHANGETHISLDAPBASE','guestusers','B65C4974-C54E-4FA5-BABE-EA61D3A19A68'),('cn=itadmin,ou=groups,ou=people,CHANGETHISLDAPBASE','itadmin','7A9ACD50-2C56-472D-B487-B1511E4109F8'),('cn=nonteachingstaff,ou=groups,ou=people,CHANGETHISLDAPBASE','nonteachingstaff','50F67796-8825-4477-8D2F-E077EBC48523'),('cn=officestaff,ou=groups,ou=people,CHANGETHISLDAPBASE','officestaff','0C37C783-63B4-4C73-AD35-20254882549F'),('cn=profilemanagement,ou=groups,ou=people,CHANGETHISLDAPBASE','profilemanagement','0E9717E4-35A3-4580-8CFE-B8F55D0620DA'),('cn=staff,ou=groups,ou=people,CHANGETHISLDAPBASE','staff','712F7BE3-7494-4932-A265-59EFF76C0177'),('cn=studentstaff,ou=groups,ou=people,CHANGETHISLDAPBASE','studentstaff','E81CCC0B-1818-4DBE-BEF6-CFFEDD6C6CCE'),('cn=tech,ou=groups,ou=people,CHANGETHISLDAPBASE','tech','7493C46F-1311-4D2D-B446-91D9B8EE6A65'),('cn=yr2016,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2016','D7061AC9-7C46-4FB9-817B-7D180755AFC2'),('cn=yr2017,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2017','2D1D2A46-D2B6-4EA6-8F35-A986FE66ABA7'),('cn=yr2018,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2018','66738AC9-CD32-49B3-84D9-877B4FD5CB8E'),('cn=yr2019,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2019','740D637C-1496-48D5-87BE-E8345114E7DB'),('cn=yr2020,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2020','CBD14138-39F7-4C00-9999-CC9C6B813EB0'),('cn=yr2021,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2021','8B75585C-BA95-4A7D-AE94-9DA6FA9A18FB'),('cn=yr2022,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2022','05EB25FE-B83A-4456-A4C8-EF233E9F5E4C'),('cn=yr2023,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2023','71348C2F-326A-4DB0-82D5-C3A84DD7E0F9'),('cn=yr2024,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2024','94847037-B811-46AD-9D56-FDB78DD3CC54'),('cn=yr2025,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2025','A503EDA4-1AC6-43C4-827D-3A65F37A09BA'),('cn=yr2026,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2026','6C819FF6-BC87-47E6-842C-146AC9E72B88'),('cn=yr2027,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2027','549990AC-77FD-4697-ACC0-F4CC47DB59A9'),('cn=yr2028,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2028','2AD7B1E9-A644-47FA-994D-0BA5216F6978'),('cn=yr2029,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2029','921D9D6E-61C9-4F7A-BCA0-65DAFC1EED17'),('cn=yr2030,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2030','50ABC7EA-7197-4660-9740-0B207D22C54C'),('cn=yr2031,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2031','79BA8419-CCDB-4C3C-BB84-85D54BBA02D9'),('cn=yr2032,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2032','2185448E-9330-4D60-B2E7-628689A2DDB1'),('cn=yr2033,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2033','3AB9A4D4-2699-4A26-A4E6-EB825DFF88AD'),('cn=yr2034,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2034','97295AE6-5D27-4833-80A6-7948C61B2B15'),('cn=yr2035,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2035','C2246AFA-D8A4-4C28-B3B6-88C83D38AAC3'),('cn=yr2036,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2036','45FBDBD7-221C-46D6-8C1B-1678770165E8'),('cn=yr2037,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2037','936CB5DB-07AA-4436-BE79-017DBE3E6F82'),('cn=yr2038,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2038','985301DA-F517-43AE-9760-2CB7310E7037'),('cn=yr2039,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2039','32283591-6F74-48F6-96F8-1236A5E6213C'),('cn=yr2040,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2040','9BCB0AA3-A928-4FC2-BB0A-AB99C302010B'),('cn=yr2041,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2041','F23372A2-01B0-4915-BCA5-AB809F72B10B'),('cn=yr2042,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2042','FFC16D4C-590D-476D-B592-3B6981FD720D'),('cn=yr2043,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2043','80E0B3CC-DBD3-4E85-A78F-E49B7491BFF8'),('cn=yr2044,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2044','1D5082DE-752D-4DA0-B99F-B2629DAB7394'),('cn=yr2045,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2045','CEB7896B-EE52-44F4-8F2B-D0402704CBE3'),('cn=yr2046,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2046','8C756F40-9EB5-4832-85E1-A8AC096AD40B'),('cn=yr2047,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2047','CAFAE4E1-8CAF-44AE-9BD7-30ED3B7CBC7A'),('cn=yr2048,ou=groups,ou=people,CHANGETHISLDAPBASE','yr2048','F6D87AD6-D81D-41BA-823F-544543F9E02E');
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
INSERT INTO `oc_ldap_group_members` VALUES ('exams','a:5:{i:0;s:5:\"exam1\";i:1;s:5:\"exam2\";i:2;s:5:\"exam3\";i:3;s:5:\"exam4\";i:4;s:5:\"exam5\";}'),('governors','a:0:{}'),('guardians','a:0:{}'),('guestusers','a:10:{i:0;s:6:\"guest1\";i:1;s:6:\"guest2\";i:2;s:6:\"guest3\";i:3;s:6:\"guest4\";i:4;s:6:\"guest5\";i:5;s:6:\"guest6\";i:6;s:6:\"guest7\";i:7;s:6:\"guest8\";i:8;s:6:\"guest9\";i:9;s:7:\"guest10\";}'),('itadmin','a:1:{i:0;s:8:\"sysadmin\";}'),('nonteachingstaff','a:0:{}'),('officestaff','a:0:{}'),('profilemanagement','a:1:{i:0;s:11:\"profileuser\";}'),('staff','a:2:{i:0;s:6:\"ismith\";i:1;s:6:\"jjones\";}'),('studentstaff','a:0:{}'),('tech','a:4:{i:0;s:5:\"tech1\";i:1;s:5:\"tech2\";i:2;s:5:\"tech3\";i:3;s:5:\"tech4\";}'),('yr2016','a:0:{}'),('yr2017','a:0:{}'),('yr2018','a:0:{}'),('yr2019','a:0:{}'),('yr2020','a:0:{}'),('yr2021','a:0:{}'),('yr2022','a:0:{}'),('yr2023','a:0:{}'),('yr2024','a:0:{}'),('yr2025','a:0:{}'),('yr2026','a:0:{}'),('yr2027','a:0:{}'),('yr2028','a:0:{}'),('yr2029','a:0:{}'),('yr2030','a:0:{}'),('yr2031','a:0:{}'),('yr2032','a:0:{}'),('yr2033','a:0:{}'),('yr2034','a:0:{}'),('yr2035','a:0:{}'),('yr2036','a:0:{}'),('yr2037','a:0:{}'),('yr2038','a:0:{}'),('yr2039','a:0:{}'),('yr2040','a:0:{}'),('yr2041','a:0:{}'),('yr2042','a:0:{}'),('yr2043','a:0:{}'),('yr2044','a:0:{}'),('yr2045','a:0:{}'),('yr2046','a:0:{}'),('yr2047','a:0:{}'),('yr2048','a:0:{}');
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
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam1','B6708436-6214-49F2-B503-FD0B0DEA9DAE'),('cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam2','08C4049E-B5C9-48F8-84D5-F8A968E044CD'),('cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam3','383F8CFA-C3A2-4314-A781-26B6A7BC107E'),('cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam4','5B3EAEBC-F071-4C7C-84A4-172D97080657'),('cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam5','005602E3-A1F0-4620-AE1D-DE6464CB7A86'),('cn=guest1,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest1','27455322-4897-48E7-8322-ADCDD88923B3'),('cn=guest10,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest10','38093A21-1219-4E92-94BC-CE0BD20D05FE'),('cn=guest2,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest2','D9816B0D-7005-4760-B29D-B6CD1C22B910'),('cn=guest3,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest3','BBDB650C-33BF-4D78-B397-F7CF7D77D41B'),('cn=guest4,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest4','12660A9D-582F-4AFB-9C0F-68407DB2373B'),('cn=guest5,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest5','6D6B068B-71F5-4DD2-8AA8-CE24B57B6C2D'),('cn=guest6,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest6','63E1AFD1-825A-42E2-9082-B13FADD16E56'),('cn=guest7,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest7','D85B6DB0-1F45-4AB0-87A1-A223496552B7'),('cn=guest8,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest8','8276C70D-CEEB-4D79-AB17-EF56020902E4'),('cn=guest9,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest9','390EF987-331A-4F62-8715-ACF45D16A681'),('cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','ismith','85135983-275D-4240-BDB9-E35F3C6A739F'),('cn=jjones,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','jjones','D25A948A-E575-444C-8A5A-374C15E5D6F9'),('cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE','profileuser','D24BB484-1DB1-4805-8A81-E9237F398A5D'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE','sysadmin','73E9650F-30AA-4A1E-B669-D7EBF51E6AAF'),('cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech1','78E9E02E-AC48-4D4E-86FE-DFE0A756B8CC'),('cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech2','7668D51F-2491-41E6-9401-3F4602E34843'),('cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech3','54409BC9-AD00-4534-BD9F-B60C029A31A5'),('cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech4','3C6E22A1-B501-4EEA-BE17-E326EAAA202B');
/*!40000 ALTER TABLE `oc_ldap_user_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_migrations`
--

DROP TABLE IF EXISTS `oc_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_migrations` (
  `app` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `version` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`app`,`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_migrations`
--

LOCK TABLES `oc_migrations` WRITE;
/*!40000 ALTER TABLE `oc_migrations` DISABLE KEYS */;
INSERT INTO `oc_migrations` VALUES ('activity','2006Date20170808154933'),('activity','2006Date20170808155040'),('activity','2006Date20170919095939'),('core','13000Date20170705121758'),('core','13000Date20170718121200'),('core','13000Date20170814074715'),('core','13000Date20170919121250'),('core','13000Date20170926101637'),('dav','1004Date20170825134824'),('dav','1004Date20170919104507'),('dav','1004Date20170924124212'),('dav','1004Date20170926103422'),('spreed','2000Date20170707093535'),('spreed','2000Date20171026140256'),('spreed','2000Date20171026140257'),('spreed','2001Date20170707115443'),('spreed','2001Date20170913104501'),('spreed','2001Date20170921145301'),('spreed','2001Date20170929092606'),('spreed','2001Date20171009132424'),('spreed','2001Date20171026134605'),('spreed','2001Date20171026141336'),('spreed','2001Date20171031102049'),('spreed','2001Date20180103144447'),('spreed','2001Date20180103150836'),('twofactor_backupcodes','1002Date20170607104347'),('twofactor_backupcodes','1002Date20170607113030'),('twofactor_backupcodes','1002Date20170919123342'),('twofactor_backupcodes','1002Date20170926101419');
/*!40000 ALTER TABLE `oc_migrations` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_mimetypes`
--

LOCK TABLES `oc_mimetypes` WRITE;
/*!40000 ALTER TABLE `oc_mimetypes` DISABLE KEYS */;
INSERT INTO `oc_mimetypes` VALUES (3,'application'),(18,'application/gpx+xml'),(22,'application/internet-shortcut'),(13,'application/javascript'),(4,'application/json'),(14,'application/octet-stream'),(7,'application/pdf'),(21,'application/vnd.garmin.tcx+xml'),(19,'application/vnd.google-earth.kml+xml'),(20,'application/vnd.google-earth.kmz'),(10,'application/vnd.oasis.opendocument.text'),(15,'application/x-gzip'),(23,'audio/mpegurl'),(24,'audio/x-scpls'),(1,'httpd'),(2,'httpd/unix-directory'),(8,'image'),(9,'image/jpeg'),(25,'image/png'),(17,'image/svg+xml'),(11,'text'),(16,'text/css'),(12,'text/plain'),(5,'video'),(6,'video/mp4');
/*!40000 ALTER TABLE `oc_mimetypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_mounts`
--

DROP TABLE IF EXISTS `oc_mounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_mounts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
-- Table structure for table `oc_notes_meta`
--

DROP TABLE IF EXISTS `oc_notes_meta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_notes_meta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL,
  `user_id` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `last_update` int(11) NOT NULL,
  `etag` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `notes_meta_file_id_user_id_index` (`file_id`,`user_id`),
  KEY `notes_meta_file_id_index` (`file_id`),
  KEY `notes_meta_user_id_index` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_notes_meta`
--

LOCK TABLES `oc_notes_meta` WRITE;
/*!40000 ALTER TABLE `oc_notes_meta` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_notes_meta` ENABLE KEYS */;
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
INSERT INTO `oc_notifications` VALUES (1,'survey_client','admin',1497075920,'dummy','23','updated','[]','','[]','','','[{\"label\":\"enable\",\"link\":\"https:\\/\\/www.constellations.com\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"POST\",\"primary\":true},{\"label\":\"disable\",\"link\":\"https:\\/\\/www.constellations.com\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"DELETE\",\"primary\":false}]'),(2,'firstrunwizard','admin',1519457282,'user','admin','profile','[]','','[]','','','[]');
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
  `apptype` varchar(32) COLLATE utf8mb4_bin NOT NULL DEFAULT 'unknown',
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
-- Table structure for table `oc_personal_sections`
--

DROP TABLE IF EXISTS `oc_personal_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_personal_sections` (
  `id` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `priority` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_sections_class` (`class`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_personal_sections`
--

LOCK TABLES `oc_personal_sections` WRITE;
/*!40000 ALTER TABLE `oc_personal_sections` DISABLE KEYS */;
INSERT INTO `oc_personal_sections` VALUES ('externalstorages','OCA\\Files_External\\Settings\\PersonalSection',10),('sharing','OCA\\FederatedFileSharing\\Settings\\PersonalSection',15);
/*!40000 ALTER TABLE `oc_personal_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_personal_settings`
--

DROP TABLE IF EXISTS `oc_personal_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_personal_settings` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `class` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `section` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `priority` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_settings_class` (`class`),
  KEY `personal_settings_section` (`section`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_personal_settings`
--

LOCK TABLES `oc_personal_settings` WRITE;
/*!40000 ALTER TABLE `oc_personal_settings` DISABLE KEYS */;
INSERT INTO `oc_personal_settings` VALUES (1,'OCA\\FederatedFileSharing\\Settings\\Personal','sharing',40),(2,'OCA\\TwoFactorBackupCodes\\Settings\\Personal','security',40),(3,'OCA\\Files_External\\Settings\\Personal','externalstorages',40),(4,'OCA\\FirstRunWizard\\Settings\\Personal','sync-clients',20);
/*!40000 ALTER TABLE `oc_personal_settings` ENABLE KEYS */;
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
INSERT INTO `oc_preferences` VALUES ('admin','avatar','generated','true'),('admin','core','lang','en'),('admin','core','timezone','Europe/London'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1519457013'),('exam1','files_external','config_version','0.5.0'),('exam1','user_ldap','displayName','Exam 1'),('exam1','user_ldap','homePath',''),('exam1','user_ldap','lastFeatureRefresh','1519457004'),('exam1','user_ldap','uid','exam1'),('exam2','files_external','config_version','0.5.0'),('exam2','user_ldap','displayName','Exam 2'),('exam2','user_ldap','homePath',''),('exam2','user_ldap','lastFeatureRefresh','1519457004'),('exam2','user_ldap','uid','exam2'),('exam3','files_external','config_version','0.5.0'),('exam3','user_ldap','displayName','Exam 3'),('exam3','user_ldap','homePath',''),('exam3','user_ldap','lastFeatureRefresh','1519457004'),('exam3','user_ldap','uid','exam3'),('exam4','files_external','config_version','0.5.0'),('exam4','user_ldap','displayName','Exam 4'),('exam4','user_ldap','homePath',''),('exam4','user_ldap','lastFeatureRefresh','1519457004'),('exam4','user_ldap','uid','exam4'),('exam5','files_external','config_version','0.5.0'),('exam5','user_ldap','displayName','Exam 5'),('exam5','user_ldap','homePath',''),('exam5','user_ldap','lastFeatureRefresh','1519457004'),('exam5','user_ldap','uid','exam5'),('guest1','files_external','config_version','0.5.0'),('guest1','user_ldap','displayName','Guest 1'),('guest1','user_ldap','homePath',''),('guest1','user_ldap','lastFeatureRefresh','1519457004'),('guest1','user_ldap','uid','guest1'),('guest10','files_external','config_version','0.5.0'),('guest10','user_ldap','displayName','Guest 10'),('guest10','user_ldap','homePath',''),('guest10','user_ldap','lastFeatureRefresh','1519457004'),('guest10','user_ldap','uid','guest10'),('guest2','files_external','config_version','0.5.0'),('guest2','user_ldap','displayName','Guest 2'),('guest2','user_ldap','homePath',''),('guest2','user_ldap','lastFeatureRefresh','1519457004'),('guest2','user_ldap','uid','guest2'),('guest3','files_external','config_version','0.5.0'),('guest3','user_ldap','displayName','Guest 3'),('guest3','user_ldap','homePath',''),('guest3','user_ldap','lastFeatureRefresh','1519457004'),('guest3','user_ldap','uid','guest3'),('guest4','files_external','config_version','0.5.0'),('guest4','user_ldap','displayName','Guest 4'),('guest4','user_ldap','homePath',''),('guest4','user_ldap','lastFeatureRefresh','1519457004'),('guest4','user_ldap','uid','guest4'),('guest5','files_external','config_version','0.5.0'),('guest5','user_ldap','displayName','Guest 5'),('guest5','user_ldap','homePath',''),('guest5','user_ldap','lastFeatureRefresh','1519457004'),('guest5','user_ldap','uid','guest5'),('guest6','files_external','config_version','0.5.0'),('guest6','user_ldap','displayName','Guest 6'),('guest6','user_ldap','homePath',''),('guest6','user_ldap','lastFeatureRefresh','1519457004'),('guest6','user_ldap','uid','guest6'),('guest7','files_external','config_version','0.5.0'),('guest7','user_ldap','displayName','Guest 7'),('guest7','user_ldap','homePath',''),('guest7','user_ldap','lastFeatureRefresh','1519457004'),('guest7','user_ldap','uid','guest7'),('guest8','files_external','config_version','0.5.0'),('guest8','user_ldap','displayName','Guest 8'),('guest8','user_ldap','homePath',''),('guest8','user_ldap','lastFeatureRefresh','1519457004'),('guest8','user_ldap','uid','guest8'),('guest9','files_external','config_version','0.5.0'),('guest9','user_ldap','displayName','Guest 9'),('guest9','user_ldap','homePath',''),('guest9','user_ldap','lastFeatureRefresh','1519457004'),('guest9','user_ldap','uid','guest9'),('ismith','files_external','config_version','0.5.0'),('ismith','user_ldap','displayName','Ian Smith'),('ismith','user_ldap','homePath',''),('ismith','user_ldap','lastFeatureRefresh','1519457004'),('ismith','user_ldap','uid','ismith'),('jjones','files_external','config_version','0.5.0'),('jjones','user_ldap','displayName','John Jones'),('jjones','user_ldap','homePath',''),('jjones','user_ldap','lastFeatureRefresh','1519457004'),('jjones','user_ldap','uid','jjones'),('profileuser','files_external','config_version','0.5.0'),('profileuser','user_ldap','displayName','Profile User'),('profileuser','user_ldap','homePath',''),('profileuser','user_ldap','lastFeatureRefresh','1519457004'),('profileuser','user_ldap','uid','profileuser'),('sysadmin','files_external','config_version','0.5.0'),('sysadmin','user_ldap','displayName','Sysadmin User'),('sysadmin','user_ldap','homePath',''),('sysadmin','user_ldap','lastFeatureRefresh','1519457004'),('sysadmin','user_ldap','uid','sysadmin'),('tech1','files_external','config_version','0.5.0'),('tech1','user_ldap','displayName','Tech 1'),('tech1','user_ldap','homePath',''),('tech1','user_ldap','lastFeatureRefresh','1519457004'),('tech1','user_ldap','uid','tech1'),('tech2','files_external','config_version','0.5.0'),('tech2','user_ldap','displayName','Tech 2'),('tech2','user_ldap','homePath',''),('tech2','user_ldap','lastFeatureRefresh','1519457004'),('tech2','user_ldap','uid','tech2'),('tech3','files_external','config_version','0.5.0'),('tech3','user_ldap','displayName','Tech 3'),('tech3','user_ldap','homePath',''),('tech3','user_ldap','lastFeatureRefresh','1519457004'),('tech3','user_ldap','uid','tech3'),('tech4','files_external','config_version','0.5.0'),('tech4','user_ldap','displayName','Tech 4'),('tech4','user_ldap','homePath',''),('tech4','user_ldap','lastFeatureRefresh','1519457004'),('tech4','user_ldap','uid','tech4');
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
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `share_type` smallint(6) NOT NULL DEFAULT '0',
  `share_with` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `uid_owner` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `uid_initiator` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL,
  `parent` bigint(20) DEFAULT NULL,
  `item_type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `item_source` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `item_target` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `file_source` bigint(20) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('local::/home/nextcloud/data/',1,1,NULL),('home::admin',2,1,NULL),('home::exam1',3,1,NULL),('home::exam2',4,1,NULL),('home::exam3',5,1,NULL),('home::exam4',6,1,NULL),('home::exam5',7,1,NULL),('home::guest1',8,1,NULL),('home::guest10',9,1,NULL),('home::guest2',10,1,NULL),('home::guest3',11,1,NULL),('home::guest4',12,1,NULL),('home::guest5',13,1,NULL),('home::guest6',14,1,NULL),('home::guest7',15,1,NULL),('home::guest8',16,1,NULL),('home::guest9',17,1,NULL),('home::ismith',18,1,NULL),('home::jjones',19,1,NULL),('home::profileuser',20,1,NULL),('home::sysadmin',21,1,NULL),('home::tech1',22,1,NULL),('home::tech2',23,1,NULL),('home::tech3',24,1,NULL),('home::tech4',25,1,NULL),('smb::admin@CHANGETHISREALM//dfs/homes/admin//',26,0,1519457283),('smb::admin@CHANGETHISREALM//dfs/subjects//',27,0,1519457283);
/*!40000 ALTER TABLE `oc_storages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_systemtag`
--

DROP TABLE IF EXISTS `oc_systemtag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_systemtag` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
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
  `systemtagid` bigint(20) unsigned NOT NULL DEFAULT '0',
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
  `systemtagid` bigint(20) unsigned NOT NULL DEFAULT '0',
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
-- Table structure for table `oc_talk_participants`
--

DROP TABLE IF EXISTS `oc_talk_participants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_talk_participants` (
  `user_id` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `room_id` int(10) unsigned NOT NULL DEFAULT '0',
  `last_ping` int(10) unsigned NOT NULL DEFAULT '0',
  `session_id` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `participant_type` smallint(5) unsigned NOT NULL DEFAULT '0',
  `in_call` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_talk_participants`
--

LOCK TABLES `oc_talk_participants` WRITE;
/*!40000 ALTER TABLE `oc_talk_participants` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_talk_participants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_talk_rooms`
--

DROP TABLE IF EXISTS `oc_talk_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_talk_rooms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT '',
  `token` varchar(32) COLLATE utf8mb4_bin DEFAULT '',
  `type` int(11) NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_bin DEFAULT '',
  `active_since` datetime DEFAULT NULL,
  `active_guests` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tr_room_token` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_talk_rooms`
--

LOCK TABLES `oc_talk_rooms` WRITE;
/*!40000 ALTER TABLE `oc_talk_rooms` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_talk_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_talk_signaling`
--

DROP TABLE IF EXISTS `oc_talk_signaling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_talk_signaling` (
  `sender` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `recipient` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `message` longtext COLLATE utf8mb4_bin NOT NULL,
  `timestamp` int(11) NOT NULL,
  KEY `ts_recipient_time` (`recipient`,`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=COMPRESSED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_talk_signaling`
--

LOCK TABLES `oc_talk_signaling` WRITE;
/*!40000 ALTER TABLE `oc_talk_signaling` DISABLE KEYS */;
/*!40000 ALTER TABLE `oc_talk_signaling` ENABLE KEYS */;
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
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
INSERT INTO `oc_users` VALUES ('admin',NULL,'1|$2y$10$Ay3fv/ex4rriJtNMGU5W2OnKTYaVNX2PxlsZQLwTXNZbjFEOLy8O6');
/*!40000 ALTER TABLE `oc_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oc_vcategory`
--

DROP TABLE IF EXISTS `oc_vcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_vcategory` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
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
  `objid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `categoryid` bigint(20) unsigned NOT NULL DEFAULT '0',
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

-- Dump completed on 2018-02-24  7:42:06
