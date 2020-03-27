#Slice [ start, stop, step]
# start and stop vaule refer to elements of a sequence

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors_partial = colors[3:6]
print(colors_partial)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[1:6]
print(nums_partial)

# In(Returns boolean indicating whether item is in sequence):

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

3.2 in student_gpas  # True

# Not In(Returns a boolean indicating whether an item is not in a sequence):

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

'Jellybean' not in my_pets  # True

# Len =  lenght- returns the lenght of the past sequence
# Min = returns the smallest element in the sequence
# Max = returns the largest element in the sequence

# Lexicographical ordering is very similar to alphabetical ordering, but it considers additional characters besides the letters of the alphabet.
# Some of the basic rules in Python are that:
# 1) Uppercase letters come earlier than lowercase letters. This means that A < Z < a < z.
# 2) Numbers come earlier than letters. This means that 0 < 9 < A < a.
#3) Space characters come before all printable characters.#

# Membership Testing:

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits  # False
'eggplant' not in fruits  # True

'eggplant' in vegetables  # True
'eggplant' not in vegetables  # False

# Membership Testing: Index:

nums = range(1, 10, 2)

nums.index(5)  # 2
nums.index(10)  # ValueError: 10 is not in list
nums.index(1)  # 0

# Membership Testing: Range:

# example 1:
nums = range(10)

0 in nums  # True
10 in nums  # False
4 in nums  # True

0 not in nums  # False
15 not in nums  # True
10 not in nums  # True

# example 2:
nums = range(1, 10, 2)

0 in nums  # False
6 in nums  # False

4 not in nums  # True
8 not in nums  # True

# Indexes(Returns index of first occuring passed item):

my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog')  # 0
my_pets.index('chicken')  # 3
my_pets.index('lizard')  # ValueError: 'lizard' is not in list

# Count(Returns the number of times an item appears in a sequence):

my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']

my_pets.count('cat')  # 2
my_pets.count('lizard')  # 0

# Concatenation(Attaches one sequence to the end of another) and Multiplcation:

obj1 = [1, 2, 3, 4, 5]
obj2 = [6, 7, 8, 9, 10]

obj1 = obj1 + obj2
print(obj1)

str = 'python'

print(str * 5)
