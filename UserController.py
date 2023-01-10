def addUser():
    from database import users
    from User import User
    username = input("Username:")
    password = input("Password")
    maxId = 0
    for user in users:
        if user.getId() > maxId:
            maxId = user.getId()

    for user in users:
        if user.getUserName() == username:
            print("Exist user")
            return False

    newUser = User()
    newUser.setId(maxId + 1)
    newUser.setUserName(username)
    newUser.setPassword(password)
    newUser.setRole("user")
    users.append(newUser)
    print("Successfully!")
    return True


def showUser():
    from database import users
    for user in users:
        print(user.__dict__)
