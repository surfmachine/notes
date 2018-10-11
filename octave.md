Octave
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# References 

- Octave Software  
  https://www.gnu.org/software/octave

- Octave Download
  https://ftp.gnu.org/gnu/octave

- Installation tips from the machine learning course
  https://www.coursera.org/learn/machine-learning/discussions/all/threads/vgCyrQoMEeWv5yIAC00Eog?page=2


-------------------------------------------------------------------------------
# Commands

## Math

Command             | Description                   |  Sample
------------------- | ----------------------------- | -------------------------   
^                   | hoch                          | 2^6 = 64
==                  | Gleich                        |
~=                  | Ungleich                      |
&&                  | AND                           |
\|\|                | OR                            |
xor(x,y)            | XOR                           |
pi                  | Value of pi                   | a = pi 

        
## Variables
 
Command             | Description                   
------------------- | ---------------------------------------------------------      
a = 3               | Define numeric with value 3 of type double (default)
a = int16(3)        | Define numeric with value 3 of type int16
s = 'hi'            | Define text with value 'hi'
b = (3 >= 1)        | Define boolean with value 1 (true)
b = (1 >= 3)        | Define boolean with value 0 (false)
v = [1 2 3]         | Define vector 1 column (matrix 1 row / 3 colum)
v = [1; 2; 3;]      | Define vector 1 row    (matrix 3 row / 1 colum)
v = 1 : 6           | Define vector 1 column with values: 1 2 3 4 5 6
v = 1 : 0.1 : 2     | Define vector 1 column with values: 1 1.1 ... 1.9 2.0
v = zeros(1,3)      | Define vector 1 column with values: 0 0 0
v = onces(1,3)      | Define vector 1 column with values: 1 1 1
v = 3*onces(1,3)    | Define vector 1 column with values: 3 3 3
A = [1 2 3; 4 5 6]  | Define matrix with 2 rows and 3 columns of doubles
A = onces(2, 3)     | Define matrix with 2 rows and 3 columns with values 1
A = 3*onces(2, 3    | Define matrix with 2 rows and 3 columns with values 3
A = rand(2,3)       | Define matrix with 2 rows and 3 columns with random (uniform) values ^4^
A = randn(2,3)      | Define matrix with 2 rows and 3 columns with random (gaussian) values ^5^
A = magic(8)        | Define matrix with 8 rows and 8 columns of doubles
I = eye(3)          | Define identity/diagonal matrix with 3 rows and columns
num2str             | Convert number to string
v = csvread(‘f’)    | Read csv file f into octave and assign it to variable v
size(a)             | Show dimension (number of rows and number of columns). ^1,2,3^
class(v)            | Show type of variable, like double or char. ^3^
who                 | Show variables in the current scope (also shown in the workspace)
clear a             | Remove variable a 
clear all           | Remove all variables


Notes:
 1) Octave stores all data in the form of multi-dimensional arrays (of the same type). 
 2) For arrays of mixed types, see “cell array” type. 
 3) The result is stored within  “ans”.
 4) The rand() function returns random numbers of a uniform probability density 
    function distributed between 0 and 1.
 5) The randn() function returns random numbers of a gaussian probability density 
    function distributed with a mean of zero and a standard-deviation of one.

Samples:

Command                                     | Description                   
------------------------------------------- | ---------------------------------  
w = -6 + sqrt(10)*(randn(1,1000));          |  create vector with 1000 random values
hist(v, 50)                                 |  show graph  
        
## Shell

Command             | Description                   
------------------- | ---------------------------------------------------------   
%                   | Comment till end of line
;                   | Suppress output, like: a = 3;
a                   | Display value(s) of variable a
disp(a)             | Display value(s) of variable a (used for more complex types)
disp(sprintf(...))  | Display text and variables, like: sprintf('Value a=%0.2f',a)
format long         | Display numbers with 14 decimal places
format short        | Display numeric with  4 decimal places
PS1(‘>> ‘)          | Change prompt to ‘>> ‘
addpath(‘p’)        | Add path p (like c:/dev/workspace/octave) to octave
v = csvread(‘f’)    | Read csv file f into octave and assign it to variable v
hist(v)             | Diagram of variable v with default number of samples
hist(v, 50)         | Diagram of variable v with 50 samples    
help eye            | Help for the command eye
help randn          | Help for the command randn    
help help           | Help of the help
   
-------------------------------------------------------------------------------
_The end._

