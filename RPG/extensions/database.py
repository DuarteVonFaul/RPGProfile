import pyrebase

firebaseConfig = {
            "apiKey": "AIzaSyAG8_VMsDMXb6aINZ4fMLatHsQ8RRAmYYI",
            "authDomain": "basenayze.firebaseapp.com",
            "databaseURL": f"https://basenayze.firebaseio.com/",
            "storageBucket": "basenayze.appspot.com",

            }

firebase = pyrebase.initialize_app(firebaseConfig)

class DataBase():

    def __init__(self,info) -> None:
        self.dados = firebase.database()
    
    def create(self,dict:dict,__group__,__key__):
        try:
            self.dados.child(__group__).child(__key__).set(dict)
            return {'status':200}
        except:
            return {'status':500}
    
    def get(self,__group__,__key__):
        return self.dados.child(__group__).child(__key__).get()
    
    def getall(self,__group__):
        return self.dados.child(__group__).get()











