users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin! Would you like you see a relatory of status? ')
        else:
            print('Hello ' + user+ '! Thank for logging in again.')
else:
    print('We need to find some users!')
