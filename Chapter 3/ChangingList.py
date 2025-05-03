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
print(f'{guests[0]}, would you like to have dinner?')
print(f'{guests[1]}, would you like to have dinner?')
print(f'{guests[2]}, would you like to have dinner?')
