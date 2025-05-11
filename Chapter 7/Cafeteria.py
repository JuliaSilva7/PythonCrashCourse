sandwich_orders = ['tuna','meat','chicken','peanut']
finished_sandwichs = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich} sandwich is ready')
    finished_sandwichs.append(current_sandwich)

print("\nThe sandwiches that were prepared are:")
for sandwich in finished_sandwichs:
    print(f'- {sandwich}',end=' ')