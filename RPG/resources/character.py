from RPG.controllers.character import create_character,register_character
from RPG.models.character      import Historic,Appearance
from flask import request, render_template


def init(app):
      
    @app.route("/api/character/register", methods=['POST'])
    def registerForm():
        char = create_character('Duarte', 
                                Historic('Anão Escravo','Anão','',['Anão','Comercio']),
                                Appearance(60,'Masculino',80.0,1.52),
                                'Mago')
        return register_character('GZ0C6y8iYnfDGTzoPLy6MijOQpG2', char )


    pass