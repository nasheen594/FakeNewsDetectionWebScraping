CREATE DATABASE  IF NOT EXISTS `detector` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `detector`;
-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: detector
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `query`
--

DROP TABLE IF EXISTS `query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `query` (
  `query_id` int NOT NULL AUTO_INCREMENT,
  `source` varchar(200) DEFAULT NULL,
  `text` varchar(500) NOT NULL,
  `appearance_link_id` varchar(45) DEFAULT NULL,
  `appearance_score` varchar(45) DEFAULT NULL,
  `cosinesim_link_id` varchar(45) DEFAULT NULL,
  `cosinesim_score` varchar(45) DEFAULT NULL,
  `matching_link_id` varchar(45) DEFAULT NULL,
  `matching_score` varchar(45) DEFAULT NULL,
  `matched` varchar(45) DEFAULT 'N',
  `social_media_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`query_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `query`
--

LOCK TABLES `query` WRITE;
/*!40000 ALTER TABLE `query` DISABLE KEYS */;
INSERT INTO `query` VALUES (1,'1','Everyone I know who had covid including myself had mild runny nose and a slight head ache for maybe a few hours  Everyone I know who got the shots had extreme chills  foggy thinking  severe headache and nausea for 2 straight days  Way WAY worse than a little runny nose','178','0.6451612903225806','189','0.10887700977722743','392','0.11858075235613148','N',NULL),(2,'1',' I ve felt sick all day its so horrible   I have   Sneezing   Coughing  Shortness of breath   Walking problems   Cold as hail  Minor throat pain  Minor headaches  Random body aches  And I ve been in contact with covid at school 5 days in a row','88','0.52','246','0.18706723832239489','246','0.23590338769847763','N',NULL),(3,'1','Florida leads all 50 states in the number of hospitalizations and deaths per capita  How Florida s massive COVID-19 spike got so bad -that s why He has failed Florida','242','0.8333333333333334','362','0.242864803309882','255','0.27694213342363316','N',NULL),(4,'1','Covid and 5G are absolutely linked  You wont change my mind','23','0.5714285714285714','302','0.0878658264503935','132','0.040683019126581434','N',NULL),(5,'1','Actor Mike Mitchell Dies of Heart Attack 7 Days After 3rd Pfizer COVID Vaccine Booster','91','0.5833333333333334','91','0.10159888308897252','192','0.13245881070552173','N',NULL),(6,'1','Republican Florida Gov  Ron DeSantis has resisted mandatory mask mandates and vaccine requirements  and along with the state Legislature  has limited local officials  ability to impose restrictions meant to stop the spread of COVID-19   ','362','1.0','362','0.23749285265534392','362','0.21869023638999616','N',NULL),(7,NULL,'Everyone knows by now that  PCR tests are fake  so are these numbers  I live in  FL and I know NO ONE with  covid   no one    CDC  Florida breaks record with more than 21 000 new COVID cases   PCRGATE  covidhoax   ','41','0.6666666666666666','219','0.18503233088317333','219','0.2645517699895167','N',NULL),(8,NULL,'One healthy doctor died after getting the Covid-19 vaccine and one woman was completely paralyzed after getting the Covid-19 vaccine  no mask for me  no vaccines for me ','267','0.9444444444444444','70','0.22078989806550903','437','0.31172070746458774','N',NULL),(9,NULL,'Ask the newly infected COVID patients if they have been in the forest  the park or garden  I bet they all have in common mosquito bites  They transmit it  Then you have either migrants with foreign DNA - Africans and AIDS AND  OR the virus is man made with Mosquitos as carriers ','11','0.3333333333333333','313','0.2850921746143676','313','0.43533797469788005','N',NULL),(10,NULL,'The new guidance follows recent decisions in Los Angeles and St  Louis to revert to indoor mask mandates amid a spike in COVID-19 cases and hospitalizations   ','40','0.8421052631578947','40','0.24733234458825643','279','0.19462734658267353','N',NULL);
/*!40000 ALTER TABLE `query` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-18 17:50:39
