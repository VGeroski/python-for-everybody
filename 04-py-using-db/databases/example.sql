CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Isa', 13);
INSERT INTO Ages (name, age) VALUES ('Otto', 25);
INSERT INTO Ages (name, age) VALUES ('Naila', 34);
INSERT INTO Ages (name, age) VALUES ('Lucien', 25);
INSERT INTO Ages (name, age) VALUES ('Windsor', 20);
INSERT INTO Ages (name, age) VALUES ('Breanna', 38);

SELECT hex(name || age) AS X FROM Ages ORDER BY X