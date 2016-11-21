# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WorkuaData(Base):
    __tablename__ = 'workua_data'

    Id = Column(Integer, primary_key=True)
    Vacancy = Column(String(255))
    Company = Column(String(255))
    Time = Column(String(255))
    Description = Column(String(255))

    def as_dict(self):
        return {
            'Id': self.Id,
            'Vacancy': self.Vacancy,
            'Company': self.Company,
            'Time': self.Time,
            'Description': self.Description,
        }


engine = create_engine('sqlite:///workua.db')

Base.metadata.create_all(engine)
