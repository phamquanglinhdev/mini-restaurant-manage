class User:
    def __init__(self):
        self.__id = None
        self.__username = None
        self.__password = None
        self.__role = None

    def setId(self, ids):
        self.__id = ids

    def getId(self):
        return self.__id

    def setUserName(self, username):
        self.__username = username

    def getUserName(self):
        return self.__username

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password

    def setRole(self, role):
        self.__role = role

    def getRole(self):
        self.__role
