-- Script that creates the table force_name on MySQL server.
-- The database name will be passed as an argument of the MySQL command
-- If the thable force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS `force_name` (id INT, name VARCHAR(256) NOT NULL);
