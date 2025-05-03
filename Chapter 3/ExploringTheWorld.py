places = ['Japan', 'Italy','Germany','Spain','China']
print(places)
# Organizing the list in alphabetical order, without changing the original
print(f'\n{sorted(places)}')
# The original list remains unchanged
print(places)
# Organizing the list in reverse alphabetical order, without changing the original
print(f'\n{sorted(places, reverse=True)}')
# The original list remains unchanged
print(places)
# Reversing the list order
places.reverse()
print(f'\n{places}')
# Reversing the list order again
places.reverse()
print(f'\n{places}')
# Organizing the list in alphabetical order
places.sort()
print(f'\n{places}')
places.sort(reverse=True)
print(f'\n{places}')
# Length of the list
length = len(places)
print(f'\nThe list has {length} items.')