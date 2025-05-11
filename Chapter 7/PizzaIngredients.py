while True:
    ingredients = input('Enter ingredients for your pizza: ').title()
    if ingredients == 'Quit':
        break
    print(f'{ingredients} will be added to your pizza.')
