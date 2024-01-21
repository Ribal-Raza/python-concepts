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


## Operators 
Operators are the tools we use in programming to perform various operations on data. They act like mathematical symbols (+, -, *, /), but can also be used for comparisons, logical operations, and manipulating data structures.

### Types of Operators in Python:

1. **Arithmetic Operators:** These perform basic mathematical operations on numbers.

	-   **Addition (+):**  Combines two values (e.g., 5 + 3 = 8)
	-   **Subtraction (-):**  Takes away one value from another (e.g., 10 - 7 = 3)
	-   **Multiplication (*):**  Repeats one value by another (e.g., 4 * 2 = 8)
	-   **Division (/):**  Splits one value by another (e.g., 12 / 4 = 3)
	-   **Modulo (%):**  Gives the remainder after division (e.g., 10 % 3 = 1)
	-   **Exponentiation (`**`):** Raises one value to the power of another (e.g., 2 ** 3 = 8)

2. **Comparison Operators:** These compare two values and return True or False.
	-   **Equality (==):**  Checks if two values are equal (e.g., 5 == 5 is True)
	-   **Inequality (!=):**  Checks if two values are not equal (e.g., 7 != 3 is True)
	-   **Greater than (>):**  Checks if one value is greater than another (e.g., 9 > 6 is True)
	-   **Less than (<):**  Checks if one value is less than another (e.g., 2 < 5 is True)
	-   **Greater than or equal to (>=):**  Checks if one value is greater than or equal to another (e.g., 4 >= 4 is True)
	-   **Less than or equal to (<=):**  Checks if one value is less than or equal to another (e.g., 8 <= 10 is True)

3. **Logical Operators:** These combine Boolean values (True or False) using logical rules.
	-   **And (&):**  True only if both conditions are True (e.g., (5 > 3) & (2 < 4) is True)
	-   **Or (|):**  True if either condition is True (e.g., (2 < 3) | (8 > 5) is True)
	-   **Not (!):**  Reverses the truth value of a condition (e.g., !(5 == 5) is False)

4. **Assignment Operators:** These assign values to variables.

	-   **(=)**: Simple assignment (e.g., age = 25)
	-   **+=**: Adds and assigns (e.g., score += 10)
	-   **-=**: Subtracts and assigns (e.g., money -= 5)
	-   ***=**: Multiplies and assigns (e.g., population *= 2)
	-   **/=**: Divides and assigns (e.g., distance /= 3)

5. **Membership Operators:** These check if a value exists within a sequence (list, tuple, string).
	-   **in:**  Checks if a value is present in a sequence (e.g., "book" in ["apple", "book", "pen"] is True)
	-   **not in:**  Checks if a value is not present in a sequence (e.g., "dog" not in ["cat", "fish", "bird"] is True)

6. **Identity Operators:** These compare object identities, not their values.
	 - Is (`is`): Checks if two objects are the same object (e.g.,  `a is a = True`)
	 - Is not (`is not`): Checks if two objects are not the same object (e.g.,  `a is not b = True`)

### **Precedence: The Order of Operations:**

Imagine operators form a queue, each waiting their turn to act. Precedence determines the order in which they operate, just like PEMDAS in math. Operators with higher precedence go first, influencing the final outcome. Remember, parentheses can override the default order.

**Python Specificity:** Python uses operator precedence strictly, so knowing the order is crucial for accurate results. For example, `2 * 3 + 1` will be evaluated as `6 + 1 = 7`, not `5 * 3 = 15`.

**General Formula:**
PEMDAS
`Parentheses > Exponents > Multiplication/Division (left to right) > Addition/Subtraction (left to right) > Comparison > Logical > Assignment`