

class User():

    def __init__(self) -> None:
        pass

    def setToken(self, token):
        self.token = token
    
    def setID(self, id):
        self.ID = id

    def getToken(self):
        return self.token

    def getID(self):
        return self.ID



user = User()