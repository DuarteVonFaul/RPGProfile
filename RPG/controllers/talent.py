from sqlalchemy.orm             import Session
from sqlalchemy                 import insert


from RPG.models.talent          import Talent



def get_talent(db:Session, Name:str):
    return db.query(Talent).filter_by(name = Name).scalar


def get_all(db:Session):
    return db.query(Talent).all()


def register_talent(db:Session, talent:Talent):
    stmt = insert(Talent).values(name = talent.name,
                                 classe = talent.classe,
                                 level  = 'noob',
                                 requirements = talent.requirements,
                                 description  = talent.description,
                                 noob         = talent.noob,
                                 experient    = talent.experient,
                                 master       = talent.master)

    db.execute(stmt)
    db.commit()
    pass
    