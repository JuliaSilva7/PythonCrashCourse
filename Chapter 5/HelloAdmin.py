users = ['admin', 'john', 'marie', 'ronnie', 'anna']
for user in users:
    if user == 'admin':
        print('Hello Admin! Would you like you see a status report? ')
    else:
        print('Hello ' + user.title() + '! Thank for logging in again.')
