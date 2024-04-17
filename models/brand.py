#!/usr/bin/python3
"""Defining the class for brand"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models import base_model

Base = declarative_base()


class Brand(BaseModel, Base):
    """class Brand"""
    __tablename__ = 'brands'

    name = Column(String)
