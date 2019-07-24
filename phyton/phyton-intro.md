Phyton Intro
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# Basics

**Phyton 3**
https://docs.python.org/3/library/index.html

**Tutorial**
- https://www.learnpython.org 
- https://www.datacamp.com/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials


## Functions
Sample:
```
def my_function_with_args(username, greeting):
    print("Hello %s, i wish you %s"%(username, greeting))
    
my_function_with_args("Tom", "a nice weekend")   
```

Sample:
```
def sum_two_numbers(a, b):
    return a + b

res = sum_two_numbers(3,9)
print (res)
```

## Classes & Objects
Sample:
```
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# call a object function
myobjectx.function()
```

## Dictionaries

**Initialize samples**
```
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
```

```
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
```

**Iterate over dictionary**
```
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
```

**Remove a value**
```
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
```

**Add a value**
```
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)
```

## Modules & Packages

### Modules

**Import a module**
```
# game.py

# import the module draw.py 
import draw

# use methode draw_game() from the draw module
def main():
    result = play_game()
    draw.draw_game(result)
```

**Importing module objects to the current namespace**
```
# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)
```

**Importing all objects from a module**
```
# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)
```

**Custom import name**
```
# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
```

**Module initialization**
```
# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()
```

### Built-in modules

**Exploring built-in modules**
```
# import the library
import urllib

# use it
urllib.urlopen(...)
```

**Show details of a module**
```
>>> import urllib
>>> dir(urllib)
```

### Packages

Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.

Each package in Python is a directory which **MUST** contain a special file called **\_\_init__.py**. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. We also must not forget to add the \_\_init__.py file inside the foo directory.

**Import**
In the first method, we must use the foo prefix whenever we access the module bar. In the second method, we don't, because we import the module to our module's namespace.
```
import foo.bar 
or
from foo import bar
```

**Export modules**
The __init__.py file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the __all__ variable, like so:
```
__init__.py:

__all__ = ["bar"]
```

-------------------------------------------------------------------------------
# Data Science Tutorials

## Numpy Array

Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays.


### Create numpy arrays
In the following example, you will first create two Python lists. Then, you will import the numpy package and create numpy arrays out of the newly created lists.

```
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))
```

### Element-wise calculations
Now we can perform element-wise calculations on height and weight.
- For example, you could take all 6 of the height and weight observations above, and calculate the BMI for each observation with a single equation. 
- These operations are very fast and computationally efficient. 
- They are particularly helpful when you have 1000s of observations in your data.

```
# Calculate bmi: weight : (height)2     // gewicht geteilt durch höhe im quadrat
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)
```

### Subsetting
Another great feature of Numpy arrays is the ability to subset. For instance, if you wanted to know which observations in our BMI array are above 23, we could quickly subset it to find out.

```
# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]
```

## Pandas Basics

### DataFrames
Pandas is a high-level data manipulation tool developed by Wes McKinney.
It is built on the Numpy package and its key data structure is called the DataFrame.
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

**There are several ways to create a DataFrame. One way way is to use a dictionary. For example:**
```
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
```

**Set the index for brics**
As you can see with the new brics DataFrame, Pandas has assigned a key for each country as the numerical values 0 through 4.
If you would like to have different index values, say, the two letter country code, you can do that easily as well.
```
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
```

**Another way to create a DataFrame is by importing a csv file using Pandas**
```
# Now, the csv cars.csv is stored and can be imported using pd.read_csv:
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
```


### Indexing DataFrames
There are several ways to index a Pandas DataFrame.
One of the easiest ways to do this is by using square bracket notation.
In the example below, you can use square brackets to select one column of the cars DataFrame.
- You can either use a single bracket or a double bracket.
- The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.

```
# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])
```

**Square brackets can also be used to access observations (rows) from a DataFrame. For example:**
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])
```

### loc & iloc
You can also use loc and iloc to perform just about any data selection operation
- loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
- iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
```

-------------------------------------------------------------------------------
# Advanced

## Generators

Generators are very easy to implement, but a bit difficult to understand.

Generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.

**yield**
When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

Here is a simple example of a generator function which returns 7 random integers:
```
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
```

## List Comprehensions

List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

**Sample**
For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
```
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)
```

Using a **list comprehension**, we could simplify this process to this notation:
```
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
```

## Multiple Function Arguments and Arguments by keyword

**Multiple Function Arguments**
It is possible to declare functions which receive a variable number of arguments, using the following syntax: __*args__
```
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5)
```

>The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function after the first 3 arguments.

**Arguments by keyword**
It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax: __**args__
```
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
```

>The following code yields the following output: The sum is: 6 Result: 1


## Regular Expressions

**Reference**
https://docs.python.org/3/library/re.html#regular-expression-syntax%22RE%20syntax 

**Sample**
```
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example
```


**Email sample**
```
# Exercise: make a regular expression that will match an email
import re

def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

# Your pattern here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)
```

