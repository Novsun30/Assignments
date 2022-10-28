-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cat`
--

DROP TABLE IF EXISTS `cat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cat` (
  `Cat` varchar(666) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat`
--

LOCK TABLES `cat` WRITE;
/*!40000 ALTER TABLE `cat` DISABLE KEYS */;
INSERT INTO `cat` VALUES ('____¶_____ねこ__貓_________¶\n____¶___¶__________________¶___¶\n__¶______¶_______________¶______¶\n_¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111¶\n¶_________________________________¶\n¶_________¶_____________¶_________¶\n¶_________________________________¶\n¶_______=________¶_________=______¶\n_¶________________________________¶\n__¶____________|WWWW|____________¶\n___¶____________\\AA/____________¶');
/*!40000 ALTER TABLE `cat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',0,'2022-10-17 22:09:40'),(2,'Mike Portnoy','DreamTheater1985','DanceOfEternity',374,'2022-10-17 22:10:01'),(3,'Kurt Cobain','Nirvana1987','ComeAsYouAre',2607,'2022-10-17 22:10:10'),(4,'Tatiana Shmailyuk','Jinjer2008','ISpeakAstronomy',51,'2022-10-17 22:10:18'),(5,'Till Lindemann','Rammstein1994','DuHast',867,'2022-10-17 22:10:25'),(6,'Tim Lambesis','AsILayDying2000','MyOwnGrave',197,'2022-10-18 19:05:59'),(7,'Corey Taylor','Slipknot1995','Psychosocial',1807,'2022-10-18 19:07:16'),(8,'Tim Henson','Polyphia2010','GOAT',94,'2022-10-18 19:08:12'),(9,'Steve Vai','SteveVai19600606','TenderSurrender',265,'2022-10-18 19:08:37');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,3,'It\'s better to burn out than to fade away',2411,'2022-10-19 17:19:33'),(2,8,'Check our new song \'Ego Death\' feat with @Steve_Vai, https://www.youtube.com/watch?v=1JNmz17gnMw',88,'2022-10-19 17:27:52'),(3,9,'I so much enjoyed being invited to lay down some shapes on the new @Polyphia track \'Ego Death\'',248,'2022-10-19 17:52:22'),(4,7,'\'THE END, SO FAR\', New Album Out Now, Get it here : slipknot1.lnk.to/TheEndSoFar',1663,'2022-10-19 18:11:57'),(5,4,'@Bloodstock_Festival 2022 was a real thing! We are proud to be a part of this legend \\m/',46,'2022-10-19 18:19:24'),(6,6,'Last show of the year tonight! Then I\'m heading home to work on new songs. It\'s been an incredible summer!',159,'2022-10-19 18:31:50'),(7,2,'Rehearsals with @John_Petrucci & @Dave_LaRue are going great so far!! Check out our evolution from G3 2001 to G3 2005 to G3 2007 and now preparing for JP\'s 1st solo tour in 2022!! ',269,'2022-10-19 18:33:08'),(8,8,'Join us on Instagram Live tomorrow with @Steve_Vai at 3pm CST',91,'2022-10-19 18:34:29'),(9,5,'Two fiery nights in Los Angeles to say: Danke, Adieu, auf Wiedersehen, USA!',832,'2022-10-19 18:36:33'),(10,9,'Thanks to Tim & Scottie from @Polyphia for joining us on stage last night in Dallas!',266,'2022-10-19 18:39:05'),(11,5,'Uno, dos, tres unforgettable nights of fire, fun and feelings in Foro Sol - a fitting finale for the North America Stadium Tour 2022! ¡Gracias México! ⚡⚡',866,'2022-10-19 18:40:00'),(12,1,'\n______¶_____ねこ__貓_________¶\n____¶___¶__________________¶___¶\n__¶______¶_______________¶______¶\n_¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111¶\n¶_________________________________¶\n¶_________¶_____________¶_________¶\n¶_________________________________¶',0,'2022-10-20 03:59:42');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-20  5:28:25
