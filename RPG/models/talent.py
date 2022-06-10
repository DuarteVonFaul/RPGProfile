
from typing import List

levelList = ['Noob','Experient', 'Master']


class Talent():

    def __init__(self,name:str,classe:List[str], requirements:List[dict],description:str,level:int):


        self.name           = name
        self.classe         = classe
        self.requirements   = requirements
        self.description    = description
        self.level          = levelList[level]
