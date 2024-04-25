-- creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus (
	IN user_id int, IN project_name varchar(255), IN score int)
BEGIN
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id,
		IFNULL (SELECT project_id FROM projects WHERE name = project_name;,
			INSERT INTO projects (name) VALUES (project_name);
			SELECT project_id FROM projects WHERE name = project_name;),
		score)
END //

DELIMITER ;
