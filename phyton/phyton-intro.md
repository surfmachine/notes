Phyton Intro
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# Intro

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
_The end._

