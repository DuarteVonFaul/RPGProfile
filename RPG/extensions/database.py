from .Pyrebase.pyrebase import pyrebase



class DataBase():

    def __init__(self,info) -> None:

        self.config = {
            "apiKey": "AIzaSyAG8_VMsDMXb6aINZ4fMLatHsQ8RRAmYYI",
            "authDomain": "basenayze.firebaseapp.com",
            "databaseURL": f"https://basenayze.firebaseio.com/{info}",
            "storageBucket": "basenayze.appspot.com",

            }
        self.firebase = pyrebase.initialize_app(self.config)
        self.dados = self.firebase.database()
    
    def escrever(self,dict:dict):
        try:
            self.dados.child().update(dict)
            return str(True)
        except:
            return str(False)
    
    def buscar(self, nome:str):
        return self.dados.child(nome).get()
    
    def buscar_todos(self):
        return self.dados.child().get()











