-------
CREATING A NEW TABLE:
CREATE TABLE
INTEGER
VARCHAR


CREATE TABLE people (
  id INTEGER,
  name VARCHAR (255)
  );


--------
ADDING A QUERY INTO TABLE:
INSERT INTO
VALUES


INSERT INTO people (id, name) VALUES (2, 'Troy')


-------
RETREIVING RECORDS:
SELECT
FROM
WHERE
OR
AND
ORDER
DESC
ASC


SELECT first_name, last_name FROM people;

SELECT * FROM people
WHERE last_name = 'Doe'
OR last_name = 'Smith';

SELECT * FROM people
WHERE last_name = 'Doe'
AND last_name < 30;

SELECT * FROM people
WHERE age < 34
ORDER BY age DESC;

SELECT * FROM people
WHERE age < 34
ORDER BY first_name, last_name;


------
UPDATE AND DELETE RECORDS:
DELETE
UPDATE
SET


UPDATE test_table
SET location = 'Unknown'

DELETE FROM test_table

SELECT * FROM people
WHERE first_name = 'Jane'
AND last_name = 'Smith';
>
UPDATE people
SET occupation = 'Programmer'
WHERE first_name = 'Jane'
AND last_name = 'Smith';
>
SELECT * FROM people;

SELECT * FROM people
WHERE occupation = 'Scientist'
OR/AND age < 58;
>
DELETE * FROM people
WHERE occupation = 'Scientist'
OR/AND age < 58;
>
SELECT * FROm people;
