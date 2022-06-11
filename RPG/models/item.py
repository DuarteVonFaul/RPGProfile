from enum import Enum
from typing import Optional
from sqlalchemy import Column, Integer, String, JSON


from RPG.extensions.database import Base


class  itemType(Enum):
    ITEM    = 'ITEM'
    ARMOR   = 'ARMOR'
    WEAPON  = 'WEAPON'
    SHIELD  = 'SHIELD'



weaponGroup = [ 'BOW',          #Arco
                'CONTUSION',    #Contusão
                'HASTE',        #HASTE
                'FIGHT',        #Luta(Briga)
                'STAFF',        #Cajado
                'DOUBLE',       #Dupla
                'LIGHT_BLADE',  #Lamina Leve
                'HLAVY_BLADE',  #Lamina Pesada
                'SPEAR',        #Lança
                'CAVALARY',     #Cavalaria
                'AX']           #Machado



class Item(Base):

    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    type  = Column(String)


class Armor(Base):

    __tablename__ = 'Armors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    type  = Column(String)
    defense = Column(Integer)
    punishment = Column(Integer)

class Shield(Base):

    __tablename__ = 'Shields'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    type  = Column(String)
    defense = Column(Integer)

class Weapon(Base):

    __tablename__ = 'Weapons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    type  = Column(String)
    damage = Column(String)
    group = Column(String)
    minimum_strength = Column(Integer)




