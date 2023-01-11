def addUser():
    from database import users
    from User import User
    username = input("Username:")
    password = input("Password:")
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
    print("___________________________________________")
    for user in users:
        print("ID:" + str(user.getId()), end=" | ")
        print("Username:" + user.getUserName(), end=" | ")
        print("Role:" + user.getRole(), end=" | ")
        print()
        print("___________________________________________")
