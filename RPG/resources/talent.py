import imp
from RPG.controllers.talent     import register_talent
from RPG.models.talent          import Talent
from RPG.extensions.database    import MySession
from RPG.config                 import groupFocus
from flask import request, render_template

import ast


def init(app):
      
    @app.route("/api/talent/register", methods=['POST', 'GET'])
    def registerFormTalent():
        name        = request.form.get('name')
        description = request.form.get('description')
        classe      = request.form.get('classe')
        requirements= ast.literal_eval(request.form.get('requirements'))
        noob        = request.form.get('noob')
        experient   = request.form.get('experient')
        master      = request.form.get('master')

        talent      = Talent(   name = name,
                                description=description,
                                classe=classe,
                                requirements=requirements,
                                noob=noob,
                                experient=experient,
                                master=master   )



        register_talent(MySession,talent)
        return render_template('temp/talentForm.html')
    
    @app.route("/talent/register")
    def registerTemplateTalent():
        return render_template('temp/talentForm.html')


    pass