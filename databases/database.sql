DROP TABLE IF EXISTS db_inventory;

CREATE TABLE db_inventory (
	id serial PRIMARY KEY,
	serial_number VARCHAR(20),
	quantity BIGINT NOT NULL DEFAULT 0,
	price BIGINT NOT NULL DEFAULT 0

);

INSERT INTO db_inventory ( serial_number, quantity, price)
	VALUES ('00001', '1', '111111'),
	('00002', '2', '222222'),
	('00003', '3', '333333'),
	('00004', '4', '444444'),
	('00005', '5', '555555');
