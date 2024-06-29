-- Script Creating test Database for project

-- Command Creating the test Database
CREATE DATABASE
IF NOT EXISTS `hbnb_test_db`;

-- Command Creating a test User
CREATE USER
IF NOT EXISTS `hbnb_test`@`localhost`
IDENTIFIED BY 'hbnb_test_pwd';

-- Command granting All Privileges to test User
GRANT ALL PRIVILEGES
ON `hbnb_test_db`.*
TO `hbnb_test`@`localhost`;

-- Command granting Specific Privilege to test User
GRANT SELECT
ON `performance_schema`.*
TO `hbnb_test`@`localhost`;
