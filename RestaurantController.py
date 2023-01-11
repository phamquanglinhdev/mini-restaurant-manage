def addRestaurant(ownerId):
    from database import restaurants
    from Restaurant import Restaurant
    maxId = 0
    for restaurant in restaurants:
        if maxId < restaurant.getId():
            maxId = restaurant.getId()
    name = input("Restaurant name:")
    address = input("Address:")
    newRestaurant = Restaurant()
    newRestaurant.setId(maxId + 1)
    newRestaurant.setName(name)
    newRestaurant.setAddress(address)
    newRestaurant.setOwnId(ownerId)
    restaurants.append(newRestaurant)
    print("Add successfully !")


def showRestaurant():
    from database import restaurants
    print("_____________________________________________")
    for restaurant in restaurants:
        print("ID", restaurant.getId())
        print("Name:", restaurant.getName())
        print("Owner:", restaurant.getOwnerUserName())
        print("Address:", restaurant.getAddress())
        print("_______________________________________")
