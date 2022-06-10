from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import create_session
from sqlalchemy import create_engine
from sqlalchemy import insert

link = '../sqlite.sqlite3'
engine = create_engine(f'sqlite:///{link}')

Session = create_session(engine)

Base = declarative_base()

'''class Talent():

    def __init__(self,name:str,classe:List[str], requirements:List[dict], **kwargs):
        self.name           = name
        self.classe         = classe
        self.requirements   = requirements
        for key, value in kwargs:
            setattr(self,key,value)
'''


class TableTalent(Base):

    __tablename__ = 'Talents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classe = Column(String)
    requirements = Column(JSON)


'''Base.metadata.create_all(engine)'''


'''tb = TableTalent(name='TEst', classe = 'test2,test3', requirements={'test1':'test2'})
Session.add(tb)'''



stmt = (
    insert(TableTalent).
    values(name='TEst', classe='test2,test3', requirements={'test1':'test2'})
)

Session.execute(stmt)
Session.commit()

