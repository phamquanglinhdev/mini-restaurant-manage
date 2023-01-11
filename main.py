import UserController
import AuthController

# if UserController.addUser():
#     UserController.showUser()
application = True
currentUser = AuthController.checkLogin()
if currentUser is not None:
    print("Login successfully !")
    import menu

    while application:
        print("===========================================")
        if currentUser.getRole() == "admin":
            menu.adminMenu()
            choose = int(input("Please choose:"))
            if choose == 1:
                import UserController

                UserController.addUser()
                input("Press anything to back to menu")
            elif choose == 2:
                import UserController

                UserController.showUser()
                input("Press anything to back to menu")
            elif choose == 3:
                import RestaurantController

                RestaurantController.addRestaurant(currentUser.getId())
                input("Press anything to back to menu")
            elif choose == 4:
                import RestaurantController

                RestaurantController.showRestaurant()
                input("Press anything to back to menu")
            else:
                print("Bye !")
                application = False
