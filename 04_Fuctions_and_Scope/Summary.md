# Functions
Functions are self-contained, reusable blocks of code that perform specific tasks. They accept inputs (arguments), execute code, and optionally return outputs (results). Some of the purposes of using functions in programming languages are:
-   **Modularization:**  Break down complex programs into smaller, manageable units.
-   **Code reusability:**  Avoid code duplication and promote efficiency.
-   **Encapsulation:**  Hide implementation details and protect core logic.
-   **Testing and debugging:**  Isolate and test specific functionalities.

### Defining and Calling a Function

```python
def function_name(parameters):
    """
    Function documentation using triple quotes (optional).
    """
    # Function body containing code to execute
    return value  # Optional return statement

function_name(arguments)
```
Above code example show the definition and calling of function. Let's break down this code.
-   **`def`**: Indicates you're defining a function.
-   **`function_name`**: Choose a descriptive name that reflects the function's purpose (e.g.,  `calculate_area`).
-   **`parameters**`: Represent the input values the function expects (optional, can be none). Use descriptive names (e.g.,  `length`,  `width`).
-   **`docstring`**: Optional but highly recommended to provide clear documentation about the function's purpose, parameters, and return value. Use triple quotes.
-   **`function body**`: Contains the code that the function will execute when called.
-   **`return statement`**: Optional to specify a value to return from the function. If no return statement is present, the function returns  `None`.

**Key Points when defining and calling functions:**

-   Indentation is crucial in Python. The function body must be consistently indented.
-   Parameters in the function call (arguments) must match the number and order of parameters in the function definition.
-   The returned value (if any) from the function can be stored in a variable or used directly.

### **Functions Naming Conventions and Rules**
-   Use lowercase with underscores for function names (e.g.,  `calculate_area`,  `find_average`).
-   Avoid using reserved keywords, built-in functions, or names of standard modules.
-   Aim for descriptive names that accurately reflect the function's purpose (e.g.,  `calculate_total_cost`,  `is_valid_email`).
-   Consistency is key: If you use underscores, stick to them throughout your codebase.

### **Functions with Arguments **

**1. Positional Arguments:**

-   The most basic way to pass arguments.
-   Arguments are passed in the same order as they are defined in the function signature.
    ```python
    def add(x, y):
        return x + y

    result = add(5, 3)  # x = 5, y = 3

    ```

**2. Keyword Arguments:**

-   Arguments are passed by explicitly specifying the argument name and its value.
-   Offer more flexibility and readability, especially when functions have many arguments.
    ```python
    def greet(name, message="Hello"):
        return f"{message}, {name}!"

    greeting = greet(name="Alice", message="Welcome")
    print(greeting)  # Output: Welcome, Alice!

    ```


**3. Default Arguments:**

-   Allows you to assign a default value to an argument.
-   If no value is passed during the function call, the default value is used.
    ```python
    def format_string(text, prefix="*"):
        return f"{prefix} {text}"

    formatted_text = format_string("Hi")  # Uses default prefix "*"
    print(formatted_text)  # Output: * Hi

    formatted_text2 = format_string("Welcome", "-")  # Uses "-" as prefix
    print(formatted_text2)  # Output: - Welcome

    ```

**4. Variable-Length Arguments:**

-   Functions can accept an arbitrary number of arguments.
-   Use `*args` for positional arguments and `**kwargs` for keyword arguments.
    ```python
    def sum_all(*numbers):
        total = 0
        for number in numbers:
            total += number
        return total

    result = sum_all(1, 2, 3, 4)  # Accepts any number of positional arguments
    print(result)  # Output: 10

    def greet_all(**people):
        for name, greeting in people.items():
            print(f"{greeting}, {name}!")

    greet_all(Alice="Hello", Bob="Hi")  # Accepts any number of keyword arguments

    ```

**5. Unpacking Arguments:**

-   Unpack a sequence (like a list or tuple) into individual arguments when calling a function.

    ```python
    def calculate_area(length, width):
        return length * width

    dimensions = (5, 3)
    area = calculate_area(*dimensions)  # Unpack dimensions tuple into x and y
    print(area)  # Output: 15

    ```