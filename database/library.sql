CREATE DATABASE library;

USE library;

-- Table for student details
CREATE TABLE student (
    student_roll int PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address1 VARCHAR(100),
    Address2 VARCHAR(100),
    PostCode VARCHAR(10),
    Mobile VARCHAR(15)
);

-- Table for book details
CREATE TABLE book (
    id INT PRIMARY KEY,
    book_id VARCHAR(100),
    author VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Table for book transactions
CREATE TABLE transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key
    student_roll VARCHAR(20) NOT NULL,  -- Alphanumeric student roll number
    book_id INT NOT NULL,               -- Foreign key referencing book.id
    issue_date DATE NOT NULL,           -- Issue date (cannot be NULL)
    return_date DATE,                   -- Return date (can be NULL)
    fine FLOAT,							-- Fine amount (can be NULL)
    FOREIGN KEY (student_roll) REFERENCES student(student_roll),
    FOREIGN KEY (book_id) REFERENCES book(id)  -- Foreign key constraint
);

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);