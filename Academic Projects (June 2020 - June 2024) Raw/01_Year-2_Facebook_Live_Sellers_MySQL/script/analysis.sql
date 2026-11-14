-- Reconstructed from the questions described in the original report.
-- Import dataset/live2.csv as a MySQL table named live2 first.
SELECT status_type, COUNT(*) AS posts, ROUND(AVG(num_likes), 4) AS avg_likes,
       SUM(num_shares) AS total_shares
FROM live2 GROUP BY status_type ORDER BY total_shares DESC;

SELECT MAX(num_reactions) AS max_photo_reactions
FROM live2 WHERE status_type = 'photo';

SELECT MAX(num_comments) AS max_video_comments
FROM live2 WHERE status_type = 'video';

SELECT DISTINCT status_type FROM live2 ORDER BY status_type;

SELECT status_id, num_shares FROM live2
WHERE num_shares > (SELECT AVG(num_shares) FROM live2)
ORDER BY num_shares DESC LIMIT 10;
