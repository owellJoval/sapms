

--This file contains 2 scripts
-- 1. The SQL scripts for creating tables
-- 2. The SQL scripts for inserting sample data


-- Below is the SQL Scripts for creating tables in the database
CREATE TABLE Lecturer (
    LecturerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Credits INT,
    LecturerID INT,
    FOREIGN KEY (LecturerID) REFERENCES Lecturer(LecturerID)
);

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    DOB DATE
);

CREATE TABLE Enrolment (
    EnrolmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Semester VARCHAR(20),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

CREATE TABLE Marks (
    MarkID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Score DECIMAL(5,2),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Date DATE,
    Status VARCHAR(10),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);



-- 2. Sample Data Insertion (DML)

-- Below is the sample data Script

-- Insert Lecturers
INSERT INTO Lecturer VALUES (1, 'Dr. John Smith', 'john.smith@unam.edu');
INSERT INTO Lecturer VALUES (2, 'Dr. Emily Johnson', 'emily.johnson@unam.edu');
INSERT INTO Lecturer VALUES (3, 'Dr. Sarah Lee', 'sarah.lee@unam.edu');

-- Insert Courses
INSERT INTO Course VALUES (101, 'Database Systems', 3, 1);
INSERT INTO Course VALUES (102, 'Operating Systems', 4, 2);
INSERT INTO Course VALUES (103, 'Data Structures', 3, 1);
INSERT INTO Course VALUES (104, 'Software Engineering', 3, 3);

-- Insert Students
INSERT INTO Student VALUES (1001, 'Alice Green', 'alice.green@university.edu', '2000-05-15');
INSERT INTO Student VALUES (1002, 'Bob Brown', 'bob.brown@university.edu', '1999-11-22');
INSERT INTO Student VALUES (1003, 'Charlie White', 'charlie.white@university.edu', '2001-03-10');
INSERT INTO Student VALUES (1004, 'Diana Blue', 'diana.blue@university.edu', '2000-08-05');

-- Insert Enrolments
INSERT INTO Enrolment VALUES (5001, 1001, 101, 'Semester 1');
INSERT INTO Enrolment VALUES (5002, 1002, 102, 'Semester 1');
INSERT INTO Enrolment VALUES (5003, 1003, 103, 'Semester 1');
INSERT INTO Enrolment VALUES (5004, 1004, 104, 'Semester 1');
INSERT INTO Enrolment VALUES (5005, 1001, 102, 'Semester 1');

-- Insert Marks
INSERT INTO Marks VALUES (9001, 1001, 101, 87.5);
INSERT INTO Marks VALUES (9002, 1002, 102, 74.0);
INSERT INTO Marks VALUES (9003, 1003, 103, 91.0);
INSERT INTO Marks VALUES (9004, 1004, 104, 66.5);
INSERT INTO Marks VALUES (9005, 1001, 102, 78.0);

-- Insert Attendance
INSERT INTO Attendance VALUES (3001, 1001, 101, '2025-02-20', 'Present');
INSERT INTO Attendance VALUES (3002, 1002, 102, '2025-02-20', 'Absent');
INSERT INTO Attendance VALUES (3003, 1003, 103, '2025-02-20', 'Present');
INSERT INTO Attendance VALUES (3004, 1004, 104, '2025-02-20', 'Present');
INSERT INTO Attendance VALUES (3005, 1001, 102, '2025-02-21', 'Absent');

