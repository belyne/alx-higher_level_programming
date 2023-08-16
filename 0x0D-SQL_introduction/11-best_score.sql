-- Task 11: Select the best
-- Author: Belyne
-- Date: Current time

-- List records with score >= 10 from "second_table" ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
