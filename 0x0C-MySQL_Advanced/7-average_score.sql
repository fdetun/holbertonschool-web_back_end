-- tasks mysql advanced
-- email validation
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER !F>
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections COr WHERE COr.user_id=user_id);
END !F>
DELIMITER ;
