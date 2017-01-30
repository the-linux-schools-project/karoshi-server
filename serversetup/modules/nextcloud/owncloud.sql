-- MySQL dump 10.13  Distrib 5.7.11, for Linux (x86_64)
--
-- Host: localhost    Database: owncloud
-- ------------------------------------------------------
-- Server version	5.7.11-0ubuntu6

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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbookchanges`
--

LOCK TABLES `oc_addressbookchanges` WRITE;
/*!40000 ALTER TABLE `oc_addressbookchanges` DISABLE KEYS */;
INSERT INTO `oc_addressbookchanges` VALUES (10,'Database:admin.vcf',10,3,1),(11,'LDAP:sysadmin.vcf',11,3,1),(12,'LDAP:guest10.vcf',12,3,1),(13,'LDAP:guest1.vcf',13,3,1),(14,'LDAP:guest2.vcf',14,3,1),(15,'LDAP:guest3.vcf',15,3,1),(16,'LDAP:guest4.vcf',16,3,1),(17,'LDAP:guest5.vcf',17,3,1),(18,'LDAP:guest6.vcf',18,3,1),(19,'LDAP:guest7.vcf',19,3,1),(20,'LDAP:guest8.vcf',20,3,1),(21,'LDAP:guest9.vcf',21,3,1),(22,'LDAP:ismith.vcf',22,3,1),(23,'LDAP:tech1.vcf',23,3,1),(24,'LDAP:tech2.vcf',24,3,1),(25,'LDAP:tech3.vcf',25,3,1),(26,'LDAP:tech4.vcf',26,3,1),(27,'LDAP:exam1.vcf',27,3,1),(28,'LDAP:exam2.vcf',28,3,1),(29,'LDAP:exam3.vcf',29,3,1),(30,'LDAP:exam4.vcf',30,3,1),(31,'LDAP:exam5.vcf',31,3,1),(32,'LDAP:profileuser.vcf',32,3,1);
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
INSERT INTO `oc_addressbooks` VALUES (1,'principals/users/FDE96242-A375-4C1B-B272-29191FE2D4B0','default','default',NULL,1),(2,'principals/users/admin','default','default',NULL,1),(3,'principals/system/system','system','system','System addressbook which holds all users of this instance',33);
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.2.1'),('activity','types','filesystem'),('backgroundjob','lastjob','12'),('comments','enabled','yes'),('comments','installed_version','0.2'),('comments','types','logging'),('core','OC_Channel','daily'),('core','installedat','1456918136.5882'),('core','lastcron','1461328713'),('core','lastupdateResult','{\"version\":\"100.0.0.0\",\"versionstring\":\"ownCloud daily\",\"url\":\"https:\\/\\/download.owncloud.org\\/community\\/owncloud-daily-stable9.zip\",\"web\":\"https:\\/\\/doc.owncloud.org\\/server\\/8.2\\/admin_manual\\/maintenance\\/upgrade.html\"}'),('core','lastupdatedat','1461328615'),('core','oc.integritycheck.checker','[]'),('core','public_documents','documents/public.php'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('core','remote_caldav','dav/appinfo/v1/caldav.php'),('core','remote_calendar','dav/appinfo/v1/caldav.php'),('core','remote_carddav','dav/appinfo/v1/carddav.php'),('core','remote_contacts','dav/appinfo/v1/carddav.php'),('core','remote_dav','dav/appinfo/v2/remote.php'),('core','remote_files','dav/appinfo/v1/webdav.php'),('core','remote_webdav','dav/appinfo/v1/webdav.php'),('core','repairlegacystoragesdone','yes'),('core','shareapi_allow_resharing','no'),('core','updater.secret.created','1461328407'),('dav','enabled','yes'),('dav','installed_version','0.1.6'),('dav','types','filesystem'),('documents','enabled','no'),('documents','installed_version','0.12.0'),('documents','ocsid','168711'),('documents','types',''),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','0.1.0'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','0.0.4'),('federation','types','authentication'),('files','cronjob_scan_files','500'),('files','enabled','yes'),('files','installed_version','1.4.4'),('files','types','filesystem'),('files_external','allow_user_mounting','no'),('files_external','enabled','yes'),('files_external','installed_version','0.5.2'),('files_external','ocsid','166048'),('files_external','types','filesystem'),('files_external','user_mounting_backends','ftp,dav,owncloud,sftp,amazons3,dropbox,googledrive,swift,smb,\\OC\\Files\\Storage\\SFTP_Key,\\OC\\Files\\Storage\\SMB_OC'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','0.8'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','0.9.1'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.1'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','0.8.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.2.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','0.9.8'),('files_videoplayer','types',''),('files_videoviewer','enabled','no'),('files_videoviewer','installed_version','0.1.3'),('files_videoviewer','ocsid','166054'),('files_videoviewer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','1.1'),('firstrunwizard','ocsid','166055'),('firstrunwizard','types',''),('gallery','enabled','yes'),('gallery','installed_version','14.5.0'),('gallery','types',''),('notes','enabled','no'),('notes','installed_version','2.0.1'),('notes','ocsid','174554'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','0.2.3'),('notifications','types','logging'),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','0.4.1'),('provisioning_api','types','prevent_group_restriction'),('systemtags','enabled','yes'),('systemtags','installed_version','0.2'),('systemtags','types','logging'),('templateeditor','enabled','yes'),('templateeditor','installed_version','0.1'),('templateeditor','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','0.1.0'),('updatenotification','types',''),('updater','enabled','no'),('updater','installed_version','0.6'),('updater','types',''),('user_ldap','cleanUpJobOffset','0'),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','0.8.0'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr','cn'),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','ldap://127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=organizationalPerson)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','1'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','1'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','organizationalPerson'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=organizationalPerson)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1');
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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendars`
--

