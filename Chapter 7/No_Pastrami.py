sandwich_orders = ['pastrami', 'tuna', 'meat', 'pastrami', 'chicken', 'peanut', 'pastrami']
finished_sandwichs = []

if 'pastrami' in sandwich_orders:
    print('Sorry, we are out of pastrami.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich} sandwich is ready')
    finished_sandwichs.append(current_sandwich)

print("\nThe sandwiches that were prepared are:")
for sandwich in finished_sandwichs:
    print(f'{sandwich} - ', end=' ')
