# Basics of Python
### Table of Contents
- [First Program Hello World](#first-program-hello-world)
- [Data Types and Variables](#1-data-and-data-types-in-programming-languages)
- [Variables in Programming](#2-variables-in-programming)
- [Varibales in Python](#3-variables-in-python)
- [Naming Rules/Conventions of Variables](#4-naming-rulesconventions-of-variables-in-python)
- [Operators](#operators)
- [Types of Operators](#types-of-operators-in-python)
- [Presedence in Operators](#precedence-the-order-of-operations)

## First Program Hello World
**Why "Hello, World!" is the First Program:**

-   **Introduction to Syntax:** It's a simple program that demonstrates the basic structure and syntax of a language, easing beginners into coding concepts.
-   **Verification of Setup:** Successfully printing "Hello, World!" confirms that your programming environment is set up correctly and you can start writing code.
-   **Milestone and Confidence Boost:** It's a symbolic first step in your programming journey, marking a successful interaction with the language and building confidence for further learning.
-   **Historical Legacy:** The tradition dates back to 1972, when it was used in a textbook to illustrate a basic concept in the B programming language, and has since become a universal practice.

**"Hello, World!" in Python:**
```python
print("Hello, World!")
```
-   `print()`: This built-in Python function is used to output text to the console.
-   `"Hello, World!"`: This string of characters within quotes is the message you want to print.
## Datatypes and Variables

### **1. Data and Data Types in Programming Languages:**

**- Data:** The raw material that computers process and manipulate. It can represent various things like numbers, text, images, sounds, and more.  **- Data Types:** A classification system that defines the type of data a value can hold and the operations that can be performed on it.

**Types of Data:**

**- Primitive Data Types:** The fundamental building blocks of data, indivisible into smaller units. - **Python's Primitive Data Types:** - Integers (int): Whole numbers (e.g., -2, 0, 100) - Floating-point numbers (float): Numbers with decimals (e.g., 3.14, -0.5) - Strings (str): Sequences of characters (e.g., "Hello, world!") - Booleans (bool): True or False values - NoneType: Represents the absence of a value

**- Non-Primitive Data Types:** Composite types created by combining primitive types, often holding multiple values. - Examples: Lists, tuples, dictionaries, sets (we'll cover these later)

### **2. Variables in Programming:**

**- Concept:** Named containers that store data values in memory, used to manage and manipulate data effectively.  **- Need for Variables:** - To store and reuse data during program execution. - To make code more readable and maintainable by giving meaningful names to data. - To perform calculations and operations on data.

**- Declaration vs. Initialization:** - **Declaration:** Informing the program about the existence of a variable and its data type. - **Initialization:** Assigning an initial value to the variable.

### **3. Variables in Python:**

**- Declaration and Initialization:** - Python doesn't require explicit declaration. A variable is created the moment you assign a value to it. - Example:  `age = 30` (declares and initializes an integer variable named "age")

### **4. Naming Rules/Conventions of Variables in Python:**
- **Rules:**
	- Must start with a letter (A-Z or a-z) or an underscore (_)  
	- Can only contain letters, numbers, and underscores  
	- Case-sensitive (age and Age are different variables)
- **Conventions:**
	- Use descriptive and meaningful names (e.g.,  `firstName`,  `total_cost`) 
	- Use lowercase for variables (e.g.,  `my_name`,  `user_input`) 
	- Use camelCase for multi-word variable names (e.g.,  `totalItems`,  `isAvailable`) 
	- Avoid reserved keywords (e.g.,  `if`,  `else`,  `while`)


## Operators:

In Python, operators are special symbols or keywords that perform operations on variables and values. They are the building blocks of expressions, allowing you to manipulate and compare data.

### Types of Operators:

1.  **Arithmetic Operators:**
    
    -   Addition (`+`): Adds two operands.
    -   Subtraction (`-`): Subtracts the right operand from the left operand.
    -   Multiplication (`*`): Multiplies two operands.
    -   Division (`/`): Divides the left operand by the right operand.
    -   Floor Division (`//`): Returns the quotient of the division, discarding the remainder.
    -   Modulus (`%`): Returns the remainder of the division.
    -   Exponentiation (`**`): Raises the left operand to the power of the right operand.
    
    Example:
    ```python
    a = 10
    b = 3
    print(a + b)  # 13
    print(a - b)  # 7
    print(a * b)  # 30
    print(a / b)  # 3.333...
    print(a // b) # 3
    print(a % b)  # 1
    print(a ** b) # 1000
    ```
    
2.  **Comparison Operators:**
    
    -   Equal to (`==`): True if the operands are equal.
    -   Not equal to (`!=`): True if the operands are not equal.
    -   Greater than (`>`): True if the left operand is greater than the right operand.
    -   Less than (`<`): True if the left operand is less than the right operand.
    -   Greater than or equal to (`>=`): True if the left operand is greater than or equal to the right operand.
    -   Less than or equal to (`<=`): True if the left operand is less than or equal to the right operand.
    
    Example:
    ```python
    x = 5
    y = 10
    print(x == y)  # False
    print(x != y)  # True
    print(x > y)   # False
    print(x < y)   # True
    print(x >= y)  # False
    print(x <= y)  # True
    ```
    
3.  **Logical Operators:**
    
    -   Logical AND (`and`): True if both operands are true.
    -   Logical OR (`or`): True if at least one operand is true.
    -   Logical NOT (`not`): True if the operand is false, and vice versa.
    
    Example:
    ```python
    p = True
    q = False
    print(p and q)  # False
    print(p or q)   # True
    print(not p)    # False
    ```
    
4.  **Assignment Operators:**
    
    -   Assignment (`=`): Assigns the value of the right operand to the left operand.
    -   Add and Assign (`+=`): Adds the right operand to the left operand and assigns the result to the left operand.
    -   Subtract and Assign (`-=`): Subtracts the right operand from the left operand and assigns the result to the left operand.
    -   Multiply and Assign (`*=`): Multiplies the left operand by the right operand and assigns the result to the left operand.
    -   Divide and Assign (`/=`): Divides the left operand by the right operand and assigns the result to the left operand.
    
    Example:
    ```python
    a = 5
    b = 2
    a += b  # equivalent to a = a + b
    print(a)  # 7
    ```
    
5.  **Bitwise Operators:**
    
    -   Bitwise AND (`&`): Performs bitwise AND operation.
    -   Bitwise OR (`|`): Performs bitwise OR operation.
    -   Bitwise XOR (`^`): Performs bitwise XOR (exclusive OR) operation.
    -   Bitwise NOT (`~`): Inverts the bits of the operand.
    -   Left Shift (`<<`): Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
    -   Right Shift (`>>`): Shifts the bits of the left operand to the right by the number of positions specified by the right operand.
    
    Example:
    ```python
    x = 5
    y = 3
    print(x & y)   # 1 (binary 101 & 011)
    print(x | y)   # 7 (binary 101 | 011)
    print(x ^ y)   # 6 (binary 101 ^ 011)
    print(~x)      # -6 (inverts the bits)
    print(x << 1)  # 10 (binary 101 shifted left by 1 position)
    print(x >> 1)  # 2  (binary 101 shifted right by 1 position)
    ```
    
6.  **Membership Operators:**
    
    -   `in`: True if a value is found in the sequence.
    -   `not in`: True if a value is not found in the sequence.
    
    Example:
    ```python
    myList = [1, 2, 3, 4, 5]
    print(3 in myList)    # True
    print(6 not in myList) # True
    ```
    
7.  **Identity Operators:**
    
    -   `is`: True if both operands are the same object.
    -   `is not`: True if operands are not the same object.
    
    Example:
    ```python
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(a is b)   # True
    print(a is not c) # True
    ```
    

These are the primary types of operators in Python along with examples for each category. Understanding and mastering these operators is crucial for effective Python programming.

### **Precedence: The Order of Operations:**

Imagine operators form a queue, each waiting their turn to act. Precedence determines the order in which they operate, just like PEMDAS in math. Operators with higher precedence go first, influencing the final outcome. Remember, parentheses can override the default order.

**Python Specificity:** Python uses operator precedence strictly, so knowing the order is crucial for accurate results. For example, `2 * 3 + 1` will be evaluated as `6 + 1 = 7`, not `5 * 3 = 15`.

**General Formula:**
PEMDAS
`Parentheses > Exponents > Multiplication/Division (left to right) > Addition/Subtraction (left to right) > Comparison > Logical > Assignment`