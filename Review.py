class Review:
    def __init__(self):
        self.__user_id = None
        self.__restaurant_id = None
        self.__point = None
        self.__message = None

    def setUserId(self, user_id):
        self.__user_id = user_id

    def getUserId(self):
        return self.__user_id

    def setRestaurantId(self, restaurant_id):
        self.__restaurant_id = restaurant_id

    def getRestaurantId(self):
        return self.__restaurant_id

    def setPoint(self, point):
        self.__point = point

    def getPoint(self):
        return self.__point

    def setMessage(self, message):
        self.__message = message

    def getMessage(self):
        return self.__message

    def showReview(self):
        username = None
        from database import users
        for user in users:
            if user.getId() == self.getUserId():
                username = user.getUserName()
        print(username, ":", self.getMessage())
