# Arithmatic operators
# We will take 2 variables and will apply different Math operators on them
num1 = 10
num2 = 3

print(num1 + num2)  # Add
print(num1 - num2)  # Subtract
print(num1 / num2)  # Divide
print(num1 * num2)  # Multiply
print(num1 % num2)  # Modulus
print(num1**num2)  # Exponent
print(num1 // num2) # Floor Division
# Comparison Operators (returns boolean value, true or false)
print(num1 == num2)  # Equality
print(num1 != num2)  # In-equality
print(num1 > num2)  # Greater than
print(num1 < num2)  # Less than
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to

# Assignment Operators
# As we have defined num1=10 and num2=3 so this
num3 = 8  # simple assignment, assigns num3 variable to value 10
num3 += 1  # adds 1 to previous value of num3
print("After `+= 1` now num3 = ", num3)
num3 -= 3  # subtracts 3 from previous value of num3
print("After `-= 3` now num3 = ", num3)
num3 *= 4  # multiplies 4 with previous value of num3
print("After `*= 4` now num3 = ", num3)
num3 /= 4  # divides 4 with previous value of num3
print("After `/= 4` now num3 = ", num3)

# Identity Operators
print(
    num1 is num1
)  # 'is' is a keyword. It checks identity of both operands and return value
print(num2 is not num3)

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

# Now find the squared distances
x = (x2 - x1) ** 2
y = (y2 - y1) ** 2

# Now calculate the sum and then square-root of those squared distances
distance = (x + y) ** 0.5
print("Euclidian distance between (2,3) and (10,8) = ", distance)
