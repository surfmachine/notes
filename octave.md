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

        
## Variables
 
Command             | Description                   
------------------- | ---------------------------------------------------------      
a = 3               | Define variable a and assign the value 3 (numeric defaults to double  type)
a = int16(3)        | Define variable a and assign the value 3 as type int16
a = magic(8)        | Create array with 8 rows and 8 columns of 
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
        
        
## Misc

Command             | Description                   
------------------- | ---------------------------------------------------------      
%                   | Comment till end of line
PS1(‘>> ‘)          | Change prompt to ‘>> ‘
addpath(‘p’)        | Add path p (like c:/dev/workspace/octave) to octave
v = csvread(‘f’)    | Read csv file f into octave and assign it to variable v
num2str             | Convert number to string
   
-------------------------------------------------------------------------------
_The end._

