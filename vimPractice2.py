#
# Example file for functions
#


# define a function
def function1():
    print("IN: function1")

# defining function with aurguments
def function2(arg1, arg2):
    print(arg1, arg2)



# defining a function that returns a value
def cube(x):
    return(x*x*x)


# defining a function that uses default values
def power(number, x=1):
    result = 1
    for i in range(x):
        result = result * number
    return result


# defining a function with variable aurguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# call functions here
print("PROGRAM OUTPUT")
function1()
function2("hello", "world")
print("The value of the cube is:", cube(3))
# print(function1())
# print(function2)
print("The rusult of the power is:", power(5, 2))
print("The default of the power is:", power(5))
print("The argument declaration of the power is:", power(x=5, number=2))
print("The various arguments added is:", multi_add(1, 2, 3))
