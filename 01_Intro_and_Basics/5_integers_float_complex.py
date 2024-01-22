"""
Exploring Numeric Data Types in Python

This code demonstrates various numeric data types (integers, floats, complex numbers)
and their associated operations and functions.
"""

# Integers

# Declare variables to store initial and discounted prices as integers
initial_price = 90
discounted_price = int(76)  # Explicitly convert 76 to integer

# Print data types and verify if a value is an integer using isinstance()
print("Data types:", type(initial_price), type(discounted_price))
print("Is discounted_price an integer?", isinstance(discounted_price, int))

# Floats

# Assign GPA and CGPA as floats
gpa = 3.25
cgpa = float(3.56)  # Explicit conversion to float

# Print data types and verify if a value is a float
print("\nData types:", type(gpa), type(cgpa))
print("Is cgpa a float?", isinstance(cgpa, float))

# Complex Numbers

# Create complex numbers using literal notation and the complex() function
complex_number1 = 10 + 4j
complex_number2 = complex(2, 5)  # Create from real and imaginary parts

# Access real and imaginary components using .real and .imag attributes
print("\nData types:", type(complex_number1), type(complex_number2))
print("Is complex_number2 a complex number?", isinstance(complex_number2, complex))
print("Real part of complex_number1:", complex_number1.real)
print("Imaginary part of complex_number1:", complex_number1.imag)

# Built-in Functions for Floats and Integers

# Demonstrate absolute value with abs() and rounding with round()
print("\nAbsolute value of gpa:", abs(gpa))
print("Absolute value of negative gpa:", abs(gpa * -1))
print("gpa rounded to nearest integer:", round(gpa))
print("gpa rounded to 1 decimal place:", round(gpa, 1))

# Math Module

# Import the math module for mathematical functions and constants
import math

# Access the mathematical constant pi
print("\nValue of pi:", math.pi)
