# coding: utf-8
from sqlalchemy import (
    Column,
    DECIMAL,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    Table,
    Text,
)
from sqlalchemy.dialects.mysql import CHAR, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Config(Base):
    __tablename__ = "config"

    ConfigID = Column(Integer, primary_key=True)
    ConfigName = Column(String(50))
    ConfigValue = Column(String(100))


class Grade(Base):
    __tablename__ = "grade"

    GradeID = Column(Integer, primary_key=True)
    GradeName = Column(String(50))


class Teacher(Base):
    __tablename__ = "teacher"

    TeacherID = Column(Integer, primary_key=True)
    TeacherName = Column(String(50), index=True)
    TeacherGender = Column(String(10))
    TeacherContact = Column(String(50))


class User(Base):
    __tablename__ = "user"

    UserID = Column(Integer, primary_key=True)
    UserName = Column(VARCHAR(50))
    Password = Column(CHAR(32))
    Role = Column(String(20))


class Class(Base):
    __tablename__ = "class"

    ClassID = Column(Integer, primary_key=True)
    ClassName = Column(String(50), index=True)
    GradeID = Column(ForeignKey("grade.GradeID"), index=True)

    grade = relationship("Grade")
    student = relationship("Student", secondary="student_class")


class Course(Base):
    __tablename__ = "course"

    CourseID = Column(Integer, primary_key=True)
    CourseName = Column(String(50))
    CourseDescription = Column(Text)
    CourseTeacherID = Column(
        ForeignKey("teacher.TeacherID", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )

    teacher = relationship("Teacher")


class Log(Base):
    __tablename__ = "log"

    LogID = Column(Integer, primary_key=True)
    UserID = Column(ForeignKey("user.UserID"), index=True)
    LogTime = Column(TIMESTAMP)
    LogContent = Column(Text)

    user = relationship("User")


class Student(Base):
    __tablename__ = "student"

    StudentID = Column(Integer, primary_key=True)
    StudentName = Column(String(50))
    StudentGender = Column(String(10))
    StudentAge = Column(Integer)
    GradeID = Column(
        ForeignKey("grade.GradeID", ondelete="SET NULL", onupdate="CASCADE"), index=True
    )
    StudentClass = Column(String(50), index=True)
    StudentContact = Column(String(50))

    grade = relationship("Grade")
    teacher = relationship("Teacher", secondary="student_teacher")


class Score(Base):
    __tablename__ = "score"

    ScoreID = Column(Integer, primary_key=True)
    StudentID = Column(ForeignKey("student.StudentID"), index=True)
    CourseID = Column(ForeignKey("course.CourseID"), index=True)
    Score = Column(DECIMAL(5, 2))

    course = relationship("Course")
    student = relationship("Student")


t_student_class = Table(
    "student_class",
    metadata,
    Column(
        "StudentID", ForeignKey("student.StudentID"), primary_key=True, nullable=False
    ),
    Column(
        "ClassID",
        ForeignKey("class.ClassID"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_student_teacher = Table(
    "student_teacher",
    metadata,
    Column(
        "StudentID",
        ForeignKey("student.StudentID", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "TeacherID",
        ForeignKey("teacher.TeacherID", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)
