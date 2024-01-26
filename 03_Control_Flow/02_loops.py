"""
Demonstration of looping statements in Python with clear explanations and examples.
"""

# -------------------
# While loops
# -------------------

"""
Print numbers from 1 to 6, stopping at 7 using break.
"""
value = 1
while value <= 10:
    print(value)
    if value == 7:
        break  # Exit the loop when value reaches 7
    value += 1

print("\n")  # Separate output for clarity

"""
Print numbers from 1 to 10, skipping 6 using continue.
"""
value2 = 1
while value2 <= 10:
    value2 += 1
    if value2 == 6:
        continue  # Skip 6 and move to the next iteration
    print(value2)

# -------------------
# For loops
# -------------------

"""
Iterate through a list of names.
"""
names = ["Sara", "Hugo", "Finn", "Steve"]
for name in names:  # Use a descriptive variable name for clarity
    print(name)

"""
Iterate through a string, printing each character.
"""
word = "TandoAdamKhan"
for character in word:
    print(character)

"""
Iterate through a list, skipping a specific name.
"""
for name in names:
    if name == "Finn":
        continue  # Skip Finn
    print(name)

"""
Iterate through a range of numbers, demonstrating different options.
"""
# Print numbers from 0 to 4
for i in range(5):
    print(i)

# Print numbers from 1 to 3
for i in range(1, 4):
    print(i)

# Print even numbers from 2 to 24
for i in range(2, 26, 2):
    print(i)

# -------------------
# Nested loops
# -------------------

"""
Combine two lists for comprehensive output.
"""
names = ["Raza", "Kaisen", "Vonka"]
actions = ["eats", "codes", "sleeps"]

for name in names:
    for action in action:
        print(name + " " + action + ".")
