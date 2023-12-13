-- 7. Cities table
-- A script that creates a database and a table in it.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id),
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INOT NULL
    name VARCHAR(256) NOT NULL
);
