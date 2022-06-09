
groupList = ['cunning', 'communication', 'constitution', 'dexterity', 'strength', 'magic', 'perception', 'will']

class Focus():

    def __init__(self, name:str, description:str, group:int) -> None:

            self.name           = name
            self.description    = description
            self.group          = groupList[group]