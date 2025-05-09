favorite_places = {
    'Annie': ['Paris', 'London', 'Berlin'],
    'Bruno': ['Tokyo', 'Porto', 'London'],
    'Carlos': ['New York', 'San Francisco', 'Paris']
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:", end=' ')
    for place in places:
        print(place, end='  ')
    print()
