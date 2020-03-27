# Edit the variable assignment under the provided function
#  so that the tuple returned from the function call is unpacked
#  into 2 variables, val1, val2


def unpacker(*args):
    return args


val1, val2 = unpacker('Python', 'rocks!')


# Range Challenge:
# Write a for loop that iterates over a range with a stop value of 10
# (assume the start value is 0 and the step value is 1).
# The body of the for loop should append the current value to the
# provided list called my_list.
# To append a value to a list, use the syntax my_list.append(val).

my_list = []

for i in range(10):
    my_list.append(1)

# Sequence challenge: Len, Min, & Max
# Find the len, min, and max of student_gpas

student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]
length = len(student_gpas)
max_gpa = max(student_gpas)
min_gpa = min(student_gpas)
