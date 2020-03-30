course = {'teacher': 'Ashley',
          'title': 'Introducing Dictionaries', 'level': 'Beginner'}

for item in course.item():
    print(item)

# OR

for key, value in course.items():
    print(key)
    print(value)
