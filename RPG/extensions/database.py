import pyrebase
from sqlalchemy             import create_engine
from sqlalchemy.orm         import Session
from sqlalchemy.ext.declarative import declarative_base

firebaseConfig = {
            "apiKey": "AIzaSyAG8_VMsDMXb6aINZ4fMLatHsQ8RRAmYYI",
            "authDomain": "basenayze.firebaseapp.com",
            "databaseURL": f"https://basenayze.firebaseio.com/",
            "storageBucket": "basenayze.appspot.com",

            }

firebase = pyrebase.initialize_app(firebaseConfig)

class FireBase():

    def __init__(self,info) -> None:
        self.dados = firebase.database()
    
    def create(self,dict:dict,__group__,__key__,__user__):
        try:
            self.dados.child(__group__).child(__key__).set(dict,__user__)
            return {'status':200}
        except:
            return {'status':500}
    
    def get(self,__group__,__key__,__user__):
        return self.dados.child(__group__).child(__key__).get(__user__)
    
    def getall(self,__group__,__user__):
        return self.dados.child(__group__).get(__user__)

class Database():
    def __init__(self, path) -> None:
        self.path = path

    def get_engine(self):
        return create_engine(f"sqlite:///{self.path}")


    def get_base(self):
        Base = declarative_base()
        return Base
    
    def get_session(self):
        return Session(self.get_engine())
    

RPGBase = Database('./sqlite.sqlite3')
Base = RPGBase.get_base()
MySession = RPGBase.get_session()











