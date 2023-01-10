from User import User

users = []
initAdmin = User()
initAdmin.setId(1)
initAdmin.setUserName("phamquanglinh")
initAdmin.setPassword("99999999")
initAdmin.setRole("admin")
users.append(initAdmin)

initUser = User()
initUser.setId(2)
initUser.setUserName("user1")
initUser.setPassword("99999999")
initUser.setRole("user")
users.append(initUser)
