from sqlalchemy.orm             import Session
from sqlalchemy                 import insert


from RPG.models.item            import Item, Armor, Weapon, Shield



def get_item(db:Session,Name:str, type:str):
    match type:
        case 'ITEM':
            db.query(Item).filter_by(name = Name).scalar()
            return 1
        case 'ARMOR':
            db.query(Armor).filter_by(name = Name).scalar() 
            return 2
        case 'WEAPON': 
            db.query(Weapon).filter_by(name = Name).scalar()
            return 2
        case 'SHIELD':
            db.query(Shield).filter_by(name = Name).scalar() 
            return 3


    return Item()

def register_item(db:Session, item:Item):
    stmt = insert(Item).values(name       = item.name,
                              description  = item.description,
                              price       = item.price,
                              type        = item.type)
    db.execute(stmt)
    db.commit
    pass

def register_weapon(db:Session, item:Weapon):
    query = insert(Weapon).values(name            = item.name,
                                description       = item.description,
                                price            = item.price,
                                type             = item.type,
                                damage           = item.damage,
                                group            = item.group,
                                minimum_strength = item.minimum_strength)
    db.execute(query)
    db.commit
    pass

def register_armor(db:Session, item:Armor):
    query = insert(Armor).values(name       = item.name,
                                description = item.description,
                                price      = item.price,
                                type       = item.type,
                                defense    = item.defense,
                                punishment = item.punishment)

    db.execute(query)
    db.commit
    pass

def register_shield(db:Session, item:Shield):
    stmt = insert(Shield).values(name       = item.name,
                                description = item.description,
                                price      = item.price,
                                type       = item.type,
                                defense    = item.defense)
    db.execute(stmt)
    db.commit
    pass



def get_all_items(db:Session):

    ListItem    = db.query(Item).all()
    ListWeapon  = db.query(Weapon).all()
    ListArmor   = db.query(Armor).all()
    ListShield  = db.query(Shield).all()

    return {[{'Item'    : ListItem},
             {'Weapons' : ListWeapon},
             {'Armors'  : ListArmor},
             {'Shields' : ListShield}]}