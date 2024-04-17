#!/usr/bin/python3
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_Base()


class BaseModel(Base):
        """The BaseModel class from which future classes will be derived"""
        id = Column(Integer, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

