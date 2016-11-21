import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from workua.create_db import Base, WorkuaData


def main():
    engine = create_engine('sqlite:///workua.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    tmp = WorkuaData()
    with open('workua.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=tmp.as_dict().keys(), delimiter='\t')
        writer.writeheader()

        for record in session.query(WorkuaData):
            writer.writerow(record.as_dict())


if __name__ == '__main__':
    print('Started export')
    main()
    print('Finished export')
