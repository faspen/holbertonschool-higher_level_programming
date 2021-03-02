-- List all records of second_table
SELECT score, name FROM second_table WHERE name != NULL OR name != '' ORDER BY score DESC;
