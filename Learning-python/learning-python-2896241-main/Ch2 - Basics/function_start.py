#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def fun1():
    print('The first function!')

fun1()

# TODO: function that takes arguments
def fun2(a, b):
    print(a + b)

fun2(2,5)

# TODO: function that returns a value
def fun3(x):
    return x*x

print(fun3(4))

# TODO: function with default value for an argument
def fun4(b, a = 2):
    print(a, b)

fun4(4)
fun4(6, 3)

# TODO: function with variable number of arguments
def fun5(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(fun5(5, 6))