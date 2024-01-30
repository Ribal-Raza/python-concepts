"""
Exploring Functions and Arguments in Python

This code demonstrates different ways to define and use functions,
along with various argument-passing techniques, accompanied by
clear and beginner-friendly docstrings.
"""


# 1. Simple Function with Docstring
def simple_hello():
    """Prints a friendly greeting to the console.

    This function doesn't take any input (arguments) and doesn't return any output.
    It simply performs the task of printing a message.
    """
    print("Hello, world!")


# Call the simple function
simple_hello()  # Output: Hello, world!


# 2. Function with Return Statement
def calculate_area(length, width):
    """Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    This function takes two inputs (length and width) and returns a single output
    (the area). It performs a calculation and provides the result to the caller.
    """
    area = length * width
    return area


# Calculate and print the area
rectangle_area = calculate_area(5, 3)
print("Area of rectangle:", rectangle_area)  # Output: Area of rectangle: 15.0


# 3. Functions with Different Argument Types
def greet_with_options(name, greeting="Hello", punctuation="!"):
    """Greets a person with customizable options.

    Args:
        name (str): The name of the person to greet (required argument).
        greeting (str, optional): The greeting to use (optional argument with a default value).
        punctuation (str, optional): The punctuation to add to the end (optional argument with a default value).

    Returns:
        str: The formatted greeting message.

    This function demonstrates different argument types:
    - Positional arguments (name): Required arguments that must be provided in a specific order.
    - Default arguments (greeting, punctuation): Optional arguments that have pre-set values if not specified.
    """
    return f"{greeting}, {name}{punctuation}"


# Call the function with different argument combinations
print(
    greet_with_options("Alice")
)  # Output: Hello, Alice! (Uses default greeting and punctuation)
print(
    greet_with_options("Bob", "Hi", ".")
)  # Output: Hi, Bob. (Overrides greeting and punctuation)


def sum_all_numbers(*numbers):
    """Calculates the sum of all provided numbers.

    Args:
        *numbers: Accepts any number of positional arguments (variable-length arguments).

    Returns:
        int or float: The total sum of the numbers.

    Variable-length arguments allow you to pass an arbitrary number of arguments to a function.
    """
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum


# Call the function with variable-length arguments
print(sum_all_numbers(1, 2, 3, 4, 5))  # Output: 15


def create_profile(**user_info):
    """Creates a user profile based on provided keyword arguments.

    Args:
        **user_info: Accepts any number of keyword arguments (variable-length keyword arguments).

    Returns:
        dict: A dictionary containing the user profile information.

    Keyword arguments allow you to pass arguments by name, making code more readable and flexible.
    Variable-length keyword arguments allow you to pass an arbitrary number of keyword arguments.
    """
    return user_info


# Call the function with variable-length keyword arguments
profile = create_profile(name="Alice", age=30, city="New York")
print(profile)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


def calculate_total_cost(base_price, tax_rate=0.1):
    """Calculates the total cost, including tax.

    Args:
        base_price (float): The initial price of the item.
        tax_rate (float, optional): The tax rate to apply. Defaults to 0.1 (10%).

    Returns:
        float: The total cost after tax.

    This function defines a second function called `calculate_tax` inside its body.
    """

    def calculate_tax(price):
        """Calculates the tax amount based on the provided price and tax rate."""
        return price * tax_rate

    tax_amount = calculate_tax(base_price)
    total_cost = base_price + tax_amount
    return total_cost


# Calculate and print the total cost
total = calculate_total_cost(100)
print("Total cost:", total)  # Output: Total cost: 110.0
