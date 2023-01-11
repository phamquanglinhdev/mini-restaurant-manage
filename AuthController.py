def checkLogin():
    from database import users
    # username = (input("Your Username:"))
    # password = input("Your Password:")
    username = "phamquanglinh"
    password = "9999"
    for user in users:
        if user.getUserName() == username:
            if user.getPassword() == password:
                return user
            else:
                print("Wrong Password !")
                return None
    print("Cannot find user !")
    return None
