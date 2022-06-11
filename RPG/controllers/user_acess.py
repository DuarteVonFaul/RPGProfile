import pyrebase


from RPG.models.user_acess import UserAcess
from RPG.extensions.database import firebaseConfig, firebase

def login(user:UserAcess):
    try:
        auth = firebase.auth()
        userInfo = auth.sign_in_with_email_and_password(user.userEmail, user.userPassword)
        return {'status': 200, 'info': userInfo}
    except:
        return{'status': 500}


def register(user:UserAcess):
    try:
        auth = firebase.auth()
        auth.create_user_with_email_and_password(user.userEmail, user.userPassword)
        return {'status': 200}
    except:
        return{'status':500}


def redefine_password(Email:str):
    try:
        auth = firebase.auth()
        auth.send_password_reset_email(Email)
        return {'status': 200}
    except:
        return{'status':500}



def refreshToken(userInfo):
    try:
        auth = firebase.auth()
        user = auth.refresh(user['refreshToken'])
        return {'status': 200}
    except:
        return{'status':500}

    



