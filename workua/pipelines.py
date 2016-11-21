# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from workua.create_db import Base, WorkuaData


class WorkuaPipeline(object):
    def __init__(self):
        engine = create_engine('sqlite:///workua.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)

        self.session = DBSession()

    def process_item(self, item, spider):
        data = WorkuaData()
        data.Vacancy = item['vacancy']
        data.Company = item['company']
        data.Time = item['time']
        data.Description = item['description']

        self.session.add(data)
        self.session.commit()
        return item
