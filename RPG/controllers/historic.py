from RPG.models.character   import Historic, Character
from RPG.models.focus       import Focus
from typing                 import Optional
import random




{'Table' : [{'Casta':['Artesão', 'artifice', 'Guerreiro']}, 
                                        {'atrribute':[{'strength':1}]},
                                        {'Focus':[{'dexterity':'Artesanato'},{'strength':'Intimidação'},{'Força':'Ferraria'}]},
                                        {'Bonus':{'Magic':2}},
                                        {'languages':['Anão','Comêrcio']},
                                        {'classe':['Guerreiro', 'Ladino']},
                                        {'benefitsTable':2}]}

{'TableBen': [  {'attribute':[{'will':1}]},
                {'Focus':[{'will':'Coragem'}]},
                {'Focus':[{'communication':'Etiqueta'}]},
                {'Focus':[{'cunning':'Heráldica'}]},
                {'attribute':[{'cunning':1}]},
                {'Focus':[{'cunning':'Engenharia'}]},
                {'Focus':[{'constitution':'Vigor'}]},
                {'attribute':[{'constitution':1}]} ]}



def benefitsTable(number:int,character:Character):
    i = 0
    while i < number:
        aux = character.historic.benefitsTable['TableBen'][random.randint(2,12)]
        for k,v in aux:
            Bonus(k,v,character,0)
        i += 1
    pass
def Bonus(argument:str, value,character:Character, num:Optional[int] = -1):
    match argument:
        case 'Casta':
            try:
                setattr(character.historic,argument,value[num - 1])
                return True
            except:
                return False

        case 'atrribute':
            try:
                for attr in character.attributes:
                    for item in value:
                        for k, v in item:
                            if attr.name == k:
                                attr.value += v
                                value.remove(item)
                return True
            except:
                return False

        case 'Focus':
            aux = value[num]
            try:
                for attr in character.attributes:
                    for k, v in aux:
                        if attr.name == k:
                            attr.addFocus(Focus())
                return True
            except:
                return False

        case 'Bonus': 
            try:
                setattr(character,argument,value)
                return True
            except:
                return False
        case 'languages':
            return value
        case 'classe':
            return value

        case 'benefitsTable':
            try:
                benefitsTable(number=value, character=character)
                return True
            except:
                return False


def benefitsGenerator(argument:int):
    match argument:
        case 2      : return 1
        case 3      : return 2
        case 4      : return 2
        case 5      : return 3
        case 6      : return 4
        case 7      : return 5
        case 8      : return 5
        case 9      : return 6
        case 10     : return 7
        case 11     : return 7
        case 12     : return 8