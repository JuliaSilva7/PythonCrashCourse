while True:
    age_ticket = int(input('What is your age? '))
    if age_ticket < 3:
        print('Your ticket is free')
    elif 12 >= age_ticket >= 3:
        print('Your ticket is 10 dollars')
    elif age_ticket > 12:
        print('Your ticket is 15 dollars')
    cinema = input("Do you wish to buy more tickets?  Type 'quit' if you don't want to buy more. ").lower()
    if cinema == 'quit':
        break