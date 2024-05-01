CREATE DATABASE kdramaDB;

USE kdramaDB;

-- create table with kdrama info
CREATE TABLE kdramaData (
	id INT AUTO_INCREMENT PRIMARY KEY,
	kdramaName VARCHAR(255) NOT NULL,
	yearOfRelease INT NOT NULL,
    airedDate VARCHAR(100),
    airedOn VARCHAR(80),
    numOfEpisode INT,
    network VARCHAR(50),
    duration INT,
	contentRating VARCHAR(100),
    synopsis VARCHAR(800),
    cast VARCHAR(500),
    genre VARCHAR(80),
    tags VARCHAR(255),
    ranks VARCHAR(50),
    rating DECIMAL(3, 1)
);
-- load data into kdrama table
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\kdrama.csv'
INTO TABLE kdramaData
CHARACTER SET utf8
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(kdramaName, yearOfRelease, airedDate, airedOn, numOfEpisode, network, duration, contentRating, synopsis, cast, genre, tags, ranks, rating);

SELECT * FROM kdramadata;

-- cleaning data
ALTER TABLE kdramadata DROP COLUMN ranks;




