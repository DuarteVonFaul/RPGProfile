from sqlalchemy.orm             import Session
from sqlalchemy                 import insert


from RPG.models.focus           import Focus


def get_focus(db:Session, Name:str):
    return db.query(Focus).filter_by(name = Name).scalar

def get_all(db:Session):
    return db.query(Focus).all()


def register_focos(db:Session,focus:Focus):

    stmt = insert(Focus).values(name = focus.name,
                                description = focus.description,
                                group       = focus.group)

    db.execute(stmt)
    db.commit()

    pass
