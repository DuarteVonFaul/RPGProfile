
from enum import Enum
import random

class ClassesType(Enum):

    Mago = {'name':'mago',
            'attrPrimary':['cunning', 'magic', 'will'],
            'life':20,
            'Mana':random.randint(11, 16),
            'defense':10
            }
    
    Ladino = {'name':'ladino',
            'attrPrimary':['communication', 'dexterity', 'perception'],
            'life':25,
            'defense':10
            }
    
    Guerreiro = {'name':'guerreiro',
            'attrPrimary':['constitution', 'dexterity', 'strength'],
            'life':30,
            'defense':10
            }
    
    Classes = Enum('Classes', ['Mago','Ladino', 'Guerreiro'])


def attrGenerator(argument:int):
    match argument:
       case 3      : return -2
       case 4      : return -1
       case 5      : return -1
       case 6      : return 0
       case 7      : return 0
       case 8      : return 0
       case 9      : return 1
       case 10     : return 1
       case 11     : return 1
       case 12     : return 2
       case 13     : return 2
       case 14     : return 2
       case 15     : return 3
       case 16     : return 3
       case 17     : return 3
       case 18     : return 4

groupList = ['cunning', 
'communication', 
'constitution', 
'dexterity', 
'strength', 
'magic', 
'perception', 
'will']

def groupFocus(argument:str):
    match argument.upper():
       case 'ASTÚCIA'     : return 'cunning'
       case 'COMUNICAÇÃO' : return 'communication'
       case 'CONSTITUIÇÃO': return 'constitution'
       case 'DESTREZA'    : return 'dexterity'
       case 'FORÇA'       : return 'strength'
       case 'MAGIA'       : return 'magic'
       case 'PERCEPÇÃO'   : return 'perception'
       case 'VONTADE'     : return 'will'


def to_dict(obj):
    # Se for um objeto, transforma num dict
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__

    # Se for um dict, lê chaves e valores; converte valores
    if isinstance(obj, dict):
        return { k:to_dict(v) for k,v in obj.items() }
    # Se for uma lista ou tupla, lê elementos; também converte
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [to_dict(e) for e in obj]
    # Se for qualquer outra coisa, usa sem conversão
    else: 
        return obj
