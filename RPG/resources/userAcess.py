from flask import request, render_template



from RPG.controllers.user_acess import (login,
                                        register,
                                        redefine_password,
                                        refreshToken)

from RPG.models.user_acess      import UserAcess


def init(app):
    
    #API
    
    @app.route("/api/v1/login", methods=['POST'])
    def loginform():
        email = request.form.get('email_login')
        password = request.form.get('password_login')
        return login(UserAcess(email, password))

    @app.route("/api/v1/register", methods=['POST'])
    def registerUser():
        email = request.form.get('email_register')
        password = request.form.get('password_register')
        return register(UserAcess(email,password))




    #Templates
    @app.route("/login")
    def logintemplate():
        return render_template('login.html', msg={"message": "Uma mensagem interessante"})

    


    pass


