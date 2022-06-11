from RPG.models.character   import Character
from RPG.models.item        import Item, Armor, Weapon, Shield, itemType

from RPG.controllers.item   import get_item





def buy_item(name:str, type:str, character:Character):
    item =  get_item(name,type)

    character.bag.append(item)
    character.coins -= item.price

def add_item(name:str, type:str, character:Character):
    item =  get_item(name,type)

    character.bag.append(item.name)


def equip_item(index:int, character:Character):
    item = character.bag[index]
    if(item.type == itemType.ITEM.value):
        return False
    else:
        if(item.type == itemType.ARMOR.value):
            if character.armor:
                add_item(character.armor.name, itemType.ARMOR.value, character)
                character.armor = get_item(item.name,item.type)
                character.bag.remove(item)
            else:
                character.armor = get_item(item.name,item.type)
                character.bag.remove(item)
        else:
            if character.primaryEquip:
                if character.primaryEquip.minimum_strength:
                    if character.primaryEquip.minimum_strength < 3:
                        if character.secondaryEquip:
                            return False
                        else:
                            if item.minimum_strength:
                                if item.minimum_strength < 3:
                                    if item.minimum_strength <= character.attributes[4].value:
                                        character.secondaryEquip = item
                                        character.bag.remove(item)
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                character.secondaryEquip = item
                                character.bag.remove(item)
                else:
                    if character.secondaryEquip:
                            return False
                    else:
                        if item.minimum_strength:
                            if item.minimum_strength < 3:
                                if item.minimum_strength <= character.attributes[4].value:
                                    character.secondaryEquip = item
                                    character.bag.remove(item)
                                else:
                                    return False
                            else:
                                return False
                        else:
                            character.secondaryEquip = item
                            character.bag.remove(item)
            else:
                if item.minumum_strength:
                    if item.minimum_strength <= character.attributes[4].value:
                        character.primaryEquip = item
                        character.bag.remove(item)
                    else:
                        return False
                else:
                    return False
                    







