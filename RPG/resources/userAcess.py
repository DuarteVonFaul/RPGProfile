from flask import request, render_template



from RPG.controllers.user_acess import (login,
                                        register,
                                        redefine_password,
                                        refreshToken)

from RPG.models.user_acess      import UserAcess


def init(app):
    
    #API
    
    @app.route("/api/user/login", methods=['POST'])
    def loginform():
        email = request.get_json()['email_login']
        password = request.get_json()['password_login']
        return login(UserAcess(email, password))

    @app.route("/api/user/register", methods=['POST'])
    def registerUser():
        email = request.get_json()['email_register']
        password = request.get_json()['password_register']
        return register(UserAcess(email,password))


    @app.route("/api/user/redefine-password", methods=['POST'])
    def redefineform():
        email = request.get_json()['email_redefine']
        return redefine_password(email)

    @app.route("/api/user/refresh-toker", methods=['POST'])
    def refreshform():
        token = request.get_json()['toker_Refrash']
        return refreshToken(token)

    


    #Templates
    @app.route("/login")
    def loginTemplate():
        return render_template('login.html')

    @app.route("/register")
    def registerTemplate():
        return render_template('sign_up.html')

    @app.route("/home")
    def registerTemplate():
        return render_template('home.html')


    pass


