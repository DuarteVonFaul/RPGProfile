from sqlalchemy import Column, Integer, String


from RPG.extensions.database import Base


groupList = ['cunning', 'communication', 'constitution', 'dexterity', 'strength', 'magic', 'perception', 'will']

class Focus(Base):

    __tablename__ = 'Focus'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    group = Column(String)
