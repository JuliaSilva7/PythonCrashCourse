pizzas = ['pepperoni', 'chicken with catupiry', 'margherita']
friend_pizza = pizzas[:]
pizzas.append('bacon')
friend_pizza.append('shrimp')
print("\nMy favorite pizzas are: " + ", ".join([pizza.title() for pizza in pizzas]))
print("My friend's favorite pizzas are: " + ", ".join([pizza.title() for pizza in friend_pizza]))
