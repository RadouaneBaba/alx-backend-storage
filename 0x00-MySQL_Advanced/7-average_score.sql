--  stored procedure ComputeAverageScoreForUser that computes and store the average score

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id_param INT)
BEGIN
	UPDATE users 
	SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id_param)
	WHERE id = user_id_param;
END //
DELIMITER ;
