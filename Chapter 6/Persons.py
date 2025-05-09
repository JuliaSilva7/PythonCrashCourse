person1 = {'first_name': 'Rose', 'last_name': 'Young', 'age': 34, 'city': 'New York'}
person2 = {'first_name': 'John', 'last_name': 'Smith', 'age': 30, 'city': 'Boston'}
person3 = {'first_name': 'Jane', 'last_name': 'Doe', 'age': 29, 'city': 'Washington'}
persons_list = [person1, person2, person3]

for person in persons_list:
    print(
        f"The person name is {person['first_name']} {person['last_name']}. She is {person['age']} years old and lives in {person['city']}.")
