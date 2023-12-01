from __future__ import unicode_literals, absolute_import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, CHAR, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, MappedColumn


ModelBase = declarative_base()
pass


class ManageEntity:
    class UserModel(ModelBase):
        __tablename__ = "user"
        UserID = Column(Integer, primary_key=True)
        Username = Column(String(50))
        Password = Column(CHAR(50))
        Role = Column(String(20))

    class LogModel(ModelBase):
        __tablename__ = "log"
        LogID = Column(Integer, primary_key=True)
        UserID = Column(
            Integer, ForeignKey("user.UserID", ondelete="RESTRICT", onupdate="RESTRICT")
        )
        LogTime = Column(DateTime)
        LogContent = Column(Text)

    class ConfigModel(ModelBase):
        __tablename__ = "config"
        ConfigID = Column(Integer, primary_key=True)
        ConfigName = Column(String(50))
        COnfigValue = Column(String(100))

    class GradeModel(ModelBase):
        GradeID = Column(Integer, primary_key=True)
        GradeName = Column(String)

    def __init__(self):
        ()
