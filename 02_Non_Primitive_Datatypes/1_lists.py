# Lists are ordered collections of items, enclosed in square brackets [].
# Items in lists can be of any datatype, including other lists.

# Initialize a list with user names
users = ["Raza", "Kashi", "Burno", "Maggie", "Chuck"]

# Create a list with mixed datatypes
user = ["Raza", 24, True]

# Initialize an empty list
empty = []

# Create a list from characters of a string
name_characters = list("Raza")

# Another way to create a list from existing elements
names = list(["Kashi", "Burno", "Maggie"])

# Display the list of name characters
print("Name Characters:", name_characters)

# Create a shallow copy of the 'users' list
users2 = users[:]
print("Shallow Copy:", users2)

# Create a deep copy of the 'users' list
users3 = users.copy()
print("Deep Copy:", users3)

# Check if "Kashi" is a member of the 'users' list
print("Is 'Kashi' in Users?", "Kashi" in users)  # Output: True

# Access items in the list using indexes
print("First Item:", users[0])
print("Last Item:", users[-1])

# Find the index of "Maggie" in the list
print("Index of 'Maggie':", users.index("Maggie"))

# Display a range of values in the list using indexes
print("Values from 0 to 3:", users[0:4])  # 4th index item is not included
print("Negative Indexes:", users[-4:-1])  # -1 represents the last item
print("Values from Index 1 to Last Item:", users[1:])

# Check the length of the 'users' list
print("Length of Users List:", len(users))

# Add new items to the list
users += ["Elsa"]
print("Users After Adding 'Elsa':", users)

users.append("Hashim")
print("Users After Appending 'Hashim':", users)

users.extend(["Rob", "Jim"])
print("Users After Extending with ['Rob', 'Jim']:", users)

# Insert an item at the beginning of the list
users.insert(0, "Bobby")
print("Users After Inserting 'Bobby' at the Beginning:", users)

# Insert multiple items at a specific index
users[1:1] = ["Amir", "Ahmar"]
print("Users After Inserting ['Amir', 'Ahmar'] at Index 1:", users)

# Replace a range of values with a single item
users[2:4] = ["Aqib"]
print("Users After Replacing Values at Index 2 to 4 with 'Aqib':", users)

# Remove items from the list
users.remove("Maggie")
print("Users After Removing 'Maggie':", users)

# Pop the last item from the list
print("Popped Item:", users.pop())
print("Users After Popping the Last Item:", users)

# Delete an item at a specific index
del users[1]
print("Users After Deleting Item at Index 1:", users)

# Delete the entire 'users2' list
del users2
# print(user2)  # Uncommenting this line will result in an error
print("List 'users2' Deleted")

# Clear all items from the 'users3' list
users3.clear()
print("Users3 After Clearing:", users3)

# Sorting lists
users[2:3] = ["david"]
users.sort()  # Sort the list (lowercase gets sorted at last)
print("Users After Sorting:", users)

# Sort the list with lowercase in alphabetical order among uppercase
users.sort(key=str.lower)
print("Users After Sorting (Case-Insensitive):", users)

# Sorting a list with integer items
nums = [44, 27, 35, 17, 10, 19, 8, 11, 3]
nums.sort()
print("Sorted Numbers:", nums)

# Different methods to reverse an array
nums.reverse()
print("Reversed Numbers:", nums)

nums.sort(reverse=True)
print("Sorted Numbers in Descending Order:", nums)

# Use sorted() to create a new list with sorted numbers in descending order
print("Sorted Numbers Using sorted() in Descending Order:", sorted(nums, reverse=True))

# Unpack the list
[num1, num2, *num3] = nums
print("Unpacked Numbers:", num1, num2, num3)
