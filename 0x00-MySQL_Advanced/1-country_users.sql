-- create users table
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL AUTO_INCREMENT,
	email varchar(255),
	name varchar(255),
	country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	UNIQUE(email),
	PRIMARY KEY(id)
);
