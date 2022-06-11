from RPG.controllers.item    import (register_armor,
                                    register_item,
                                    register_shield,
                                    register_weapon)

from RPG.models.item          import (  Item,
                                        itemType,
                                        Weapon,
                                        Shield,
                                        Armor)

from RPG.extensions.database    import MySession

from flask import request, render_template, redirect


def init(app):
      
    @app.route("/api/item/register", methods=['POST', 'GET'])
    def registerFormItem():
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('group')
        type  = itemType.ITEM.value
        item = Item(name=name,
                    description=description,
                    price=price,
                    type=type)
        register_item(MySession,item)
        return redirect('/item/register')

    @app.route("/api/weapon/register", methods=['POST', 'GET'])
    def registerFormWwapon():
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        type  = itemType.WEAPON.value
        damage = request.form.get('damage')
        group = request.form.get('group')
        aux = request.form.get('minimum_strength')
        minimum_strength = int(aux) if aux.upper() != 'FALSE' else None
        weapon = Item(name=name,
                    description=description,
                    price=price,
                    type=type,
                    damage=damage,
                    group=group,
                    minimum_strength=minimum_strength)
        register_weapon(MySession,weapon)
        return redirect('/weapon/register')
    
    @app.route("/api/armor/register", methods=['POST', 'GET'])
    def registerFormArmor():
        name        = request.form.get('name')
        description = request.form.get('description')
        price       = request.form.get('price')
        defense     = int(request.form.get('defense'))
        punishment  = int(request.form.get('punishment'))
        type        = str(itemType.ARMOR.value)

        armor       = Armor( name=name,
                            description=description,
                            price=price,
                            defense=defense,
                            punishment=punishment,
                            type=type)

        register_armor(MySession,armor)
        return redirect('/armor/register')

    @app.route("/api/shield/register", methods=['POST', 'GET'])
    def registerFormShield():
        name        = request.form.get('name')
        description = request.form.get('description')
        price       = request.form.get('price')
        defense     = int(request.form.get('defense'))
        type        = itemType.SHIELD.value
        shield      = Shield( name=name,
                        description=description,
                        price=price,
                        defense=defense,
                        type=type)

        register_shield(MySession,shield)
        return redirect('/shield/register')
    


    @app.route("/item/register")
    def registerTemplateItem():
        return render_template('temp/itemForm.html')

    @app.route("/weapon/register")
    def registerTemplateweapon():
        return render_template('temp/weaponForm.html')

    @app.route("/armor/register")
    def registerTemplatearmor():
        return render_template('temp/armorForm.html')

    @app.route("/shield/register")
    def registerTemplateshield():
        return render_template('temp/shieldForm.html')


    pass