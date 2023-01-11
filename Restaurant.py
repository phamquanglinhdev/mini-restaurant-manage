class Restaurant:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__owner_id = None
        self.__address = None

    def setId(self, ids):
        self.__id = ids

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setOwnId(self, own_id):
        self.__owner_id = own_id

    def getOwnId(self):
        return self.__owner_id

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def getOwnerUserName(self):
        from database import users
        for user in users:
            if user.getId() == self.__owner_id:
                return user.getUserName()
