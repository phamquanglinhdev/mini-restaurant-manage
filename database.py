from User import User
from Restaurant import Restaurant

users = []
initAdmin = User()
initAdmin.setId(1)
initAdmin.setUserName("phamquanglinh")
initAdmin.setPassword("9999")
initAdmin.setRole("admin")
users.append(initAdmin)

initUser = User()
initUser.setId(2)
initUser.setUserName("user1")
initUser.setPassword("99999999")
initUser.setRole("user")
users.append(initUser)

restaurants = []
initRestaurant = Restaurant()
initRestaurant.setId(1)
initRestaurant.setName("KFC")
initRestaurant.setAddress("USA")
initRestaurant.setOwnId(1)
restaurants.append(initRestaurant)
