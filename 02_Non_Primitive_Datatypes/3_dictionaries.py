"""
Demonstrates working with dictionaries in Python, including:
- Creation
- Accessing items
- Membership checking
- Modifying values
- Removing items
- Clearing and deleting dictionaries
- Copying dictionaries
- Nested dictionaries
"""

# =============================================================================
# Creating Dictionaries
# =============================================================================

# Create a dictionary using curly braces:
user = {
    "name": "Raza",
    "age": 24,
}

# Create a dictionary using the dict() constructor:
user2 = dict(name="Ahmar", age=26)

# Print both dictionaries to observe their structure:
print(user)
print(user2)

# =============================================================================
# Accessing Items
# =============================================================================

# Access a value by key:
print(user["name"])  # Output: Raza

# Use get() for safer access with a default value:
print(user.get("age"))  # Output: 24

# =============================================================================
# Listing Keys, Values, and Items
# =============================================================================

# Get a view of all keys:
print(user.keys())  # Output: dict_keys(['name', 'age'])

# Get a view of all values:
print(user.values())  # Output: dict_values(['Raza', 24])

# Get a view of key-value pairs as tuples:
print(user.items())  # Output: dict_items([('name', 'Raza'), ('age', 24)])

# =============================================================================
# Membership Checking
# =============================================================================

# Check if a key exists in the dictionary:
print("age" in user)  # Output: True
print("loginstatus" in user)  # Output: False

# =============================================================================
# Modifying and Adding Values
# =============================================================================

# Change an existing value:
user["name"] = "Korg"
print(user)  # Output: {'name': 'Korg', 'age': 24}

# Add a new key-value pair:
user.update({"loginstatus": True})
print(user)  # Output: {'name': 'Korg', 'age': 24, 'loginstatus': True}

# =============================================================================
# Removing Items
# =============================================================================

# Remove a key-value pair and return its value:
print(user.pop("loginstatus"))  # Output: True
print(user)  # Output: {'name': 'Korg', 'age': 24}

# Add another key-value pair:
user["isadult"] = True
print(user)  # Output: {'name': 'Korg', 'age': 24, 'isadult': True}

# Remove and return a random key-value pair:
print(user.popitem())  # Output: (random key-value pair)
print(user)  # Output: {'name': 'Korg', 'age': 24} (removed one pair)

# =============================================================================
# Clearing and Deleting Dictionaries
# =============================================================================

# Remove all key-value pairs:
user.clear()
print(user)  # Output: {}

# Delete the entire dictionary object:
del user2

# =============================================================================
# Copying Dictionaries
# =============================================================================

# Shallow copy (references same objects):
user2 = user  # Both refer to the same dictionary
user2["name"] = "Raza"  # Change in user2 reflects in user
print(user)  # Output: {'name': 'Raza', 'age': 24}

# Create a new, independent copy:
user3 = user.copy()  # Creates a shallow copy
user4 = dict(user)  # Another way to create a shallow copy

# =============================================================================
# Nested Dictionaries
# =============================================================================

# Create nested dictionaries:
visitor1 = {"name": "1visit", "age": 23}
visitor2 = dict(visitor1)  # Create a shallow copy
visitor2["name"] = "2visit"

# Create
visitors = {"visitor1": visitor1, "visitor2": visitor2}

# Access nested values using nested keys
print(visitors["visitor1"]["name"])  # Output: 1visit

# =============================================================================
# Summary
# =============================================================================
"""
Dictionaries are versatile data structures in Python for storing and managing key-value pairs. They offer efficient access, modification, and manipulation of diverse data types. Remember the following key points:
- Keys must be immutable (e.g., strings, numbers, tuples) to ensure uniqueness.
- Views like keys(), values(), and items() reflect changes in the original dictionary.
- Use get() for safer value retrieval with default values.
- Shallow copying creates references, while copy() and dict(original) methods provide independent copies.
- Nested dictionaries allow you to model complex relationships among data.
"""