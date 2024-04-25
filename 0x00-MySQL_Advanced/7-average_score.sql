--  stored procedure ComputeAverageScoreForUser that computes and store the average score

DELMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	INSERT INTO users (average_score) VALUES (
		SELECT AVG(score) FROM corrections WHERE user_id = user_id)
	WHERE id = user_id;
END //
DELIMITER ;
