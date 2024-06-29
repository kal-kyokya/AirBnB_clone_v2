-- Script preparing a MSQL server for the project

-- Command Creating the Database
CREATE DATABASE
IF NOT EXISTS `hbnb_dev_db`;

-- Command Creating a User
CREATE USER
IF NOT EXISTS `hbnb_dev`@`localhost`
IDENTIFIED BY 'hbnb_dev_pwd';

-- Command Setting one particular Database as 'in use'
USE `hbnb_dev_db`;

-- Command granting All Privileges to user
GRANT ALL PRIVILEGES
ON `hbnb_dev_db`
TO `hbnb_dev`@`localhost`;

-- Command Setting another databse in Use
USE `performance_schema`;

-- Command granting particular privilege to User
GRANT SELECT
ON `performance_schema`.*
TO `hbnb_dev`@`localhost`;
