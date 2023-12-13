"""NOTE Databases NOTE"""
CREATE TABLE person(
    person_id INTEGER PRIMARY KEY;
    name TEXT,
    age INTEGER
) STRICT;

# to find the name of someone that is older than 40 years of age...
SELECT name
FROM person
WHERE age < 40;

# to find the name and age of someone who's length of their name is 4 and the person_id is between 1 and 10...
SELECT name, age
FROM person
WHERE length(name) = 4 AND person_id BETWEEN 1 AND 10;

# to find truthy ages, aka non-zero...
SELECT name 
FROM person
WHERE age;

"""NOTE ORDER BY, ASC, DESC NOTE"""

# say I want to get all the names in ascending by their ages...
SELECT name 
FROM person
ORDER BY age ASC;

# say I want to get all the names in descending order by the length of each of their names...
SELECT name
FROM person
ORDER BY length(name) DESC;

# now lets put them all together...
SELECT name
FROM person
WHERE age < 40
ORDER BY age ASC; # <- make sure to respect this line order. if WHERE is before ORDER, there will be an error...

"""NOTE UPDATE, SET NOTE"""

# update a person's age if their person id is equal to 2...
UPDATE person
SET age = age + 1
WHERE person_id = 2;
# now let's check their new age...
SELECT name
FROM person
WHERE person_id = 2;
('Alex', 47) -> ('Alex', 48)

"""NOTE INSERT INTO NOTE"""
# insert multiple different values into a table...
INSERT INTO person (person_id, name, age)
VALUES (3, 'Example', 99);
#...
UPDATE person
SET name = "Someone", age = 91 # you can set multiple in a row like this...
WHERE person_id = 3;
#...
SELECT name, age
FROM person
WHERE person_id = 3;
# output: Someone, 91

"""NOTE DELETE, DROP TABLE NOTE"""
DELETE 
FROM person
WHERE person_id = 3;
#...
SELECT name, age
FROM person;
# all people who have a person_id of 3 should be deleted...

# now to completely drop a table...
DROP TABLE person; # very simple and yet very powerful...

"""NOTE NULL NOTE"""
# FIRST OFF 0 IS NOT NULL!
SELECT course_number, title, unit_count
FROM course
WHERE unit_count IS NULL; # "IS" not "="...

# say that course_number is TEXT NOT NULL. therefore...
INSERT INTO course (course_id)
VALUES (1);
# THIS WILL RESULT IN A ERROR, because the course number is not given a value...
# it has a NOT NULL restriction, so it must be given a text...

"""NOTE CHECK, UNIQUE NOTE"""
# If CHECK or UNIQUE fails, there will be an error. 
# unit_count INTEGER NOT NULL CHECL (unit_count > 0)
# course_number TEXT NOT NULL UNIQUE

"""NOTE RELATIONSHIPS AND JOINS NOTE"""
# this one is prolly the most important and hardest topic on SQLite...

# take a look at how FOREIGN keys are constructed...
CREATE TABLE enrollment(
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id)
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
    ) STRICT;

INSERT INTO student (student_id, name)
VALUES (1, 'Boo');
INSERT INTO course (course_id, course_number, unit_count)
VALUES (2, 'Alex')
INSERT INTO enrollment (student_id, course_id)
VALUES (1, 2) # this is valid. it will create a primary key for us...
# on the other hand...
INSERT INTO enrollment (student_id, course_id)
VALUES (1, 2) # this will cause an error because the course_id and enrollment_id together are not UNIQUE.
INSERT INTO enrollment (student_id, course_id)
VALUES (5, 6) # this will also cause an error because the course_id and enrollment_id do not exist already. 

# lets say we want to know the students that are enrolled in ICS 33...
SELECT s.name
FROM student as s
    INNER JOIN enrollment AS e ON e.student_id = s.student_id
    INNER JOIN course AS c ON c.course_id = e.course_id
WHERE c.course_number = 'ICS 33';

# lets say we want to know the students that are enrolled in ICS 33 in ascending order by name...
SELECT s.name
FROM student AS s
    INNER JOIN enrollment AS e ON e.student_id = s.student_id
    INNER JOIN course AS c ON c.course_id = e.course_id
WHERE c.course_number = 'ICS 33'
ORDER BY s.name ASC;

SELECT s.name
FROM student AS s
    INNER JOIN enrollment AS e ON e.student_id = s.student_id
    INNER JOIN course AS c ON c.course_id = e.course_id
ORDER BY s.name ASC, c.course_number ASC;

"""NOTE Avoiding Injection Attacks..."""
# this part was on the project 2 so you should be very familiar I think...

INSERT INTO person (name, age) VALUES (?, ?);
(('Boo', 13))

# you prolly won't see this on the test but...
INSERT INTO person (name, age) VALUE (:name, :age);
{'name': 'Boo', 'age': 13}

SELECT s.name
FROM student AS s
    INNER JOIN enrollment AS e ON e.student_id = s.student_id
    INNER JOIN course AS c ON c.course_id = e.course_id
WHERE c.course = "ICS 33"

SELECT c.course_number, s.name
FROM student AS s
    INNER JOIN enrollment AS e ON e.student_id = s.student_id
    INNER JOIN course AS c ON c.course_id = e.course_id
ORDER BY c.course_number ASC, s.name ASC; # in this case, we don't need a WHERE clause

# avoid injections
connection.execute('INSERT INTO person (name, age) VALUES (?, ?);', ('Boo', 13))


SELECT location_id, street_address, city, state_province, country_name
FROM locations
NATURAL JOIN counries;

SELECT first_name, last_name, department_id, depart_name
FROM employees
JOIN departments USING (department_id);









""""

