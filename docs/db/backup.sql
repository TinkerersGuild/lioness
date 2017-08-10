CREATE DATABASE IF NOT EXISTS `testlioness`;
USE `testlioness`;

/*DROP TABLE IF EXISTS `reviews`;
DROP TABLE IF EXISTS `restaurant_reviews`;

DROP TABLE IF EXISTS `restaurants`;

DROP TABLE IF EXISTS `users`;
*/

CREATE TABLE IF NOT EXISTS `users`(
	`user_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`title` VARCHAR(255),
	`botrank` TINYINT UNSIGNED NOT NULL DEFAULT 0,
	`phone` BIGINT,
	`address` VARCHAR(255),
	PRIMARY KEY(`user_id`)
);


CREATE TABLE IF NOT EXISTS `genres`(
	`genre_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`genre` VARCHAR(255) NOT NULL,
	`description` TEXT,
	PRIMARY KEY(`genre_id`)
);


CREATE TABLE IF NOT EXISTS `cuisines`(
	`cuisine_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`cuisine` VARCHAR(255) NOT NULL,
	`description` TEXT,
	PRIMARY KEY(`cuisine_id`)
);

CREATE TABLE IF NOT EXISTS `books`(
	`book_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`title` VARCHAR(255),
	`author` VARCHAR(255),
	`description` TEXT,
	`genre_id` INT UNSIGNED NOT NULL,
	PRIMARY KEY(`book_id`),
	CONSTRAINT FOREIGN KEY(`genre_id`) REFERENCES `genres`(`genre_id`)
);

CREATE TABLE IF NOT EXISTS `restaurants`(
	`restaurant_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`cuisine_id` INT UNSIGNED, 
	`name` VARCHAR(255),
	`phone` BIGINT,
	`address` VARCHAR(255),
	`description` TEXT,
	`hours` VARCHAR(255),
	PRIMARY KEY(`restaurant_id`),
	CONSTRAINT FOREIGN KEY(`cuisine_id`) REFERENCES `cuisines`(`cuisine_id`)
);

 
CREATE TABLE IF NOT EXISTS `restaurant_reviews`(
	`review_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`reviewer_id` INT UNSIGNED NOT NULL,
	`restaurant_id` INT UNSIGNED NOT NULL,
	`review` TEXT,
	`rating` SMALLINT,
	PRIMARY KEY(`review_id`),
	CONSTRAINT FOREIGN KEY(`reviewer_id`) REFERENCES `users`(`user_id`),
	CONSTRAINT FOREIGN KEY(`restaurant_id`) REFERENCES `restaurants`(`restaurant_id`)

);
CREATE TABLE IF NOT EXISTS `book_reviews`(
	`review_id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
	`reviewer_id` INT UNSIGNED NOT NULL,
	`book_id` INT UNSIGNED NOT NULL,
	`review` TEXT,
	`rating` SMALLINT,
	PRIMARY KEY(`review_id`),
	CONSTRAINT FOREIGN KEY(`reviewer_id`) REFERENCES `users`(`user_id`),
	CONSTRAINT FOREIGN KEY(`book_id`) REFERENCES `books`(`book_id`)

);


INSERT INTO `users`(`name`, `title`, `botrank`) VALUES('jai', 'botmaster', 255);
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
