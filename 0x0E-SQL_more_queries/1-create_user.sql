-- 1. Root user
-- A script that creates the MySQL server user

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * 'user_0d1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