## Exception Handling

**Reference**
https://docs.python.org/3/tutorial/errors.html#handling-exceptions

**Sample**
```
while True:
    try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")
```

**Multicatch**
```
except (RuntimeError, TypeError, NameError):
    ...
```

**Catch all**
```
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

## Sets & set operations (diff, intersection, etc.)

Sets are lists with no duplicate entries.
```
uniqueWords = set("my name is Eric and Eric is my name".split())
print(uniqueWords)
```
> Result:
> {'is', 'Eric', 'and', 'name', 'my'}

**Intersection**
o find out which members attended both events, you may use the "intersection" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))
```

**Symmetric difference**
To find out which members attended only one of the events, use the "symmetric_difference" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
```

**Difference**
To find out which members attended only one event and not the other, use the "difference" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))
```

**Union**
To receive a list of all participants, use the "union" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))
```

## Serialization (JSON)

Python provides built-in JSON libraries to encode and decode JSON.

In Python 2.5, the simplejson module is used, whereas in Python 2.7, the json module is used. Since this interpreter uses Python 2.7, we'll be using json.

**Import**
In order to use the json module, it must first be imported:
```
import json
```

**Formats**
There are two basic formats for JSON data. 
- string:
The String format is mainly used to pass the data into another program or load into a datastructure.

- object datastructure:
The object datastructure, in Python, consists of lists and dictionaries nested inside each other. The object datastructure allows one to use python methods (for lists and dictionaries) to add, list, search and remove elements from the datastructure. 

**Load**
To load JSON back to a data structure, use the "loads" method. This method takes a string and turns it back into the json object datastructure:
```
import json 
...
print(json.loads(json_string))
```

**Dump**
To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String:
```
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
```

## Partial functions

You can create partial functions in python by using the partial function from the functools library.

> Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.

**Import required**
```
from functools import partial
```

****
```
from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2 (replace x with 2)
dbl = partial(multiply,2)   
print(dbl(4))
```

> An important note: the default values will start replacing variables from the left. The 2 will replace x. y will equal 4 when dbl(4) is called. It does not make a difference in this example, but it does in the example below.


## Code Introspection

Code introspection is the ability to examine classes, functions and keywords to know what they are, what they do and what they know.

**Python provides several functions and utilities for code introspection**
```
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__
```

Often the most important one is the help function, since you can use it to find what other functions do:
> help(dir)
> help(hasattr)
> help(id)

## Closures

A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step

**Nested Function**
Firstly, a Nested Function is a function defined inside another function. 
```
def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

transmit_to_space("Test message")
```


**nonlocal**
It's very important to note that the nested functions can access the variables of the enclosing scope. However, at least in python, they are only readonly. However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.
```
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)

print_msg(9)
```
> Without the nonlocal keyword, the output would be "3 9", however, with its usage, we get "3 3", that is the value of the "number" variable gets modified. 

**return a function**
Now, how about we return the function object rather than calling the nested function within (remember that even functions are objects in Python).


```
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    
    return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
```

Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved. This technique by which the data is attached to some code even after end of those other original functions is called as closures in python

> ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.(Eg. When there are few methods in a class, use closures instead).

Also, Decorators in Python make extensive use of closures.


## Decorators

### Syntax /  Function

**Syntax**
Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. We shall deal with functions for this tutorial. 

The syntax:
```
@decorator
def functions(arg):
    return "value"

# Is equivalent to:
def function(arg):
    return "value"
function = decorator(function) 
```
> this passes the function to the decorator, and reassigns it to the functions

**Function**
As you may have seen, a decorator is just another function which takes a functions and returns one. For example you could do this:
```
def repeater(old_function):
    def new_function(*args, **kwds): 
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value
```

### Samples

**Repeat a function twice**
```
@repeater
def multiply(num1, num2):
    print(num1 * num2)

>>> multiply(2, 3)
6
6
```

**Change output**
You can also make it change the output
```
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function
```

**Change input**
```
def double_Ii(old_function):
    def new_function(arg): # only works if the old function has one argument
        return old_function(arg * 2) # modify the argument passed
    return new_function
```

**Do checking**
```
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    
    return new_function
```

**Multiply output by a variable amount**
Let's say you want to multiply the output by a variable amount. You could define the decorator and use it as follows:
```
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15
```

-------------------------------------------------------------------------------
# Conda

>> Execute command within the Anaconda Shell!

## Environment 

Command                              | Description
------------------------------------ | ---------------------------------------- 
conda info --envs                    | Show environments
conda create -n myenv phython=3.6.2  | Create environment with given phyton version
conda activate myenv                 | Activate the myenv environment
conda list                           | Show packages of active environment



-------------------------------------------------------------------------------
# Azure

- Create an Azure Machine Learning service workspace 
  https://docs.microsoft.com/en-us/azure/machine-learning/service/setup-create-workspace#sdk


-------------------------------------------------------------------------------
_The end._

