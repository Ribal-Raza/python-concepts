"""
Demonstrates working with sets in Python, including:
- Creation
- Adding items
- Copying sets
- Removing items
- Merging sets
- Uniqueness and ordering
- Other set operations
"""

# =============================================================================
# Creating Sets
# =============================================================================

# Create sets using curly braces or the set() constructor:
first = {3, 1, 2, 4}  # Values are automatically ordered
first1 = set({5, 7, 6, 4})  # Another way to create a set

# Print both sets to observe their order and uniqueness:
print(first)  # Output: {1, 2, 3, 4}
print(first1)  # Output: {4, 5, 6, 7}

# =============================================================================
# Adding Items
# =============================================================================

# Add individual items using add():
first.add(8)

# Add multiple items using update():
first.update({24, 5})

# Print the modified set:
print(first)  # Output: {1, 2, 3, 4, 5, 8, 24}

# =============================================================================
# Copying Sets
# =============================================================================

# Create a shallow copy using set():
first2 = set(first)
first2.update({9, 10})  # Modify the copy

# Create a shallow copy by assignment:
first3 = first  # Both refer to the same set
first3.update({9, 10})  # Modifies both first and first3

# Observe that a shallow copy modifies both sets:
print(first)  # Output: {1, 2, 3, 4, 5, 8, 9, 10, 24}
print(first3)  # Output: {1, 2, 3, 4, 5, 8, 9, 10, 24}

# =============================================================================
# Removing Items
# =============================================================================

# Remove and return an arbitrary item using pop():
first.pop()

# Remove a specific item using remove():
first.remove(5)

# Clear the entire set using clear():
first2.clear()

# Delete the entire set object using del:
del first3

# =============================================================================
# Merging Sets
# =============================================================================

# Create a new set that includes all unique elements from both sets:
newset = first.union(second)

# Print the original sets and the merged set:
print(first)  # Output: {1, 2, 3, 4, 8, 24}
print(second)  # Output: {5, 6, 7}
print(newset)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 24}

# =============================================================================
# Uniqueness and Ordering
# =============================================================================

# Sets automatically remove duplicates and maintain a specific order:
mixset = {1, 2, True, 3, 4, False, 0}
print(mixset)  # Output: {0, 1, 2, 3, 4} (0 and False are treated as equal)

# Remember: you cannot access elements by index or key-value pairs in sets.

# =============================================================================
# Other Set Operations
# =============================================================================

# Keep only elements present in both sets:
first1.intersection_update(second)
print(first1)  # Output: {4}

# Remove elements from first that are also present in second:
first.difference_update(second)
print(first)  # Output: {1, 2, 3, 8, 24}

# Create a new set with elements in first but not in first1:
set_difference = first.difference(first1)
print(set_difference)  # Output: {1, 2, 3, 8, 24}

# Check if myset is a subset of first:
myset = {3, 8, 10}
print(myset.issubset(first))  # Output: True

# Check if first is a superset of myset:
print(first.issuperset(myset))  # Output: True

# Update myset with the symmetric difference of its elements and first:
myset.symmetric_difference_update(first)
print(myset)  # Output: {1, 2, 4} (elements unique to each set)

# =============================================================================
# Summary
# =============================================================================
"""
Sets are useful data structures for storing unique and ordered collections of items. Remember:

- Sets eliminate duplicates and maintain a specific order.
- Use `add()` to add individual items, `update()` for multiple items.
- Shallow copies reference the same objects, use `set()` for independent copies.
- Use `pop()` to remove any item, `remove()` for specific items.
- Explore `intersection_update()`, `difference_update()`, and `symmetric_difference_update()` for various set operations.

I hope this comprehensive and well-commented code breakdown empowers you to effectively use sets in your Python projects!
"""
