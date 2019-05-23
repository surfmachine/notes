Phyton
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# Basics

**Tutorial**
- https://www.learnpython.org 


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


-------------------------------------------------------------------------------
_The end._

