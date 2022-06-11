from unicodedata import name
from RPG.controllers.focus      import register_focos
from RPG.models.focus           import Focus
from RPG.extensions.database    import MySession
from RPG.config                 import groupFocus
from flask import request, render_template


def init(app):
      
    @app.route("/api/focus/register", methods=['POST', 'GET'])
    def registerFormFocus():
        name = request.form.get('name')
        description = request.form.get('description')
        group = request.form.get('group')
        focus = Focus(name=name,description=description,group=groupFocus(group))
        register_focos(MySession,focus)
        return render_template('temp/focusForm.html')
    
    @app.route("/focus/register")
    def registerTemplateFocus():
        return render_template('temp/focusForm.html')


    pass