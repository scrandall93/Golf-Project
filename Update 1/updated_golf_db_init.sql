create database golf;
USE golf;

-- drop database user if exists 
DROP USER IF EXISTS 'sam1'@'localhost';

-- create sam1 and granting privileges to the golf database 
CREATE USER 'sam1'@'localhost' IDENTIFIED WITH mysql_native_password BY '________';

-- grant all privileges to the `golf` database to user sam1 on localhost 
GRANT ALL PRIVILEGES ON `golf`.* TO 'sam1'@'localhost';

-- drop tables
DROP TABLE IF EXISTS Golfers;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Clubs;
DROP TABLE IF EXISTS Scores;
DROP TABLE IF EXISTS CourseRatings;

-- create tables
CREATE TABLE `Golfers` (
	`golfer_id` INT NOT NULL DEFAULT 0,
	`golfer_name` VARCHAR(50) NOT NULL,
	`golfer_age` INT NOT NULL,
	`club_id` INT NOT NULL,
	PRIMARY KEY (`golfer_id`)
);

CREATE TABLE `Scores` (
	`score_id` INT NOT NULL DEFAULT 0,
	`score_par` INT NOT NULL,
	`score_total` INT NOT NULL,
	`course_id` INT NOT NULL,
	`golfer_id` INT NOT NULL,
	`score_date` DATE NOT NULL,
    `holes_played` INT NOT NULL,
	PRIMARY KEY (`score_id`)
);

CREATE TABLE `Clubs` (
	`club_id` INT NOT NULL,
	`club_brand_name` VARCHAR(50) NOT NULL,
	`club_model_name` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`club_id`)
);

CREATE TABLE `Courses` (
	`course_id` INT NOT NULL,
	`course_name` VARCHAR(75) NOT NULL,
	`course_front_par` INT NOT NULL,
	`course_back_par` INT NOT NULL,
	PRIMARY KEY (`course_id`)
);

CREATE TABLE `CourseRatings` (
	`rating_id` INT NOT NULL,
	`course_id` INT NOT NULL,
	`rating_year` INT NOT NULL,
	`course_slope_rating` INT NOT NULL,
	`course_rating` INT NOT NULL,
	PRIMARY KEY (`rating_id`)
);

-- assign foreign keys

ALTER TABLE Scores
ADD CONSTRAINT FK_course_id
FOREIGN KEY (course_id) REFERENCES Courses(course_id);

ALTER TABLE Scores
ADD CONSTRAINT FK_golfer_id
FOREIGN KEY (golfer_id) REFERENCES Golfers(golfer_id);

ALTER TABLE Golfers
ADD CONSTRAINT FK_club_id
FOREIGN KEY (club_id) REFERENCES Clubs(club_id);

ALTER TABLE CourseRatings
ADD CONSTRAINT FK_course_id1
FOREIGN KEY (course_id) REFERENCES Courses(course_id);
