favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
participants_list = ['jen','phil','rose','michael']
for person in participants_list:
    if person in favorite_languages:
        print(f'{person.title()}, thank you for taking the poll.')
    elif person not in favorite_languages:
        print(f'{person.title()}, please take the poll.')