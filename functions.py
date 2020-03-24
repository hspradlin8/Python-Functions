# Packing
# example 1


def packer(*args):
    for val in args:
        print(val)


packer('hi', 'i', 'love', 'python')

# example 2


def packer_cat(*args):
    return val


packer('Hey', 'Lil', 'Jerry')

# Unpacking: strict and requires exactness

# example 1


def unpacker():
    return (1, 2, 3)


var1, var2, var3 = unpacker()

print(var1)
print(var2)
print(var3)

# example 2


def unpacker():
    return "Hey"


var1, var2, var3 = unpacker()

print(var1)
print(var2)
print(var3)
