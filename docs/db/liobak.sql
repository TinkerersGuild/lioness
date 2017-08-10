-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: lioness
-- ------------------------------------------------------
-- Server version	5.5.54-0+deb8u1

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
-- Table structure for table `objecttypes`
--

DROP TABLE IF EXISTS `objecttypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objecttypes` (
  `typeID` int(11) NOT NULL AUTO_INCREMENT,
  `Type` varchar(255) NOT NULL,
  PRIMARY KEY (`typeID`),
  UNIQUE KEY `typeID` (`typeID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objecttypes`
--

LOCK TABLES `objecttypes` WRITE;
/*!40000 ALTER TABLE `objecttypes` DISABLE KEYS */;
/*!40000 ALTER TABLE `objecttypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurants` (
  `restaurantID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `description` text,
  `hours` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`restaurantID`),
  UNIQUE KEY `restaurantID` (`restaurantID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,'Safeway',NULL,NULL,NULL,NULL),(2,'Lucy\'s Dumplings',NULL,NULL,NULL,NULL),(3,'The Korean Place',NULL,NULL,NULL,NULL),(4,'Spud bar',NULL,NULL,NULL,NULL),(5,'Shuji Sushi',NULL,NULL,NULL,NULL),(6,'Kebabji',NULL,NULL,NULL,NULL),(7,'Rolls',NULL,NULL,NULL,NULL),(8,'Bay City Burrito',NULL,NULL,NULL,NULL),(9,'Samurai',NULL,NULL,NULL,NULL),(10,'Schnitz',NULL,NULL,NULL,NULL),(11,'Le Resistance',NULL,NULL,NULL,NULL),(12,'Subway',NULL,NULL,NULL,NULL),(13,'Beer Deluxe',NULL,NULL,NULL,NULL),(14,'The Hawthorn',NULL,NULL,NULL,NULL),(15,'The Nevermind',NULL,NULL,NULL,NULL),(16,'Santorini',NULL,NULL,NULL,NULL),(17,'Zen',NULL,NULL,NULL,NULL),(18,'Haddons',NULL,NULL,NULL,NULL),(19,'Pixel Alley',NULL,NULL,NULL,NULL),(20,'Grill\'d',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `reviewID` int(11) NOT NULL AUTO_INCREMENT,
  `reviewerID` int(11) NOT NULL,
  `reviewType` int(11) NOT NULL,
  `reviewedID` int(11) NOT NULL,
  `review` text,
  `rating` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`reviewID`),
  UNIQUE KEY `reviewID` (`reviewID`),
  KEY `reviewerID` (`reviewerID`),
  KEY `reviewType` (`reviewType`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`reviewerID`) REFERENCES `users` (`userID`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`reviewType`) REFERENCES `objecttypes` (`typeID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store` (
  `text` text NOT NULL,
  `tag` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES ('y','a','U189HEXD5'),('fish','generic','U189HEXD5'),('fish','cake','U189HEXD5'),('actually, blame','python','U189HEXD5'),('<http://fish.com>','interesting','U189HEXD5'),('http','generic','U189HEXD5'),('<http://fish>','generic','U189HEXD5'),('<https://fish.com> This is a link about','fish','U189HEXD5'),('<http://random.com>','generic','U189HEXD5'),('<http://somewhere.com>','generic','U189HEXD5'),('<http://xkcd.com> awesome','stuff!','U189HEXD5'),('<http://fish.com>','carp','U189HEXD5'),('<http://random.com>','and?','U189HEXD5'),('<https://www.hoversurf.com>','#shutUpAndTakeMyMoney','U189HEXD5'),('<http://inspirobot.me>','generic','U189G0UNB'),('<http://generated.inspirobot.me/049/aXm8734xjU.jpg>','generic','U18A0GF0D'),('<https://youtu.be/DeAw6aXHzcY>','generic','U189G0UNB'),('<http://imgur.com/Ku4iPBz>','generic','U189G0UNB'),('<https://buzzconf.io/call-for-presenters>','generic','U189HEXD5'),('<https://www.youtube.com/watch?v=a-FHY5FNsWc>','generic','U189HEXD5'),('<https://www.scientificamerican.com/article/china-shatters-ldquo-spooky-action-at-a-distance-rdquo-record-preps-for-quantum-internet/?WT.mc_id=SA_TW_SPC_NEWS&amp;sf88969013=1>','generic','U189HEXD5'),('<https://www.youtube.com/watch?v=vMTchVXedkk>','generic','U18HWJHK4'),('<https://www.swinburne.edu.au/current-students/manage-course/exams-results-assessment/results/grades/higher-education/> Anyone looked into what \"They do not apply to engineering degrees\" means under the *Honours categories*','section?','U28G7R9RB'),('<http://joanielemercier.com/no-logram/> The second best thing you can do with a room that\'s constantly lightly','raining','U4WRWC90C'),('<https://hobbyking.com/en_us/catalog/product/view/id/63725/s/skateboard-conversion-kit/> Kinda takes the fun out of','it.','U189HEXD5'),('<https://cloud.google.com/blog/big-data/2017/06/build-your-own-machine-learning-powered-robot-arm-using-tensorflow-and-google-cloud>','generic','U189HEXD5');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `userID` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'jai','botmaster',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-11 17:51:11
