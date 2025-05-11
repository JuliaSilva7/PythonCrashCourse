dream_vacations = {}
while True:
    person = input('What is your name? ')
    place = input("If you could visit one place in the world, where would you go? ")
    dream_vacations[person] = place
    next_person = input('Would you like to continue the pool? [yes/no] ')
    if next_person == 'no':
        break

for person, place in dream_vacations.items():
    print(f'{person} wants to visit {place}!')
