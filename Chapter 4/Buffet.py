dishes = 'fish', 'french fries', 'mousse', 'cheeseburger', 'chocolate cake'
print(f"{', '.join([dish.title() for dish in dishes])}")
dishes = 'fish', 'french fries', 'mousse', 'cheesecake', 'strawberry cake'
print(f"The new menu is composed of {', '.join([dish.title() for dish in dishes])}")