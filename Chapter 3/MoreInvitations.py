guests = ['Rose', 'Rick', 'Adrian']
# Initial invitations
print(f'{guests[0]}, would you like to have dinner?')
print(f'{guests[1]}, would you like to have dinner?')
print(f'{guests[2]}, would you like to have dinner?')
print(f'{guests[1]} will not be able to come.')
# Removing Rick from the list, because he would not be able to come
guests.remove('Rick')
# Adding Jose to the list
guests.append('Jose')
# Making new invitations
print(f'\n{guests[0]}, would you like to have dinner?')
print(f'{guests[1]}, would you like to have dinner?')
print(f'{guests[2]}, would you like to have dinner?')
# People in the restaurant
print(f'The guests at the table were {guests[0]}, {guests[1]} and {guests[2]}')
guests.insert(0, 'John')
guests.insert(2, 'Tina')
guests.append('Liana')
# Making new invitations again
print(f'\n{guests[0]}, would you like to have dinner?')
print(f'{guests[1]}, would you like to have dinner?')
print(f'{guests[2]}, would you like to have dinner?')
print(f'{guests[3]}, would you like to have dinner?')
print(f'{guests[4]}, would you like to have dinner?')
print(f'{guests[5]}, would you like to have dinner?')
# Uninviting people
print('I can only invite two people to the dinner.')
uninvited = guests.pop()
print(f'\n{uninvited}, I am sorry for not being able to invite you.')
uninvited = guests.pop()
print(f'{uninvited}, I am sorry for not being able to invite you.')
uninvited = guests.pop()
print(f'{uninvited}, I am sorry for not being able to invite you.')
uninvited = guests.pop()
print(f'{uninvited}, I am sorry for not being able to invite you.')
# Maintaining invitations
print(f'\n{guests[0]}, you are still invited to the dinner.')
print(f'{guests[1]}, you are still invited to the dinner.')
# Deleting the names of the list
del[guests[0]]
del[guests[0]]
print(f'A lista vazia é {guests}')
