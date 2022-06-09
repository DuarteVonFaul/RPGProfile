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
        print()
        email = request.get_json()['email_login']
        password = request.get_json()['password_login']
        return login(UserAcess(email, password))

    @app.route("/api/v1/register", methods=['POST'])
    def registerUser():
        email = request.get_json()['email_register']
        password = request.get_json()['password_register']
        return register(UserAcess(email,password))


    @app.route("/api/v1/redefine-password", methods=['POST'])
    def redefineform():
        email = request.get_json()['email_redefine']
        return redefine_password(email)

    


    #Templates
    @app.route("/login")
    def logintemplate():
        return render_template('login.html', msg={"message": "Uma mensagem interessante"})

    @app.route("/redefine-password")
    def redefinetemplate():
        return render_template('login.html', msg={"message": "Uma mensagem interessante"})

    


    pass


