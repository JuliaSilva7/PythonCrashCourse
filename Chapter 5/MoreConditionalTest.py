car = 'Ford'
print(f'Is car == "Ford" ?')
print(car == 'Ford')
print(f'Is car != "Ford"?')
print(car != 'Ford')

user = 'Alex'
print(f'Is the name "Alex" already registered?')
print(user.lower() == 'alex')
print(f'Is the name "Richard" already registered?')
print(user.lower() == 'richard')

age = 18
print(f'Is that person underage?')
print(age < 21)
print(f'Is that person of legal age?')
print(age >= 21)

rose_age = 21
john_age = 17
print(f'Are Rose and John of legal age?')
print(rose_age >= 21 and john_age >= 21)
print(f'At least one of them are of legal age?')
print(rose_age >= 21 or john_age >= 21)

numbers_list = [1,2,3,4,5]
number = 5
print(f'Is number 5 in list?')
print(number in numbers_list)
print(f'Is number 5 not in list?')
print(number not in numbers_list)

