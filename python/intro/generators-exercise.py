# Exercise
# Write a generator function which returns the Fibonacci series.
# They are calculated using the following formula:
# - The first two numbers of the series is always equal to 1,
#   and each consecutive number returned is the sum of the last two numbers.
# - Hint: Can you use only two variables in the generator function?

# Remember that assignments can be done simultaneously.
# The code will simultaneously switch the values of a and b.
# Code:
#   a = 1
#   b = 2
#   a, b = b, a
#   print(a,b)
# Output:
#   2 1

# fill in this function
def fib():
    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break