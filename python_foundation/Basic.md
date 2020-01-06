# Variable
Syntax: <variable> = <expr>

```python
x = 7
y = 4 + 5
z = "hello"
```

```python
my_var = 5
my_var = my_var + 1
```

```python
sum, mult = x + y, x * y
```

```python
x = 2
y = 4
x = y
y = x
# x ?? y ??
```

# Data Types
-type conversion

## Numerical Data
1. Integer
2. Float
3. Others (Binary etc)  

### Operator
Math Operator:
- +
- -
- *
- /
- //
- % 
- **

```python
num = 15
# num % 3 ?
# num % 7 ?
```

Assignment Operator*
Order of operation following math rules

## String
- Can use *
- Iterable but immutable
```python
"Hello" + " World"
```
```python
"Hello" * 5
```

### Indexing
```python
s = "hello world"
# s[0] ??? s[1] ??? s[13] ??
```

### Slicing
Syntax: **string[start_index : end_index]**
```python
s = "hello world"
# s[0:3] ??
# s[-1] ??
# s[:4] ??
```

### Length of string
Syntax: **len(string)**

### String Formatting

### String Method

### Escape Sequence

## Boolean
- True / False

### Comparison Operator
- <
- >
- ==
- !=
- >=
- <= 
- is
- is not

```python
li = [4, 5, 6]
li2 = li
li is li2
li is not None
```

### Logical Operator
- not 
- and
- or

### Membership Operator
For all sequences (string, list, tuple)
- in 
- not in

## List
- Have an index
- To access an element in a list: list[el]
- Iterable and mutable
```python
item_list = [1, 2, "hello"]
item_list[1] = [32]
# item_list ??

item_list2 = item_list
item_list2[0] = "world"
# item_list2 ?? item_list ??
```

### List Method

# Control Flow
Syntax: 
```
if Boolean:
    # Run this code if True
else:
    # Run this code if False
```

# Function
- To organize the program
- DRY principle
- One function for one functionality
- Recipe metaphor
Syntax:

```python
def function_name(parameter1, parameter2, ...):
    # BLOCK OF CODE
```

-indentation
-block

## Return Statement
- Optional
- return makes the function stop
- return a *value*

## Parameter
- Input for function

## Default Parameter
- Default Input for function

## Calling a function
-function_name(para1, para2, ...)
-Executing the function (running blocks of code inside the function)

## Local vs Global Scope




-print(<expr>, <expr>)
-comment #
-input -> <variable> = eval(input(<prompt>))
```python
if True:
    # block 1
else:
    # block 2
```