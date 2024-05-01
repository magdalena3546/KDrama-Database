-- average rating of kdramas in db
SELECT 
	AVG(rating) AS averageRating
FROM kdramadata;

-- average duration 
SELECT 
	AVG(duration) AS averageDuration
FROM kdramadata;

-- Analysis of the influence of airing date on ratings
SELECT 
	airedOn,
    AVG(rating) as averageRating
FROM kdramadata
GROUP BY airedOn
ORDER BY averageRating DESC;

-- Analysis of the influence of network on ratings
SELECT 
	network,
    AVG(rating) as averageRating
FROM kdramadata
GROUP BY network
ORDER BY averageRating DESC;

-- Analysis of the influence of duration on ratings
SELECT
	duration, 
	AVG(rating) as averageRating
FROM kdramadata
GROUP BY duration
ORDER BY duration DESC;
	
-- Analysis of the influence of the number of episodes on ratings
SELECT
	numOfEpisode, 
	AVG(rating) as averageRating
FROM kdramadata
GROUP BY numOfEpisode
ORDER BY averageRating DESC;

-- The most popular actor
SELECT actor, COUNT(*) AS apperances
FROM (
SELECT 
	TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(cast, ',', n.digit + 1), ',', -1)) AS actor
FROM kdramadata
JOIN (
	SELECT 0 AS digit UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9
    ) AS n 
    ON LENGTH(REPLACE(cast, ',', '')) <= LENGTH(cast) - n.digit
) AS castTable
GROUP BY actor
ORDER BY apperances DESC;



