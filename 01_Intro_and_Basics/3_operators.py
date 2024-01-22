"""
Demonstration of Arithmetic, Comparison, Assignment, and Identity Operators

This code explores various operators in Python:
- Arithmetic operators for performing numerical calculations
- Comparison operators for comparing values
- Assignment operators for assigning and updating variables
- Identity operators for checking object identity
"""

#num1 = 10
num2 = 3

# Demonstrate addition, subtraction, division, multiplication, modulus, exponent, 
# and floor division
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Division:", num1 / num2)
print("Multiplication:", num1 * num2)
print("Modulus (remainder):", num1 % num2)
print("Exponent:", num1 ** num2)
print("Floor division (integer division):", num1 // num2)
print("")
# Comparison Operators (returns boolean value, true or false)
# Comparison Operators

# Demonstrate equality, inequality, greater than, less than, greater than or equal to, 
# less than or equal to
print("Equality:", num1 == num2)
print("Inequality:", num1 != num2)
print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)
print("Greater than or equal to:", num1 >= num2)
print("Less than or equal to:", num1 <= num2)

# Assignment Operators

num3 = 8  # Simple assignment

# Demonstrate compound assignment operators for addition, subtraction, multiplication, 
# and division
num3 += 1
print("After `+= 1`:", num3)
num3 -= 3
print("After `-= 3`:", num3)
num3 *= 4
print("After `*= 4`:", num3)
num3 /= 4
print("After `/= 4`:", num3)

# Identity Operators

# Demonstrate the `is` and `is not` operators for checking object identity
print("num1 is num1:", num1 is num1)
print("num2 is not num3:", num2 is not num3)

# Exercise Question: Find an Euclidian distance between (2, 3) and (10, 8)
# In (2,3), 2 is coordinate value on x-axis, 3 is coordinate value on y axis. Similar in (10,8)
# General formula to calculate Euclidian distance is
# distance = √((x2 - x1)^2 + (y2 - y1)^2)
# (square root of the sum of squared differences in coordinates)
# First lets store the values of location (2,3) and (10,8) in variables
x1 = 2
y1 = 3
x2 = 10
y2 = 8

# find the squared distances
x = (x2 - x1) ** 2
y = (y2 - y1) ** 2

# Now calculate the sum and then square-root of those squared distances
distance = (x + y) ** 0.5
print("Euclidian distance between (2,3) and (10,8) = ", distance)
