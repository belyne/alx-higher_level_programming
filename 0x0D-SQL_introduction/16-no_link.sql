-- Task 16: Say my name
-- Author: Belyne
-- Date: Current date

-- List records from "second_table" with a name value, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
