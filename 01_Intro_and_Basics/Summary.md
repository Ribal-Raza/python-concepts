# Basics of Python

## Table of Contents

-   [First Program: Hello, World!](#first-program-hello-world)
-   [Data Types and Variables](#data-types-and-variables)
-   [Operators](#operators)
-   [Indentation](#indentation)
-   [Data Types in Detail](#data-types-in-detail)
    -   [String in Python](#string-in-python)
        -   [String Manipulation Methods](#string-manipulation-methods)
        -   [Styles of Writing Strings](#styles-of-writing-strings)
    -   [Boolean Data Type](#boolean-data-type)
    -   [Numeric Data Types](#numeric-data-types)
        -   [Integer (int) Data Type](#integer-int-data-type)
        -   [Float (float) Data Type](#float-float-data-type)
        -   [Complex (complex) Data Type](#complex-complex-data-type)
        -   [Math Module in Python](#math-module-in-python)
        -   [Built-in Functions for Numeric Values](#built-in-functions-for-numeric-values)
- [Questions](#conceptualcommonly-asked-questions)

## First Program: Hello, World!

**Why "Hello, World!" is the First Program:**

-   Introduction to Syntax.
-   Verification of Setup.
-   Milestone and Confidence Boost.
-   Historical Legacy.

pythonCopy code

`print("Hello, World!")` 

## Data Types and Variables

### 1. Data Types and Variables in Programming Languages

-   **Data:** The raw material that computers process and manipulate.
-   **Data Types:** Classifications defining the type of data a value can hold.

**Types of Data:**

-   **Primitive Data Types:** Fundamental building blocks.
    
    -   Integers (int)
    -   Floating-point numbers (float)
    -   Strings (str)
    -   Booleans (bool)
    -   NoneType
-   **Non-Primitive Data Types:** Composite types.
    
    -   Lists, tuples, dictionaries, sets

### Checking Type of Data:

-   Using the `type()` Function:
    ```python
    x = 5
    print(type(x))  # <class 'int'>
    
    y = "Hello, World!"
    print(type(y))  # <class 'str'>
    ``` 
    
-   Using `isinstance()` Function:
    ```python
    a = 3.14
    print(isinstance(a, float))  # True
    
    b = [1, 2, 3]
    print(isinstance(b, list))   # True
    ``` 
    
-   Using `__class__` Attribute: 
    ```python
    name = "John"
    print(name.__class__)  # <class 'str'>
    
    numbers = [1, 2, 3]
    print(numbers.__class__)  # <class 'list'>
    ``` 
    
-   Using `type()` with a Literal:
    ```python
    print(type(10))       # <class 'int'>
    print(type(3.14))     # <class 'float'>
    print(type("Hello"))  # <class 'str'>
    ``` 
    
-   Using `type()` with `type()`:
    ```python
    print(type(type("Hello")))  # <class 'type'>
    ``` 
    
-   Using `__name__` Attribute: 
    ```python
    value = 42
    print(value.__class__.__name__)  # 'int'
    ``` 
    

### 2. Variables in Programming

-   **Concept:** Named containers for storing data.
    
-   **Need for Variables:**
    
    -   Store and reuse data.
    -   Enhance code readability.
    -   Perform calculations.
-   **Declaration vs. Initialization:**
    
    -   **Declaration:** Informing about the variable.
    -   **Initialization:** Assigning an initial value.

### 3. Variables in Python

-   Declaration and Initialization:
    -   Python doesn't require explicit declaration.
    -   Example: `age = 30` (integer variable named "age")

### 4. Naming Rules/Conventions of Variables in Python

**Rules:**

-   Must start with a letter or underscore.
-   Can contain letters, numbers, and underscores.
-   Case-sensitive.

**Conventions:**

-   Use descriptive and meaningful names.
-   Use lowercase for variables.
-   Use camelCase for multi-word variable names.
-   Avoid reserved keywords.

## Operators

-   Special symbols or keywords for operations.
-   Building blocks for expressions.

### Types of Operators:

1.  **Arithmetic Operators:**
    
    -   Addition (`+`)
    -   Subtraction (`-`)
    -   Multiplication (`*`)
    -   Division (`/`)
    -   Floor Division (`//`)
    -   Modulus (`%`)
    -   Exponentiation (`**`)
2.  **Comparison Operators:**
    
    -   Equal to (`==`)
    -   Not equal to (`!=`)
    -   Greater than (`>`)
    -   Less than (`<`)
    -   Greater than or equal to (`>=`)
    -   Less than or equal to (`<=`)
3.  **Logical Operators:**
    
    -   Logical AND (`and`)
    -   Logical OR (`or`)
    -   Logical NOT (`not`)
4.  **Assignment Operators:**
    
    -   Assignment (`=`)
    -   Add and Assign (`+=`)
    -   Subtract and Assign (`-=`)
    -   Multiply and Assign (`*=`)
    -   Divide and Assign (`/=`)
5.  **Bitwise Operators:**
    
    -   Bitwise AND (`&`)
    -   Bitwise OR (`|`)
    -   Bitwise XOR (`^`)
    -   Bitwise NOT (`~`)
    -   Left Shift (`<<`)
    -   Right Shift (`>>`)
6.  **Membership Operators:**
    
    -   `in`
    -   `not in`
7.  **Identity Operators:**
    
    -   `is`
    -   `is not`

### Precedence: The Order of Operations

-   Operators with higher precedence go first.
- PEMDAS is a general rule.
-   Parentheses > Exponents > Multiplication/Division > Addition/Subtraction > Comparison > Logical > Assignment

## Indentation

-   Spaces or tabs at the beginning of a line.
-   Defines code blocks in Python.
-   Consistent indentation is crucial.

Example:
```python
if x > 0:
    print("Positive")
else:
    print("Non-positive")
``` 

## Data Types in Detail

### String in Python

-   Sequence of characters.
-   Enclosed in single (`'`) or double (`"`) quotes.

**Example:**
```python
message = "Hello, World!"
``` 

#### String Manipulation Methods

1.  **Concatenation:**
    
    -   Combining strings using the `+` operator.
    ```python
    str1 = "Hello"
    str2 = "World"
    result = str1 + ", " + str2 + "!"
    print(result)
    ``` 
    
2.  **Repetition:**
    
    -   Repeating a string using the `*` operator.
    ```python
    word = "Hello"
    repeated_word = word * 3
    print(repeated_word)
    ``` 
    
3.  **Slicing:**
    -   Extracting a portion of a string.
    ```python
    message = "Hello, World!"
    part = message[7:12]
    print(part)
    ```
    
4.  **Length:**
    -   Finding the length of a string using `len()`.
    ```python
    text = "Python"
    length = len(text)
    print(length)
    ``` 
    
5.  **Lowercase and Uppercase:**
    -   Converting case using `lower()` and `upper()`.    
    ```python
    text = "Python"
    lower_text = text.lower()
    upper_text = text.upper()
    print(lower_text, upper_text)
    ``` 
    
6.  **Stripping Whitespace:**
    -   Removing leading and trailing whitespaces.
    ```python
    message = "   Hello, World!   "
    stripped_message = message.strip()
    print(stripped_message)
    ```
    
7.  **Replacement:**
    -   Replacing a substring with another.    
    ```python
    sentence = "I like programming in Java."
    updated_sentence = sentence.replace("Java", "Python")
    print(updated_sentence)
    ``` 
    
#### Styles of Writing Strings

1.  **Single and Double Quotes:**
    -   Both are acceptable. 
    ```python
    single_quoted = 'Hello, World!'
    double_quoted = "Hello, World!"
    ``` 
    
2.  **Triple Quotes:**
    -   Used for multi-line strings.    
    ```python
    multi_line = """This is a
    multi-line
    string."""
    ``` 
    
3.  **Escape Characters:**
    
    -   Special characters using `\`.
    
    ```python
    escaped_string = "This is a line with a \"quote\"."
    ``` 
    
4.  **Raw Strings:**
    
    -   Ignores escape characters.
    
    `raw_string = r"C:\Users\Username\Documents"` 
    

### Boolean Data Type

-   Represents truth values: `True` or `False`.
-   Used for logical operations.

**Example:**
```python
is_greater = 5 > 3  # True
is_equal = 5 == 3  # False
``` 

### Numeric Data Types

#### Integer (int) Data Type

-   Represents whole numbers.
-   No limit on size (up to available memory).

**Example:**

`x = 42` 

#### Float (float) Data Type

-   Represents decimal numbers.
-   Can also represent integers.

**Example:**

`y = 3.14` 

#### Complex (complex) Data Type

-   Represents complex numbers.

**Example:**

`z = 2 + 3j` 

#### Math Module in Python

-   Provides mathematical functions.

**Example:**
```python
import math

result = math.sqrt(25)
print(result)  # 5.0
``` 

#### Built-in Functions for Numeric Values

1.  **`abs(x)`:** Returns the absolute value of x.
    
    ```python
    absolute_value = abs(-5)
    print(absolute_value)  # 5
    ``` 
    
2.  **`round(x)`:** Rounds x to the nearest integer.
    ```python
    rounded_value = round(3.14)
    print(rounded_value)  # 3
    ``` 
    
3.  **`divmod(x, y)`:** Returns the quotient and remainder of x/y.
    ```python
    quotient, remainder = divmod(10, 3)
    print(quotient, remainder)  # 3 1
    ``` 
    
4.  **`pow(x, y)` or `x ** y`:** Raises x to the power of y.    
    ```python
    result = pow(2, 3)
    print(result)  # 8
    ``` 
    
5.  **`max(iterable)` and `min(iterable)`:** Returns the maximum and minimum values.    
    ```python
    numbers = [1, 5, 2, 8, 3]
    max_value = max(numbers)
    min_value = min(numbers)
    print(max_value, min_value)  # 8 1
    ``` 
    
6.  **`sum(iterable)`:** Returns the sum of all elements in the iterable.
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(total)  # 15
    ``` 
    
7.  **Conversion Functions:**
    
    -   `int(x)`
    -   `float(x)`
    -   `complex(x)`
    
    ```python
    num_str = "42"
    num_int = int(num_str)
    num_float = float(num_str)
    num_complex = complex(num_str)
    ```

## Conceptual/Commonly Asked Questions:


#### **Data Types:**

-   **Q: What are the advantages and disadvantages of mutable and immutable data types in Python?**
    
	-   **A:** Mutables (lists, dictionaries) are flexible but can lead to unexpected changes. Immutables (strings, tuples) are safer but less flexible for data manipulation. Choose based on your needs.
    
-   **Q: When would you use a set over a list or dictionary?**
    
	-   **A:** Use sets for unique elements where order doesn't matter. They offer fast membership checks and eliminate duplicates.
    

#### **Variables:**

-   **Q: Why is it important to use descriptive variable names?**
    
	-   **A:** Descriptive names improve code readability and maintainability, making it easier for others (or future you) to understand the program's logic.
    
-   **Q: Can you explain the concept of variable scope in Python?**
    
	-   **A:** Scope defines where a variable is accessible within a program. Local variables are defined within functions and only accessible within that function, while global variables are defined outside functions and accessible throughout the program.
    

#### **Operators:**

-   **Q: Explain the difference between logical and bitwise operators.**
    
	-   **A:** Logical operators (`and`,  `or`,  `not`) work on boolean values and are used for conditional statements. Bitwise operators (`&`,  `|`,  `^`) work on individual bits of numbers and are used for low-level manipulation.
    
-   **Q: Give an example of how operator precedence can affect the outcome of an expression.**
    
	-   **A:**  `5 - 2 * 3` evaluates to 1 because multiplication has higher precedence than subtraction. Parentheses can override precedence:  `(5 - 2) * 3` evaluates to 9.
    

#### **Indentation:**

-   **Q: What are the consequences of incorrect indentation in Python?**
	-   **A:** Incorrect indentation leads to syntax errors and program malfunction. Python relies on indentation to define code blocks, so any deviation leads to issues.

#### **String Data Type:**

-   **Q: How can you efficiently search for substrings within a string?**
    
	-   **A:** Use methods like `find()`,  `index()`,  `rfind()`, and `startswith()` depending on your specific search needs.
    
-   **Q: Explain the difference between `strip()` and `lstrip()/rstrip()` for string manipulation.**
    
	-   **A:**  `strip()` removes all whitespace characters from both the beginning and end of a string.  `lstrip()` and `rstrip()` remove whitespace only from the left or right side, respectively.
    

#### **Boolean Data Type:**

-   **Q: What are some common truthy and falsy values in Python besides  `True`  and  `False`?**
	-   **A:** Numbers (except 0), empty strings, empty lists or dictionaries, None, are generally truthy. Zero, empty sets, the boolean False, and None are typically falsy.

#### **Numeric Data Types:**

-   **Q: When should you use floats over integers, and vice versa?**
    
	-   **A:** Use integers for whole numbers where precision isn't needed. Use floats for decimal values or calculations involving fractions.
    
-   **Q: How can you handle potential overflow errors when working with large numbers?**
    
	-   **A:** Python raises an OverflowError for exceeding integer limits. Consider using libraries like `decimal` for high-precision calculations or implementing overflow checks in your code.