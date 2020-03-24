# Edit the variable assignment under the provided function
#  so that the tuple returned from the function call is unpacked
#  into 2 variables, val1, val2


def unpacker(*args):
    return args


val1, val2 = unpacker('Python', 'rocks!')
