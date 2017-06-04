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
INSERT INTO `oc_accounts` VALUES ('admin','{\"displayname\":{\"value\":\"admin\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam1','{\"displayname\":{\"value\":\"Exam 1\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam2','{\"displayname\":{\"value\":\"Exam 2\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam3','{\"displayname\":{\"value\":\"Exam 3\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam4','{\"displayname\":{\"value\":\"Exam 4\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('exam5','{\"displayname\":{\"value\":\"Exam 5\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest1','{\"displayname\":{\"value\":\"Guest 1\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest10','{\"displayname\":{\"value\":\"Guest 10\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest2','{\"displayname\":{\"value\":\"Guest 2\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest3','{\"displayname\":{\"value\":\"Guest 3\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest4','{\"displayname\":{\"value\":\"Guest 4\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest5','{\"displayname\":{\"value\":\"Guest 5\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest6','{\"displayname\":{\"value\":\"Guest 6\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest7','{\"displayname\":{\"value\":\"Guest 7\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest8','{\"displayname\":{\"value\":\"Guest 8\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('guest9','{\"displayname\":{\"value\":\"Guest 9\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('ismith','{\"displayname\":{\"value\":\"Ian Smith\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('jjones','{\"displayname\":{\"value\":\"John Jones\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('profileuser','{\"displayname\":{\"value\":\"Profile User\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('sysadmin','{\"displayname\":{\"value\":\"Sysadmin User\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech1','{\"displayname\":{\"value\":\"Tech 1\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech2','{\"displayname\":{\"value\":\"Tech 2\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech3','{\"displayname\":{\"value\":\"Tech 3\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}'),('tech4','{\"displayname\":{\"value\":\"Tech 4\",\"scope\":\"contacts\"},\"address\":{\"value\":\"\",\"scope\":\"private\"},\"website\":{\"value\":\"\",\"scope\":\"private\"},\"email\":{\"value\":null,\"scope\":\"contacts\"},\"avatar\":{\"scope\":\"contacts\"},\"phone\":{\"value\":\"\",\"scope\":\"private\"},\"twitter\":{\"value\":\"\",\"scope\":\"private\"}}');
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
INSERT INTO `oc_activity` VALUES (1,1485536381,30,'file_created','admin','admin','files','created_self','[{\"2\":\"\"}]','','[]','','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=','files',2),(2,1485536381,30,'file_created','admin','admin','files','created_self','[{\"3\":\"\\/Nextcloud.mp4\"}]','','[]','/Nextcloud.mp4','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/','files',3),(3,1485536381,30,'file_created','admin','admin','files','created_self','[{\"7\":\"\\/Photos\"}]','','[]','/Photos','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/','files',7),(4,1485536381,30,'file_created','admin','admin','files','created_self','[{\"8\":\"\\/Photos\\/Nut.jpg\"}]','','[]','/Photos/Nut.jpg','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/Photos','files',8),(5,1485536381,30,'file_created','admin','admin','files','created_self','[{\"9\":\"\\/Photos\\/Hummingbird.jpg\"}]','','[]','/Photos/Hummingbird.jpg','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/Photos','files',9),(6,1485536381,30,'file_created','admin','admin','files','created_self','[{\"10\":\"\\/Photos\\/Coast.jpg\"}]','','[]','/Photos/Coast.jpg','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/Photos','files',10),(7,1485536382,30,'file_created','admin','admin','files','created_self','[{\"11\":\"\\/Documents\"}]','','[]','/Documents','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/','files',11),(8,1485536382,30,'file_created','admin','admin','files','created_self','[{\"12\":\"\\/Documents\\/About.txt\"}]','','[]','/Documents/About.txt','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/Documents','files',12),(9,1485536382,30,'file_created','admin','admin','files','created_self','[{\"13\":\"\\/Documents\\/About.odt\"}]','','[]','/Documents/About.odt','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/Documents','files',13),(10,1485536382,30,'file_created','admin','admin','files','created_self','[{\"14\":\"\\/Nextcloud Manual.pdf\"}]','','[]','/Nextcloud Manual.pdf','https://CHANGETHISREALM/nextcloud/index.php/apps/files/?dir=/','files',14),(11,1485536382,30,'calendar','admin','admin','dav','calendar_add_self','[\"admin\",\"Personal\"]','','[]','','','calendar',1),(12,1496580921,30,'calendar','system','system','dav','calendar_add_self','[\"system\",\"Contact birthdays\"]','','[]','','','calendar',2);
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_addressbookchanges`
--

LOCK TABLES `oc_addressbookchanges` WRITE;
/*!40000 ALTER TABLE `oc_addressbookchanges` DISABLE KEYS */;
INSERT INTO `oc_addressbookchanges` VALUES (1,'Database:admin.vcf',1,2,1),(2,'LDAP:sysadmin.vcf',2,2,1),(3,'LDAP:guest10.vcf',3,2,1),(4,'LDAP:guest1.vcf',4,2,1),(5,'LDAP:guest2.vcf',5,2,1),(6,'LDAP:guest3.vcf',6,2,1),(7,'LDAP:guest4.vcf',7,2,1),(8,'LDAP:guest5.vcf',8,2,1),(9,'LDAP:guest6.vcf',9,2,1),(10,'LDAP:guest7.vcf',10,2,1),(11,'LDAP:guest8.vcf',11,2,1),(12,'LDAP:guest9.vcf',12,2,1),(13,'LDAP:ismith.vcf',13,2,1),(14,'LDAP:jjones.vcf',14,2,1),(15,'LDAP:tech1.vcf',15,2,1),(16,'LDAP:tech2.vcf',16,2,1),(17,'LDAP:tech3.vcf',17,2,1),(18,'LDAP:tech4.vcf',18,2,1),(19,'LDAP:exam1.vcf',19,2,1),(20,'LDAP:exam2.vcf',20,2,1),(21,'LDAP:exam3.vcf',21,2,1),(22,'LDAP:exam4.vcf',22,2,1),(23,'LDAP:exam5.vcf',23,2,1),(24,'LDAP:profileuser.vcf',24,2,1),(25,'Database:admin.vcf',25,2,3),(26,'LDAP:sysadmin.vcf',26,2,3),(27,'LDAP:guest10.vcf',27,2,3),(28,'LDAP:guest1.vcf',28,2,3),(29,'LDAP:guest2.vcf',29,2,3),(30,'LDAP:guest3.vcf',30,2,3),(31,'LDAP:guest4.vcf',31,2,3),(32,'LDAP:guest5.vcf',32,2,3),(33,'LDAP:guest6.vcf',33,2,3),(34,'LDAP:guest7.vcf',34,2,3),(35,'LDAP:guest8.vcf',35,2,3),(36,'LDAP:guest9.vcf',36,2,3),(37,'LDAP:ismith.vcf',37,2,3),(38,'LDAP:jjones.vcf',38,2,3),(39,'LDAP:tech1.vcf',39,2,3),(40,'LDAP:tech2.vcf',40,2,3),(41,'LDAP:tech3.vcf',41,2,3),(42,'LDAP:tech4.vcf',42,2,3),(43,'LDAP:exam1.vcf',43,2,3),(44,'LDAP:exam2.vcf',44,2,3),(45,'LDAP:exam3.vcf',45,2,3),(46,'LDAP:exam4.vcf',46,2,3),(47,'LDAP:exam5.vcf',47,2,3),(48,'LDAP:profileuser.vcf',48,2,3);
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
INSERT INTO `oc_addressbooks` VALUES (1,'principals/users/admin','Contacts','contacts',NULL,1),(2,'principals/system/system','system','system','System addressbook which holds all users of this instance',49);
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
INSERT INTO `oc_appconfig` VALUES ('activity','enabled','yes'),('activity','installed_version','2.4.1'),('activity','types','filesystem'),('backgroundjob','lastjob','13'),('comments','enabled','yes'),('comments','installed_version','1.1.0'),('comments','types','logging'),('core','installedat','1485536380.8184'),('core','lastcron','1496582017'),('core','lastupdateResult','[]'),('core','lastupdatedat','1496581983'),('core','moveavatarsdone','yes'),('core','oc.integritycheck.checker','[]'),('core','previewsCleanedUp','1'),('core','public_files','files_sharing/public.php'),('core','public_webdav','dav/appinfo/v1/publicwebdav.php'),('core','repairlegacystoragesdone','yes'),('core','updater.secret.created','1496581824'),('core','vendor','nextcloud'),('dav','enabled','yes'),('dav','installed_version','1.1.1'),('dav','types','filesystem'),('federatedfilesharing','enabled','yes'),('federatedfilesharing','installed_version','1.1.1'),('federatedfilesharing','types',''),('federation','enabled','yes'),('federation','installed_version','1.1.1'),('federation','types','authentication'),('files','cronjob_scan_files','500'),('files','enabled','yes'),('files','installed_version','1.6.1'),('files','types','filesystem'),('files_external','enabled','yes'),('files_external','installed_version','1.1.2'),('files_external','types','filesystem'),('files_pdfviewer','enabled','yes'),('files_pdfviewer','installed_version','1.0.1'),('files_pdfviewer','ocsid','166049'),('files_pdfviewer','types',''),('files_reader','enabled','no'),('files_reader','installed_version','1.0.4'),('files_reader','ocsid','167127'),('files_reader','types',''),('files_sharing','enabled','yes'),('files_sharing','installed_version','1.1.1'),('files_sharing','types','filesystem'),('files_texteditor','enabled','yes'),('files_texteditor','installed_version','2.2'),('files_texteditor','ocsid','166051'),('files_texteditor','types',''),('files_trashbin','enabled','yes'),('files_trashbin','installed_version','1.1.0'),('files_trashbin','types','filesystem'),('files_versions','enabled','yes'),('files_versions','installed_version','1.4.0'),('files_versions','types','filesystem'),('files_videoplayer','enabled','yes'),('files_videoplayer','installed_version','1.0.0'),('files_videoplayer','types',''),('firstrunwizard','enabled','yes'),('firstrunwizard','installed_version','2.0'),('firstrunwizard','types','logging'),('gallery','enabled','yes'),('gallery','installed_version','16.0.0'),('gallery','types',''),('logreader','enabled','yes'),('logreader','installed_version','2.0.0'),('logreader','ocsid','170871'),('logreader','types',''),('lookup_server_connector','enabled','yes'),('lookup_server_connector','installed_version','1.0.0'),('lookup_server_connector','types','authentication'),('nextcloud_announcements','enabled','yes'),('nextcloud_announcements','installed_version','1.0'),('nextcloud_announcements','pub_date','Sat, 10 Dec 2016 00:00:00 +0100'),('nextcloud_announcements','types','logging'),('notes','enabled','no'),('notes','installed_version','2.2.0'),('notes','types',''),('notifications','enabled','yes'),('notifications','installed_version','1.0.1'),('notifications','types','logging'),('password_policy','enabled','yes'),('password_policy','installed_version','1.1.0'),('password_policy','types',''),('provisioning_api','enabled','yes'),('provisioning_api','installed_version','1.1.0'),('provisioning_api','types','prevent_group_restriction'),('richdocuments','enabled','no'),('richdocuments','installed_version','1.11.31'),('richdocuments','types','prevent_group_restriction'),('richdocuments','wopi_url','https://newcloud.constellations.com'),('serverinfo','enabled','yes'),('serverinfo','installed_version','1.1.1'),('serverinfo','types',''),('sharebymail','enabled','yes'),('sharebymail','installed_version','1.0.1'),('sharebymail','types','filesystem'),('survey_client','enabled','yes'),('survey_client','installed_version','0.1.5'),('survey_client','types',''),('systemtags','enabled','yes'),('systemtags','installed_version','1.1.3'),('systemtags','types','logging'),('theming','enabled','yes'),('theming','installed_version','1.1.1'),('theming','types','logging'),('twofactor_backupcodes','enabled','yes'),('twofactor_backupcodes','installed_version','1.0.0'),('twofactor_backupcodes','types',''),('updatenotification','enabled','yes'),('updatenotification','installed_version','1.1.1'),('updatenotification','types',''),('user_ldap','enabled','yes'),('user_ldap','has_memberof_filter_support','1'),('user_ldap','home_folder_naming_rule',''),('user_ldap','installed_version','1.1.2'),('user_ldap','last_jpegPhoto_lookup','0'),('user_ldap','ldap_agent_password',''),('user_ldap','ldap_attributes_for_group_search',''),('user_ldap','ldap_attributes_for_user_search',''),('user_ldap','ldap_backup_host',''),('user_ldap','ldap_backup_port',''),('user_ldap','ldap_base','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_groups','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_base_users','OU=People,CHANGETHISLDAPBASE'),('user_ldap','ldap_cache_ttl','600'),('user_ldap','ldap_configuration_active','1'),('user_ldap','ldap_display_name','displayName'),('user_ldap','ldap_dn',''),('user_ldap','ldap_dynamic_group_member_url',''),('user_ldap','ldap_email_attr',''),('user_ldap','ldap_experienced_admin','0'),('user_ldap','ldap_expert_username_attr','sAMAccountName'),('user_ldap','ldap_expert_uuid_group_attr',''),('user_ldap','ldap_expert_uuid_user_attr',''),('user_ldap','ldap_group_display_name','cn'),('user_ldap','ldap_group_filter','(&(|(objectclass=posixGroup)))'),('user_ldap','ldap_group_filter_mode','0'),('user_ldap','ldap_group_member_assoc_attribute','uniqueMember'),('user_ldap','ldap_groupfilter_groups',''),('user_ldap','ldap_groupfilter_objectclass','posixGroup'),('user_ldap','ldap_host','127.0.0.1'),('user_ldap','ldap_login_filter','(&(&(|(objectclass=person)))(samaccountname=%uid))'),('user_ldap','ldap_login_filter_mode','0'),('user_ldap','ldap_loginfilter_attributes',''),('user_ldap','ldap_loginfilter_email','0'),('user_ldap','ldap_loginfilter_username','1'),('user_ldap','ldap_nested_groups','0'),('user_ldap','ldap_override_main_server',''),('user_ldap','ldap_paging_size','500'),('user_ldap','ldap_port','389'),('user_ldap','ldap_quota_attr',''),('user_ldap','ldap_quota_def',''),('user_ldap','ldap_tls','0'),('user_ldap','ldap_turn_off_cert_check','0'),('user_ldap','ldap_turn_on_pwd_change','0'),('user_ldap','ldap_user_display_name_2',''),('user_ldap','ldap_user_filter_mode','0'),('user_ldap','ldap_userfilter_groups',''),('user_ldap','ldap_userfilter_objectclass','posixAccount'),('user_ldap','ldap_userlist_filter','(&(|(objectclass=posixAccount)))'),('user_ldap','types','authentication'),('user_ldap','use_memberof_to_detect_membership','1'),('workflowengine','enabled','yes'),('workflowengine','installed_version','1.1.1'),('workflowengine','types','filesystem');
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
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_calendarchanges`
--

LOCK TABLES `oc_calendarchanges` WRITE;
/*!40000 ALTER TABLE `oc_calendarchanges` DISABLE KEYS */;
INSERT INTO `oc_calendarchanges` VALUES (1,'system-Database:admin.vcf.ics',1,2,3),(2,'system-Database:admin.vcf-death.ics',2,2,3),(3,'system-Database:admin.vcf-anniversary.ics',3,2,3),(4,'system-LDAP:sysadmin.vcf.ics',4,2,3),(5,'system-LDAP:sysadmin.vcf-death.ics',5,2,3),(6,'system-LDAP:sysadmin.vcf-anniversary.ics',6,2,3),(7,'system-LDAP:guest10.vcf.ics',7,2,3),(8,'system-LDAP:guest10.vcf-death.ics',8,2,3),(9,'system-LDAP:guest10.vcf-anniversary.ics',9,2,3),(10,'system-LDAP:guest1.vcf.ics',10,2,3),(11,'system-LDAP:guest1.vcf-death.ics',11,2,3),(12,'system-LDAP:guest1.vcf-anniversary.ics',12,2,3),(13,'system-LDAP:guest2.vcf.ics',13,2,3),(14,'system-LDAP:guest2.vcf-death.ics',14,2,3),(15,'system-LDAP:guest2.vcf-anniversary.ics',15,2,3),(16,'system-LDAP:guest3.vcf.ics',16,2,3),(17,'system-LDAP:guest3.vcf-death.ics',17,2,3),(18,'system-LDAP:guest3.vcf-anniversary.ics',18,2,3),(19,'system-LDAP:guest4.vcf.ics',19,2,3),(20,'system-LDAP:guest4.vcf-death.ics',20,2,3),(21,'system-LDAP:guest4.vcf-anniversary.ics',21,2,3),(22,'system-LDAP:guest5.vcf.ics',22,2,3),(23,'system-LDAP:guest5.vcf-death.ics',23,2,3),(24,'system-LDAP:guest5.vcf-anniversary.ics',24,2,3),(25,'system-LDAP:guest6.vcf.ics',25,2,3),(26,'system-LDAP:guest6.vcf-death.ics',26,2,3),(27,'system-LDAP:guest6.vcf-anniversary.ics',27,2,3),(28,'system-LDAP:guest7.vcf.ics',28,2,3),(29,'system-LDAP:guest7.vcf-death.ics',29,2,3),(30,'system-LDAP:guest7.vcf-anniversary.ics',30,2,3),(31,'system-LDAP:guest8.vcf.ics',31,2,3),(32,'system-LDAP:guest8.vcf-death.ics',32,2,3),(33,'system-LDAP:guest8.vcf-anniversary.ics',33,2,3),(34,'system-LDAP:guest9.vcf.ics',34,2,3),(35,'system-LDAP:guest9.vcf-death.ics',35,2,3),(36,'system-LDAP:guest9.vcf-anniversary.ics',36,2,3),(37,'system-LDAP:ismith.vcf.ics',37,2,3),(38,'system-LDAP:ismith.vcf-death.ics',38,2,3),(39,'system-LDAP:ismith.vcf-anniversary.ics',39,2,3),(40,'system-LDAP:jjones.vcf.ics',40,2,3),(41,'system-LDAP:jjones.vcf-death.ics',41,2,3),(42,'system-LDAP:jjones.vcf-anniversary.ics',42,2,3),(43,'system-LDAP:tech1.vcf.ics',43,2,3),(44,'system-LDAP:tech1.vcf-death.ics',44,2,3),(45,'system-LDAP:tech1.vcf-anniversary.ics',45,2,3),(46,'system-LDAP:tech2.vcf.ics',46,2,3),(47,'system-LDAP:tech2.vcf-death.ics',47,2,3),(48,'system-LDAP:tech2.vcf-anniversary.ics',48,2,3),(49,'system-LDAP:tech3.vcf.ics',49,2,3),(50,'system-LDAP:tech3.vcf-death.ics',50,2,3),(51,'system-LDAP:tech3.vcf-anniversary.ics',51,2,3),(52,'system-LDAP:tech4.vcf.ics',52,2,3),(53,'system-LDAP:tech4.vcf-death.ics',53,2,3),(54,'system-LDAP:tech4.vcf-anniversary.ics',54,2,3),(55,'system-LDAP:exam1.vcf.ics',55,2,3),(56,'system-LDAP:exam1.vcf-death.ics',56,2,3),(57,'system-LDAP:exam1.vcf-anniversary.ics',57,2,3),(58,'system-LDAP:exam2.vcf.ics',58,2,3),(59,'system-LDAP:exam2.vcf-death.ics',59,2,3),(60,'system-LDAP:exam2.vcf-anniversary.ics',60,2,3),(61,'system-LDAP:exam3.vcf.ics',61,2,3),(62,'system-LDAP:exam3.vcf-death.ics',62,2,3),(63,'system-LDAP:exam3.vcf-anniversary.ics',63,2,3),(64,'system-LDAP:exam4.vcf.ics',64,2,3),(65,'system-LDAP:exam4.vcf-death.ics',65,2,3),(66,'system-LDAP:exam4.vcf-anniversary.ics',66,2,3),(67,'system-LDAP:exam5.vcf.ics',67,2,3),(68,'system-LDAP:exam5.vcf-death.ics',68,2,3),(69,'system-LDAP:exam5.vcf-anniversary.ics',69,2,3),(70,'system-LDAP:profileuser.vcf.ics',70,2,3),(71,'system-LDAP:profileuser.vcf-death.ics',71,2,3),(72,'system-LDAP:profileuser.vcf-anniversary.ics',72,2,3);
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
INSERT INTO `oc_calendars` VALUES (1,'principals/users/admin','Personal','personal',1,NULL,0,NULL,NULL,'VEVENT,VTODO',0),(2,'principals/system/system','Contact birthdays','contact_birthdays',73,NULL,0,'#FFFFCA',NULL,'VEVENT,VTODO',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
INSERT INTO `oc_credentials` VALUES ('admin','password::logincredentials/credentials','5d322b259527eaafa73f0c58a643e49cf197b542251eedb01a558061bb315628cc1959f537f44525947c3f1b45080441|0dHZwyYF7SouQ1YL|7c58568381934b95f4a4e656e3b42aae4601762d858fc9d67b33a9b1141a72af36f1ce9a62ab60fbf12774b270f010e0f3ae5985582b3e8327c358501ca68536');
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
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oc_file_locks`
--

LOCK TABLES `oc_file_locks` WRITE;
/*!40000 ALTER TABLE `oc_file_locks` DISABLE KEYS */;
INSERT INTO `oc_file_locks` VALUES (1,0,'files/468c740695b998c9b920835b3af18225',1496585585),(2,0,'files/3ef927705e35f104f5c8825610e550db',1496585585),(3,0,'files/b6ef755cfc70b5eb94f5d3aad8ba833d',1496585585),(4,0,'files/bc76dde1a029b9698a1164dc9d6f4422',1496584507),(5,0,'files/19e2bab88baf1319b217efd58191b0f6',1496584517),(6,0,'files/b624b0b689f8b7987114baba780343a9',1496585585),(7,0,'files/4932f6750d1ab3d6d78cc1186c63684b',1496585585),(8,0,'files/d9d3c831b50d33efa33468cea5a71f87',1496585598),(9,0,'files/6df0a7b6a31d3edeafceb9e33fab7462',1496585598),(10,0,'files/38f1a462ac005ca53e80d2b991446fcc',1496585598),(11,0,'files/94d6e57f87a95ab97190ea200c471d58',1496585598),(12,0,'files/cfbd69ed0090cc1caf9dbe05fd8042d8',1496585598),(13,0,'files/ca4df8e6507667c4d92cc61d5087dea6',1496585598),(14,0,'files/76287b2f29364703dfd1d9b543a9b4ea',1496585598),(15,0,'files/6003c26f820e7dfb8cf1349b1eee4192',1496585598),(16,0,'files/2435b19aac73d728634114271a94692d',1496585599),(17,0,'files/6e8cf50c1e58f7a4b10888adcedb0b36',1496585599),(18,0,'files/169ecf9ce9d92154b2d8f3bb3ae0a844',1496585599),(19,0,'files/8d808264268ae2fe9bc1ba387ea3d422',1496585599),(20,0,'files/efa36becfb53dfc0a084fad7ebb763ca',1496585599),(21,0,'files/090c687ea032887bd3cf5159fbd056c3',1496585599),(22,0,'files/4462d021359874962ce01e459811fd2f',1496585599),(23,0,'files/3fc6c5255194229c8fe7207c019f799d',1496585599),(24,0,'files/6084875355c6496bfa3869067c30ecad',1496585599),(25,0,'files/15d2a20f46c7c6478e1b8c46a26f3ca5',1496585599),(26,0,'files/96de6c364514d73c48c4d1bb07cb500e',1496585599),(27,0,'files/f9b7ca3604813ca018716be621bb7909',1496585599),(28,0,'files/425771ea215a22884c97372156d65b74',1496585599),(29,0,'files/e41ae426cf9e334493d9afb4f152fe0c',1496585599),(30,0,'files/ee32bae6d3c598e340831969e79c6340',1496585599),(31,0,'files/3e0af14d5271af42865bdaa6a9b668ef',1496585599),(32,0,'files/8671085f83169f0aea2666d218187ac8',1496585599),(33,0,'files/17413e9f17505bee9526191609042e85',1496585599),(34,0,'files/11c6efefe7042583d9bc33a4020aeb62',1496585600),(35,0,'files/6868cf08f134e4ecd9c67e38641df516',1496585600),(36,0,'files/53bdcb48596b35a4b3c4b46049293841',1496585600),(37,0,'files/d2e62dd5312a143f14c48e4079259435',1496585600),(38,0,'files/2b472e2132c1f0e68c63cc5652e1ecff',1496585600),(39,0,'files/7107b3afb9d25db8c4c2c58e71e8c0ac',1496585600),(40,0,'files/d111446f5e9fbcc2b884c7750ee38333',1496585600),(41,0,'files/644e3737ba82d44a82e48bfdeead565b',1496585600),(42,0,'files/b2e4494a9b232ace38f0844901b5b4ba',1496585600),(43,0,'files/228a47e1c54e7c56e1df5be52615f554',1496585600),(44,0,'files/e526643dddafa352b50c684f266f0f52',1496585600),(45,0,'files/75e937c1a5f51672e9370021e0832cbe',1496585600),(46,0,'files/aeb66e606de35cf9f9a90a92affda4ea',1496585600),(47,0,'files/ccd5867b110c51fe9b9df5956b9f22dd',1496585600),(48,0,'files/960eaf74e10ed139629e1d5351eb03b6',1496585600),(49,0,'files/01dca4ad8fd9480b7bb7da811a81ff67',1496585600),(50,0,'files/45e5e4c8b19c96fc636c08cac20d67ff',1496585601),(51,0,'files/c2a592af53bcc32c877c55c3397f3520',1496585601),(52,0,'files/7b21c6d5f713d8f353ded49e1f03f917',1496585601),(53,0,'files/7e8fbb8106ae4c1074e0b4fa29f63161',1496585601),(54,0,'files/90a7deb8600fbfa23023022e5837929d',1496585601),(55,0,'files/8526746e8561ee494303fe5516868760',1496585601),(56,0,'files/4ce3813fc4f10a4d285dc75556af3c46',1496585601),(57,0,'files/b3075f30bbd9d7fcf6c4adacd01f73a8',1496585601),(58,0,'files/e0ab5ae5038b2e8094771d158b3ff28f',1496585602),(59,0,'files/bb166a694622fcc1e912d40218e27fb6',1496585602),(60,0,'files/e311f1828423114f4155ca3a2b8379b4',1496585602),(61,0,'files/71acfc7d82e7bd20caebd7ae1b6a7074',1496585602),(62,0,'files/c951a56970345a6ef9485b44b958d96a',1496585602),(63,0,'files/62106b3c9c93cb6201616390d72d6c18',1496585602),(64,0,'files/1db07ec45c357821a2cdaa02b49e80bf',1496585602),(65,0,'files/7b8d5f40dc16bc9620dc4265867c21d7',1496585602),(66,0,'files/f69ef922556068be6b410fdad929dbf3',1496585602),(67,0,'files/05ca4d2ebc744e27d3816f5927324151',1496585602),(68,0,'files/21f5bad14a6891111b84535c2a470714',1496585603),(69,0,'files/c6bcf25f530d95f4968a16d8338e0186',1496585602),(70,0,'files/426ff408e4cdd6b41283493029c043a0',1496585602),(71,0,'files/8366011ba17daffcef757e70ea1423ae',1496585602),(72,0,'files/ae5fa984d8d64b5bf0cacdab2950c08b',1496585602),(73,0,'files/1a5e469fc6e0f5606d5214ae00f09e4b',1496585602),(74,0,'files/9d234c9d14c8a953be7befa36d266579',1496585602),(75,0,'files/87f7c82d06b0c2764f101a3daf2d8ad4',1496585602),(76,0,'files/0ac839f5f56bf15ef6734de860656114',1496585602),(77,0,'files/af3d1cd190ca4bbdf43f6129da9bd90f',1496585602),(78,0,'files/a55f85a32fd0e8fcd9da5d91f70f9686',1496585603),(79,0,'files/d000c55983973b420e1b5ceb6293c72f',1496585603),(80,0,'files/dbdfbd901dcc1fe63971eb6f304c1ffb',1496585603),(81,0,'files/74166daef647b6b8b80bb306691fccb1',1496585603),(82,0,'files/d30ec14b07a3b00930de3eb8c64dc288',1496585603),(83,0,'files/432a2b508d74d7116d000851bf0fc15b',1496585603),(84,0,'files/825cf7559668f0c024e3ccb19b4a74e1',1496585603),(85,0,'files/abe316fd989e85780c949437aff18e44',1496585603),(86,0,'files/3ad0c4e483598c57e0741217b6d9f69d',1496585603),(87,0,'files/559b1a8612d7dffa4d1ac9dae22dd25d',1496585603),(88,0,'files/bc34c4b092e5d2a1a5dbc4b2043fcb93',1496585603),(89,0,'files/68b1df65433ab9d426792edc5978434b',1496585603),(90,0,'files/acac882e88713ec5896229565693e055',1496585603),(91,0,'files/5b43511fff6e25bae5b18dc0cb0f63f9',1496585603),(92,0,'files/5c7f1675da37cffa2909ddfc424b34df',1496585603),(93,0,'files/1a3c3f93ca79c2ca62845777b136b4fe',1496585603),(94,0,'files/dd177a3f1cecb9068cb92a25aa63317c',1496585603),(95,0,'files/8958ec724777ee6e1e489571e6cb6b2f',1496585603),(96,0,'files/f77be4599c82c8f9c4a6a222705284a9',1496585604),(97,0,'files/488f4074bf8bbafabcfe2531b2de081e',1496585604),(98,0,'files/0f6311ca80bc495458c035be47d65680',1496585604),(99,0,'files/dae6f5bf941fc648fd12873ca1886de5',1496585604),(100,0,'files/117734283db6fc2b7df28542840a143d',1496585604),(101,0,'files/d7639b8862753bb00bd95fcc197824ae',1496585604),(102,0,'files/156b0709faf76708c3094c27219f1ead',1496585604),(103,0,'files/f291807a89244bdad30b57ce6c12ebc4',1496585604),(104,0,'files/e0bd635c6d81d13841803ca8d11167a0',1496585604),(105,0,'files/b6e959f26bf3ca22766f78c502f6bd4c',1496585604),(106,0,'files/2d3187baa44db6ec069206fa5d36dd53',1496585604),(107,0,'files/f97be52c27501c6c5e61b270ecaf091d',1496585604),(108,0,'files/219681c0c1f76776bca5080643ef5bbc',1496585604),(109,0,'files/9714630514ffd94bf0173dac5216fc01',1496585604);
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
INSERT INTO `oc_filecache` VALUES (1,1,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,7074735,1496580916,1496580916,0,0,'59340334b26e4',23,''),(2,1,'files','45b963397aa40d4a0063e0d85e4fe7a1',1,'files',2,1,7074735,1485536382,1485536382,0,0,'588b7c7e1c615',31,''),(3,1,'files/Nextcloud.mp4','77a79c09b93e57cba23c11eb0e6048a6',2,'Nextcloud.mp4',4,3,462413,1485536381,1485536381,0,0,'2e0c6f035652f7ec29d5958b4d90fde1',27,''),(4,3,'','d41d8cd98f00b204e9800998ecf8427e',-1,'',2,1,-1,1496581971,1496580917,0,0,'59340754032f6',23,''),(5,3,'appdata_ocll5awmjb7q','e7a8a61323a5dca2ede2cbe9c5cb7bbc',4,'appdata_ocll5awmjb7q',2,1,183135,1485596908,1485536412,0,0,'588c68ecc2bdf',31,''),(6,3,'appdata_ocll5awmjb7q/preview','2cea38b94d1285578586b5cc14b5a347',5,'preview',2,1,0,1485536381,1485536381,0,0,'588b7c7dcac41',31,''),(7,1,'files/Photos','d01bb67e7b71dd49fd06bad922f521c9',2,'Photos',2,1,2360011,1485536381,1485536381,0,0,'588b7c7df1166',31,''),(8,1,'files/Photos/Nut.jpg','aa8daeb975e1d39412954fd5cd41adb4',7,'Nut.jpg',6,5,955026,1485536381,1485536381,0,0,'1ed8bdc1f6c252ec7919cd0f3cd9a2f6',27,''),(9,1,'files/Photos/Hummingbird.jpg','e077463269c404ae0f6f8ea7f2d7a326',7,'Hummingbird.jpg',6,5,585219,1485536381,1485536381,0,0,'7d97a07608c81805c42b0a073b7c870e',27,''),(10,1,'files/Photos/Coast.jpg','a6fe87299d78b207e9b7aba0f0cb8a0a',7,'Coast.jpg',6,5,819766,1485536382,1485536382,0,0,'96570532ff5c2c31c2a19894f2100869',27,''),(11,1,'files/Documents','0ad78ba05b6961d92f7970b2b3922eca',2,'Documents',2,1,78496,1485536382,1485536382,0,0,'588b7c7e14bf5',31,''),(12,1,'files/Documents/About.txt','9da7b739e7a65d74793b2881da521169',11,'About.txt',8,7,1074,1485536382,1485536382,0,0,'81f0f098ceab77b31b34ae011daa7edb',27,''),(13,1,'files/Documents/About.odt','b2ee7d56df9f34a0195d4b611376e885',11,'About.odt',10,9,77422,1485536382,1485536382,0,0,'483a2ec102c031cc5ee0f1cbca1fc9f0',27,''),(14,1,'files/Nextcloud Manual.pdf','2bc58a43566a8edde804a4a97a9c7469',2,'Nextcloud Manual.pdf',11,9,4173815,1485536382,1485536382,0,0,'77f87781841d789a7de2e7fceeaba571',27,''),(15,3,'appdata_ocll5awmjb7q/avatar','3ba2a1f8dae2d92bb188e5f04d81f384',5,'avatar',2,1,0,1485536384,1485536384,0,0,'588b7c809c846',31,''),(16,3,'appdata_ocll5awmjb7q/avatar/admin','f814e8679325f67adbe104542afb0d51',15,'admin',2,1,0,1485536384,1485536384,0,0,'588b7c809aa0f',31,''),(17,3,'appdata_ocll5awmjb7q/theming','3e18ef4914086f27159792884373e207',5,'theming',2,1,2117,1485536388,1485536388,0,0,'588b7c84a926b',31,''),(18,3,'appdata_ocll5awmjb7q/theming/0','344e998ce0e8878359748028a1db4ae6',17,'0',2,1,2117,1485536388,1485536388,0,0,'588b7c84a926b',31,''),(19,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_folder.svg','34598e545dd2228f6b91a229c698d807',18,'icon-core-filetypes_folder.svg',12,5,254,1485536388,1485536388,0,0,'5367e1366ec8cacaca54a3b2c4e82c55',27,''),(20,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_video.svg','98d9e39165989a3d076a962b447c8bb7',18,'icon-core-filetypes_video.svg',12,5,328,1485536388,1485536388,0,0,'d6952fced18acbb9df9d2e4325a6259b',27,''),(21,3,'appdata_ocll5awmjb7q/theming/0/icon-core-filetypes_application-pdf.svg','ab4efc1fac68882bbceadde19af542df',18,'icon-core-filetypes_application-pdf.svg',12,5,1535,1485536388,1485536388,0,0,'e872d2b15ec22c71eb95bdc1b0cb963d',27,''),(22,3,'files_external','c270928b685e7946199afdfb898d27ea',4,'files_external',2,1,0,1496580907,1496580907,0,0,'5934032b1ebed',31,''),(23,3,'appdata_ocll5awmjb7q/appstore','a50221ec28c7669b947e8a7c718800f8',5,'appstore',2,1,181018,1485596908,1485536413,0,0,'588c68ecc2bdf',31,''),(24,3,'appdata_ocll5awmjb7q/appstore/apps.json','0ddc045c916e17c7cae94638e0fd98fb',23,'apps.json',13,9,156803,1485596908,1485596908,0,0,'3e763404747f8de72d4f1a6c0032a892',27,''),(25,3,'appdata_ocll5awmjb7q/appstore/categories.json','b213cc26ba8b8058df581e5d83c5b6ec',23,'categories.json',13,9,24215,1485596908,1485596908,0,0,'d83b19a6557c0bfb0838cf9c68965183',27,''),(26,1,'cache','0fea6a13c52b4d4725368f24b045ca84',1,'cache',2,1,0,1496580916,1496580916,0,0,'59340334af0d4',31,''),(27,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628','2f1ddb6ca6c0dd1f1c2bec0c1a67350b',4,'appdata_3aedb9fdcb13fa275eeeccf635bc6628',2,1,224139,1496581971,1496581971,0,0,'59340754032f6',31,''),(28,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar','199a71386bc25e8da26ae529cf2154e0',27,'avatar',2,1,0,1496580926,1496580926,0,0,'5934033ed0b66',31,''),(29,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/admin','f74e3411e2fd86fdf5205e677295ccd5',28,'admin',2,1,0,1496580917,1496580917,0,0,'59340335b08d4',31,''),(30,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/sysadmin','40992a3a04cc0cae9c052289c99fe5e0',28,'sysadmin',2,1,0,1496580924,1496580924,0,0,'5934033c2e5c7',31,''),(31,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest10','d19691008155053b11d32967675d2c11',28,'guest10',2,1,0,1496580924,1496580924,0,0,'5934033c4f898',31,''),(32,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest1','c83ca98d9aa4aa20de46e1c8690d8239',28,'guest1',2,1,0,1496580924,1496580924,0,0,'5934033c5ef09',31,''),(33,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest2','d6fc4c8b880229eefe0aa72dbb34b27c',28,'guest2',2,1,0,1496580924,1496580924,0,0,'5934033c79944',31,''),(34,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest3','33f683920b04b76d417480142c0ae6ca',28,'guest3',2,1,0,1496580924,1496580924,0,0,'5934033cac207',31,''),(35,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest4','55aafa1407b59e3bb7dcade4be425f63',28,'guest4',2,1,0,1496580925,1496580925,0,0,'5934033d07901',31,''),(36,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest5','3dd43ae0dbdfcd4fe1c50bc8f3974eff',28,'guest5',2,1,0,1496580925,1496580925,0,0,'5934033d21755',31,''),(37,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest6','f189bcfd30d49f85232c9b30eda2d9f7',28,'guest6',2,1,0,1496580925,1496580925,0,0,'5934033d3edd9',31,''),(38,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest7','8f88adf747d424494a3b621a9e7c369c',28,'guest7',2,1,0,1496580925,1496580925,0,0,'5934033d52db5',31,''),(39,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest8','6574861f2444443511aa6e6e09299e93',28,'guest8',2,1,0,1496580925,1496580925,0,0,'5934033d69bba',31,''),(40,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/guest9','6f6d098c1972c59ed24affe81373bb04',28,'guest9',2,1,0,1496580925,1496580925,0,0,'5934033d918fb',31,''),(41,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/ismith','664a31bdf20ae6fefa874006f7b5f9b0',28,'ismith',2,1,0,1496580925,1496580925,0,0,'5934033db8e5b',31,''),(42,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/jjones','21dbf6eaa0cdd181bbbf98300ecdd530',28,'jjones',2,1,0,1496580925,1496580925,0,0,'5934033dce59c',31,''),(43,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/tech1','71c7dc04b9286ac6b2854b20bc3e6a1b',28,'tech1',2,1,0,1496580925,1496580925,0,0,'5934033de09a9',31,''),(44,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/tech2','5b9ff5e9a627e136a4ed622824e05353',28,'tech2',2,1,0,1496580926,1496580926,0,0,'5934033e15845',31,''),(45,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/tech3','fbad00c216a2960ca4c4fbb6dbbca63e',28,'tech3',2,1,0,1496580926,1496580926,0,0,'5934033e2588a',31,''),(46,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/tech4','0f9a8a89196b94e5074e6c7a36001c7f',28,'tech4',2,1,0,1496580926,1496580926,0,0,'5934033e3d526',31,''),(47,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/theming','568d776b51be78cf7d16210e826650bf',27,'theming',2,1,2117,1496580926,1496580926,0,0,'5934033ec8f65',31,''),(48,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/exam1','2784d0b81a907f7e418d8462c1549029',28,'exam1',2,1,0,1496580926,1496580926,0,0,'5934033e538fe',31,''),(49,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/theming/0','865fc39fe5af523ad5128ea1b1cdb58a',47,'0',2,1,2117,1496580926,1496580926,0,0,'5934033ec8f65',31,''),(50,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/theming/0/icon-core-filetypes_application-pdf.svg','bc3f0513c98fdef035ab17eacda467e2',49,'icon-core-filetypes_application-pdf.svg',12,5,1535,1496580926,1496580926,0,0,'35be93d7e0cb70b1d3bc1fb1f1cd4b24',27,''),(51,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/preview','b439c37c1c8d02ce65b8f7d50874e02f',27,'preview',2,1,0,1496580926,1496580926,0,0,'5934033e750ff',31,''),(52,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/exam2','cc308aa96c80af69d77ead5c858aca93',28,'exam2',2,1,0,1496580926,1496580926,0,0,'5934033e77256',31,''),(53,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/theming/0/icon-core-filetypes_video.svg','7c48458bcc6baf58f0bcc1507ec81cb3',49,'icon-core-filetypes_video.svg',12,5,328,1496580926,1496580926,0,0,'44d56613e4f637dee3b00e744d721cbc',27,''),(54,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/exam3','d81f94d48e9c1099e384012a152174b6',28,'exam3',2,1,0,1496580926,1496580926,0,0,'5934033e9b4be',31,''),(55,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/exam4','599968bda72cfab340b0dc61a1343ff9',28,'exam4',2,1,0,1496580926,1496580926,0,0,'5934033eadd9f',31,''),(56,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/exam5','3b65fa3c4184baac13344aff4455037b',28,'exam5',2,1,0,1496580926,1496580926,0,0,'5934033ebdd31',31,''),(57,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/theming/0/icon-core-filetypes_folder.svg','bb2fcf8f9d94f012b5d1ce16016d2bdf',49,'icon-core-filetypes_folder.svg',12,5,254,1496580926,1496580926,0,0,'244ad57b1a5e4db1b109418bb6d81245',27,''),(58,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/avatar/profileuser','e297cfd22ca3ed7007940e1b953b9746',28,'profileuser',2,1,0,1496580926,1496580926,0,0,'5934033ecf312',31,''),(59,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/appstore','c3e4f7121db209a5c82432a87aa30fea',27,'appstore',2,1,222022,1496581971,1496581971,0,0,'59340754032f6',31,''),(60,3,'appdata_3aedb9fdcb13fa275eeeccf635bc6628/appstore/apps.json','c9f4f0ac9e38601185d0783485cc2588',59,'apps.json',13,9,222022,1496581971,1496581971,0,0,'454419d94a94def9eb44852002a58409',27,'');
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
INSERT INTO `oc_jobs` VALUES (1,'OCA\\Federation\\SyncJob','null',1485536386,1485536386,0),(2,'OCA\\Files_Versions\\BackgroundJob\\ExpireVersions','null',1485536399,1485536399,0),(4,'OCA\\UpdateNotification\\Notification\\BackgroundJob','null',1485536497,1485536497,0),(5,'OCA\\Files_Trashbin\\BackgroundJob\\ExpireTrash','null',1485536500,1485536500,0),(6,'OCA\\Files_Sharing\\DeleteOrphanedSharesJob','null',1485596907,1485596907,0),(7,'OCA\\Files_Sharing\\ExpireSharesJob','null',1485597009,1485597009,0),(8,'OCA\\NextcloudAnnouncements\\Cron\\Crawler','null',1496580906,1496580906,0),(9,'OCA\\DAV\\CardDAV\\SyncJob','null',1496580920,1496580920,0),(10,'OCA\\Activity\\BackgroundJob\\EmailNotification','null',1496580940,1496580940,0),(11,'OCA\\Activity\\BackgroundJob\\ExpireActivities','null',1496581985,1496581985,0),(12,'OCA\\Files\\BackgroundJob\\ScanFiles','null',1496581997,1496581997,0),(13,'OCA\\Files\\BackgroundJob\\DeleteOrphanedItems','null',1496582017,1496582017,0),(14,'OCA\\Files\\BackgroundJob\\CleanupFileLocks','null',0,1485536381,0),(15,'\\OC\\Authentication\\Token\\DefaultTokenCleanupJob','null',0,1485536381,0),(16,'OCA\\FirstRunWizard\\Notification\\BackgroundJob','{\"uid\":\"admin\"}',0,1485536384,0),(17,'OCA\\User_LDAP\\Jobs\\UpdateGroups','null',0,1485536435,0),(18,'OCA\\User_LDAP\\Jobs\\CleanUp','null',0,1485536435,0),(19,'OCA\\UpdateNotification\\ResetTokenBackgroundJob','null',0,1496581824,0),(20,'OCA\\User_LDAP\\Migration\\UUIDFixUser','{\"records\":[{\"dn\":\"cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam1\",\"uuid\":\"20AA7607-49AA-4FA6-BFBD-D025FE77F77E\"},{\"dn\":\"cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam2\",\"uuid\":\"F0DD3D26-A403-4714-B362-30BD7965F709\"},{\"dn\":\"cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam3\",\"uuid\":\"CC101DDC-F0ED-4255-8000-5EA1E025B9F3\"},{\"dn\":\"cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam4\",\"uuid\":\"60A324AE-E302-4CAE-A44D-6005F87AA5FC\"},{\"dn\":\"cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"exam5\",\"uuid\":\"1446431E-1E45-4E07-984D-D7F1A7158D80\"},{\"dn\":\"cn=guest1,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest1\",\"uuid\":\"15B3552C-147F-494C-8092-93A39BAB41E7\"},{\"dn\":\"cn=guest10,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest10\",\"uuid\":\"B093E322-EE90-4588-A55D-5CB933B2305C\"},{\"dn\":\"cn=guest2,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest2\",\"uuid\":\"3CC5C6EA-6687-4C83-85F6-17A315413348\"},{\"dn\":\"cn=guest3,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest3\",\"uuid\":\"D914F1E6-B18B-4185-99F9-6C34FE5E917E\"},{\"dn\":\"cn=guest4,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest4\",\"uuid\":\"F344E216-488F-4E1B-B9A3-8CCB8B169040\"},{\"dn\":\"cn=guest5,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest5\",\"uuid\":\"CD5B8079-425A-4183-B1B7-74C7FAB2A340\"},{\"dn\":\"cn=guest6,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest6\",\"uuid\":\"20DF7D55-ED0B-4F36-9077-B8B500C55B59\"},{\"dn\":\"cn=guest7,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest7\",\"uuid\":\"02DDEF08-8E11-4DA5-A5DF-E70BC93BC469\"},{\"dn\":\"cn=guest8,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest8\",\"uuid\":\"E40C0AF1-0BD8-48D9-AFF7-C740FB59FD0F\"},{\"dn\":\"cn=guest9,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"guest9\",\"uuid\":\"C53624B3-E00E-432B-9E95-13BED15CE932\"},{\"dn\":\"cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"ismith\",\"uuid\":\"453833F9-B981-4F38-BD31-6B4928047821\"},{\"dn\":\"cn=jjones,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"jjones\",\"uuid\":\"871E4AE0-BFA7-4BB3-9DEB-609B1A24BA15\"},{\"dn\":\"cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE\",\"name\":\"profileuser\",\"uuid\":\"1971BAEB-1084-4844-A392-A6FB19585BE9\"},{\"dn\":\"cn=sysadmin,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"sysadmin\",\"uuid\":\"2B58FEAC-FADC-4610-8B53-87E2DA684A9E\"},{\"dn\":\"cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech1\",\"uuid\":\"A6473A6C-8E17-4069-BAD7-D197528B182B\"},{\"dn\":\"cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech2\",\"uuid\":\"F0E16E39-9C92-44AE-B766-F6EA61E0502D\"},{\"dn\":\"cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech3\",\"uuid\":\"FCDCF27B-BD54-417A-95C3-115214B3AF3F\"},{\"dn\":\"cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE\",\"name\":\"tech4\",\"uuid\":\"DD94CD74-D2C4-4A83-BA55-7DE227804F12\"}]}',0,1496581971,0),(21,'OC\\Settings\\RemoveOrphaned','null',0,1496581971,0),(22,'OC\\Repair\\NC11\\MoveAvatarsBackgroundJob','null',0,1496581975,0),(23,'OC\\Repair\\NC11\\CleanPreviewsBackgroundJob','{\"uid\":\"admin\"}',0,1496581975,0);
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
INSERT INTO `oc_ldap_group_mapping` VALUES ('cn=exams,ou=groups,ou=people,CHANGETHISLDAPBASE','exams','B1CB913D-6E9C-4E29-85BE-4A1717C31CA7'),('cn=guestusers,ou=groups,ou=people,CHANGETHISLDAPBASE','guestusers','6791694F-30DE-46EA-BBFD-35CAB804C50E'),('cn=itadmin,ou=groups,ou=people,CHANGETHISLDAPBASE','itadmin','E96641F8-F146-49AF-B4D2-922BE38F3215'),('cn=profilemanagement,ou=groups,ou=people,CHANGETHISLDAPBASE','profilemanagement','F4205451-5E04-4CB6-9568-617EF3590EFA'),('cn=staff,ou=groups,ou=people,CHANGETHISLDAPBASE','staff','79E5FB59-2A15-4FA7-B289-5452CD3D7106'),('cn=tech,ou=groups,ou=people,CHANGETHISLDAPBASE','tech','BEC7E602-41FF-4129-817A-6C119E34B2C9');
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
INSERT INTO `oc_ldap_user_mapping` VALUES ('cn=exam1,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam1','20AA7607-49AA-4FA6-BFBD-D025FE77F77E'),('cn=exam2,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam2','F0DD3D26-A403-4714-B362-30BD7965F709'),('cn=exam3,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam3','CC101DDC-F0ED-4255-8000-5EA1E025B9F3'),('cn=exam4,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam4','60A324AE-E302-4CAE-A44D-6005F87AA5FC'),('cn=exam5,ou=exams,ou=other,ou=people,CHANGETHISLDAPBASE','exam5','1446431E-1E45-4E07-984D-D7F1A7158D80'),('cn=guest1,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest1','15B3552C-147F-494C-8092-93A39BAB41E7'),('cn=guest10,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest10','B093E322-EE90-4588-A55D-5CB933B2305C'),('cn=guest2,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest2','3CC5C6EA-6687-4C83-85F6-17A315413348'),('cn=guest3,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest3','D914F1E6-B18B-4185-99F9-6C34FE5E917E'),('cn=guest4,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest4','F344E216-488F-4E1B-B9A3-8CCB8B169040'),('cn=guest5,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest5','CD5B8079-425A-4183-B1B7-74C7FAB2A340'),('cn=guest6,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest6','20DF7D55-ED0B-4F36-9077-B8B500C55B59'),('cn=guest7,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest7','02DDEF08-8E11-4DA5-A5DF-E70BC93BC469'),('cn=guest8,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest8','E40C0AF1-0BD8-48D9-AFF7-C740FB59FD0F'),('cn=guest9,ou=guestusers,ou=other,ou=people,CHANGETHISLDAPBASE','guest9','C53624B3-E00E-432B-9E95-13BED15CE932'),('cn=ismith,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','ismith','453833F9-B981-4F38-BD31-6B4928047821'),('cn=jjones,ou=staff,ou=personnel,ou=people,CHANGETHISLDAPBASE','jjones','871E4AE0-BFA7-4BB3-9DEB-609B1A24BA15'),('cn=profileuser,ou=other,ou=people,CHANGETHISLDAPBASE','profileuser','1971BAEB-1084-4844-A392-A6FB19585BE9'),('cn=sysadmin,ou=itadmin,ou=personnel,ou=people,CHANGETHISLDAPBASE','sysadmin','2B58FEAC-FADC-4610-8B53-87E2DA684A9E'),('cn=tech1,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech1','A6473A6C-8E17-4069-BAD7-D197528B182B'),('cn=tech2,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech2','F0E16E39-9C92-44AE-B766-F6EA61E0502D'),('cn=tech3,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech3','FCDCF27B-BD54-417A-95C3-115214B3AF3F'),('cn=tech4,ou=tech,ou=personnel,ou=people,CHANGETHISLDAPBASE','tech4','DD94CD74-D2C4-4A83-BA55-7DE227804F12');
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
INSERT INTO `oc_notifications` VALUES (1,'survey_client','admin',1485536412,'dummy','23','updated','[]','','[]','','','[{\"label\":\"enable\",\"link\":\"https:\\/\\/CHANGETHISREALM\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"POST\",\"primary\":true},{\"label\":\"disable\",\"link\":\"https:\\/\\/CHANGETHISREALM\\/nextcloud\\/ocs\\/v2.php\\/apps\\/survey_client\\/api\\/v1\\/monthly\",\"type\":\"DELETE\",\"primary\":false}]');
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
INSERT INTO `oc_preferences` VALUES ('admin','core','lang','en'),('admin','core','timezone','Europe/Berlin'),('admin','files_external','config_version','0.5.0'),('admin','firstrunwizard','show','0'),('admin','login','lastLogin','1496580916'),('exam1','files_external','config_version','0.5.0'),('exam1','user_ldap','displayName','Exam 1'),('exam1','user_ldap','homePath',''),('exam1','user_ldap','lastFeatureRefresh','1496581997'),('exam1','user_ldap','uid','exam1'),('exam2','files_external','config_version','0.5.0'),('exam2','user_ldap','displayName','Exam 2'),('exam2','user_ldap','homePath',''),('exam2','user_ldap','lastFeatureRefresh','1496581997'),('exam2','user_ldap','uid','exam2'),('exam3','files_external','config_version','0.5.0'),('exam3','user_ldap','displayName','Exam 3'),('exam3','user_ldap','homePath',''),('exam3','user_ldap','lastFeatureRefresh','1496581997'),('exam3','user_ldap','uid','exam3'),('exam4','files_external','config_version','0.5.0'),('exam4','user_ldap','displayName','Exam 4'),('exam4','user_ldap','homePath',''),('exam4','user_ldap','lastFeatureRefresh','1496581997'),('exam4','user_ldap','uid','exam4'),('exam5','files_external','config_version','0.5.0'),('exam5','user_ldap','displayName','Exam 5'),('exam5','user_ldap','homePath',''),('exam5','user_ldap','lastFeatureRefresh','1496581997'),('exam5','user_ldap','uid','exam5'),('guest1','files_external','config_version','0.5.0'),('guest1','user_ldap','displayName','Guest 1'),('guest1','user_ldap','homePath',''),('guest1','user_ldap','lastFeatureRefresh','1496581997'),('guest1','user_ldap','uid','guest1'),('guest10','files_external','config_version','0.5.0'),('guest10','user_ldap','displayName','Guest 10'),('guest10','user_ldap','homePath',''),('guest10','user_ldap','lastFeatureRefresh','1496581997'),('guest10','user_ldap','uid','guest10'),('guest2','files_external','config_version','0.5.0'),('guest2','user_ldap','displayName','Guest 2'),('guest2','user_ldap','homePath',''),('guest2','user_ldap','lastFeatureRefresh','1496581997'),('guest2','user_ldap','uid','guest2'),('guest3','files_external','config_version','0.5.0'),('guest3','user_ldap','displayName','Guest 3'),('guest3','user_ldap','homePath',''),('guest3','user_ldap','lastFeatureRefresh','1496581997'),('guest3','user_ldap','uid','guest3'),('guest4','files_external','config_version','0.5.0'),('guest4','user_ldap','displayName','Guest 4'),('guest4','user_ldap','homePath',''),('guest4','user_ldap','lastFeatureRefresh','1496581997'),('guest4','user_ldap','uid','guest4'),('guest5','files_external','config_version','0.5.0'),('guest5','user_ldap','displayName','Guest 5'),('guest5','user_ldap','homePath',''),('guest5','user_ldap','lastFeatureRefresh','1496581997'),('guest5','user_ldap','uid','guest5'),('guest6','files_external','config_version','0.5.0'),('guest6','user_ldap','displayName','Guest 6'),('guest6','user_ldap','homePath',''),('guest6','user_ldap','lastFeatureRefresh','1496581997'),('guest6','user_ldap','uid','guest6'),('guest7','files_external','config_version','0.5.0'),('guest7','user_ldap','displayName','Guest 7'),('guest7','user_ldap','homePath',''),('guest7','user_ldap','lastFeatureRefresh','1496581997'),('guest7','user_ldap','uid','guest7'),('guest8','files_external','config_version','0.5.0'),('guest8','user_ldap','displayName','Guest 8'),('guest8','user_ldap','homePath',''),('guest8','user_ldap','lastFeatureRefresh','1496581997'),('guest8','user_ldap','uid','guest8'),('guest9','files_external','config_version','0.5.0'),('guest9','user_ldap','displayName','Guest 9'),('guest9','user_ldap','homePath',''),('guest9','user_ldap','lastFeatureRefresh','1496581997'),('guest9','user_ldap','uid','guest9'),('ismith','files_external','config_version','0.5.0'),('ismith','user_ldap','displayName','Ian Smith'),('ismith','user_ldap','homePath',''),('ismith','user_ldap','lastFeatureRefresh','1496581997'),('ismith','user_ldap','uid','ismith'),('jjones','files_external','config_version','0.5.0'),('jjones','user_ldap','displayName','John Jones'),('jjones','user_ldap','homePath',''),('jjones','user_ldap','lastFeatureRefresh','1496581997'),('jjones','user_ldap','uid','jjones'),('profileuser','files_external','config_version','0.5.0'),('profileuser','user_ldap','displayName','Profile User'),('profileuser','user_ldap','homePath',''),('profileuser','user_ldap','lastFeatureRefresh','1496581997'),('profileuser','user_ldap','uid','profileuser'),('sysadmin','files_external','config_version','0.5.0'),('sysadmin','user_ldap','displayName','Sysadmin User'),('sysadmin','user_ldap','homePath',''),('sysadmin','user_ldap','lastFeatureRefresh','1496581997'),('sysadmin','user_ldap','uid','sysadmin'),('tech1','files_external','config_version','0.5.0'),('tech1','user_ldap','displayName','Tech 1'),('tech1','user_ldap','homePath',''),('tech1','user_ldap','lastFeatureRefresh','1496581997'),('tech1','user_ldap','uid','tech1'),('tech2','files_external','config_version','0.5.0'),('tech2','user_ldap','displayName','Tech 2'),('tech2','user_ldap','homePath',''),('tech2','user_ldap','lastFeatureRefresh','1496581997'),('tech2','user_ldap','uid','tech2'),('tech3','files_external','config_version','0.5.0'),('tech3','user_ldap','displayName','Tech 3'),('tech3','user_ldap','homePath',''),('tech3','user_ldap','lastFeatureRefresh','1496581997'),('tech3','user_ldap','uid','tech3'),('tech4','files_external','config_version','0.5.0'),('tech4','user_ldap','displayName','Tech 4'),('tech4','user_ldap','homePath',''),('tech4','user_ldap','lastFeatureRefresh','1496581997'),('tech4','user_ldap','uid','tech4');
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
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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

-- Dump completed on 2017-06-04 15:18:52
