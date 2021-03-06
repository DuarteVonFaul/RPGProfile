from typing import List, Optional
import random
from sqlalchemy import Column, Integer, String, JSON

from RPG.config import  attrGenerator,ClassesType
from RPG.models.attribute import Attribute
from RPG.extensions.database import Base


attrList = ['cunning', 'communication', 'constitution', 'dexterity', 'strength', 'magic', 'perception', 'will']

class Appearance():

    def __init__(self, age:int, sex:str, weight:float, height:int) -> None:
        self.age    = age
        self.sex    = sex
        self.weight = weight
        self.height = height
        pass

class TB_Historic(Base):

    __tablename__ = 'Historics'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    description = Column(String)
    languages = Column(String)
    bonus = Column(JSON)
    benefitsTable = Column(JSON)

class Historic():

    def __init__(self, breed:str, description:str, name:str, languages) -> None:
        self.name           = name
        self.breed          = breed
        self.description    = description
        self.languages      = languages

        pass


class Classe():

    def __init__(self, dict:dict) -> None:

        for key, value in dict.items():
            setattr(self,key,value)
        pass



class Character():

    def __init__(self,**kwargs:Optional(dict)) -> None:
        
        self.name           = ''
        self. historic      = ''
        self.appearance     = ''

        self.classe         = ''
        self.level          = ''
        self.exp            = ''

        self.attributes     = []
        self.talents        = []

        self.coins          = ''
        self.armor          = ''
        self.primaryEquip   = ''
        self.secondaryEquip = ''
        self.bag            = []

        for key, value in kwargs.items():
            setattr(self,key,value)

        
        pass

    def build(self,name:str, historic:Historic, appearance:Appearance, classe:str):

        for attr in attrList:
            self.attributes.append(Attribute(attr,attrGenerator(random.randint(3,18))))

        self.classe = Classe(ClassesType.__getitem__(classe).value)
        
        for item in self.attributes:
            if item.name == 'constitution':
                self.classe.life += item.value + random.randint(1,6)
        if self.classe.name == 'Mago':
            for item in self.attributes:
                if item.name == 'magic':
                    self.classe.mana += item.value + random.randint(1,6)

        for attr in self.classe.primaryAttr:
            for item in self.attributes:
                if item.name ==attr:
                    item.primaryAttr(True)

        self.level  = 1
        self.exp    = 0
        self.coins  = 10000


        self.name       = name
        self.historic   = historic
        self.appearance = appearance

        self.bag            = False
        self.talents        = False
        self.armor          = False
        self.primaryEquip   = False
        self.secondaryEquip = False




    pass