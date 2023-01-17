import UserController
import AuthController

# if UserController.addUser():
#     UserController.showUser()
try:
    application = True
    currentUser = None
    while application:
        if currentUser is None:
            currentUser = AuthController.checkLogin()
        if currentUser is not None:
            print("Login successfully !")
            import menu

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

                    sortType = int(input("Sort By (1 = Id, 2= Name):"))
                    if sortType == 1:
                        RestaurantController.showRestaurant()
                    else:
                        RestaurantController.sortByNameRestaurant()
                    input("Press anything to back to menu")
                elif choose == 5:
                    import RestaurantController

                    RestaurantController.showRestaurant()
                    RestaurantController.editRestaurant(int(input("Enter id of restaurant:")), currentUser)
                    input("Press anything to back to menu")
                elif choose == 6:
                    import RestaurantController

                    RestaurantController.showRestaurant()
                    RestaurantController.showSingleRestaurant(int(input("Show restaurant ? Id :")))
                    input("Press anything to back to menu")
                elif choose == 7:
                    import RestaurantController
                    import ReviewController

                    RestaurantController.showRestaurant()
                    ReviewController.addReview(currentUser.getId(), int(input("Review restaurant ? Id:")))
                    input("Press anything to back to menu")
                elif choose == 8:
                    currentUser = None
                else:
                    print("Bye !")
                    application = False
            elif currentUser.getRole() == "user":
                menu.userMenu()
                choose = int(input("Please choose:"))
                if choose == 1:
                    import RestaurantController

                    RestaurantController.addRestaurant(currentUser.getId())
                    input("Press anything to back to menu")
                elif choose == 2:
                    import RestaurantController

                    sortType = int(input("Sort By (1 = Id, 2= Name):"))
                    if sortType == 1:
                        RestaurantController.showRestaurant()
                    else:
                        RestaurantController.sortByNameRestaurant()
                    input("Press anything to back to menu")
                elif choose == 3:
                    import RestaurantController

                    RestaurantController.showRestaurant()
                    RestaurantController.editRestaurant(int(input("Enter id of restaurant:")), currentUser)
                    input("Press anything to back to menu")
                elif choose == 4:
                    import RestaurantController

                    RestaurantController.showRestaurant()
                    RestaurantController.showSingleRestaurant(int(input("Show restaurant ? Id :")))
                    input("Press anything to back to menu")
                elif choose == 5:
                    import RestaurantController
                    import ReviewController

                    RestaurantController.showRestaurant()
                    ReviewController.addReview(currentUser.getId(), int(input("Review restaurant ? Id:")))
                    input("Press anything to back to menu")
                elif choose == 6:
                    currentUser = None
                else:
                    print("Bye !")
                    application = False
except:
    print("Error ! Application will be stop")
