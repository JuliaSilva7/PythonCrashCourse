ingredients = ''
while ingredients!='quit':
    ingredients = input('Enter ingredients for your pizza: ').lower()
    if ingredients != 'quit':
        print(f'{ingredients} will be added to your pizza.')

active = True
while active:
    ingredients = input('Enter ingredients for your pizza: ').lower()
    if ingredients == 'quit':
        active = False
    else:
        print(f'{ingredients} will be added to your pizza.')

while True:
    ingredients = input('Enter ingredients for your pizza: ').lower()
    if ingredients == 'quit':
        break
    print(f'{ingredients} will be added to your pizza.')


