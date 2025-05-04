current_users = ['lena', 'john', 'marie', 'ronnie', 'anna']
new_users = ['rick', 'Marie', 'ronnie', 'annabeth', 'liana']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('This username is already being used.')
    else:
        print('This name is available.')
