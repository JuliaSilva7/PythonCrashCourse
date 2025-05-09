joe = {'name': 'Joe', 'animal_type': 'bird', 'owner': 'John'}
ymir = {'name': 'Ymir', 'animal_type': 'cat', 'owner': 'Daniel'}
maxi = {'name': 'Maxi', 'animal_type': 'dog', 'owner': 'Jane'}

pets = [joe, ymir, maxi]

for pet in pets:
    print(f"{pet['name']} is a {pet['animal_type']} and is owned by {pet['owner']}.")
