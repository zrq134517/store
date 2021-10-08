`user`/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `account` VARCHAR(50) DEFAULT NULL,
  `username` VARCHAR(50) DEFAULT NULL,
  `password` VARCHAR(50) DEFAULT NULL,
  `country` VARCHAR(50) DEFAULT NULL,
  `province` VARCHAR(50) DEFAULT NULL,
  `street` VARCHAR(50) DEFAULT NULL,
  `door` VARCHAR(50) DEFAULT NULL,
  `money` INT(11) DEFAULT NULL,
  `bank_name` VARCHAR(50) DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

INSERT  INTO `user`(`account`,`username`,`password`,`country`,`province`,`street`,`door`,`money`,`bank_name`) VALUES ('10000000','贾生','123422','美国','纽约','S002','S0002',9600,'法国大众银行'),('39148269','5','5','5','5','5','5',999,'汉科软地球中国区老牛湾分行'),('69692150','zrq','123456','1','1','1','1',879700,'汉科软地球中国区老牛湾分行'),('66185949','q','123456','2','2','2','',4000,'汉科软地球中国区老牛湾分行'),('60447385','aaa','123','a','a','a','a',0,'汉科软地球中国区老牛湾分行'),('12918341','v','123','v','v','v','v',-500,'汉科软地球中国区老牛湾分行'),('47495622','e','123','e','e','e','e',44500,'汉科软地球中国区老牛湾分行'),('42895060','r','123','r','r','r','r',500,'汉科软地球中国区老牛湾分行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
