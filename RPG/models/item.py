from enum import Enum
from typing import Optional


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

class Item():

    def __init__(self, name:str, description:str, price:int) -> None:

        self.name       = name
        self.descriptio = description
        self.price      = price
        self.type       = itemType.ITEM.value



class Armor(Item):

    def __init__(self, name: str, description: str, price: int, defense:int, punishment:int) -> None:
        super().__init__(name, description, price)
        self.defense = defense
        self.punishment = punishment
        self.type = itemType.ARMOR.value

class Shield(Item):

    def __init__(self, name: str, description: str, price: int, defense:int )-> None:
        super().__init__(name, description, price)
        self.defense = defense
        self.type = itemType.SHIELD.value

class Weapon(Item):

    def __init__(self, name: str, description: str, price: int, damage:str, group:int, minimum_strength:Optional[int] = None) -> None:
        super().__init__(name, description, price)
        self.damage = damage
        self.group = weaponGroup[group]
        self.type = itemType.WEAPON.value

        if minimum_strength != None:
            self.minimum_strength = minimum_strength
        else:
            self.minimum_strength = False




