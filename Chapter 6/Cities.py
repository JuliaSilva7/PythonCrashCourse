cities = {
    'London': {
        'country': 'England',
        'population': 9000000,
        'fact': 'London is home to the historic Tower of London'
    },
    'New York': {
        'country': 'USA',
        'population': 8400000,
        'fact': 'New York is known as the "Big Apple"'
    },
    'Berlin': {
        'country': 'Germany',
        'population': 3600000,
        'fact': 'Berlin was once divided by the Berlin Wall'
    }
}

for city, informations in cities.items():
    print(
        f"The city of {city} is located at {informations['country']}. {informations['fact']} and It's population is {informations['population']}.")
