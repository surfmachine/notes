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

## Basic operations

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
A = magic(8)        | Define matrix with N-by-N magic square of doubles
I = eye(3)          | Define identity/diagonal matrix with 3 rows and columns
O = flipud(eye(3))  | Define opposite identity matrix
num2str             | Convert number to string
v = csvread(‘f’)    | Read csv file f into octave and assign it to variable v
length(v)           | Show length of a vector
size(a)             | Show dimension (number of rows and number of columns). ^1,2,3^
class(v)            | Show type of variable, like double or char. ^3^
who                 | Show variables in the current scope (also shown in the workspace)
whos                | Show vairables witd details (name, size, bytes, class)
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


## Files and directories

Command             | Description                   
------------------- | ---------------------------------------------------------   
pwd                 | Print working directory (show current directory)
cd 'p'              | Change to directory p
addpath(‘p’)        | Add path p (like c:/dev/workspace/octave) to octave
ls                  | List directories
load f              | Load file f 
load ('f')          | Load file f 
v = csvread(‘f’)    | Read csv file f into octave and assign it to variable v
save f.mat v;       | Save data of v in compressed format to current directory
save f.txt v -ascii;| Save data of v in text format (ascii)


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
hist(v)             | Diagram of variable v with default number of samples
hist(v, 50)         | Diagram of variable v with 50 samples    
help eye            | Help for the command eye
help randn          | Help for the command randn    
help help           | Help of the help

-------------------------------------------------------------------------------
# Samples

## Moving data around

### Vector with graph
Create vector with 1000 random values (and some calculation) 
and show graph with 50 samples:
```
w = -6 + sqrt(10)*(randn(1,1000));
hist(v, 50)                       
```

### Size 
Show size of a matrix 
or size of a single dimension (row or column) of a matrix:
```
A= [1 2; 3 4; 5 6]
size(A)                             % show size of matirx, ans = 3 2
sz = size(A);                       % result of size is a 1x2 matrix (vector)
size(A,1)                           % number of rows of size, ans = 1
size(A,2)                           % number of colums of size, ans = 2
```

### Length
Show length of a vector 
or largest dimension (row or column) of a matrix
```
v = [1 2 3]
length(v)                           % show length of the vector, ans = 3
A= [1 2; 3 4; 5 6]
length(A)                           % show largest dimension of A, ans = 3
```

### Load file with vector data, create partial vector and save to file
Load the file 'prices' with 1000 rows (let's say 1 2 ... 1000)
and then create a vector with 10 rows starting from index 1 to 10
and then save the data of the new vector to a file:
```
load prices                         % prices = [1 2 3 ... 1000]
v = prices /1:10                    % v = [1 2 3 4 5 6 7 8 9 10]
save prices2.mat v;                 % save data of v in compressed format
save prices3.txt v - ascii          % save data of v in text format (ascii)
```

### Show partial data of an array with ":"
Show partial data of an array with ":", which means every element along that row/column;  
```
A = [1 2; 3 4; 5 6];
    1   2
    3   4
    5   6
A (2,:)                             % show the data of row 2
    3   4
A (:,2)                             % show the data of column 2
    2
    4
    6
A ([1 3], :)                        % show the data of row 1 and 3
    1   2
    5   6
```

### Assign or add partial data of an array with new data
```
A = [1 2; 3 4; 5 6];
    1   2
    3   4
    5   6
A (:.2) = [10; 11; 12]
    1   10
    3   11
    5   12
A = [A, [100; 101; 102]];
    1   10   100
    3   11   101
    5   12   102
```

### Put all elements of a matrix into a vector
```
A = [1 2; 3 4];
    1   2
    3   4
A (:)
    1   
    3
    2
    4
```

### Concat matrix A and B
```
A = [1 2; 3 4];
    1   2
    3   4
B = [11 12; 13 14];
    11   12
    13   14
C = [A B]                           % Is the same as [A, B]
    1   2   11   12
    3   4   13   14
D = [A; B]
    1   2
    3   4
    11   12
    13   14
```

## Computing on data

### Test Data 
```
A = [1 2; 3 4; 5 6];
    1    2
    3    4
    5    6
B = [11 12; 13 14; 15 16];
    11   12
    13   14
    15   16
C = [1 1; 2 2]
    1    1
    2    2
v = [1; 2; 3]
```

### Multiplication
```
R=A*C               % Multiplication                
    5    5          % R row 1 = A * C row 1         
    11   11         % R row 2 = A * C row 2 
    17   17         % R (1,1) = A(1,1) * C(1,1) + A(1,2) * C(2,1)
```

### Multiplication element by element with "."
```
R=A .* B            
    11   24
    39   56
    75   96
```

### Create square with ".^"
```
R=A .^ 2           
    1    4      
    9    16
    25   36
```

### Create reciprocal with "./"
```
r=1 ./ v            
    1.00000   
    0.50000     
    0.33333
```

### Create log, exp, abs, negative
```
r=log(v)            % Create log
r=exp(v)            % Create exponent
r=abs(v)            % Create absolute value like abs(-3)=3
r=-v                % Create negative value like -1*v=-v
```

### Increment all values of a vector by one
```
r=v + ones(lenth(v),1);
r=v + 1;
```

### Transpose matrix
```
R=A'
    1   3   5
    2   4   6

R=(A')'             % Transpose of transpose gives back original A
```

### Maximum value
```
v = [1 15 2 0.5];        % vector:    
max(v)                   % ans = 15
[val, ind] = max(v))     % val = 15   ind = 2

A=[1 2; 3 4; 5 6];       % matrix
max(A);                  % maximum per row,        ans = 5 6
max(A, [], 1);           % maximum of 1st dimension of A (max, per row)
max(A, [], 2);           % maximun of 2nd dimension of A (max. per column)
max(max(A));             % maximun of the matrix,  ans = 6
max(A(:));               % maximum of vector A(:), ans = 6   
```

### compare & find element-wise
```
v = [1 15 2 0.5];        % vector:
v < 3                    % compare each element
    1  0  1  1    

find(v < 3)              % find elements <3 (conditon)
    1 3 4                % returns the indexes matching the condition  
 
[r, c] = find (A >=7)    % returns rows and columns witch match the condition
```

### sum & prod of vector
```
v = [1 15 2 0.5];        
sum(v);                  % ans = 18.500
prod(v);                 % ans = 15
```

### sum of matrix
```
A = [1 2; 3 4; 5 6]      % matrix
sum (A);                 % sum per column, ans = 9 12
sum(A,1);                % sum per 1st dimension (column), ans = 9 12
sum(A,2);                % sum per 2nd dimension (row), ans = 3 7 11 as row
```

### prod of matrix diagonal element-wise, then sum of matrix
```
A=magic(3);                    % create 3x3 matrix   
E=eye(3);                      % create 3x3 identiy 
R=A .* E;                      % multiply elementwise, only diagonal values are left
sum(R);                        % create sum of the diagoanl
sum(sum(A.*eye(3)))            % sum of diagonal values top/left to bottom/right
sum(sum(A.*flipud(eye(3))))    % sum of diagonal values bottom/left to top/right
```

### inverse of matrix (sudo inverse)
```
A=magic(3);                    % create 3x3 matrix   
B=pinv(A);                     % create inverse of A (i.e. 1/A(1,1), etc.) 
I=A*B                          % create identiy matrix (up to numerical roundof for the zero's) 
```


### round down & up with floor & ceil
```
v = [1 15 2 0.5];        
floor(v);                % ans = 1 15 2 0
ceil(v);                 % ans = 1 15 2 1
```

## Plotting data

### 

-------------------------------------------------------------------------------
_The end._

