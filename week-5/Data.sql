-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',10,'2022-01-26 09:51:42'),(2,'majiko','oiol1122','ogkbor5',54213,'2022-01-26 10:39:17'),(3,'likinpark','ckao562','asoqq99326q',545641,'2022-01-26 10:39:21'),(4,'ivy','wulia39873','446as8787',4541,'2022-01-26 10:39:23'),(5,'jason','sarrowq997','asdi663',65432,'2022-01-26 10:39:25'),(6,'rookie','ppaink4696','7q5s5445s',230545,'2022-01-26 10:39:28');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,2,'majikoです，my new song:https://www.youtube.com/watch?v=9XEkn3Xhy6Y ','2022-01-27 13:25:49'),(2,3,'hello,my song update:https://www.youtube.com/watch?v=eVTXPUF4Oz4&list=OLAK5uy_l7UpnO_79mPipz84ZO6Pt7v6VZEj1bQoU&index=1','2022-01-27 13:30:22'),(3,1,'管理員測試','2022-01-27 13:32:20'),(4,5,'hi i\'m Jason Mraz, u must listen:https://www.youtube.com/watch?v=EkHTsc9PU2A','2022-01-27 14:01:29'),(5,6,'hi everyone ,i\'m lpl king of mid player,my top play:https://www.youtube.com/watch?v=sPJreC2ramE&t=166s','2022-01-27 14:03:35');
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

-- Dump completed on 2022-01-28  0:45:39
