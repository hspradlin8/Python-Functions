# Iterating with Enumerate

groceries = ['roast beef', 'cucumbers', 'lettuce',
             'peanut butter', 'bread', 'dog food']

# you put a 1 by groceries so the list will start at 1.
# otherwise it will start 0.
for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')
