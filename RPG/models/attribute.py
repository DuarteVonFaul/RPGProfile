from RPG.models.focus import Focus


class Attribute():

    def __init__(self,name,value) -> None:
        self.name = name
        self.value = value
        self.focusList = False
        self.primary   = False
        pass

    def primaryAttr(self,bool:bool):
        primary = bool

    def addFocus(self,focus:Focus):
        if(self.focusList == False):
            self.focusList == [focus]
        else:
            self.focusList.append(focus)

    pass