course = {'teacher': 'Ashley',
          'title': 'Introducing Dictionaries', 'level': 'Beginner'}

for item in course.item():
    print(item)

# OR

for key, value in course.items():
    print(key)
    print(value)

# Packing with dictionaries:


def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacher(name='Ashley', job='Instructor', topic='Python')


# Unpacking with Dictionaries:

teacher = {
    'name': 'Ashley',
    'job': 'Instructor',
    'topic': 'Python'
}


def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)


print_teacher(**teacher)
