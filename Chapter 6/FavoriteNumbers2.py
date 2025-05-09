favorite_numbers = {'Dina':[3,4,5],'Hannah':[77,100,2],'Jessica':[1,7],'Rei':[1,4],'Timmy':[9,4,88]}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number are: ", end='')
    for number in numbers:
        print(f"{number}", end='  ')
    print()