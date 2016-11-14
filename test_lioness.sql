CREATE DATABASE IF NOT EXISTS `testlioness`;
USE `testlioness`;

DROP TABLE IF EXISTS `reviews`;

DROP TABLE IF EXISTS `users`;

DROP TABLE IF EXISTS `objectTypes`;
DROP TABLE IF EXISTS `restaurants`;

CREATE TABLE IF NOT EXISTS `users`(
	`userID` INT NOT NULL UNIQUE AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`title` VARCHAR(255),
	`phone` BIGINT,
	`address` VARCHAR(255),
	PRIMARY KEY(`userID`)
);

CREATE TABLE IF NOT EXISTS `restaurants`(
	`restaurantID` INT NOT NULL UNIQUE AUTO_INCREMENT,
	`name` VARCHAR(255),
	`phone` BIGINT,
	`address` VARCHAR(255),
	`description` TEXT,
	`hours` VARCHAR(255),
	PRIMARY KEY(`restaurantID`)

);

CREATE TABLE IF NOT EXISTS `objecttypes`(
	`typeID` INT NOT NULL UNIQUE AUTO_INCREMENT,
	`Type` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`typeID`)
);

CREATE TABLE IF NOT EXISTS `reviews`(
	`reviewID` INT NOT NULL UNIQUE AUTO_INCREMENT,
	`reviewerID` INT NOT NULL,
	`reviewType` INT NOT NULL,
	`reviewedID` INT NOT NULL,
	`review` TEXT,
	`rating` SMALLINT,
	PRIMARY KEY(`reviewID`),
	CONSTRAINT FOREIGN KEY(`reviewerID`) REFERENCES `users`(`userID`),
	CONSTRAINT FOREIGN KEY(`reviewType`) REFERENCES `objecttypes`(`typeID`)
);

INSERT INTO `users`(`name`, `title`) VALUES('jai', 'botmaster');
INSERT INTO `restaurants`(`name`) VALUES('Safeway');
INSERT INTO `restaurants`(`name`) VALUES('Lucy\'s Dumplings');
INSERT INTO `restaurants`(`name`) VALUES('The Korean Place');
INSERT INTO `restaurants`(`name`) VALUES('Spud bar');
INSERT INTO `restaurants`(`name`) VALUES('Shuji Sushi');
INSERT INTO `restaurants`(`name`) VALUES('Kebabji');
INSERT INTO `restaurants`(`name`) VALUES('Rolls');
INSERT INTO `restaurants`(`name`) VALUES('Bay City Burrito');
INSERT INTO `restaurants`(`name`) VALUES('Samurai');
INSERT INTO `restaurants`(`name`) VALUES('Schnitz');
INSERT INTO `restaurants`(`name`) VALUES('Le Resistance');
INSERT INTO `restaurants`(`name`) VALUES('Subway');
INSERT INTO `restaurants`(`name`) VALUES('Beer Deluxe');
INSERT INTO `restaurants`(`name`) VALUES('The Hawthorn');
INSERT INTO `restaurants`(`name`) VALUES('The Nevermind');
INSERT INTO `restaurants`(`name`) VALUES('Santorini');
INSERT INTO `restaurants`(`name`) VALUES('Zen');
INSERT INTO `restaurants`(`name`) VALUES('Haddons');
