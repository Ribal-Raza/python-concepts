"""
Exploring Strings and Booleans in Python

This code demonstrates:
- String creation and manipulation
- String methods for formatting, searching, and modification
- Boolean data type and its usage
"""

# Literal Assignment: Defining the title components
first = "Mr."
last = "Raza"

# Displaying and checking the type of 'first'
print(first, last)
print(type(first))  # The type() function returns the type of a value

# Assignment with Constructor Function: Using the str constructor to define a string 'pizza'
pizza = str("Jalapeno")
print(pizza)
print(type(pizza))

# Type Casting: Converting an integer to a string using the str() function
print(type(str(42)))  # The str() function converts other data types to a string

# isinstance Function: Checking if 'pizza' is an instance of a string
print(
    isinstance(pizza, str)
)  # isinstance checks whether a value is an instance of a class
print(pizza.__class__)  # __class__ returns the data type of a value

# String Concatenation: Combining 'first' and 'last' to form 'full_name'
full_name = first + " " + last
print(full_name)
full_name += "!"  # Adding an exclamation mark to 'full_name'
print(full_name)

# Multiple Line String: Creating a multiline string 'paragraph'
paragraph = """Hello! 
I am Raza
how are you!"""
print(paragraph)

# Escape Characters: Utilizing escape characters in 'sentence'
sentence = "I'm Raza. \t Who are you? \n I saw you at bar\\club."
print(sentence)

# String Methods: Demonstrating various string manipulation methods
print(first)
print(first.lower())  # Making all characters lowercase
print(first.upper())  # Making all characters uppercase
print(first.capitalize())  # Making the first character uppercase

print(paragraph.title())  # Making the first character of every word uppercase
print(
    paragraph.replace("how are you", "whatsup")
)  # Replacing a word or words with others
print(
    len(paragraph)
)  # Returning the total number of characters in a string, including whitespaces

paragraph += "        "
paragraph = "       " + paragraph
print(paragraph)
print(len(paragraph))

print(paragraph.split())  # Returning an array/set of words without whitespaces
print(
    paragraph.strip()
)  # Removing whitespaces before and after the string. Other methods: lstrip(), rstrip()
print(paragraph.splitlines())  # Returning a collection/array of lines
print("")

# Build a Menu with String Manipulation Methods
title = "menu".upper()
print(title.center(20, "="))  # Displaying a centered title with padding
print("Coffee".ljust(16, ".") + "$1".rjust(4))  # Formatting a menu item and its price
print("Sandwich".ljust(16, ".") + "$3".rjust(4))
print("Salad".ljust(16, ".") + "$2".rjust(4))
print("")

# Indexes: Demonstrating string indexing and slicing
print(first[1])  # Accessing the character at index 1
print(first[-1])  # Accessing the last character using negative indexing
print(first[0:-1])  # Slicing the string from index 0 to the second-to-last character

# String Methods: startswith() and endswith()
print(first.startswith("M"))  # Checking if 'first' starts with "M" (case-sensitive)
print(first.startswith("Mr"))  # Checking if 'first' starts with "Mr"
print(first.startswith("m"))  # Checking if 'first' starts with "m" (case-sensitive)
print(first.endswith("."))  # Checking if 'first' ends with a period
print("")

# Boolean Data Types: Demonstrating boolean literals and their types
my_value = True
y = bool(False)
print(type(my_value))
print(isinstance(y, bool))
print(
    isinstance(type(y), bool)
)  # False, because type(y) returns <class 'bool'> while bool itself is type
