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
INSERT INTO `oc_accounts` VALUES ('admin','{\"displayname\":{\"value\":\"admin\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam1','{\"displayname\":{\"value\":\"Exam 1\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam2','{\"displayname\":{\"value\":\"Exam 2\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam3','{\"displayname\":{\"value\":\"Exam 3\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam4','{\"displayname\":{\"value\":\"Exam 4\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam5','{\"displayname\":{\"value\":\"Exam 5\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest1','{\"displayname\":{\"value\":\"Guest 1\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest10','{\"displayname\":{\"value\":\"Guest 10\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest2','{\"displayname\":{\"value\":\"Guest 2\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest3','{\"displayname\":{\"value\":\"Guest 3\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest4','{\"displayname\":{\"value\":\"Guest 4\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest5','{\"displayname\":{\"value\":\"Guest 5\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest6','{\"displayname\":{\"value\":\"Guest 6\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest7','{\"displayname\":{\"value\":\"Guest 7\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest8','{\"displayname\":{\"value\":\"Guest 8\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest9','{\"displayname\":{\"value\":\"Guest 9\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('ismith','{\"displayname\":{\"value\":\"Ian Smith\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('profileuser','{\"displayname\":{\"value\":\"Profile User\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('sysadmin','{\"displayname\":{\"value\":\"Sysadmin User\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech1','{\"displayname\":{\"value\":\"Tech 1\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech2','{\"displayname\":{\"value\":\"Tech 2\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech3','{\"displayname\":{\"value\":\"Tech 3\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech4','{\"displayname\":{\"value\":\"Tech 4\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_activity`
--

LOCK TABLES `oc_activity` WRITE;
/*!40000 ALTER TABLE `oc_activity` DISABLE KEYS */;
INSERT INTO `oc_activity` VALUES (1,1485536381,30,'file_created','admin','admin','files','created_self','[{\"2\":\"\"}]','','[]','','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=','files',2),(2,1485536381,30,'file_created','admin','admin','files','created_self','[{\"3\":\"\\/Nextcloud.mp4\"}]','','[]','/Nextcloud.mp4','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',3),(3,1485536381,30,'file_created','admin','admin','files','created_self','[{\"7\":\"\\/Photos\"}]','','[]','/Photos','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',7),(4,1485536381,30,'file_created','admin','admin','files','created_self','[{\"8\":\"\\/Photos\\/Nut.jpg\"}]','','[]','/Photos/Nut.jpg','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Photos','files',8),(5,1485536381,30,'file_created','admin','admin','files','created_self','[{\"9\":\"\\/Photos\\/Hummingbird.jpg\"}]','','[]','/Photos/Hummingbird.jpg','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Photos','files',9),(6,1485536381,30,'file_created','admin','admin','files','created_self','[{\"10\":\"\\/Photos\\/Coast.jpg\"}]','','[]','/Photos/Coast.jpg','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Photos','files',10),(7,1485536382,30,'file_created','admin','admin','files','created_self','[{\"11\":\"\\/Documents\"}]','','[]','/Documents','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',11),(8,1485536382,30,'file_created','admin','admin','files','created_self','[{\"12\":\"\\/Documents\\/About.txt\"}]','','[]','/Documents/About.txt','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Documents','files',12),(9,1485536382,30,'file_created','admin','admin','files','created_self','[{\"13\":\"\\/Documents\\/About.odt\"}]','','[]','/Documents/About.odt','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/Documents','files',13),(10,1485536382,30,'file_created','admin','admin','files','created_self','[{\"14\":\"\\/Nextcloud Manual.pdf\"}]','','[]','/Nextcloud Manual.pdf','https://www.constellations.com/nextcloud/index.php/apps/files/?dir=/','files',14),(11,1485536382,30,'calendar','admin','admin','dav','calendar_add_self','[\"admin\",\"Personal\"]','','[]','','','calendar',1),(12,1496390443,30,'calendar','system','system','dav','calendar_add_self','[\"system\",\"Contact birthdays\"]','','[]','','','calendar',2);
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
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbookchanges`
--

LOCK TABLES `oc_addressbookchanges` WRITE;
/*!40000 ALTER TABLE `oc_addressbookchanges` DISABLE KEYS */;
INSERT INTO `oc_addressbookchanges` VALUES (1,'Database:admin.vcf',1,2,1),(2,'LDAP:sysadmin.vcf',2,2,1),(3,'LDAP:guest10.vcf',3,2,1),(4,'LDAP:guest1.vcf',4,2,1),(5,'LDAP:guest2.vcf',5,2,1),(6,'LDAP:guest3.vcf',6,2,1),(7,'LDAP:guest4.vcf',7,2,1),(8,'LDAP:guest5.vcf',8,2,1),(9,'LDAP:guest6.vcf',9,2,1),(10,'LDAP:guest7.vcf',10,2,1),(11,'LDAP:guest8.vcf',11,2,1),(12,'LDAP:guest9.vcf',12,2,1),(13,'LDAP:ismith.vcf',13,2,1),(14,'LDAP:tech1.vcf',14,2,1),(15,'LDAP:tech2.vcf',15,2,1),(16,'LDAP:tech3.vcf',16,2,1),(17,'LDAP:tech4.vcf',17,2,1),(18,'LDAP:exam1.vcf',18,2,1),(19,'LDAP:exam2.vcf',19,2,1),(20,'LDAP:exam3.vcf',20,2,1),(21,'LDAP:exam4.vcf',21,2,1),(22,'LDAP:exam5.vcf',22,2,1),(23,'LDAP:profileuser.vcf',23,2,1),(24,'Database:admin.vcf',24,2,3),(25,'LDAP:sysadmin.vcf',25,2,3),(26,'LDAP:guest10.vcf',26,2,3),(27,'LDAP:guest1.vcf',27,2,3),(28,'LDAP:guest2.vcf',28,2,3),(29,'LDAP:guest3.vcf',29,2,3),(30,'LDAP:guest4.vcf',30,2,3),(31,'LDAP:guest5.vcf',31,2,3),(32,'LDAP:guest6.vcf',32,2,3),(33,'LDAP:guest7.vcf',33,2,3),(34,'LDAP:guest8.vcf',34,2,3),(35,'LDAP:guest9.vcf',35,2,3),(36,'LDAP:ismith.vcf',36,2,3),(37,'LDAP:tech1.vcf',37,2,3),(38,'LDAP:tech2.vcf',38,2,3),(39,'LDAP:tech3.vcf',39,2,3),(40,'LDAP:tech4.vcf',40,2,3),(41,'LDAP:exam1.vcf',41,2,3),(42,'LDAP:exam2.vcf',42,2,3),(43,'LDAP:exam3.vcf',43,2,3),(44,'LDAP:exam4.vcf',44,2,3),(45,'LDAP:exam5.vcf',45,2,3),(46,'LDAP:profileuser.vcf',46,2,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbooks`
--

LOCK TABLES `oc_addressbooks` WRITE;
/*!40000 ALTER TABLE `oc_addressbooks` DISABLE KEYS */;
INSERT INTO `oc_addressbooks` VALUES (1,'principals/users/admin','Contacts','contacts',NULL,1),(2,'principals/system/system','system','system','System addressbook which holds all users of this instance',47);
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_admin_settings`
--

LOCK TABLES `oc_admin_settings` WRITE;
/*!40000 ALTER TABLE `oc_admin_settings` DISABLE KEYS */;
INSERT INTO `oc_admin_settings` VALUES (1,'OCA\\Federation\\Settings\\Admin','sharing',30),(2,'OCA\\ServerInfo\\Settings\\AdminSettings','serverinfo',0),(3,'OCA\\LogReader\\Settings\\Admin','logging',90),(4,'OCA\\FederatedFileSharing\\Settings\\Admin','sharing',20),(5,'OCA\\Theming\\Settings\\Admin','theming',5),(6,'OCA\\Survey_Client\\Settings\\AdminSettings','survey_client',50),(7,'OCA\\UpdateNotification\\Controller\\AdminController','server',1),(8,'OCA\\NextcloudAnnouncements\\Settings\\Admin','additional',30),(9,'OCA\\SystemTags\\Settings\\Admin','workflow',70),(10,'OCA\\Files\\Settings\\Admin','additional',5),(11,'OCA\\User_LDAP\\Settings\\Admin','ldap',5),(12,'OCA\\Files_External\\Settings\\Admin','externalstorages',40),(14,'OCA\\Richdocuments\\Settings\\Admin','richdocuments',0);
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.4.1'),('activity','types','filesystem'),('backgroundjob','lastjob','13'),('comments','enabled','yes'),('comments','installed_version','1.1.0'),('comments','types','logging'),('core','installedat','1485536380.8184'),('core','lastcron','1496390920'),('core','lastupdateResult','[]'),('core','lastupdatedat','1496390898'),('core','moveavatarsdone','yes'),('core','oc.integritycheck.checker','[]'),('core','previewsCleanedUp','1'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('core','repairlegacystoragesdone','yes'),('core','updater.secret.created','1496390643'),('core','vendor','nextcloud'),('dav','enabled','yes'),('dav','installed_version','1.1.1'),('dav','types','filesystem'),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','1.1.1'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','1.1.1'),('federation','types','authentication'),('files','cronjob_scan_files','500'),('files','enabled','yes'),('files','installed_version','1.6.1'),('files','types','filesystem'),('files_external','enabled','yes'),('files_external','installed_version','1.1.2'),('files_external','types','filesystem'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','1.0.1'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_reader','enabled','no'),('files_reader','installed_version','1.0.4'),('files_reader','ocsid','167127'),('files_reader','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','1.1.1'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.2'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','1.1.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.4.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','1.0.0'),('files_videoplayer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','2.0'),('firstrunwizard','types','logging'),('gallery','enabled','yes'),('gallery','installed_version','16.0.0'),('gallery','types',''),('logreader','enabled','yes'),('logreader','installed_version','2.0.0'),('logreader','ocsid','170871'),('logreader','types',''),('lookup_server_connector','enabled','yes'),('lookup_server_connector','installed_version','1.0.0'),('lookup_server_connector','types','authentication'),('nextcloud_announcements','enabled','yes'),('nextcloud_announcements','installed_version','1.0'),('nextcloud_announcements','pub_date','Sat, 10 Dec 2016 00:00:00 +0100'),('nextcloud_announcements','types','logging'),('notes','enabled','no'),('notes','installed_version','2.2.0'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','1.0.1'),('notifications','types','logging'),('password_policy','enabled','yes'),('password_policy','installed_version','1.1.0'),('password_policy','types',''),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','1.1.0'),('provisioning_api','types','prevent_group_restriction'),('richdocuments','enabled','no'),('richdocuments','installed_version','1.11.31'),('richdocuments','types','prevent_group_restriction'),('richdocuments','wopi_url','https://CHANGETHISREALM'),('serverinfo','enabled','yes'),('serverinfo','installed_version','1.1.1'),('serverinfo','types',''),('sharebymail','enabled','yes'),('sharebymail','installed_version','1.0.1'),('sharebymail','types','filesystem'),('survey_client','enabled','yes'),('survey_client','installed_version','0.1.5'),('survey_client','types',''),('systemtags','enabled','yes'),('systemtags','installed_version','1.1.3'),('systemtags','types','logging'),('theming','enabled','yes'),('theming','installed_version','1.1.1'),('theming','types','logging'),('twofactor_backupcodes','enabled','yes'),('twofactor_backupcodes','installed_version','1.0.0'),('twofactor_backupcodes','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','1.1.1'),('updatenotification','types',''),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','1.1.2'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr','sAMAccountName'),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=person)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_turn_on_pwd_change','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','posixAccount'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=posixAccount)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1'),('workflowengine','enabled','yes'),('workflowengine','installed_version','1.1.1'),('workflowengine','types','filesystem');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarchanges`
--

LOCK TABLES `oc_calendarchanges` WRITE;
/*!40000 ALTER TABLE `oc_calendarchanges` DISABLE KEYS */;
INSERT INTO `oc_calendarchanges` VALUES (1,'system-Database:admin.vcf.ics',1,2,3),(2,'system-Database:admin.vcf-death.ics',2,2,3),(3,'system-Database:admin.vcf-anniversary.ics',3,2,3),(4,'system-LDAP:sysadmin.vcf.ics',4,2,3),(5,'system-LDAP:sysadmin.vcf-death.ics',5,2,3),(6,'system-LDAP:sysadmin.vcf-anniversary.ics',6,2,3),(7,'system-LDAP:guest10.vcf.ics',7,2,3),(8,'system-LDAP:guest10.vcf-death.ics',8,2,3),(9,'system-LDAP:guest10.vcf-anniversary.ics',9,2,3),(10,'system-LDAP:guest1.vcf.ics',10,2,3),(11,'system-LDAP:guest1.vcf-death.ics',11,2,3),(12,'system-LDAP:guest1.vcf-anniversary.ics',12,2,3),(13,'system-LDAP:guest2.vcf.ics',13,2,3),(14,'system-LDAP:guest2.vcf-death.ics',14,2,3),(15,'system-LDAP:guest2.vcf-anniversary.ics',15,2,3),(16,'system-LDAP:guest3.vcf.ics',16,2,3),(17,'system-LDAP:guest3.vcf-death.ics',17,2,3),(18,'system-LDAP:guest3.vcf-anniversary.ics',18,2,3),(19,'system-LDAP:guest4.vcf.ics',19,2,3),(20,'system-LDAP:guest4.vcf-death.ics',20,2,3),(21,'system-LDAP:guest4.vcf-anniversary.ics',21,2,3),(22,'system-LDAP:guest5.vcf.ics',22,2,3),(23,'system-LDAP:guest5.vcf-death.ics',23,2,3),(24,'system-LDAP:guest5.vcf-anniversary.ics',24,2,3),(25,'system-LDAP:guest6.vcf.ics',25,2,3),(26,'system-LDAP:guest6.vcf-death.ics',26,2,3),(27,'system-LDAP:guest6.vcf-anniversary.ics',27,2,3),(28,'system-LDAP:guest7.vcf.ics',28,2,3),(29,'system-LDAP:guest7.vcf-death.ics',29,2,3),(30,'system-LDAP:guest7.vcf-anniversary.ics',30,2,3),(31,'system-LDAP:guest8.vcf.ics',31,2,3),(32,'system-LDAP:guest8.vcf-death.ics',32,2,3),(33,'system-LDAP:guest8.vcf-anniversary.ics',33,2,3),(34,'system-LDAP:guest9.vcf.ics',34,2,3),(35,'system-LDAP:guest9.vcf-death.ics',35,2,3),(36,'system-LDAP:guest9.vcf-anniversary.ics',36,2,3),(37,'system-LDAP:ismith.vcf.ics',37,2,3),(38,'system-LDAP:ismith.vcf-death.ics',38,2,3),(39,'system-LDAP:ismith.vcf-anniversary.ics',39,2,3),(40,'system-LDAP:tech1.vcf.ics',40,2,3),(41,'system-LDAP:tech1.vcf-death.ics',41,2,3),(42,'system-LDAP:tech1.vcf-anniversary.ics',42,2,3),(43,'system-LDAP:tech2.vcf.ics',43,2,3),(44,'system-LDAP:tech2.vcf-death.ics',44,2,3),(45,'system-LDAP:tech2.vcf-anniversary.ics',45,2,3),(46,'system-LDAP:tech3.vcf.ics',46,2,3),(47,'system-LDAP:tech3.vcf-death.ics',47,2,3),(48,'system-LDAP:tech3.vcf-anniversary.ics',48,2,3),(49,'system-LDAP:tech4.vcf.ics',49,2,3),(50,'system-LDAP:tech4.vcf-death.ics',50,2,3),(51,'system-LDAP:tech4.vcf-anniversary.ics',51,2,3),(52,'system-LDAP:exam1.vcf.ics',52,2,3),(53,'system-LDAP:exam1.vcf-death.ics',53,2,3),(54,'system-LDAP:exam1.vcf-anniversary.ics',54,2,3),(55,'system-LDAP:exam2.vcf.ics',55,2,3),(56,'system-LDAP:exam2.vcf-death.ics',56,2,3),(57,'system-LDAP:exam2.vcf-anniversary.ics',57,2,3),(58,'system-LDAP:exam3.vcf.ics',58,2,3),(59,'system-LDAP:exam3.vcf-death.ics',59,2,3),(60,'system-LDAP:exam3.vcf-anniversary.ics',60,2,3),(61,'system-LDAP:exam4.vcf.ics',61,2,3),(62,'system-LDAP:exam4.vcf-death.ics',62,2,3),(63,'system-LDAP:exam4.vcf-anniversary.ics',63,2,3),(64,'system-LDAP:exam5.vcf.ics',64,2,3),(65,'system-LDAP:exam5.vcf-death.ics',65,2,3),(66,'system-LDAP:exam5.vcf-anniversary.ics',66,2,3),(67,'system-LDAP:profileuser.vcf.ics',67,2,3),(68,'system-LDAP:profileuser.vcf-death.ics',68,2,3),(69,'system-LDAP:profileuser.vcf-anniversary.ics',69,2,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendars`
--

LOCK TABLES `oc_calendars` WRITE;
/*!40000 ALTER TABLE `oc_calendars` DISABLE KEYS */;
INSERT INTO `oc_calendars` VALUES (1,'principals/users/admin','Personal','personal',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(2,'principals/system/system','Contact birthdays','contact_birthdays',70,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
INSERT INTO `oc_credentials` VALUES ('admin','password::logincredentials/credentials','dae2ffd01acca255a6123590101845499c34c5760bb368ac8ff802dd8067b76915a5e1ecb64039fcbefdf9981522a5ab|2yY/COD/nHaFCU5L|5abb1f8fd68ba1b5d7524247b4fe1c153abe8eef68477d07fc160c4763f528ac2e5fd11a4aa145c7041519fae6d0e270526c5f41191bf8062f9320cd59b24c83');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_applicable`
--

LOCK TABLES `oc_external_applicable` WRITE;
/*!40000 ALTER TABLE `oc_external_applicable` DISABLE KEYS */;
INSERT INTO `oc_external_applicable` VALUES (2,2,1,NULL),(9,9,1,NULL),(1,1,2,'itadmin'),(3,3,2,'itadmin'),(4,4,2,'itadmin'),(6,6,2,'itadmin'),(10,10,2,'itadmin'),(5,5,2,'officestaff'),(7,7,2,'officestaff'),(8,8,2,'staff');
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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_config`
--

LOCK TABLES `oc_external_config` WRITE;
/*!40000 ALTER TABLE `oc_external_config` DISABLE KEYS */;
INSERT INTO `oc_external_config` VALUES (1,1,'host','blackmesa.com'),(2,1,'share','dfs/applications'),(3,1,'root',''),(4,1,'domain',''),(5,2,'host','blackmesa.com'),(6,2,'share','dfs/homes/$user'),(7,2,'root',''),(8,2,'domain',''),(9,3,'host','blackmesa.com'),(10,3,'share','dfs/itadminshare'),(11,3,'root',''),(12,3,'domain',''),(13,4,'host','blackmesa.com'),(14,4,'share','dfs/netlogon'),(15,4,'root',''),(16,4,'domain',''),(17,5,'host','blackmesa.com'),(18,5,'share','dfs/officeshare'),(19,5,'root',''),(20,5,'domain',''),(21,6,'host','blackmesa.com'),(22,6,'share','dfs/staffshare'),(23,6,'root',''),(24,6,'domain',''),(25,7,'host','blackmesa.com'),(26,7,'share','dfs/staffshare'),(27,7,'root',''),(28,7,'domain',''),(29,8,'host','blackmesa.com'),(30,8,'share','dfs/staffshare'),(31,8,'root',''),(32,8,'domain',''),(33,9,'host','blackmesa.com'),(34,9,'share','dfs/subjects'),(35,9,'root',''),(36,9,'domain',''),(37,10,'host','blackmesa.com'),(38,10,'share','dfs/sysvol'),(39,10,'root',''),(40,10,'domain','');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_mounts`
--

LOCK TABLES `oc_external_mounts` WRITE;
/*!40000 ALTER TABLE `oc_external_mounts` DISABLE KEYS */;
INSERT INTO `oc_external_mounts` VALUES (1,'/applications','smb','password::sessioncredentials',100,1),(2,'/home','smb','password::sessioncredentials',100,1),(3,'/itadminshare','smb','password::sessioncredentials',100,1),(4,'/netlogon','smb','password::sessioncredentials',100,1),(5,'/officeshare','smb','password::sessioncredentials',100,1),(6,'/staffshare','smb','password::sessioncredentials',100,1),(7,'/staffshare','smb','password::sessioncredentials',100,1),(8,'/staffshare','smb','password::sessioncredentials',100,1),(9,'/subjects','smb','password::sessioncredentials',100,1),(10,'/sysvol','smb','password::sessioncredentials',100,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_external_options`
--

LOCK TABLES `oc_external_options` WRITE;
/*!40000 ALTER TABLE `oc_external_options` DISABLE KEYS */;
INSERT INTO `oc_external_options` VALUES (1,1,'encrypt','true'),(2,1,'previews','true'),(3,1,'filesystem_check_changes','1'),(4,1,'enable_sharing','false'),(5,2,'encrypt','true'),(6,2,'previews','true'),(7,2,'filesystem_check_changes','1'),(8,2,'enable_sharing','false'),(9,3,'encrypt','true'),(10,3,'previews','true'),(11,3,'filesystem_check_changes','1'),(12,3,'enable_sharing','false'),(13,4,'encrypt','true'),(14,4,'previews','true'),(15,4,'filesystem_check_changes','1'),(16,4,'enable_sharing','false'),(17,5,'encrypt','true'),(18,5,'previews','true'),(19,5,'filesystem_check_changes','1'),(20,5,'enable_sharing','false'),(21,6,'encrypt','true'),(22,6,'previews','true'),(23,6,'filesystem_check_changes','1'),(24,6,'enable_sharing','false'),(25,7,'encrypt','true'),(26,7,'previews','true'),(27,7,'filesystem_check_changes','1'),(28,7,'enable_sharing','false'),(29,8,'encrypt','true'),(30,8,'previews','true'),(31,8,'filesystem_check_changes','1'),(32,8,'enable_sharing','false'),(33,9,'encrypt','true'),(34,9,'previews','true'),(35,9,'filesystem_check_changes','1'),(36,9,'enable_sharing','false'),(37,10,'encrypt','true'),(38,10,'previews','true'),(39,10,'filesystem_check_changes','1'),(40,10,'enable_sharing','false');
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
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (1,0,'files/468c740695b998c9b920835b3af18225',1496394500),(2,0,'files/3ef927705e35f104f5c8825610e550db',1496394500),(3,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1496394500),(4,0,'files/bc76dde1a029b9698a1164dc9d6f4422',1496394037),(5,0,'files/af9a150df0eeee9b47333ce3a16cdaa7',1496394040),(6,0,'files/0b0bf7504da3e85a19c1ff28e71bdc41',1496394045),(7,0,'files/fd954ccb78c90d140492adb71821fd2a',1496394046),(8,0,'files/4fcd164ca020351227b482b90ca24ff3',1496394049),(9,0,'files/1b7d2e1df610642697ddfd5aa3c80cc5',1496394049),(10,0,'files/e192c9c41a458131730f33cf3a877f3e',1496394509),(11,0,'files/d34a1526233961dbb2802b95deb72855',1496394509),(12,0,'files/38f1a462ac005ca53e80d2b991446fcc',1496394509),(13,0,'files/94d6e57f87a95ab97190ea200c471d58',1496394509),(14,0,'files/ae772ffacde058275a973302b93e169f',1496394509),(15,0,'files/096c72660c7f861dfaeb3f51df57197d',1496394509),(16,0,'files/76287b2f29364703dfd1d9b543a9b4ea',1496394509),(17,0,'files/6003c26f820e7dfb8cf1349b1eee4192',1496394509),(18,0,'files/6fa5d6c56809e6801e7e198b29eca196',1496394509),(19,0,'files/10ae186be1ecece42101a1bcc32b4b77',1496394509),(20,0,'files/169ecf9ce9d92154b2d8f3bb3ae0a844',1496394510),(21,0,'files/8d808264268ae2fe9bc1ba387ea3d422',1496394510),(22,0,'files/87de26ddb4dff01f24bb1a8210defeb5',1496394510),(23,0,'files/d262910fa945abe9119fd0f3a9a6de43',1496394510),(24,0,'files/4462d021359874962ce01e459811fd2f',1496394510),(25,0,'files/3fc6c5255194229c8fe7207c019f799d',1496394510),(26,0,'files/8ef2d85679707501fc1095d25eb0b682',1496394510),(27,0,'files/62405c20776865a9e4e7964f74d457cd',1496394510),(28,0,'files/96de6c364514d73c48c4d1bb07cb500e',1496394510),(29,0,'files/f9b7ca3604813ca018716be621bb7909',1496394510),(30,0,'files/63d5d7085d4117087077904073755b9e',1496394510),(31,0,'files/286f76bab953e2e814b788ef70fa1ea1',1496394510),(32,0,'files/ee32bae6d3c598e340831969e79c6340',1496394510),(33,0,'files/3e0af14d5271af42865bdaa6a9b668ef',1496394510),(34,0,'files/34925b8736ee67966919655e742e03dc',1496394510),(35,0,'files/938a85501d3457771e2c4f73fe55f157',1496394510),(36,0,'files/11c6efefe7042583d9bc33a4020aeb62',1496394510),(37,0,'files/6868cf08f134e4ecd9c67e38641df516',1496394510),(38,0,'files/99ff37d7dc81f895bfb5346724b070cb',1496394510),(39,0,'files/14048f7db5b202aa77b195f4fc2a4dbf',1496394510),(40,0,'files/2b472e2132c1f0e68c63cc5652e1ecff',1496394511),(41,0,'files/7107b3afb9d25db8c4c2c58e71e8c0ac',1496394511),(42,0,'files/9b74ef140e521ee464f8305a218459e5',1496394511),(43,0,'files/7744c5b897b642b6867d07cfb5d7fa3b',1496394511),(44,0,'files/b2e4494a9b232ace38f0844901b5b4ba',1496394511),(45,0,'files/228a47e1c54e7c56e1df5be52615f554',1496394511),(46,0,'files/4b7f0af13a6167f01d4887164c044262',1496394511),(47,0,'files/305b1af4a205f72c7c0017aa4b2e9e1d',1496394511),(48,0,'files/aeb66e606de35cf9f9a90a92affda4ea',1496394511),(49,0,'files/ccd5867b110c51fe9b9df5956b9f22dd',1496394511),(50,0,'files/30b9d0c4bd8213ec68b5cee4f255acc5',1496394511),(51,0,'files/29bea8be4a30d864c1bcc5cd58b9f397',1496394511),(52,0,'files/45e5e4c8b19c96fc636c08cac20d67ff',1496394511),(53,0,'files/c2a592af53bcc32c877c55c3397f3520',1496394511),(54,0,'files/49f0261cef4ab4ba3f8b910e12c7f265',1496394511),(55,0,'files/86b30fa9fe56a46242e32a307eed8780',1496394511),(56,0,'files/90a7deb8600fbfa23023022e5837929d',1496394512),(57,0,'files/8526746e8561ee494303fe5516868760',1496394512),(58,0,'files/8cad288655d889893ed44e29ec10e3e6',1496394512),(59,0,'files/6230dbcf5c8ca19efe93ea8259c8b9ae',1496394512),(60,0,'files/e0ab5ae5038b2e8094771d158b3ff28f',1496394512),(61,0,'files/bb166a694622fcc1e912d40218e27fb6',1496394512),(62,0,'files/edf7e258cefa2d279f6ce26454d8dd5d',1496394512),(63,0,'files/e306a0840b08ca7036b20582047cc76d',1496394512),(64,0,'files/c951a56970345a6ef9485b44b958d96a',1496394512),(65,0,'files/62106b3c9c93cb6201616390d72d6c18',1496394512),(66,0,'files/82a20bc40b5fc30df7efb956922f1648',1496394512),(67,0,'files/f197c1ba0d1ed14fa06259e3f3b9df77',1496394512),(68,0,'files/f69ef922556068be6b410fdad929dbf3',1496394512),(69,0,'files/05ca4d2ebc744e27d3816f5927324151',1496394512),(70,0,'files/f67a7df60b2d85da0266c12e68d9a19a',1496394513),(71,0,'files/ef517730a5903a1bee1176c2a3da0895',1496394512),(72,0,'files/1800b28555989540fccde957c847c98a',1496394512),(73,0,'files/25bb2e3f7514cb4a3ebcc08d17a55126',1496394512),(74,0,'files/ae5fa984d8d64b5bf0cacdab2950c08b',1496394512),(75,0,'files/1a5e469fc6e0f5606d5214ae00f09e4b',1496394512),(76,0,'files/2843a76602870b9a4e266475f28cc642',1496394512),(77,0,'files/3f490dc517d57c993030a7639720521e',1496394512),(78,0,'files/dbdfbd901dcc1fe63971eb6f304c1ffb',1496394513),(79,0,'files/74166daef647b6b8b80bb306691fccb1',1496394513),(80,0,'files/8f0e42cf56103e5e80189204f0a2b460',1496394513),(81,0,'files/f0be4a8c870b2e824d438b64f7fe7df4',1496394513),(82,0,'files/3b04d49a64e66acda07cc7a9583037ec',1496394513),(83,0,'files/38e62f2e3865347d49a52c722cec2113',1496394513),(84,0,'files/752ed0a3b64d9c2923e7ef72371ce73d',1496394513),(85,0,'files/30166d371d466f9bc17add43c64e0aca',1496394513),(86,0,'files/ece111b8a9bceb8bb4327ee753dbc361',1496394513),(87,0,'files/aeff46c35b374d652d0d7205aaf9548d',1496394513),(88,0,'files/1e0e072649d14f260ca358bcfc3aab19',1496394513),(89,0,'files/a0f74505864a1dff810245c941c5557f',1496394513),(90,0,'files/5c7f1675da37cffa2909ddfc424b34df',1496394513),(91,0,'files/1a3c3f93ca79c2ca62845777b136b4fe',1496394513),(92,0,'files/7e16c874e7a0c6e69cff1eabe72fa3ab',1496394513),(93,0,'files/1be7b422738e14fd7fd3ace6625949bb',1496394513),(94,0,'files/f77be4599c82c8f9c4a6a222705284a9',1496394514),(95,0,'files/488f4074bf8bbafabcfe2531b2de081e',1496394514),(96,0,'files/66e37553fbc23e3cc06ca221df58e0d8',1496394514),(97,0,'files/a38da859388da630b26a778cbff57e43',1496394514),(98,0,'files/117734283db6fc2b7df28542840a143d',1496394514),(99,0,'files/d7639b8862753bb00bd95fcc197824ae',1496394514),(100,0,'files/1fcc22f4f3267fa7b0966502e1aa4a92',1496394514),(101,0,'files/cc99197747809d8c08b915a44eacff31',1496394514),(102,0,'files/e0bd635c6d81d13841803ca8d11167a0',1496394514),(103,0,'files/b6e959f26bf3ca22766f78c502f6bd4c',1496394514),(104,0,'files/e16340ed9987aea87345df3a5c1693cc',1496394514),(105,0,'files/109864a8212cee033995f5ed54955d98',1496394514),(106,0,'files/219681c0c1f76776bca5080643ef5bbc',1496394514),(107,0,'files/9714630514ffd94bf0173dac5216fc01',1496394514);
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
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_filecache`
--

LOCK TABLES `oc_filecache` WRITE;
/*!40000 ALTER TABLE `oc_filecache` DISABLE KEYS */;
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,7074735,1496390439,1496390439,0,0,'59311b27c66ac',23,''),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,7074735,1485536382,1485536382,0,0,'588b7c7e1c615',31,''),(3,1,'files/Nextcloud.mp4','77a79c09b93e57cba23c11eb0e6048a6',2,'Nextcloud.mp4',4,3,462413,1485536381,1485536381,0,0,'2e0c6f035652f7ec29d5958b4d90fde1',27,''),(4,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1496390901,1496390440,0,0,'59311cf5b1750',23,''),(5,3,'appdata_ocll5awmjb7q','e7a8a61323a5dca2ede2cbe9c5cb7bbc',4,'appdata_ocll5awmjb7q',2,1,183135,1485596908,1485536412,0,0,'588c68ecc2bdf',31,''),(6,3,'appdata_ocll5awmjb7q/preview','2cea38b94d1285578586b5cc14b5a347',5,'preview',2,1,0,1485536381,1485536381,0,0,'588b7c7dcac41',31,''),(7,1,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',2,'Photos',2,1,2360011,1485536381,1485536381,0,0,'588b7c7df1166',31,''),(8,1,'files/Photos/Nut.jpg','aa8daeb975e1d39412954fd5cd41adb4',7,'Nut.jpg',6,5,955026,1485536381,1485536381,0,0,'1ed8bdc1f6c252ec7919cd0f3cd9a2f6',27,''),(9,1,'files/Photos/Hummingbird.jpg','e077463269c404ae0f6f8ea7f2d7a326',7,'Hummingbird.jpg',6,5,585219,1485536381,1485536381,0,0,'7d97a07608c81805c42b0a073b7c870e',27,''),(10,1,'files/Photos/Coast.jpg','a6fe87299d78b207e9b7aba0f0cb8a0a',7,'Coast.jpg',6,5,819766,1485536382,1485536382,0,0,'96570532ff5c2c31c2a19894f2100869',27,''),(11,1,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',2,'Documents',2,1,78496,1485536382,1485536382,0,0,'588b7c7e14bf5',31,''),(12,1,'files/Documents/About.txt','9da7b739e7a65d74793b2881da521169',11,'About.txt',8,7,1074,1485536382,1485536382,0,0,'81f0f098ceab77b31b34ae011daa7edb',27,''),(13,1,'files/Documents/About.odt','b2ee7d56df9f34a0195d4b611376e885',11,'About.odt',10,9,77422,1485536382,1485536382,0,0,'483a2ec102c031cc5ee0f1cbca1fc9f0',27,''),(14,1,'files/Nextcloud Manual.pdf','2bc58a43566a8edde804a4a97a9c7469',2,'Nextcloud Manual.pdf',11,9,4173815,1485536382,1485536382,0,0,'77f87781841d789a7de2e7fceeaba571',27,''),(15,3,'appdata_ocll5awmjb7q/avatar','3ba2a1f8dae2d92bb188e5f04d81f384',5,'avatar',2,1,0,1485536384,1485536384,0,0,'588b7c809c846',31,''),(16,3,'appdata_ocll5awmjb7q/avatar/admin','f814e8679325f67adbe104542afb0d51',15,'admin',2,1,0,1485536384,1485536384,0,0,'588b7c809aa0f',31,''),(17,3,'appdata_ocll5awmjb7q/theming','3e18ef4914086f27159792884373e207',5,'theming',2,1,2117,1485536388,1485536388,0,0,'588b7c84a926b',31,''),(18,3,'appdata_ocll5awmjb7q/theming/0','344e998ce0e8878359748028a1db4ae6',17,'0',2,1,2117,1485536388,1485536388,0,0,'588b7c84a926b',31,''),(19,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_folder.svg','34598e545dd2228f6b91a229c698d807',18,'icon-core-filetypes_folder.svg',12,5,254,1485536388,1485536388,0,0,'5367e1366ec8cacaca54a3b2c4e82c55',27,''),(20,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_video.svg','98d9e39165989a3d076a962b447c8bb7',18,'icon-core-filetypes_video.svg',12,5,328,1485536388,1485536388,0,0,'d6952fced18acbb9df9d2e4325a6259b',27,''),(21,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_application-pdf.svg','ab4efc1fac68882bbceadde19af542df',18,'icon-core-filetypes_application-pdf.svg',12,5,1535,1485536388,1485536388,0,0,'e872d2b15ec22c71eb95bdc1b0cb963d',27,''),(22,3,'files_external','c270928b685e7946199afdfb898d27ea',4,'files_external',2,1,0,1496390436,1496390436,0,0,'59311b24db8b3',31,''),(23,3,'appdata_ocll5awmjb7q/appstore','a50221ec28c7669b947e8a7c718800f8',5,'appstore',2,1,181018,1485596908,1485536413,0,0,'588c68ecc2bdf',31,''),(24,3,'appdata_ocll5awmjb7q/appstore/apps.json','0ddc045c916e17c7cae94638e0fd98fb',23,'apps.json',13,9,156803,1485596908,1485596908,0,0,'3e763404747f8de72d4f1a6c0032a892',27,''),(25,3,'appdata_ocll5awmjb7q/appstore/categories.json','b213cc26ba8b8058df581e5d83c5b6ec',23,'categories.json',13,9,24215,1485596908,1485596908,0,0,'d83b19a6557c0bfb0838cf9c68965183',27,''),(26,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1496390439,1496390439,0,0,'59311b27c1d27',31,''),(27,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db','a0be0f52884cdbc5d4905a279cf0ff4a',4,'appdata_db157d6de6f0ffcf48907c1c0c1a97db',2,1,224607,1496390901,1496390884,0,0,'59311cf5b1750',31,''),(28,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar','b35d212ca547cb790eddce4b94650624',27,'avatar',2,1,0,1496390450,1496390450,0,0,'59311b32b716e',31,''),(29,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/admin','3b65858cd882eca60532f4eaa01fd24f',28,'admin',2,1,0,1496390440,1496390440,0,0,'59311b28c0cd5',31,''),(30,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/sysadmin','2343d734a4697e4a898f20c783ae9fa0',28,'sysadmin',2,1,0,1496390448,1496390448,0,0,'59311b3057bf2',31,''),(31,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest10','faafab522b99f6e21d5d74028e379ed8',28,'guest10',2,1,0,1496390448,1496390448,0,0,'59311b309790d',31,''),(32,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/theming','c3350a63a5553262210f0f176b903385',27,'theming',2,1,2602,1496390901,1496390449,0,0,'59311cf5b1750',31,''),(33,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/theming/0','adf08154b4391e51a98698873f59e716',32,'0',2,1,2602,1496390901,1496390901,0,0,'59311cf5b1750',31,''),(34,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/theming/0/icon-core-filetypes_folder.svg','bd73c549324cb04a8b52424c5cd45854',33,'icon-core-filetypes_folder.svg',12,5,254,1496390449,1496390449,0,0,'04e242ff84084e209423d65a7f8ea55c',27,''),(35,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/theming/0/icon-core-filetypes_application-pdf.svg','32258f68b4e1b93e4539a70c420db947',33,'icon-core-filetypes_application-pdf.svg',12,5,1535,1496390449,1496390449,0,0,'b6f78a7e6b9dc241169129c9d56dc24d',27,''),(36,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest1','d2054290c1ef4583d505c377e9ae2ff1',28,'guest1',2,1,0,1496390449,1496390449,0,0,'59311b317566f',31,''),(37,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/theming/0/icon-core-filetypes_video.svg','b868380fd3872f4a90afa6413e23a8e5',33,'icon-core-filetypes_video.svg',12,5,328,1496390449,1496390449,0,0,'2fc18c9436b05c09d518a6864414ba74',27,''),(38,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/preview','6e90dd4f25fbea0b1beac3a80e9a416d',27,'preview',2,1,0,1496390449,1496390449,0,0,'59311b31af63a',31,''),(39,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest2','28b30f9e7172afe602177c937f5c71f0',28,'guest2',2,1,0,1496390449,1496390449,0,0,'59311b31cd901',31,''),(40,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest3','eb00f528be2f279cb2c191f5825908a8',28,'guest3',2,1,0,1496390449,1496390449,0,0,'59311b31ef222',31,''),(41,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest4','6b05fb367f299ceb5c127e34c8f33169',28,'guest4',2,1,0,1496390450,1496390450,0,0,'59311b320576e',31,''),(42,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest5','2f8d0347d591878d29d3b3f41ab058f2',28,'guest5',2,1,0,1496390450,1496390450,0,0,'59311b3210d74',31,''),(43,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest6','e17494844505656b9936c94f2a4efa3b',28,'guest6',2,1,0,1496390450,1496390450,0,0,'59311b321b022',31,''),(44,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest7','f971fe5a7347f61866907a86ca035a1a',28,'guest7',2,1,0,1496390450,1496390450,0,0,'59311b322491a',31,''),(45,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest8','2c2d5bdeb81c6cf7a6b9b2c4f9346b76',28,'guest8',2,1,0,1496390450,1496390450,0,0,'59311b322d221',31,''),(46,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/guest9','30874283ea5e21ca0a605f57d44088f5',28,'guest9',2,1,0,1496390450,1496390450,0,0,'59311b32353d8',31,''),(47,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/ismith','5e39c310a8e06f75967f987b7aa13140',28,'ismith',2,1,0,1496390450,1496390450,0,0,'59311b323da20',31,''),(48,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/tech1','c6f6f18a333552c3276aafab02ca594b',28,'tech1',2,1,0,1496390450,1496390450,0,0,'59311b32464f7',31,''),(49,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/tech2','cdc72f0a27040e5d20797784bfec7e5f',28,'tech2',2,1,0,1496390450,1496390450,0,0,'59311b3251f16',31,''),(50,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/tech3','aa01588d7e89c6d998f963ba8d434a25',28,'tech3',2,1,0,1496390450,1496390450,0,0,'59311b325c215',31,''),(51,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/tech4','4b95ad99b5214ecaa24227ded20e4050',28,'tech4',2,1,0,1496390450,1496390450,0,0,'59311b32784db',31,''),(52,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/exam1','7f44ec34bdebbdd57c7ab3e3348a2c13',28,'exam1',2,1,0,1496390450,1496390450,0,0,'59311b32871cd',31,''),(53,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/exam2','fec17497491b473f1837349fdfd50fa8',28,'exam2',2,1,0,1496390450,1496390450,0,0,'59311b3293641',31,''),(54,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/exam3','395b3bfa561d7ac29a4229d5b9e7b774',28,'exam3',2,1,0,1496390450,1496390450,0,0,'59311b329aa0d',31,''),(55,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/exam4','92e95366097e279eb0a07276edd0baa2',28,'exam4',2,1,0,1496390450,1496390450,0,0,'59311b32a27a5',31,''),(56,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/exam5','d52db9a0b7c0c7e9fb4bb0b318cc09a7',28,'exam5',2,1,0,1496390450,1496390450,0,0,'59311b32a9ddf',31,''),(57,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/avatar/profileuser','2508c0d4b5323c0ccfbfb1504cb7b0ac',28,'profileuser',2,1,0,1496390450,1496390450,0,0,'59311b32b4ff3',31,''),(58,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/appstore','a16c550d0d1ba3f8d4b014dd717bc097',27,'appstore',2,1,222005,1496390884,1496390884,0,0,'59311ce4d360d',31,''),(59,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/appstore/apps.json','0042184075d18d80853a793930a4becf',58,'apps.json',13,9,222005,1496390884,1496390884,0,0,'6eca339237728fea8add4c837ac6ccfa',27,''),(60,3,'appdata_db157d6de6f0ffcf48907c1c0c1a97db/theming/0/icon-core-filetypes_folder-external.svg','28ac1ca8d812a11c143734100111d50d',33,'icon-core-filetypes_folder-external.svg',12,5,485,1496390901,1496390901,0,0,'aa5e46b74a7f2d761dfeeee17cb0be90',27,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_jobs`
--

LOCK TABLES `oc_jobs` WRITE;
/*!40000 ALTER TABLE `oc_jobs` DISABLE KEYS */;
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Federation\\SyncJob','null',1485536386,1485536386,0),(2,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1485536399,1485536399,0),(4,'OCA\\UpdateNotification\\Notification\\BackgroundJob','null',1485536497,1485536497,0),(5,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1485536500,1485536500,0),(6,'OCA\\Files_Sharing\\DeleteOrphanedSharesJob','null',1485596907,1485596907,0),(7,'OCA\\Files_Sharing\\ExpireSharesJob','null',1485597009,1485597009,0),(8,'OCA\\NextcloudAnnouncements\\Cron\\Crawler','null',1496390436,1496390436,0),(9,'OCA\\DAV\\CardDAV\\SyncJob','null',1496390443,1496390443,0),(10,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1496390619,1496390619,0),(11,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1496390900,1496390900,0),(12,'OCA\\Files\\BackgroundJob\\ScanFiles','null',1496390908,1496390908,0),(13,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',1496390920,1496390920,0),(14,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',0,1485536381,0),(15,'\\OC\\Authentication\\Token\\DefaultTokenCleanupJob','null',0,1485536381,0),(16,'OCA\\FirstRunWizard\\Notification\\BackgroundJob','{\"uid\":\"admin\"}',0,1485536384,0),(17,'OCA\\User_LDAP\\Jobs\\UpdateGroups','null',0,1485536435,0),(18,'OCA\\User_LDAP\\Jobs\\CleanUp','null',0,1485536435,0),(19,'OCA\\UpdateNotification\\ResetTokenBackgroundJob','null',0,1496390642,0),(20,'OCA\\User_LDAP\\Migration\\UUIDFixUser','{\"records\":[{\"dn\":\"cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam1\",\"uuid\":\"D19A952F-1B9A-49C9-9798-719B663DCAE8\"},{\"dn\":\"cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam2\",\"uuid\":\"17265C57-7AA9-44D3-8B1A-D6269C0028BC\"},{\"dn\":\"cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam3\",\"uuid\":\"24C6F83F-FA94-4F77-A4A6-51E6C86E5031\"},{\"dn\":\"cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam4\",\"uuid\":\"3538E98E-45B9-4C8D-8BA1-BA096F3B3EB9\"},{\"dn\":\"cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam5\",\"uuid\":\"A2502A78-9D8E-40B5-BC61-40C568CA7F71\"},{\"dn\":\"cn=guest1,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest1\",\"uuid\":\"E5A0A065-0CF3-40D4-9393-B4D257E19CCD\"},{\"dn\":\"cn=guest10,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest10\",\"uuid\":\"DB61F09E-79A4-480C-A33F-9CAF4A120604\"},{\"dn\":\"cn=guest2,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest2\",\"uuid\":\"5A7E4981-B52A-4EDB-AE14-156059F71E75\"},{\"dn\":\"cn=guest3,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest3\",\"uuid\":\"AA6DFD53-71D7-4B74-8D60-532F44013399\"},{\"dn\":\"cn=guest4,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest4\",\"uuid\":\"640ACB45-AF1B-42F8-914F-0549C981E36C\"},{\"dn\":\"cn=guest5,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest5\",\"uuid\":\"016FC041-77B7-436F-8A28-A27B2206A6CF\"},{\"dn\":\"cn=guest6,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest6\",\"uuid\":\"20F1D6F6-8C88-4A3C-88B0-276AFAD0A489\"},{\"dn\":\"cn=guest7,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest7\",\"uuid\":\"D53CB83C-695F-45FF-941F-2ED22DAD2A1F\"},{\"dn\":\"cn=guest8,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest8\",\"uuid\":\"D9BBB150-6574-404C-BD4D-3B1964FDC071\"},{\"dn\":\"cn=guest9,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest9\",\"uuid\":\"9FD5AE74-F77D-40D4-82E7-CAA820E96E5C\"},{\"dn\":\"cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"ismith\",\"uuid\":\"3290EBBE-396C-4D9E-A5A5-29F5B56F4108\"},{\"dn\":\"cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"profileuser\",\"uuid\":\"DDEA5A08-AC3C-4942-8B8F-EAB332FDD73A\"},{\"dn\":\"cn=sysadmin,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"sysadmin\",\"uuid\":\"0755B088-B796-465F-BF0C-E2AF70219089\"},{\"dn\":\"cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech1\",\"uuid\":\"3180491D-2DB0-4783-A8F6-A2C28D2F313B\"},{\"dn\":\"cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech2\",\"uuid\":\"BB1CAF7F-763A-445A-A167-1E8D03704999\"},{\"dn\":\"cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech3\",\"uuid\":\"BF5F1165-BA86-4559-A8FD-947EE90A5A25\"},{\"dn\":\"cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech4\",\"uuid\":\"550AD814-1279-4635-AB4A-86D4C547F2A3\"}]}',0,1496390884,0),(21,'OC\\Settings\\RemoveOrphaned','null',0,1496390884,0),(22,'OC\\Repair\\NC11\\MoveAvatarsBackgroundJob','null',0,1496390888,0),(23,'OC\\Repair\\NC11\\CleanPreviewsBackgroundJob','{\"uid\":\"admin\"}',0,1496390888,0);
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
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=exams,ou=groups,ou=people,CHANGETHISLDAPBASE','exams','11C5C858-2019-410F-A4D7-E0779AAE4C91'),('cn=guestusers,ou=groups,ou=people,CHANGETHISLDAPBASE','guestusers','5CE251D0-F5C9-4282-A849-E53FD8F9B112'),('cn=itadmin,ou=groups,ou=people,CHANGETHISLDAPBASE','itadmin','A9407EBE-A4B2-42EC-A1AB-8027848F152F'),('cn=profilemanagement,ou=groups,ou=people,CHANGETHISLDAPBASE','profilemanagement','F9127271-108A-4025-91E7-AAF4DE141ACA'),('cn=staff,ou=groups,ou=people,CHANGETHISLDAPBASE','staff','B0AF5A3F-1DC8-4DA6-85DC-C53E6234334E'),('cn=tech,ou=groups,ou=people,CHANGETHISLDAPBASE','tech','91C2CFCE-FAAB-4AB2-A79F-C7D2FDE44C44');
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
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam1','D19A952F-1B9A-49C9-9798-719B663DCAE8'),('cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam2','17265C57-7AA9-44D3-8B1A-D6269C0028BC'),('cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam3','24C6F83F-FA94-4F77-A4A6-51E6C86E5031'),('cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam4','3538E98E-45B9-4C8D-8BA1-BA096F3B3EB9'),('cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam5','A2502A78-9D8E-40B5-BC61-40C568CA7F71'),('cn=guest1,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest1','E5A0A065-0CF3-40D4-9393-B4D257E19CCD'),('cn=guest10,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest10','DB61F09E-79A4-480C-A33F-9CAF4A120604'),('cn=guest2,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest2','5A7E4981-B52A-4EDB-AE14-156059F71E75'),('cn=guest3,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest3','AA6DFD53-71D7-4B74-8D60-532F44013399'),('cn=guest4,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest4','640ACB45-AF1B-42F8-914F-0549C981E36C'),('cn=guest5,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest5','016FC041-77B7-436F-8A28-A27B2206A6CF'),('cn=guest6,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest6','20F1D6F6-8C88-4A3C-88B0-276AFAD0A489'),('cn=guest7,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest7','D53CB83C-695F-45FF-941F-2ED22DAD2A1F'),('cn=guest8,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest8','D9BBB150-6574-404C-BD4D-3B1964FDC071'),('cn=guest9,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest9','9FD5AE74-F77D-40D4-82E7-CAA820E96E5C'),('cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','ismith','3290EBBE-396C-4D9E-A5A5-29F5B56F4108'),('cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE','profileuser','DDEA5A08-AC3C-4942-8B8F-EAB332FDD73A'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE','sysadmin','0755B088-B796-465F-BF0C-E2AF70219089'),('cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech1','3180491D-2DB0-4783-A8F6-A2C28D2F313B'),('cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech2','BB1CAF7F-763A-445A-A167-1E8D03704999'),('cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech3','BF5F1165-BA86-4559-A8FD-947EE90A5A25'),('cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech4','550AD814-1279-4635-AB4A-86D4C547F2A3');
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
INSERT INTO `oc_preferences` VALUES ('admin','core','lang','en'),('admin','core','timezone','Europe/London'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1496390439'),('exam1','files_external','config_version','0.5.0'),('exam1','user_ldap','displayName','Exam 1'),('exam1','user_ldap','homePath',''),('exam1','user_ldap','lastFeatureRefresh','1496390909'),('exam1','user_ldap','uid','exam1'),('exam2','files_external','config_version','0.5.0'),('exam2','user_ldap','displayName','Exam 2'),('exam2','user_ldap','homePath',''),('exam2','user_ldap','lastFeatureRefresh','1496390909'),('exam2','user_ldap','uid','exam2'),('exam3','files_external','config_version','0.5.0'),('exam3','user_ldap','displayName','Exam 3'),('exam3','user_ldap','homePath',''),('exam3','user_ldap','lastFeatureRefresh','1496390909'),('exam3','user_ldap','uid','exam3'),('exam4','files_external','config_version','0.5.0'),('exam4','user_ldap','displayName','Exam 4'),('exam4','user_ldap','homePath',''),('exam4','user_ldap','lastFeatureRefresh','1496390909'),('exam4','user_ldap','uid','exam4'),('exam5','files_external','config_version','0.5.0'),('exam5','user_ldap','displayName','Exam 5'),('exam5','user_ldap','homePath',''),('exam5','user_ldap','lastFeatureRefresh','1496390909'),('exam5','user_ldap','uid','exam5'),('guest1','files_external','config_version','0.5.0'),('guest1','user_ldap','displayName','Guest 1'),('guest1','user_ldap','homePath',''),('guest1','user_ldap','lastFeatureRefresh','1496390909'),('guest1','user_ldap','uid','guest1'),('guest10','files_external','config_version','0.5.0'),('guest10','user_ldap','displayName','Guest 10'),('guest10','user_ldap','homePath',''),('guest10','user_ldap','lastFeatureRefresh','1496390909'),('guest10','user_ldap','uid','guest10'),('guest2','files_external','config_version','0.5.0'),('guest2','user_ldap','displayName','Guest 2'),('guest2','user_ldap','homePath',''),('guest2','user_ldap','lastFeatureRefresh','1496390909'),('guest2','user_ldap','uid','guest2'),('guest3','files_external','config_version','0.5.0'),('guest3','user_ldap','displayName','Guest 3'),('guest3','user_ldap','homePath',''),('guest3','user_ldap','lastFeatureRefresh','1496390909'),('guest3','user_ldap','uid','guest3'),('guest4','files_external','config_version','0.5.0'),('guest4','user_ldap','displayName','Guest 4'),('guest4','user_ldap','homePath',''),('guest4','user_ldap','lastFeatureRefresh','1496390909'),('guest4','user_ldap','uid','guest4'),('guest5','files_external','config_version','0.5.0'),('guest5','user_ldap','displayName','Guest 5'),('guest5','user_ldap','homePath',''),('guest5','user_ldap','lastFeatureRefresh','1496390909'),('guest5','user_ldap','uid','guest5'),('guest6','files_external','config_version','0.5.0'),('guest6','user_ldap','displayName','Guest 6'),('guest6','user_ldap','homePath',''),('guest6','user_ldap','lastFeatureRefresh','1496390909'),('guest6','user_ldap','uid','guest6'),('guest7','files_external','config_version','0.5.0'),('guest7','user_ldap','displayName','Guest 7'),('guest7','user_ldap','homePath',''),('guest7','user_ldap','lastFeatureRefresh','1496390909'),('guest7','user_ldap','uid','guest7'),('guest8','files_external','config_version','0.5.0'),('guest8','user_ldap','displayName','Guest 8'),('guest8','user_ldap','homePath',''),('guest8','user_ldap','lastFeatureRefresh','1496390909'),('guest8','user_ldap','uid','guest8'),('guest9','files_external','config_version','0.5.0'),('guest9','user_ldap','displayName','Guest 9'),('guest9','user_ldap','homePath',''),('guest9','user_ldap','lastFeatureRefresh','1496390909'),('guest9','user_ldap','uid','guest9'),('ismith','files_external','config_version','0.5.0'),('ismith','user_ldap','displayName','Ian Smith'),('ismith','user_ldap','homePath',''),('ismith','user_ldap','lastFeatureRefresh','1496390909'),('ismith','user_ldap','uid','ismith'),('profileuser','files_external','config_version','0.5.0'),('profileuser','user_ldap','displayName','Profile User'),('profileuser','user_ldap','homePath',''),('profileuser','user_ldap','lastFeatureRefresh','1496390909'),('profileuser','user_ldap','uid','profileuser'),('sysadmin','files_external','config_version','0.5.0'),('sysadmin','user_ldap','displayName','Sysadmin User'),('sysadmin','user_ldap','homePath',''),('sysadmin','user_ldap','lastFeatureRefresh','1496390909'),('sysadmin','user_ldap','uid','sysadmin'),('tech1','files_external','config_version','0.5.0'),('tech1','user_ldap','displayName','Tech 1'),('tech1','user_ldap','homePath',''),('tech1','user_ldap','lastFeatureRefresh','1496390909'),('tech1','user_ldap','uid','tech1'),('tech2','files_external','config_version','0.5.0'),('tech2','user_ldap','displayName','Tech 2'),('tech2','user_ldap','homePath',''),('tech2','user_ldap','lastFeatureRefresh','1496390909'),('tech2','user_ldap','uid','tech2'),('tech3','files_external','config_version','0.5.0'),('tech3','user_ldap','displayName','Tech 3'),('tech3','user_ldap','homePath',''),('tech3','user_ldap','lastFeatureRefresh','1496390909'),('tech3','user_ldap','uid','tech3'),('tech4','files_external','config_version','0.5.0'),('tech4','user_ldap','displayName','Tech 4'),('tech4','user_ldap','homePath',''),('tech4','user_ldap','lastFeatureRefresh','1496390909'),('tech4','user_ldap','uid','tech4');
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
-- Table structure for table `oc_reader_bookmarks`
--

DROP TABLE IF EXISTS `oc_reader_bookmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oc_reader_bookmarks` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `file_id` bigint(20) unsigned NOT NULL,
  `type` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `name` varchar(512) COLLATE utf8_bin NOT NULL DEFAULT '',
  `value` varchar(512) COLLATE utf8_bin NOT NULL DEFAULT '',
  `content` varchar(4096) COLLATE utf8_bin DEFAULT NULL,
  `last_modified` bigint(20) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `reader_bookmarks_file_id_index` (`file_id`),
  KEY `reader_bookmarks_user_id_index` (`user_id`),
  KEY `reader_bookmarks_name_index` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `file_id` bigint(20) unsigned NOT NULL,
  `scope` varchar(32) COLLATE utf8_bin NOT NULL DEFAULT '',
  `name` varchar(128) COLLATE utf8_bin NOT NULL DEFAULT '',
  `value` varchar(4096) COLLATE utf8_bin NOT NULL DEFAULT '',
  `last_modified` bigint(20) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `reader_preferences_file_id_index` (`file_id`),
  KEY `reader_preferences_user_id_index` (`user_id`),
  KEY `reader_preferences_scope_index` (`scope`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_storages`
--

LOCK TABLES `oc_storages` WRITE;
/*!40000 ALTER TABLE `oc_storages` DISABLE KEYS */;
INSERT INTO `oc_storages` VALUES ('home::admin',1,1,NULL),('1',2,1,NULL),('local::/home/nextcloud/data/',3,1,NULL),('smb::admin@blackmesa.com//dfs/homes/admin//',4,0,1496390902),('smb::admin@blackmesa.com//dfs/subjects//',5,0,1496390902),('failedstorage',6,1,NULL),('smb::admin@blackmesa.com//dfs/homes/exam1//',7,1,NULL),('home::exam1',8,1,NULL),('smb::admin@blackmesa.com//dfs/homes/exam2//',9,1,NULL),('home::exam2',10,1,NULL),('smb::admin@blackmesa.com//dfs/homes/exam3//',11,1,NULL),('home::exam3',12,1,NULL),('smb::admin@blackmesa.com//dfs/homes/exam4//',13,1,NULL),('home::exam4',14,1,NULL),('smb::admin@blackmesa.com//dfs/homes/exam5//',15,1,NULL),('home::exam5',16,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest1//',17,1,NULL),('home::guest1',18,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest10//',19,1,NULL),('home::guest10',20,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest2//',21,1,NULL),('home::guest2',22,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest3//',23,1,NULL),('home::guest3',24,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest4//',25,1,NULL),('home::guest4',26,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest5//',27,1,NULL),('home::guest5',28,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest6//',29,1,NULL),('home::guest6',30,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest7//',31,1,NULL),('home::guest7',32,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest8//',33,1,NULL),('home::guest8',34,1,NULL),('smb::admin@blackmesa.com//dfs/homes/guest9//',35,1,NULL),('home::guest9',36,1,NULL),('smb::admin@blackmesa.com//dfs/homes/ismith//',37,1,NULL),('smb::admin@blackmesa.com//dfs/staffshare//',38,1,NULL),('home::ismith',39,1,NULL),('smb::admin@blackmesa.com//dfs/homes/profileuser//',40,1,NULL),('home::profileuser',41,1,NULL),('smb::admin@blackmesa.com//dfs/homes/sysadmin//',42,1,NULL),('smb::admin@blackmesa.com//dfs/applications//',43,1,NULL),('smb::admin@blackmesa.com//dfs/itadminshare//',44,1,NULL),('smb::admin@blackmesa.com//dfs/netlogon//',45,1,NULL),('smb::admin@blackmesa.com//dfs/sysvol//',46,1,NULL),('home::sysadmin',47,1,NULL),('smb::admin@blackmesa.com//dfs/homes/tech1//',48,1,NULL),('home::tech1',49,1,NULL),('smb::admin@blackmesa.com//dfs/homes/tech2//',50,1,NULL),('home::tech2',51,1,NULL),('smb::admin@blackmesa.com//dfs/homes/tech3//',52,1,NULL),('home::tech3',53,1,NULL),('smb::admin@blackmesa.com//dfs/homes/tech4//',54,1,NULL),('home::tech4',55,1,NULL);
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

-- Dump completed on 2017-06-02  9:14:33
