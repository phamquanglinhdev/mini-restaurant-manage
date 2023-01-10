import UserController
import AuthController

# if UserController.addUser():
#     UserController.showUser()
currentUser = AuthController.checkLogin()
if currentUser is not None:
    print("Login successfully !")
    print(currentUser.__dict__)
