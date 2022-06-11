
from RPG.models.character import Character, Appearance, Historic
from RPG.extensions.database import db
from RPG.config           import to_dict






def create_character(nome:str,historic:Historic,appearance:Appearance, classe:str):
    character = Character()
    character.builder(nome, historic, appearance, classe)
    return  to_dict(character)

def register_character(UID:str, character:dict, userToken):
    try:
        name = character['name']
        db.create(character,'Personagens',f'{UID}/{name}',userToken)
        return{'status':200, 'character':character}
    except:
        return{'status':500}
