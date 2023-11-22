-- 创建学生表
CREATE TABLE Student (
  StudentID INT PRIMARY KEY,
  StudentName VARCHAR(50),
  StudentGender VARCHAR(10),
  StudentAge INT,
  StudentGrade VARCHAR(10),
  StudentClass VARCHAR(50),
  StudentContact VARCHAR(50)
);

-- 创建课程表
CREATE TABLE Course (
  CourseID INT PRIMARY KEY,
  CourseName VARCHAR(50),
  CourseDescription TEXT,
  CourseTeacher VARCHAR(50)
);

-- 创建成绩表
CREATE TABLE Score (
  ScoreID INT PRIMARY KEY,
  StudentID INT,
  CourseID INT,
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
  FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
  Score DECIMAL(5, 2)
);

-- 创建教师表
CREATE TABLE Teacher (
  TeacherID INT PRIMARY KEY,
  TeacherName VARCHAR(50),
  TeacherGender VARCHAR(10),
  TeacherContact VARCHAR(50)
);

-- 创建班级表
CREATE TABLE Class (
  ClassID INT PRIMARY KEY,
  ClassName VARCHAR(50),
  GradeID INT,
  FOREIGN KEY (GradeID) REFERENCES Grade(GradeID)
);

-- 创建年级表
CREATE TABLE Grade (
  GradeID INT PRIMARY KEY,
  GradeName VARCHAR(50)
);

-- 创建用户表
CREATE TABLE User (
  UserID INT PRIMARY KEY,
  Username VARCHAR(50),
  Password VARCHAR(50),
  Role VARCHAR(20)
);

-- 创建日志表
CREATE TABLE Log (
  LogID INT PRIMARY KEY,
  UserID INT,
  LogTime TIMESTAMP,
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  LogContent TEXT
);

-- 创建系统配置表
CREATE TABLE Config (
  ConfigID INT PRIMARY KEY,
  ConfigName VARCHAR(50),
  ConfigValue VARCHAR(100)
);

-- 创建学生-班级关系表
CREATE TABLE Student_Class (
  StudentID INT,
  ClassID INT,
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
  FOREIGN KEY (ClassID) REFERENCES Class(ClassID),
  PRIMARY KEY (StudentID, ClassID)
);