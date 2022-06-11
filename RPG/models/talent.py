from sqlalchemy import Column, Integer, String, JSON


from RPG.extensions.database import Base


class Talent(Base):

    __tablename__ = 'Talents'

    id              = Column(Integer, primary_key=True)
    name            = Column(String)
    classe          = Column(String)
    level           = Column(String)
    description     = Column(String)
    requirements    = Column(JSON)
    noob            = Column(String)
    experient       = Column(String)
    master          = Column(String)






