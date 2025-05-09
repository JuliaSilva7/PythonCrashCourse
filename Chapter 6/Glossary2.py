glossary = {'len()': 'A function that counts the number of caracters in a string.',
            'list()': 'A function that creates a list.',
            'int()': 'A function that converts a string to an integer.',
            'print()': 'A function that displays a message on the screen.',
            'input()': 'A function that waits for the user to type something and then displays it.',
            'float()': 'A function that converts a string to a floating point number.',
            'range()': 'A function that creates a sequence of numbers.',
            'str()': 'A function that converts a number or a list into a string.',
            'sorted()': 'A function that sorts a list.',
            'set()': 'A function that creates a set.',}

for word, definition in glossary.items():
    print(f'{word.title()}: {definition}\n')