LOCK TABLES `oc_calendars` WRITE;
/*!40000 ALTER TABLE `oc_calendars` DISABLE KEYS */;
INSERT INTO `oc_calendars` VALUES (1,'principals/users/FDE96242-A375-4C1B-B272-29191FE2D4B0','default','default',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(2,'principals/users/admin','default','default',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(3,'principals/system/system','contact_birthdays','contact_birthdays',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(4,'principals/users/admin','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(5,'principals/users/sysadmin','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(6,'principals/users/guest10','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(7,'principals/users/guest1','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(8,'principals/users/guest2','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(9,'principals/users/guest3','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(10,'principals/users/guest4','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(11,'principals/users/guest5','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(12,'principals/users/guest6','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(13,'principals/users/guest7','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(14,'principals/users/guest8','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(15,'principals/users/guest9','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(16,'principals/users/ismith','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(17,'principals/users/tech1','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(18,'principals/users/tech2','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(19,'principals/users/tech3','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(20,'principals/users/tech4','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(21,'principals/users/exam1','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(22,'principals/users/exam2','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(23,'principals/users/exam3','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(24,'principals/users/exam4','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(25,'principals/users/exam5','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0),(26,'principals/users/profileuser','Contact birthdays','contact_birthdays',1,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;


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
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_mounts`
--

LOCK TABLES `oc_external_mounts` WRITE;
/*!40000 ALTER TABLE `oc_external_mounts` DISABLE KEYS */;
INSERT INTO `oc_external_mounts` VALUES (2,'/home','smb','password::sessioncredentials',100,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_options`
--

LOCK TABLES `oc_external_options` WRITE;
/*!40000 ALTER TABLE `oc_external_options` DISABLE KEYS */;
INSERT INTO `oc_external_options` VALUES (5,2,'encrypt','true'),(6,2,'previews','true'),(7,2,'filesystem_check_changes','1'),(8,2,'enable_sharing','false');
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
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (23,0,'files/2c7eaecb9090bd89cef1dcd4d0d5881a',1461331968),(24,0,'files/2265a7864cbb01fd760398e786dc9eee',1461332311),(25,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1461332257),(26,0,'files/7f472eca153e78ea7caaa6d969440cba',1461331968),(28,0,'files/3513aba8aa4305d3ad33fc7122d4af30',1461331968),(29,0,'files/37c85de42508b164a7d7f502df40796e',1461331968),(30,0,'files/173a67328b2dceac7a89367cdcc7b1b6',1461331968),(31,0,'files/47b35dd91a203e06efeb4436117e4def',1461331968),(32,0,'files/a3594fd4eca7119cb937772e1f8f5415',1461331968),(33,0,'files/4d0a5085369fc0554c67b8420144d947',1461331967),(34,0,'files/b90e2f3adbfcaaa9507228281d9f15e7',1461331968),(45,0,'files/468c740695b998c9b920835b3af18225',1461332257),(46,0,'files/1a3c3f93ca79c2ca62845777b136b4fe',1461332311),(47,0,'files/6868cf08f134e4ecd9c67e38641df516',1461332311),(48,0,'files/3e0af14d5271af42865bdaa6a9b668ef',1461332311),(49,0,'files/7107b3afb9d25db8c4c2c58e71e8c0ac',1461332311),(50,0,'files/228a47e1c54e7c56e1df5be52615f554',1461332311),(51,0,'files/ccd5867b110c51fe9b9df5956b9f22dd',1461332311),(52,0,'files/c2a592af53bcc32c877c55c3397f3520',1461332311),(53,0,'files/8526746e8561ee494303fe5516868760',1461332311),(54,0,'files/bb166a694622fcc1e912d40218e27fb6',1461332312),(55,0,'files/62106b3c9c93cb6201616390d72d6c18',1461332312),(56,0,'files/05ca4d2ebc744e27d3816f5927324151',1461332312),(57,0,'files/1a5e469fc6e0f5606d5214ae00f09e4b',1461332312),(58,0,'files/488f4074bf8bbafabcfe2531b2de081e',1461332312),(59,0,'files/d7639b8862753bb00bd95fcc197824ae',1461332312),(60,0,'files/b6e959f26bf3ca22766f78c502f6bd4c',1461332312),(61,0,'files/9714630514ffd94bf0173dac5216fc01',1461332312),(62,0,'files/94d6e57f87a95ab97190ea200c471d58',1461332312),(63,0,'files/6003c26f820e7dfb8cf1349b1eee4192',1461332312),(64,0,'files/8d808264268ae2fe9bc1ba387ea3d422',1461332312),(65,0,'files/3fc6c5255194229c8fe7207c019f799d',1461332312),(66,0,'files/f9b7ca3604813ca018716be621bb7909',1461332313),(67,0,'files/74166daef647b6b8b80bb306691fccb1',1461332313);
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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,3259772,1457516558,1457516557,0,0,'56dff00ed63cd',23,NULL),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,3259772,1457516558,1457516558,0,0,'56dff00ed739e',31,NULL),(10,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,3259772,1456918806,1456918805,0,0,'56d6d11666336',23,NULL),(11,3,'cache','0fea6a13c52b4d4725368f24b045ca84',10,'cache',2,1,0,1456918805,1456918805,0,0,'56d6d1157c00d',31,NULL),(12,3,'files','45b963397aa40d4a0063e0d85e4fe7a1',10,'files',2,1,3259772,1456920501,1456918806,0,0,'56d6d7b5510f3',31,NULL),(13,3,'files/ownCloud_User_Manual.pdf','fbaae4021d9c766fc309c54e81133013',12,'ownCloud_User_Manual.pdf',4,3,2544989,1456918805,1456918805,0,0,'8af623094069ea4d8ac3224c53e45087',27,NULL),(14,3,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',12,'Documents',2,1,36227,1456918805,1456918805,0,0,'56d6d115f0a2e',31,NULL),(15,3,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',14,'Example.odt',7,3,36227,1456918806,1456918806,0,0,'b859bcb5612690ce134572e1fd540b62',27,NULL),(16,3,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',12,'Photos',2,1,678556,1456918806,1456918806,0,0,'56d6d116682f7',31,NULL),(17,3,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',16,'Squirrel.jpg',6,5,233724,1456918806,1456918806,0,0,'959059e80e056225ecde63b1668ea456',27,NULL),(18,3,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',16,'San Francisco.jpg',6,5,216071,1456918806,1456918806,0,0,'6c253191799e50a282124d1aba2a0a02',27,NULL),(19,3,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',16,'Paris.jpg',6,5,228761,1456918806,1456918806,0,0,'84b53d7c493a7bdfa3f3a9550db976e0',27,NULL),(20,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1457516557,1457516557,0,0,'56dff00d7af3f',31,NULL),(21,5,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,0,1456920501,1456920501,0,0,'56d6d7b553492',23,NULL),(22,5,'test.txt','dd18bf3a8e0a2a3e53e2661c7fb53534',21,'test.txt',9,8,0,1456920501,1456920501,0,0,'56d6d7b53aa6e',27,NULL),(23,1,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',2,'Documents',2,1,36227,1457516557,1457516557,0,0,'56dff00de86b4',31,NULL),(24,1,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',23,'Example.odt',7,3,36227,1457516558,1457516558,0,0,'ec8aa877ee070ddc7a6e85050199a600',27,NULL),(25,1,'files/ownCloud_User_Manual.pdf','fbaae4021d9c766fc309c54e81133013',2,'ownCloud_User_Manual.pdf',4,3,2544989,1457516558,1457516558,0,0,'e897730ed8d693b343d07871d9192549',27,NULL),(26,1,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',2,'Photos',2,1,678556,1457516558,1457516558,0,0,'56dff00ed88e8',31,NULL),(27,1,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',26,'San Francisco.jpg',6,5,216071,1457516558,1457516558,0,0,'eda6805ba5a61d2708857a763726d503',27,NULL),(28,1,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',26,'Paris.jpg',6,5,228761,1457516558,1457516558,0,0,'0e61d068b0a507710db7b15dc540b3eb',27,NULL),(29,1,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',26,'Squirrel.jpg',6,5,233724,1457516558,1457516558,0,0,'a2fd50d566664c764d638817666a73b9',27,NULL),(30,2,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1457518934,1457518934,0,0,'56dff956d9d51',23,NULL),(31,2,'files_external','c270928b685e7946199afdfb898d27ea',30,'files_external',2,1,0,1457518934,1457518934,0,0,'56dff956ca18f',31,NULL),(32,8,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,714783,1457519003,1457519003,0,0,'56dff99b9afff',23,NULL),(33,8,'cache','0fea6a13c52b4d4725368f24b045ca84',32,'cache',2,1,0,1457519002,1457519002,0,0,'56dff99ae728c',31,NULL),(34,8,'files','45b963397aa40d4a0063e0d85e4fe7a1',32,'files',2,1,714783,1457519003,1457519003,0,0,'56dff99b9a159',31,NULL),(35,8,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',34,'Documents',2,1,36227,1457519003,1457519003,0,0,'56dff99b37d25',31,NULL),(36,8,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',35,'Example.odt',7,3,36227,1457519003,1457519003,0,0,'af71ca06a8a6c580a99c02344900def9',27,NULL),(37,8,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',34,'Photos',2,1,678556,1457519003,1457519003,0,0,'56dff99b9914e',31,NULL),(38,8,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',37,'San Francisco.jpg',6,5,216071,1457519003,1457519003,0,0,'d91c7378999aefdd564f6ea8687579b7',27,NULL),(39,8,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',37,'Paris.jpg',6,5,228761,1457519003,1457519003,0,0,'80becc70c276c68c858ba043e2bc9056',27,NULL),(40,8,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',37,'Squirrel.jpg',6,5,233724,1457519003,1457519003,0,0,'ac4372d06b18bb242c6f5e5f435a58f1',27,NULL),(41,7,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1457515990,1457515990,0,0,'56dff99f3ef83',23,NULL),(42,17,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,714783,1461328368,1461328367,0,0,'571a19f07aef0',23,NULL),(43,17,'cache','0fea6a13c52b4d4725368f24b045ca84',42,'cache',2,1,0,1461328367,1461328367,0,0,'571a19efc765d',31,NULL),(44,17,'files','45b963397aa40d4a0063e0d85e4fe7a1',42,'files',2,1,714783,1461328368,1461328368,0,0,'571a19f07a2df',31,NULL),(45,17,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',44,'Photos',2,1,678556,1461328368,1461328368,0,0,'571a19f04fb6c',31,NULL),(46,17,'files/Photos/Paris.jpg','a208ddedf08367bbc56963107248dda5',45,'Paris.jpg',6,5,228761,1461328368,1461328368,0,0,'4011ec5d0c354abffeea9985d773ba94',27,NULL),(47,17,'files/Photos/Squirrel.jpg','de85d1da71bcd6232ad893f959063b8c',45,'Squirrel.jpg',6,5,233724,1461328368,1461328368,0,0,'90e0edb44c4331688228e8c5a414c02e',27,NULL),(48,17,'files/Photos/San Francisco.jpg','9fc714efbeaafee22f7058e73d2b1c3b',45,'San Francisco.jpg',6,5,216071,1461328368,1461328368,0,0,'deee77915af6f557239e32901b6a7f0a',27,NULL),(49,17,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',44,'Documents',2,1,36227,1461328368,1461328368,0,0,'571a19f078a17',31,NULL),(50,17,'files/Documents/Example.odt','c89c560541b952a435783a7d51a27d50',49,'Example.odt',7,3,36227,1461328368,1461328368,0,0,'c2b9baa597874f3a4818ec4f5d3460e7',27,NULL),(51,18,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1461328368,1461328368,0,0,'571a19f0e3d4d',23,NULL),(52,18,'files_external','c270928b685e7946199afdfb898d27ea',51,'files_external',2,1,0,1461328368,1461328368,0,0,'571a19f0de0fe',31,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Files_sharing\\Lib\\DeleteOrphanedSharesJob','null',1457519138),(2,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1461328364),(3,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1461328372),(4,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1461328384),(5,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1461328391),(6,'OCA\\user_ldap\\lib\\Jobs','null',1461328619),(7,'\\OCA\\User_LDAP\\Jobs\\CleanUp','null',1461328627),(8,'OCA\\Files\\BackgroundJob\\ScanFiles','null',1461328652),(9,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',1461328657),(10,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',1461328662),(11,'OCA\\Files_sharing\\ExpireSharesJob','null',1461328670),(12,'OCA\\DAV\\CardDAV\\SyncJob','null',1461328710),(13,'OCA\\Federation\\SyncJob','null',1457519123),(14,'OCA\\UpdateNotification\\ResetTokenBackgroundJob','null',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

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
INSERT INTO `oc_preferences` VALUES ('admin','core','lang','en'),('admin','core','timezone','Europe/London'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1461328655'),('exam1','files_external','config_version','0.5.0'),('exam1','user_ldap','displayName','Exam 1'),('exam1','user_ldap','homePath',''),('exam1','user_ldap','lastFeatureRefresh','1461328711'),('exam1','user_ldap','uid','exam1'),('exam2','files_external','config_version','0.5.0'),('exam2','user_ldap','displayName','Exam 2'),('exam2','user_ldap','homePath',''),('exam2','user_ldap','lastFeatureRefresh','1461328711'),('exam2','user_ldap','uid','exam2'),('exam3','files_external','config_version','0.5.0'),('exam3','user_ldap','displayName','Exam 3'),('exam3','user_ldap','homePath',''),('exam3','user_ldap','lastFeatureRefresh','1461328711'),('exam3','user_ldap','uid','exam3'),('exam4','files_external','config_version','0.5.0'),('exam4','user_ldap','displayName','Exam 4'),('exam4','user_ldap','homePath',''),('exam4','user_ldap','lastFeatureRefresh','1461328711'),('exam4','user_ldap','uid','exam4'),('exam5','files_external','config_version','0.5.0'),('exam5','user_ldap','displayName','Exam 5'),('exam5','user_ldap','homePath',''),('exam5','user_ldap','lastFeatureRefresh','1461328711'),('exam5','user_ldap','uid','exam5'),('guest1','files_external','config_version','0.5.0'),('guest1','user_ldap','displayName','Guest 1'),('guest1','user_ldap','homePath',''),('guest1','user_ldap','lastFeatureRefresh','1461328710'),('guest1','user_ldap','uid','guest1'),('guest10','files_external','config_version','0.5.0'),('guest10','user_ldap','displayName','Guest 10'),('guest10','user_ldap','homePath',''),('guest10','user_ldap','lastFeatureRefresh','1461328710'),('guest10','user_ldap','uid','guest10'),('guest2','files_external','config_version','0.5.0'),('guest2','user_ldap','displayName','Guest 2'),('guest2','user_ldap','homePath',''),('guest2','user_ldap','lastFeatureRefresh','1461328710'),('guest2','user_ldap','uid','guest2'),('guest3','files_external','config_version','0.5.0'),('guest3','user_ldap','displayName','Guest 3'),('guest3','user_ldap','homePath',''),('guest3','user_ldap','lastFeatureRefresh','1461328710'),('guest3','user_ldap','uid','guest3'),('guest4','files_external','config_version','0.5.0'),('guest4','user_ldap','displayName','Guest 4'),('guest4','user_ldap','homePath',''),('guest4','user_ldap','lastFeatureRefresh','1461328710'),('guest4','user_ldap','uid','guest4'),('guest5','files_external','config_version','0.5.0'),('guest5','user_ldap','displayName','Guest 5'),('guest5','user_ldap','homePath',''),('guest5','user_ldap','lastFeatureRefresh','1461328711'),('guest5','user_ldap','uid','guest5'),('guest6','files_external','config_version','0.5.0'),('guest6','user_ldap','displayName','Guest 6'),('guest6','user_ldap','homePath',''),('guest6','user_ldap','lastFeatureRefresh','1461328711'),('guest6','user_ldap','uid','guest6'),('guest7','files_external','config_version','0.5.0'),('guest7','user_ldap','displayName','Guest 7'),('guest7','user_ldap','homePath',''),('guest7','user_ldap','lastFeatureRefresh','1461328711'),('guest7','user_ldap','uid','guest7'),('guest8','files_external','config_version','0.5.0'),('guest8','user_ldap','displayName','Guest 8'),('guest8','user_ldap','homePath',''),('guest8','user_ldap','lastFeatureRefresh','1461328711'),('guest8','user_ldap','uid','guest8'),('guest9','files_external','config_version','0.5.0'),('guest9','user_ldap','displayName','Guest 9'),('guest9','user_ldap','homePath',''),('guest9','user_ldap','lastFeatureRefresh','1461328711'),('guest9','user_ldap','uid','guest9'),('ismith','files_external','config_version','0.5.0'),('ismith','user_ldap','displayName','Ian Smith'),('ismith','user_ldap','homePath',''),('ismith','user_ldap','lastFeatureRefresh','1461328711'),('ismith','user_ldap','uid','ismith'),('profileuser','files_external','config_version','0.5.0'),('profileuser','user_ldap','displayName','Profile User'),('profileuser','user_ldap','homePath',''),('profileuser','user_ldap','lastFeatureRefresh','1461328711'),('profileuser','user_ldap','uid','profileuser'),('sysadmin','files_external','config_version','0.5.0'),('sysadmin','user_ldap','displayName','Sysadmin User'),('sysadmin','user_ldap','homePath',''),('sysadmin','user_ldap','lastFeatureRefresh','1461328710'),('sysadmin','user_ldap','uid','sysadmin'),('tech1','files_external','config_version','0.5.0'),('tech1','user_ldap','displayName','Tech 1'),('tech1','user_ldap','homePath',''),('tech1','user_ldap','lastFeatureRefresh','1461328711'),('tech1','user_ldap','uid','tech1'),('tech2','files_external','config_version','0.5.0'),('tech2','user_ldap','displayName','Tech 2'),('tech2','user_ldap','homePath',''),('tech2','user_ldap','lastFeatureRefresh','1461328711'),('tech2','user_ldap','uid','tech2'),('tech3','files_external','config_version','0.5.0'),('tech3','user_ldap','displayName','Tech 3'),('tech3','user_ldap','homePath',''),('tech3','user_ldap','lastFeatureRefresh','1461328711'),('tech3','user_ldap','uid','tech3'),('tech4','files_external','config_version','0.5.0'),('tech4','user_ldap','displayName','Tech 4'),('tech4','user_ldap','homePath',''),('tech4','user_ldap','lastFeatureRefresh','1461328711'),('tech4','user_ldap','uid','tech4');
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
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

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

-- Dump completed on 2016-04-22 13:42:56
