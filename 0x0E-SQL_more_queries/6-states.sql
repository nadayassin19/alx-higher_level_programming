-- 6. States table
-- A script that creates a database and a table in it.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    PRIMARY KEY (id),
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL 
);
