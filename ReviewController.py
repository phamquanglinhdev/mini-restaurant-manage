def addReview(userId, restaurantId):
    from database import reviews
    from Review import Review
    newReview = Review()
    newReview.setUserId(userId)
    newReview.setRestaurantId(restaurantId)
    newReview.setPoint(int(input("Point for restaurant:")))
    newReview.setMessage(input("Your message:"))
    reviews.append(newReview)
