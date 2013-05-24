-- MySQL dump 10.13  Distrib 5.1.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ocsweb
-- ------------------------------------------------------
-- Server version	5.1.41-3ubuntu12.3

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
-- Table structure for table `accesslog`
--

DROP TABLE IF EXISTS `accesslog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accesslog` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `USERID` varchar(255) DEFAULT NULL,
  `LOGDATE` datetime DEFAULT NULL,
  `PROCESSES` text,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `USERID` (`USERID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accesslog`
--

LOCK TABLES `accesslog` WRITE;
/*!40000 ALTER TABLE `accesslog` DISABLE KEYS */;
/*!40000 ALTER TABLE `accesslog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accountinfo`
--

DROP TABLE IF EXISTS `accountinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accountinfo` (
  `HARDWARE_ID` int(11) NOT NULL,
  `TAG` varchar(255) DEFAULT 'NA',
  PRIMARY KEY (`HARDWARE_ID`),
  KEY `TAG` (`TAG`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountinfo`
--

LOCK TABLES `accountinfo` WRITE;
/*!40000 ALTER TABLE `accountinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `accountinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bios`
--

DROP TABLE IF EXISTS `bios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bios` (
  `HARDWARE_ID` int(11) NOT NULL,
  `SMANUFACTURER` varchar(255) DEFAULT NULL,
  `SMODEL` varchar(255) DEFAULT NULL,
  `SSN` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `BMANUFACTURER` varchar(255) DEFAULT NULL,
  `BVERSION` varchar(255) DEFAULT NULL,
  `BDATE` varchar(255) DEFAULT NULL,
  `ASSETTAG` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`),
  KEY `SSN` (`SSN`),
  KEY `ASSETTAG` (`ASSETTAG`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bios`
--

LOCK TABLES `bios` WRITE;
/*!40000 ALTER TABLE `bios` DISABLE KEYS */;
/*!40000 ALTER TABLE `bios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklist_macaddresses`
--

DROP TABLE IF EXISTS `blacklist_macaddresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist_macaddresses` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MACADDRESS` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`MACADDRESS`),
  KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklist_macaddresses`
--

LOCK TABLES `blacklist_macaddresses` WRITE;
/*!40000 ALTER TABLE `blacklist_macaddresses` DISABLE KEYS */;
INSERT INTO `blacklist_macaddresses` VALUES (1,'00:00:00:00:00:00'),(2,'FF:FF:FF:FF:FF:FF'),(3,'44:45:53:54:00:00'),(4,'44:45:53:54:00:01'),(5,'00:01:02:7D:9B:1C'),(6,'00:08:A1:46:06:35'),(7,'00:08:A1:66:E2:1A'),(8,'00:09:DD:10:37:68'),(9,'00:0F:EA:9A:E2:F0'),(10,'00:10:5A:72:71:F3'),(11,'00:11:11:85:08:8B'),(12,'10:11:11:11:11:11'),(13,'44:45:53:54:61:6F'),(14,'');
/*!40000 ALTER TABLE `blacklist_macaddresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklist_serials`
--

DROP TABLE IF EXISTS `blacklist_serials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist_serials` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `SERIAL` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`SERIAL`),
  KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklist_serials`
--

LOCK TABLES `blacklist_serials` WRITE;
/*!40000 ALTER TABLE `blacklist_serials` DISABLE KEYS */;
INSERT INTO `blacklist_serials` VALUES (1,'N/A'),(2,'(null string)'),(3,'INVALID'),(4,'SYS-1234567890'),(5,'SYS-9876543210'),(6,'SN-12345'),(7,'SN-1234567890'),(8,'1111111111'),(9,'1111111'),(10,'1'),(11,'0123456789'),(12,'12345'),(13,'123456'),(14,'1234567'),(15,'12345678'),(16,'123456789'),(17,'1234567890'),(18,'123456789000'),(19,'12345678901234567'),(20,'0000000000'),(21,'000000000'),(22,'00000000'),(23,'0000000'),(24,'000000'),(25,'NNNNNNN'),(26,'xxxxxxxxxxx'),(27,'EVAL'),(28,'IATPASS'),(29,'none'),(30,'To Be Filled By O.E.M.'),(31,'Tulip Computers'),(32,'Serial Number xxxxxx'),(33,'SN-123456fvgv3i0b8o5n6n7k'),(34,'');
/*!40000 ALTER TABLE `blacklist_serials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `NAME` varchar(50) NOT NULL,
  `IVALUE` int(11) DEFAULT NULL,
  `TVALUE` varchar(255) DEFAULT NULL,
  `COMMENTS` text,
  PRIMARY KEY (`NAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES ('FREQUENCY',0,'','Specify the frequency (days) of inventories. (0: inventory at each login. -1: no inventory)'),('PROLOG_FREQ',24,'','Specify the frequency (hours) of prolog, on agents'),('IPDISCOVER',2,'','Max number of computers per gateway retrieving IP on the network'),('INVENTORY_DIFF',1,'','Activate/Deactivate inventory incremental writing'),('IPDISCOVER_LATENCY',100,'','Default latency between two arp requests'),('INVENTORY_TRANSACTION',1,'','Enable/disable db commit at each inventory section'),('REGISTRY',0,'','Activates or not the registry query function'),('IPDISCOVER_MAX_ALIVE',7,'','Max number of days before an Ip Discover computer is replaced'),('DEPLOY',1,'','Activates or not the automatic deployment option'),('UPDATE',0,'','Activates or not the update feature'),('TRACE_DELETED',0,'','Trace deleted/duplicated computers (Activated by GLPI)'),('LOGLEVEL',0,'','ocs engine loglevel'),('AUTO_DUPLICATE_LVL',7,'','Duplicates bitmap'),('DOWNLOAD',0,'','Activate softwares auto deployment feature'),('DOWNLOAD_CYCLE_LATENCY',60,'','Time between two cycles (seconds)'),('DOWNLOAD_PERIOD_LENGTH',10,'','Number of cycles in a period'),('DOWNLOAD_FRAG_LATENCY',10,'','Time between two downloads (seconds)'),('DOWNLOAD_PERIOD_LATENCY',0,'','Time between two periods (seconds)'),('DOWNLOAD_TIMEOUT',30,'','Validity of a package (in days)'),('LOCAL_SERVER',0,'localhost','Server address used for local import'),('LOCAL_PORT',80,'','Server port used for local import'),('DOWNLOAD_PACK_DIR',0,'/var/lib/ocsinventory-reports','Directory for download files'),('IPDISCOVER_IPD_DIR',0,'/var/lib/ocsinventory-reports','Directory for Ipdiscover files'),('GUI_VERSION',0,'5005','Version of the installed GUI and database'),('DOWNLOAD_SERVER_URI',0,'$IP$/local','Server url used for group of server'),('DOWNLOAD_SERVER_DOCROOT',0,'d:\\\\tele_ocs','Server directory used for group of server'),('LOCK_REUSE_TIME',600,'','Validity of a computer\'s lock'),('INVENTORY_WRITE_DIFF',0,'','Configure engine to make a differential update of inventory sections (row level). Lower DB backend load, higher frontend load'),('INVENTORY_CACHE_ENABLED',1,'','Enable some stuff to improve DB queries, especially for GUI multicriteria searching system'),('DOWNLOAD_GROUPS_TRACE_EVENTS',1,'','Specify if you want to track packages affected to a group on computer\'s level'),('ENABLE_GROUPS',1,'','Enable the computer\'s groups feature'),('GROUPS_CACHE_OFFSET',43200,'','Random number computed in the defined range. Designed to avoid computing many groups in the same process'),('GROUPS_CACHE_REVALIDATE',43200,'','Specify the validity of computer\'s groups (default: compute it once a day - see offset)'),('IPDISCOVER_BETTER_THRESHOLD',1,'','Specify the minimal difference to replace an ipdiscover agent'),('IPDISCOVER_NO_POSTPONE',0,'','Disable the time before a first election (not recommended)'),('IPDISCOVER_USE_GROUPS',1,'','Enable groups for ipdiscover (for example, you might want to prevent some groups'),('GENERATE_OCS_FILES',0,'','Use with ocsinventory-injector, enable the multi entities feature'),('OCS_FILES_FORMAT',0,'OCS','Generate either compressed file or clear XML text'),('OCS_FILES_OVERWRITE',0,'','Specify if you want to keep trace of all inventory between to synchronisation with the higher level server'),('OCS_FILES_PATH',0,'/tmp','Path to ocs files directory (must be writeable)'),('PROLOG_FILTER_ON',0,'','Enable prolog filter stack'),('INVENTORY_FILTER_ENABLED',0,'','Enable core filter system to modify some things \"on the fly\"'),('INVENTORY_FILTER_FLOOD_IP',0,'','Enable inventory flooding filter. A dedicated ipaddress ia allowed to send a new computer only once in this period'),('INVENTORY_FILTER_FLOOD_IP_CACHE_TIME',300,'','Period definition for INVENTORY_FILTER_FLOOD_IP'),('INVENTORY_FILTER_ON',0,'','Enable inventory filter stack'),('GUI_REPORT_RAM_MAX',512,'','Filter on RAM for console page'),('GUI_REPORT_RAM_MINI',128,'','Filter on RAM for console page'),('GUI_REPORT_NOT_VIEW',3,'','Filter on DAY for console page'),('GUI_REPORT_PROC_MINI',1000,'','Filter on Hard Drive for console page'),('GUI_REPORT_DD_MAX',4000,'','Filter on Hard Drive for console page'),('GUI_REPORT_PROC_MAX',3000,'','Filter on PROCESSOR for console page'),('GUI_REPORT_DD_MINI',500,'','Filter on PROCESSOR for console page'),('GUI_REPORT_AGIN_MACH',30,'','Filter on lastdate for console page');
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conntrack`
--

DROP TABLE IF EXISTS `conntrack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conntrack` (
  `IP` varchar(255) NOT NULL DEFAULT '',
  `TIMESTAMP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`IP`)
) ENGINE=MEMORY DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conntrack`
--

LOCK TABLES `conntrack` WRITE;
/*!40000 ALTER TABLE `conntrack` DISABLE KEYS */;
/*!40000 ALTER TABLE `conntrack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `controllers`
--

DROP TABLE IF EXISTS `controllers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `controllers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `MANUFACTURER` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `CAPTION` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `VERSION` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `controllers`
--

LOCK TABLES `controllers` WRITE;
/*!40000 ALTER TABLE `controllers` DISABLE KEYS */;
/*!40000 ALTER TABLE `controllers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deleted_equiv`
--

DROP TABLE IF EXISTS `deleted_equiv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deleted_equiv` (
  `DATE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `DELETED` varchar(255) NOT NULL,
  `EQUIVALENT` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deleted_equiv`
--

LOCK TABLES `deleted_equiv` WRITE;
/*!40000 ALTER TABLE `deleted_equiv` DISABLE KEYS */;
/*!40000 ALTER TABLE `deleted_equiv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy`
--

DROP TABLE IF EXISTS `deploy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy` (
  `NAME` varchar(255) NOT NULL,
  `CONTENT` longblob NOT NULL,
  PRIMARY KEY (`NAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy`
--

LOCK TABLES `deploy` WRITE;
/*!40000 ALTER TABLE `deploy` DISABLE KEYS */;
/*!40000 ALTER TABLE `deploy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `devices`
--

DROP TABLE IF EXISTS `devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devices` (
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `IVALUE` int(11) DEFAULT NULL,
  `TVALUE` varchar(255) DEFAULT NULL,
  `COMMENTS` text,
  KEY `HARDWARE_ID` (`HARDWARE_ID`),
  KEY `TVALUE` (`TVALUE`),
  KEY `IVALUE` (`IVALUE`),
  KEY `NAME` (`NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devices`
--

LOCK TABLES `devices` WRITE;
/*!40000 ALTER TABLE `devices` DISABLE KEYS */;
/*!40000 ALTER TABLE `devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `devicetype`
--

DROP TABLE IF EXISTS `devicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devicetype` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devicetype`
--

LOCK TABLES `devicetype` WRITE;
/*!40000 ALTER TABLE `devicetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `devicetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dico_ignored`
--

DROP TABLE IF EXISTS `dico_ignored`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dico_ignored` (
  `EXTRACTED` varchar(255) NOT NULL,
  PRIMARY KEY (`EXTRACTED`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dico_ignored`
--

LOCK TABLES `dico_ignored` WRITE;
/*!40000 ALTER TABLE `dico_ignored` DISABLE KEYS */;
/*!40000 ALTER TABLE `dico_ignored` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dico_soft`
--

DROP TABLE IF EXISTS `dico_soft`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dico_soft` (
  `EXTRACTED` varchar(255) NOT NULL,
  `FORMATTED` varchar(255) NOT NULL,
  PRIMARY KEY (`EXTRACTED`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dico_soft`
--

LOCK TABLES `dico_soft` WRITE;
/*!40000 ALTER TABLE `dico_soft` DISABLE KEYS */;
/*!40000 ALTER TABLE `dico_soft` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `download_affect_rules`
--

DROP TABLE IF EXISTS `download_affect_rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `download_affect_rules` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `RULE` int(11) NOT NULL,
  `PRIORITY` int(11) NOT NULL,
  `CFIELD` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `OP` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `COMPTO` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `SERV_VALUE` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `RULE_NAME` varchar(200) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `download_affect_rules`
--

LOCK TABLES `download_affect_rules` WRITE;
/*!40000 ALTER TABLE `download_affect_rules` DISABLE KEYS */;
/*!40000 ALTER TABLE `download_affect_rules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `download_available`
--

DROP TABLE IF EXISTS `download_available`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `download_available` (
  `FILEID` varchar(255) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `PRIORITY` int(11) NOT NULL,
  `FRAGMENTS` int(11) NOT NULL,
  `SIZE` int(11) NOT NULL,
  `OSNAME` varchar(255) NOT NULL,
  `COMMENT` text,
  PRIMARY KEY (`FILEID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `download_available`
--

LOCK TABLES `download_available` WRITE;
/*!40000 ALTER TABLE `download_available` DISABLE KEYS */;
/*!40000 ALTER TABLE `download_available` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `download_enable`
--

DROP TABLE IF EXISTS `download_enable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `download_enable` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FILEID` varchar(255) NOT NULL,
  `INFO_LOC` varchar(255) NOT NULL,
  `PACK_LOC` varchar(255) NOT NULL,
  `CERT_PATH` varchar(255) DEFAULT NULL,
  `CERT_FILE` varchar(255) DEFAULT NULL,
  `SERVER_ID` int(11) DEFAULT NULL,
  `GROUP_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FILEID` (`FILEID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `download_enable`
--

LOCK TABLES `download_enable` WRITE;
/*!40000 ALTER TABLE `download_enable` DISABLE KEYS */;
/*!40000 ALTER TABLE `download_enable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `download_history`
--

DROP TABLE IF EXISTS `download_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `download_history` (
  `HARDWARE_ID` int(11) NOT NULL,
  `PKG_ID` int(11) NOT NULL DEFAULT '0',
  `PKG_NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`PKG_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `download_history`
--

LOCK TABLES `download_history` WRITE;
/*!40000 ALTER TABLE `download_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `download_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `download_servers`
--

DROP TABLE IF EXISTS `download_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `download_servers` (
  `HARDWARE_ID` int(11) NOT NULL,
  `URL` varchar(250) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `ADD_PORT` int(11) NOT NULL,
  `ADD_REP` varchar(250) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `GROUP_ID` int(11) NOT NULL,
  PRIMARY KEY (`HARDWARE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `download_servers`
--

LOCK TABLES `download_servers` WRITE;
/*!40000 ALTER TABLE `download_servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `download_servers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drives`
--

DROP TABLE IF EXISTS `drives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `drives` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `LETTER` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `FILESYSTEM` varchar(255) DEFAULT NULL,
  `TOTAL` int(11) DEFAULT NULL,
  `FREE` int(11) DEFAULT NULL,
  `NUMFILES` int(11) DEFAULT NULL,
  `VOLUMN` varchar(255) DEFAULT NULL,
  `CREATEDATE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drives`
--

LOCK TABLES `drives` WRITE;
/*!40000 ALTER TABLE `drives` DISABLE KEYS */;
/*!40000 ALTER TABLE `drives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engine_mutex`
--

DROP TABLE IF EXISTS `engine_mutex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `engine_mutex` (
  `NAME` varchar(255) NOT NULL DEFAULT '',
  `PID` int(11) DEFAULT NULL,
  `TAG` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`NAME`,`TAG`)
) ENGINE=MEMORY DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engine_mutex`
--

LOCK TABLES `engine_mutex` WRITE;
/*!40000 ALTER TABLE `engine_mutex` DISABLE KEYS */;
/*!40000 ALTER TABLE `engine_mutex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engine_persistent`
--

DROP TABLE IF EXISTS `engine_persistent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `engine_persistent` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) NOT NULL DEFAULT '',
  `IVALUE` int(11) DEFAULT NULL,
  `TVALUE` varchar(255) DEFAULT NULL,
  UNIQUE KEY `NAME` (`NAME`),
  KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engine_persistent`
--

LOCK TABLES `engine_persistent` WRITE;
/*!40000 ALTER TABLE `engine_persistent` DISABLE KEYS */;
INSERT INTO `engine_persistent` VALUES (2,'INVENTORY_CACHE_CLEAN_DATE',1255610513,NULL);
/*!40000 ALTER TABLE `engine_persistent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `files` (
  `NAME` varchar(255) NOT NULL,
  `VERSION` varchar(255) NOT NULL,
  `OS` varchar(255) NOT NULL,
  `CONTENT` longblob NOT NULL,
  PRIMARY KEY (`NAME`,`OS`,`VERSION`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `HARDWARE_ID` int(11) NOT NULL DEFAULT '0',
  `REQUEST` longtext,
  `CREATE_TIME` int(11) NOT NULL DEFAULT '0',
  `REVALIDATE_FROM` int(11) NOT NULL DEFAULT '0',
  `XMLDEF` longtext,
  PRIMARY KEY (`HARDWARE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups_cache`
--

DROP TABLE IF EXISTS `groups_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups_cache` (
  `HARDWARE_ID` int(11) NOT NULL DEFAULT '0',
  `GROUP_ID` int(11) NOT NULL DEFAULT '0',
  `STATIC` int(11) DEFAULT '0',
  PRIMARY KEY (`HARDWARE_ID`,`GROUP_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups_cache`
--

LOCK TABLES `groups_cache` WRITE;
/*!40000 ALTER TABLE `groups_cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `groups_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hardware`
--

DROP TABLE IF EXISTS `hardware`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hardware` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICEID` varchar(255) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `WORKGROUP` varchar(255) DEFAULT NULL,
  `USERDOMAIN` varchar(255) DEFAULT NULL,
  `OSNAME` varchar(255) DEFAULT NULL,
  `OSVERSION` varchar(255) DEFAULT NULL,
  `OSCOMMENTS` varchar(255) DEFAULT NULL,
  `PROCESSORT` varchar(255) DEFAULT NULL,
  `PROCESSORS` int(11) DEFAULT '0',
  `PROCESSORN` smallint(6) DEFAULT NULL,
  `MEMORY` int(11) DEFAULT NULL,
  `SWAP` int(11) DEFAULT NULL,
  `IPADDR` varchar(255) DEFAULT NULL,
  `ETIME` datetime DEFAULT NULL,
  `LASTDATE` datetime DEFAULT NULL,
  `LASTCOME` datetime DEFAULT NULL,
  `QUALITY` decimal(7,4) DEFAULT NULL,
  `FIDELITY` bigint(20) DEFAULT '1',
  `USERID` varchar(255) DEFAULT NULL,
  `TYPE` int(11) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `WINCOMPANY` varchar(255) DEFAULT NULL,
  `WINOWNER` varchar(255) DEFAULT NULL,
  `WINPRODID` varchar(255) DEFAULT NULL,
  `WINPRODKEY` varchar(255) DEFAULT NULL,
  `USERAGENT` varchar(50) DEFAULT NULL,
  `CHECKSUM` int(11) DEFAULT '131071',
  `SSTATE` int(11) DEFAULT '0',
  `DNS` varchar(255) DEFAULT NULL,
  `DEFAULTGATEWAY` varchar(255) DEFAULT NULL,
  `UUID` varchar(255) DEFAULT NULL,
  `IPSRC` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`DEVICEID`,`ID`),
  KEY `NAME` (`NAME`),
  KEY `CHECKSUM` (`CHECKSUM`),
  KEY `USERID` (`USERID`),
  KEY `WORKGROUP` (`WORKGROUP`),
  KEY `OSNAME` (`OSNAME`),
  KEY `MEMORY` (`MEMORY`),
  KEY `DEVICEID` (`DEVICEID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hardware`
--

LOCK TABLES `hardware` WRITE;
/*!40000 ALTER TABLE `hardware` DISABLE KEYS */;
/*!40000 ALTER TABLE `hardware` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hardware_osname_cache`
--

DROP TABLE IF EXISTS `hardware_osname_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hardware_osname_cache` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OSNAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `OSNAME` (`OSNAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hardware_osname_cache`
--

LOCK TABLES `hardware_osname_cache` WRITE;
/*!40000 ALTER TABLE `hardware_osname_cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `hardware_osname_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inputs`
--

DROP TABLE IF EXISTS `inputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inputs` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `MANUFACTURER` varchar(255) DEFAULT NULL,
  `CAPTION` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `INTERFACE` varchar(255) DEFAULT NULL,
  `POINTTYPE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inputs`
--

LOCK TABLES `inputs` WRITE;
/*!40000 ALTER TABLE `inputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `inputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itmgmt_comments`
--

DROP TABLE IF EXISTS `itmgmt_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itmgmt_comments` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `COMMENTS` longtext COLLATE utf8_unicode_ci,
  `USER_INSERT` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DATE_INSERT` date DEFAULT NULL,
  `ACTION` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VISIBLE` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itmgmt_comments`
--

LOCK TABLES `itmgmt_comments` WRITE;
/*!40000 ALTER TABLE `itmgmt_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `itmgmt_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `javainfo`
--

DROP TABLE IF EXISTS `javainfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `javainfo` (
  `HARDWARE_ID` int(11) NOT NULL,
  `JAVANAME` varchar(255) COLLATE utf8_unicode_ci DEFAULT 'NONAME',
  `JAVAPATHLEVEL` int(11) DEFAULT '0',
  `JAVACOUNTRY` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `JAVACLASSPATH` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `JAVAHOME` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `javainfo`
--

LOCK TABLES `javainfo` WRITE;
/*!40000 ALTER TABLE `javainfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `javainfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locks`
--

DROP TABLE IF EXISTS `locks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locks` (
  `HARDWARE_ID` int(11) NOT NULL,
  `ID` int(11) DEFAULT NULL,
  `SINCE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`HARDWARE_ID`),
  KEY `SINCE` (`SINCE`)
) ENGINE=MEMORY DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locks`
--

LOCK TABLES `locks` WRITE;
/*!40000 ALTER TABLE `locks` DISABLE KEYS */;
/*!40000 ALTER TABLE `locks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memories`
--

DROP TABLE IF EXISTS `memories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `memories` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `CAPTION` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `CAPACITY` varchar(255) DEFAULT NULL,
  `PURPOSE` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `SPEED` varchar(255) DEFAULT NULL,
  `NUMSLOTS` smallint(6) DEFAULT NULL,
  `SERIALNUMBER` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memories`
--

LOCK TABLES `memories` WRITE;
/*!40000 ALTER TABLE `memories` DISABLE KEYS */;
/*!40000 ALTER TABLE `memories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modems`
--

DROP TABLE IF EXISTS `modems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `modems` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `MODEL` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modems`
--

LOCK TABLES `modems` WRITE;
/*!40000 ALTER TABLE `modems` DISABLE KEYS */;
/*!40000 ALTER TABLE `modems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitors`
--

DROP TABLE IF EXISTS `monitors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitors` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `MANUFACTURER` varchar(255) DEFAULT NULL,
  `CAPTION` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `SERIAL` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitors`
--

LOCK TABLES `monitors` WRITE;
/*!40000 ALTER TABLE `monitors` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `netmap`
--

DROP TABLE IF EXISTS `netmap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `netmap` (
  `IP` varchar(15) NOT NULL,
  `MAC` varchar(17) NOT NULL,
  `MASK` varchar(15) NOT NULL,
  `NETID` varchar(15) NOT NULL,
  `DATE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MAC`),
  KEY `IP` (`IP`),
  KEY `NETID` (`NETID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `netmap`
--

LOCK TABLES `netmap` WRITE;
/*!40000 ALTER TABLE `netmap` DISABLE KEYS */;
/*!40000 ALTER TABLE `netmap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_devices`
--

DROP TABLE IF EXISTS `network_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `network_devices` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `MACADDR` varchar(255) DEFAULT NULL,
  `USER` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `MACADDR` (`MACADDR`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_devices`
--

LOCK TABLES `network_devices` WRITE;
/*!40000 ALTER TABLE `network_devices` DISABLE KEYS */;
/*!40000 ALTER TABLE `network_devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `networks`
--

DROP TABLE IF EXISTS `networks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `networks` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `TYPEMIB` varchar(255) DEFAULT NULL,
  `SPEED` varchar(255) DEFAULT NULL,
  `MACADDR` varchar(255) DEFAULT NULL,
  `STATUS` varchar(255) DEFAULT NULL,
  `IPADDRESS` varchar(255) DEFAULT NULL,
  `IPMASK` varchar(255) DEFAULT NULL,
  `IPGATEWAY` varchar(255) DEFAULT NULL,
  `IPSUBNET` varchar(255) DEFAULT NULL,
  `IPDHCP` varchar(255) DEFAULT NULL,
  `VIRTUALDEV` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `MACADDR` (`MACADDR`),
  KEY `IPADDRESS` (`IPADDRESS`),
  KEY `IPGATEWAY` (`IPGATEWAY`),
  KEY `IPSUBNET` (`IPSUBNET`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `networks`
--

LOCK TABLES `networks` WRITE;
/*!40000 ALTER TABLE `networks` DISABLE KEYS */;
/*!40000 ALTER TABLE `networks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operators`
--

DROP TABLE IF EXISTS `operators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operators` (
  `ID` varchar(255) NOT NULL DEFAULT '',
  `FIRSTNAME` varchar(255) DEFAULT NULL,
  `LASTNAME` varchar(255) DEFAULT NULL,
  `PASSWD` varchar(50) DEFAULT NULL,
  `ACCESSLVL` int(11) DEFAULT NULL,
  `COMMENTS` text,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operators`
--

LOCK TABLES `operators` WRITE;
/*!40000 ALTER TABLE `operators` DISABLE KEYS */;
INSERT INTO `operators` VALUES ('admin','admin','admin','admin',1,'Default administrator account');
/*!40000 ALTER TABLE `operators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ports`
--

DROP TABLE IF EXISTS `ports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ports` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `CAPTION` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ports`
--

LOCK TABLES `ports` WRITE;
/*!40000 ALTER TABLE `ports` DISABLE KEYS */;
/*!40000 ALTER TABLE `ports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `printers`
--

DROP TABLE IF EXISTS `printers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `printers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `DRIVER` varchar(255) DEFAULT NULL,
  `PORT` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `printers`
--

LOCK TABLES `printers` WRITE;
/*!40000 ALTER TABLE `printers` DISABLE KEYS */;
/*!40000 ALTER TABLE `printers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prolog_conntrack`
--

DROP TABLE IF EXISTS `prolog_conntrack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prolog_conntrack` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICEID` varchar(255) DEFAULT NULL,
  `TIMESTAMP` int(11) DEFAULT NULL,
  `PID` int(11) DEFAULT NULL,
  KEY `ID` (`ID`),
  KEY `DEVICEID` (`DEVICEID`)
) ENGINE=MEMORY DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prolog_conntrack`
--

LOCK TABLES `prolog_conntrack` WRITE;
/*!40000 ALTER TABLE `prolog_conntrack` DISABLE KEYS */;
/*!40000 ALTER TABLE `prolog_conntrack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regconfig`
--

DROP TABLE IF EXISTS `regconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regconfig` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) DEFAULT NULL,
  `REGTREE` int(11) DEFAULT NULL,
  `REGKEY` text,
  `REGVALUE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `NAME` (`NAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regconfig`
--

LOCK TABLES `regconfig` WRITE;
/*!40000 ALTER TABLE `regconfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `regconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registry`
--

DROP TABLE IF EXISTS `registry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registry` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `REGVALUE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `NAME` (`NAME`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registry`
--

LOCK TABLES `registry` WRITE;
/*!40000 ALTER TABLE `registry` DISABLE KEYS */;
/*!40000 ALTER TABLE `registry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registry_name_cache`
--

DROP TABLE IF EXISTS `registry_name_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registry_name_cache` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `NAME` (`NAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registry_name_cache`
--

LOCK TABLES `registry_name_cache` WRITE;
/*!40000 ALTER TABLE `registry_name_cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `registry_name_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registry_regvalue_cache`
--

DROP TABLE IF EXISTS `registry_regvalue_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registry_regvalue_cache` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `REGVALUE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `REGVALUE` (`REGVALUE`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registry_regvalue_cache`
--

LOCK TABLES `registry_regvalue_cache` WRITE;
/*!40000 ALTER TABLE `registry_regvalue_cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `registry_regvalue_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slots`
--

DROP TABLE IF EXISTS `slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slots` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `DESIGNATION` varchar(255) DEFAULT NULL,
  `PURPOSE` varchar(255) DEFAULT NULL,
  `STATUS` varchar(255) DEFAULT NULL,
  `PSHARE` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slots`
--

LOCK TABLES `slots` WRITE;
/*!40000 ALTER TABLE `slots` DISABLE KEYS */;
/*!40000 ALTER TABLE `slots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `softwares`
--

DROP TABLE IF EXISTS `softwares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `softwares` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `PUBLISHER` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `VERSION` varchar(255) DEFAULT NULL,
  `FOLDER` text,
  `COMMENTS` text,
  `FILENAME` varchar(255) DEFAULT NULL,
  `FILESIZE` int(11) DEFAULT '0',
  `SOURCE` int(11) DEFAULT NULL,
  `FROM` varchar(64) NOT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `NAME` (`NAME`),
  KEY `VERSION` (`VERSION`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `softwares`
--

LOCK TABLES `softwares` WRITE;
/*!40000 ALTER TABLE `softwares` DISABLE KEYS */;
/*!40000 ALTER TABLE `softwares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `softwares_name_cache`
--

DROP TABLE IF EXISTS `softwares_name_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `softwares_name_cache` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `NAME` (`NAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `softwares_name_cache`
--

LOCK TABLES `softwares_name_cache` WRITE;
/*!40000 ALTER TABLE `softwares_name_cache` DISABLE KEYS */;
/*!40000 ALTER TABLE `softwares_name_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sounds`
--

DROP TABLE IF EXISTS `sounds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sounds` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `MANUFACTURER` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sounds`
--

LOCK TABLES `sounds` WRITE;
/*!40000 ALTER TABLE `sounds` DISABLE KEYS */;
/*!40000 ALTER TABLE `sounds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storages`
--

DROP TABLE IF EXISTS `storages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storages` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `MANUFACTURER` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `MODEL` varchar(255) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `TYPE` varchar(255) DEFAULT NULL,
  `DISKSIZE` int(11) DEFAULT NULL,
  `SERIALNUMBER` varchar(255) DEFAULT NULL,
  `FIRMWARE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storages`
--

LOCK TABLES `storages` WRITE;
/*!40000 ALTER TABLE `storages` DISABLE KEYS */;
/*!40000 ALTER TABLE `storages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subnet`
--

DROP TABLE IF EXISTS `subnet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subnet` (
  `NETID` varchar(15) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `ID` int(11) DEFAULT NULL,
  `MASK` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`NETID`),
  KEY `ID` (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subnet`
--

LOCK TABLES `subnet` WRITE;
/*!40000 ALTER TABLE `subnet` DISABLE KEYS */;
/*!40000 ALTER TABLE `subnet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `Tag` varchar(255) NOT NULL DEFAULT '',
  `Login` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`Tag`,`Login`),
  KEY `Tag` (`Tag`),
  KEY `Login` (`Login`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `videos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `CHIPSET` varchar(255) DEFAULT NULL,
  `MEMORY` varchar(255) DEFAULT NULL,
  `RESOLUTION` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`HARDWARE_ID`,`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos`
--

LOCK TABLES `videos` WRITE;
/*!40000 ALTER TABLE `videos` DISABLE KEYS */;
/*!40000 ALTER TABLE `videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `virtualmachines`
--

DROP TABLE IF EXISTS `virtualmachines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `virtualmachines` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `HARDWARE_ID` int(11) NOT NULL,
  `NAME` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `STATUS` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `SUBSYSTEM` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VMTYPE` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `UUID` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VCPU` int(11) DEFAULT NULL,
  `MEMORY` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`,`HARDWARE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `virtualmachines`
--

LOCK TABLES `virtualmachines` WRITE;
/*!40000 ALTER TABLE `virtualmachines` DISABLE KEYS */;
/*!40000 ALTER TABLE `virtualmachines` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-08-07 12:57:57
