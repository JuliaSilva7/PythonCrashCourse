rivers = {'nile': 'egypt', 'amazon': 'brazil', 'seine': 'france'}
for river,contry in rivers.items():
    print(f'The {river.title()} runs through {contry.title()}.')
for river in rivers.keys():
    print(f'River: {river.title()}')
for country in rivers.values():
    print(f'Country: {country.title()}')
