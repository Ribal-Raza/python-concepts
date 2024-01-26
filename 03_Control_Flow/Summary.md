### Table of Contents
- [Control Flow](#control-flow)
    - [Conditional Statements](#conditional-statements)
        - [`if` statement](#if-statement)
        - [`else` statement](#else-statement)
        - [`elif` statement](#elif-statement)
        - [Different syntaxs](#different-syntax-variations)
            - [Inline If or Ternary](#inline-if-statements-ternary-operators)
            - [Nested if/else](#nested-if-statements)
    - [Looping Statements](#looping-statements)
        - [`for` Loop](#for-loop)
        - [`while` Loop](#while-loop)
        - [`break/continue` Statements](#break-and-continue-statements)
        - [Nested Loops](#nested-loops)
        - [Looping over Lists, Sets, Tuples and dicts](#looping-over-non-primitive-data-types)
        - [Considerations](#considerations-while-using-looping-statements)
    
# Control Flow
Control flow refers to the mechanism that determines the order in which statements in a program are executed. In simpler terms, it's like a roadmap that guides the computer on what to do next. Different control flow structures allow you to:

-   **Make decisions:** Based on certain conditions, choose which code to execute.
-   **Repeat tasks:** Execute a block of code multiple times, either a fixed number of times or until a condition is met.
-   **Skip or jump to different parts of your code:** Transfer control to a specific location in your program.
There are following control flow structures in python:
- Conditional Statements ( `if`, `else`, `elif` statements)
- Looping Statements (`while`, `do...while`, `for`, `for...in` etc)
- Break and Continue statements

## Conditional Statements
Conditional Statements are used to make decisions based on one or more conditions. 
### **`if` Statement:**

-   Executes a code block if a specified condition evaluates to True.
-   Syntax:
	```python
	if condition:
    # Code to execute if condition is True
	```

### **`else` Statement:**
-   Executes a code block if the `if` condition is False.
-   Optional, but often used to provide alternative actions.
-   Syntax:
	```python
	if condition:
	    # Code to execute if condition is True
	else:
	    # Code to execute if condition is False
	```

### **`elif` Statement:**

-   Short for "else if."
-   Allows for checking multiple conditions sequentially.
-   Only executes if preceding `if` and `elif` conditions are False.
-   Syntax:
	```python
	if condition1:
	    # Code to execute if condition1 is True
	elif condition2:
	    # Code to execute if condition1 is False and condition2 is True
	elif condition3:
	    # Code to execute if condition1 and condition2 are False and condition3 is True
	...
	else:
	    # Code to execute if all conditions are False
	```

### **Different Syntax Variations:**

#### **Inline If Statements (Ternary Operators):**

-   Concise way to write conditional logic within a single line.
-   Syntax:
	```python
	result = value1 if condition else value2
	```

#### **Nested If Statements:**

-   Place `if`,  `else`, or `elif` statements within other `if` statements.
-   Useful for more complex decision-making.
-   Syntax:
	```python
	if condition1:
	    # Code to execute if condition1 is True
	    if condition2:
	        # Code to execute if condition1 and condition2 are True
	    else:
	        # Code to execute if condition1 is True but condition2 is False
	else:
	    # Code to execute if condition1 is False

	```

**Example:**
```python
age = 25

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
## Looping Statements
Looping statements allow you to execute a block of code repeatedly until a certain condition is met or a specific iteration count is reached. This repetitive execution is essential for tasks like iterating through collections, performing calculations multiple times, or implementing game logic.

### **Different Types of Loops**

1. #### **`for` Loop:**

-   Used to iterate over elements in an iterable (list, tuple, string, set, dictionary).
-   Executes the code block for each element.
	```python
	numbers = [1, 2, 3, 4, 5]
	for number in numbers:
	    print(number)
	```

2. #### ** `while` Loop:**

-   Repeatedly executes a code block as long as a condition is True.
-   The condition is checked before each iteration.
	```python
	count = 0
	while count < 5:
	    print("Count:", count)
	    count += 1

	```

3. #### **`break` and `continue` Statements:**
-   `break`: Immediately exits the current loop.
-   `continue`: Skips the remaining statements in the current iteration and moves to the next.
**Example:**
	```python
	for i in range(10):
	    if i == 5:
	    break  # Exit the loop when i is 5
	    print(i)

	for i in range(10):
	    if i % 2 == 0:
	        continue  # Skip even numbers
	    print(i)
	```
### **Nested Loops:**

-   Inner loops are placed within outer loops.
-   The inner loop executes completely for each iteration of the outer loop.
-   Useful for iterating over multi-dimensional data structures.
	```python
	for row in range(3):
	    for col in range(4):
	        print(row, col)  # Prints (0, 0), (0, 1), ..., (2, 3)
	```

### **Looping over Non-primitive Data Types:**

1. **Lists and Tuples:**
    The  `for`  loop iterates over individual elements.
    ```python
    fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(fruit)
    ```
    
2. **Sets:**
    The  `for`  loop iterates over unique elements.
    ```python
    my_set = {1, 2, 3, 2}
    
    for element in my_set:
        print(element)  # Prints unique elements (1, 2, 3)
    
    ```
    
3. **Dictionaries:**
    The  `for`  loop iterates over keys or key-value pairs.
    ```python
    person = {"name": "Alice", "age": 30}
    
    # Iterate over keys
    for key in person:
        print(key)
    
    # Iterate over key-value pairs
    for key, value in person.items():
        print(key, value) 
    ```

### **Considerations while using looping statements:**
-   Choose the appropriate loop type (`for`  or  `while`) based on the iteration requirements.
-    Python doesn't have a `do...while` loop like some other languages.
-   Use  `break`  and  `continue`  judiciously to control loop flow.
-   Nested loops can be powerful but should be used cautiously to avoid complexity.
-   Adapt looping based on the data structure you're working with (lists, tuples, sets, dictionaries).