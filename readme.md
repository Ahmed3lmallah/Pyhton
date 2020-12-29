# Python

**Content Table:**
1. [Python Basics](#python-basics)
	1. [Running files](#running-files)
	1. [Data Types, Numbers, and Operations](#data-types-numbers-and-operations)
		1. [Comments](#comments)
		1. [Order of Operations](#order-of-operations)
	1. [Strings & Printing](#strings--printing)
		1. [Concatenation](#concatenation)
		1. [Multi-line Printing](#multiline-printing)
		1. [Escaping](#escaping)
		1. [Repeating](#repeating)
	1. [Functions](#functions)
	1. [Tuples & Arrays](#tuples--arrays)
		1. [Arrays](#arrays)
		1. [Tuples](#tuples)
	1. [Lists and Dictionaries](#dictionaries-and-lists)
		1. [Lists](#lists)
		1. [Dictionaries](#dictionaries)
		1. [Summary](#summary)
	1. [Loops & Branching](#conditionals--loops)
		1. [Conditionals](#conditionals)
		1. [Simple While Loop](#simple-while-loop)
		1. [While with Break](#while-with-break)
		1. [Simple For loop](#simple-for-loop)
		1. [For loop with Continue](#for-loop-with-continue)
	1. [Dates & Times](#dates--time)
	1. [Modules](#modules)
	1. [File I/O](#file-io)
1. [Python Classes](#python-classes)
	1. [Classes](#classes)
	1. [Class Data and Methods](#class-data-and-methods)
	1. [Function Overloading](#function-overloading)
	1. [Inheritance](#inheritance)
	1. [Operator Overloading](#operator-overloading)

# Python Basics

We can run Python code by executing the `python` command in the terminal, assuming it was already installed.

## Running files

* Python 3: `python3 fileName.py`

* Python 2: `python fileName.py`

## Data Types, Numbers, and Operations

### Comments

	"""
	Comments
	"""

Inline comments: `# Comment`
	
### Order of Operations

* `()` (Parentheses)
* `**` (Exponent)
* `~ + -` (Unary Operations) 
* `* / % //` (Division & Multiplications), where `//` integer (floor) division, `/` float division, `%` modulus, and `/0` returns an error.	
* `>> <<` (Shift bitwise)
* `&` (AND bitwise)
* `^ |` (NOT, OR bitwise)
* `<= < > >=` (Comparison)
* `<> ++ !=` (Equality)
* `= %= /= //= -= += *= **=` (Assignment)

## Strings & Printing

To print, we simply use the `print()` function

### Concatenation

1. We can use concatenation as follows, `print("Rate: " + str(rate))`, where `str()` function is used to convert the data type to string.

1. Another way to do concatenation is as follows, `print("Rate: {}".format(str(rate)))`

1. Otherwise, we can also use the following format:

		start_date = "2018-01-01"
		print(f"Start date: {start_date}")
	
### Multiline Printing

	print("""
	This 
	is
	a
	multi-line
	string.
	""")
	
### Escaping

* New Lines 

		print("1\n2\n3")
	
* Tabs

		print("1\t2\t3")
	
* Backslashes

		print("\\")

* Quotes
	
		print("\'")
		print("\"")
	
#### Repeating

	print("#" * 5)

## Functions

Use `import math` to import functions from the `math` module

Use `def` to declare a function. Function code is everything indented after the `def` line up to the `return` statement.

	def my_function():
		print("myFunction")
		
	def another_function(val):
		return val * 100
		
	def repeat_print(s, times):
		print(s * times)
		
	def hypotenuse(x, y):
		return math.sqrt( x ** 2 + y ** 2)
		
	my_function()
	
	a = another_function(5)
	
	print("a: " + str(a))
	
	repeat_print("$", 5)
	
	b = 5
	
	print("Hypotenuse: " + str(hypotenuse(a, another_function(b))))
	
## Tuples & Arrays

### Arrays

Arrays are a sqeuence of elements and they are more constrained than lists.

We begin by importing thr `array` function from the `array` module:

	from array import array
	
First argument to the `array()` function is the type of the elements in the array:

	a1 = array('l') # Integer
	
We can initialize the arrays to values as follow:

	a2 = array('l', [10,20,30])

To initialize an array of characters we use the unicode `u` type:

	a3 = array('u', 'Hello')
	
For decimal values:

	a4 = array('d', [3.14, 2.71, 1.41])

* `.pop()` is used to remove the last value from the array

* `.append()` is used to append elements to the end of the array

* `insert(location, element)` is used to place an element at a specific location

To return the element at a specific index:

	print("a4[0]: " + str(a4[0]))

### Tuples

Tuples are sequence of elements that are immutable.

To initialize a tuple:

	t1 = (1,2,3)
	t2 = (1.1, 2.2, 3.3)
	t3 = ("Hello", "World")
	t4 = ("!")
	
To return the element at a specific index:

	print("t4[0]: " + str(t4[0]))

We can add two tuples by using `t3 + t4` this returns a new tuple with all elements of `t3` and `t4`.

## Dictionaries and Lists

### Lists

Lists are mutable sequences or generic sequencies of varying elements

	l0 = [] # empty list
	l1 = [5,10,15,20] # integer list
	l2 = [3, 'Hello'] # list of different types
	
* `.append(element)` can be used to append an element to the end of the list

To return the element at a specific index:

	print("l1[0]: " + str(l1[0]))

To return partial content of the list we can use `[:2]`, which will return everything in the list up to second element.

We can reassign values of elements in the list:

	l2[0] = 6
	
We can add two lists by using `l1 + l2` this returns a new list with all elements of `l1` and `l2`.

### Dictionaries

Dictionaries are similar to maps in Java, where we can define a data structure using a key-value pair.

	d0 = {}
	d1 = {'key':'value', 'key2':'value2'}
	d2 = {'key': 1, 'key2': 2}

To return an element using it's key:

	print("d1['key'])

We can reassign values of elements (or add new elements) in the dictionary:

	d1['key'] = 'reassigned value'
	d1['new key'] = 'new value'

* `.keys()` is used to return a list of keys in the dictionary.

* `.values()` is used to return a list of values in the dictionary.

#### Summary

* **Arrays**: mutable but all elements have to be of the same type - initialized using the `array()` function.
* **Tuples**: basically immutable arrays - initialized using `()`.
* **Lists**:  mutable and elements can be of different types - initialized using `[]`.
* **Dictionaries**: Similar to `maps` in Java - initialized using `{}`.

## Conditionals & Loops

### Conditionals

	a = 15
	if a < 15:
		print('a is less than 15')
	elif a == 15:
		print ('a is equal to 15')
	else:
		print('a isn\'t equal to 15')
		
### Simple While Loop

	while a > 0:
		print(a, end=' ')
		a -= 1

### While with Break

* Used to break out of the while loop

		while a > 0:
			if a == 7:
				break
			print(a, end=' ')
			a += 1

### Simple For Loop

	for i in c:
		print(i, end=' ')

### For Loop with Continue

* Used to skip current iteration

		for i in c:
			if i == 3:
				continue
			print(i, end=' ')

## Dates & Time

[Quick Dates & Time hands-on](./hands_on/dates_time.py)

## Modules

Modules are basic Python source files where we define objects or functions.

* `mymodule.py`

		def myFunction():
			return 'muFunction'

* Another file in the same directory
	
		import mymodule
		
		print(myFunction()) # returns an error
		
		print(mymodule.myFunction())
		
		from mymodule import myFunction
		
		print(myFunction()) # This works!

## File I/O

[Quick File I/O hands-on](./hands_on/file_io.py)

# Python Classes

## Classes

## Class Data and Methods

## Function Overloading

[Quick Classes, Data & Methods, and Function Overloading & Overriding hands-on](./hands_on/class.py)

## Inheritance

[Quick Class Inheritance hands-on](./hands_on/inheritance.py)

## Operator Overloading

[Quick Operator Overloading hands-on](./hands_on/operator_overloading.py)