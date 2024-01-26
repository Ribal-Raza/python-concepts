### Table of Contents
- [Non-primitive Data types](#non-primitive-data-types)
    - [List](#lists)
        - [Ways to initialize Lists](#different-ways-to-initialize-lists)
        - [Lists Methods/Functions](#some-list-methodsfunctions)
        - [Questions](#questions-related-to-lists)
    - [Tuple](#tuple)
        - [Ways to initialize Tuples](#different-ways-to-initialize-tuples)
        - [Tuple Methods/Functions](#tuple-methodsfunctions)
        - [Packing and unpacking Tuples](#packing-and-unpacking-tuples)
        - [Questions](#questions-related-to-tuples)
    - [Dictionaries](#dictionaries)
        - [Ways to Initialize Dictionaries](#different-ways-to-initialize-dictionaries)
        - [Copying Dictionaries](#copy-dictionaries-deep-and-shallow)
        - [Dictionaries Functions/Methods](#built-in-dictionary-methodsfunctions)
        - [Packing and Unpacking Dictionaries](#packing-and-unpacking-dictionaries)
        - [Nested Dictionaries](#nested-dictionaries)
        - [Acessing Dictionary items](#accessing-dictionary-items)
        - [Questions](#questions-related-to-dictionaries)


# Non-primitive data types
Unlike primitive data types, which store single values (e.g., integers, strings, booleans), non-primitive can hold collections of values, to offer greater flexibility and organization for complex data scenarios.
Following are some main purposes of non-primitive data types.
 1. Facilitate the storage and manipulation of multiple interrelated data items.
 2. Provide efficient ways to represent complex data relationships and structures.
 3. Enhance code organization and readability by keeping related data together.

**Common Non-Primitive Data Types in Python:**
1. Lists
2. Tuples
3. Dictionaries
4. Sets

## Lists

Lists are mutable, ordered collections of items enclosed in square brackets `[]`. They can store values of different data types within the same list, offering versatility for representing diverse data. Lists fall under the **mutable** category, meaning you can add, remove, or change items within a list after it's initialized.

**Purpose:**
-   Organize and group related data for improved code structure and readability.
-   Represent sequences of items that may change over time (e.g., shopping lists, to-do lists).
-   Efficiently process and manipulate data using built-in list methods and operations.
    

### **Different Ways to Initialize Lists**

1.  **Empty List:**
    ```python
    empty_list = []
    ```
2.  **List with Items:**
    ```python
    numbers = [1, 2, 3, 4, 5]
    mixed_list = ["apple", 10, True, [3, 4]]
    ```
3.  **Using  `list()`  Constructor:**
    ```python
    new_list = list("hello")  # Creates a list from a string's characters
    ```   
4.  **List Comprehension:**
    ```python
    squares = [x * x for x in range(1, 11)]  # Creates a list of squares from 1 to 10
    
    ```    
5.  **Copying an Existing List:**
    ```python
    copied_list = numbers[:]  # Shallow copy (references same elements)
    copied_list = numbers.copy()  # Deep copy (creates new objects)
    ```

### **Some List Methods/Functions**

1.  **`append(x)`:** Adds an item `x` to the end of the list.
2.  **`insert(i, x)`:** Inserts an item `x` at index `i` in the list.
3.  **`remove(x)`:** Removes the first occurrence of `x` from the list.
4.  **`pop([i])`:** Removes and returns the item at index `i` (default: -1, last item).
5.  **`index(x, [start], [end])`:** Returns the index of the first occurrence of `x` between indices `start` and `end`.
6.  **`count(x)`:** Counts the number of occurrences of `x` in the list.
7.  **`sort()`:** Sorts the list in ascending order (in-place modification).
8.  **`reverse()`:** Reverses the order of elements in the list (in-place modification).
9.  **`clear()`:** Removes all elements from the list.
10.  **`copy()`:** Creates a shallow copy of the list (new list, same elements).

### **Questions Related to Lists**
**Lists:**
1.  **Explain the difference between shallow and deep copies of lists.**
    -   **Shallow copy:** Creates a new list with references to the same elements as the original list. Modifying one list affects the other. Use `list[:]` or slicing.
    -   **Deep copy:** Creates a new list with independent copies of the elements from the original list. Modifications in one list don't affect the other. Use `list.copy()` or dedicated modules like `copy.deepcopy()`.
    
2.  **How do you iterate over elements in a list?**
    
    -   Use a `for` loop to access each element sequentially.
    -   Use `enumerate()` to get both the index and element in each iteration.
    
3.  **How do you remove duplicate elements from a list?**
    
    -   Convert the list to a set (which removes duplicates). Use `set(my_list)` and convert back to a list if needed.
    -   Use a loop and checking for uniqueness with additional data structures.
    
4.  **How do you check if a list contains a specific element?**
    
    -   Use the `in` operator:  `x in my_list`.
    -   Use the `index()` method to try finding the element's index (raises `ValueError` if not found).
    
5.  **Explain the time and space complexity of common list operations (e.g., append, insert, access, search).**
    -   Most list operations have constant time complexity (`O(1)`)

## Tuple
Tuples are ordered collections of items enclosed in parentheses  `()`. They can store values of different data types within the same tuple, offering versatility for representing diverse data. Tuples fall under the **unmutable** category, meaning you cannot add, remove, or change individual elements within a tuple after it's initialized.

**Purpose:**
   -   Store fixed, ordered sequences of data that won't change over time.
   -   Represent relationships between items that shouldn't be modified (e.g., coordinates, calendar dates).
   -   Facilitate efficient lookups and access by index.

### **Different Ways to Initialize Tuples**

1.  **Empty Tuple:**
    ```python
    empty_tuple = ()
    ```
2.  **Tuple with Items:**
    ```python
    numbers = (1, 2, 3, 4, 5)
    mixed_tuple = ("apple", 10, True, [3, 4])
    ```
3.  **Using  `tuple()`  Constructor:**
    ```python
    new_tuple = tuple("hello")  # Creates a tuple from a string's characters
    ```
4.  **Packing Elements:**    
    ```python
    day_tuple = 2023, 10, 26  # Tuple created directly from comma-separated values
    
    ```
### **Tuple Methods/Functions**

1.  **`len(tuple)`:**  Returns the number of elements in the tuple.
2.  **`tuple[index]`:**  Accesses the element at the specified index (0-based).
3.  **`tuple.count(x)`:**  Counts the number of occurrences of  `x`  in the tuple.
4.  **`tuple.index(x, [start], [end])`:**  Returns the index of the first occurrence of  `x`  between indices  `start`  and  `end`.
5.  **`in`:**  Checks if an element exists in the tuple.
6.  **`min(tuple)`:**  Returns the smallest element in the tuple.
7.  **`max(tuple)`:**  Returns the largest element in the tuple.
8.  **`slice(start, stop, step)`:**  Creates a slice of the tuple from index  `start`  to  `stop`  with step  `step`.
9.  **`tuple + tuple2`:**  Concatenates two tuples.
10.  **`*tuple`:**  Repeats the tuple n times (e.g.,  `3 * (1, 2) = (1, 2, 1, 2, 1, 2)`).

### **Packing and Unpacking Tuples**

-   **Packing:**  Creating a tuple from existing variables:
    ```python
    a, b, c = 10, "apple", True  # Packs values into variables
    ```
    
-   **Unpacking:**  Assigning tuple elements to variables:
    ```python
    x, y, z = (1, 2, 3)  # Unpacks values into variables
    ```

### **Questions Related to Tuples**

1.  **Why use tuples instead of lists when immutability is not strictly required?**
    -   Tuples can provide an extra layer of security and prevent accidental modifications of data.
    -   They can be used as keys in dictionaries, where immutability helps ensure consistent hashing and lookup behavior.
    -   They can improve readability and code clarity by explicitly conveying an intent to preserve the data as-is.
2.  **How do you check if a tuple contains all unique elements?**
    -   Convert the tuple to a set. If the set length matches the tuple length, all elements are unique.
    -   Use  `len(set(tuple)) == len(tuple)`.
3.  **How do you swap adjacent elements in a tuple?**
    -   Create a new tuple with the swapped elements:  `swapped_tuple = (b, a)`.
    -   Tuples themselves cannot be modified in-place.
4.  **What are the performance implications of mutable vs. immutable data types?**
  -   **Immutable data types (tuples):**
    
	    -   Potentially faster for lookups and certain operations due to simpler internal structure (no mutability overhead).
	    -   May require more memory when creating new objects due to copying (for deep immutability).
	    -   Useful for performance-critical data that shouldn't be modified.
-   **Mutable data types (lists):**
    -   More efficient for modifying data in-place, avoiding creation of new objects.
    -   Can be slower for lookups and operations that heavily rely on immutability assumptions.
    -   Suitable for data that needs frequent updates or manipulation.
  
My apologies, I wasn't able to complete the previous response due to some technical limitations. Here's the final part focusing on the last two points and incorporating insights from the ratings:

**4. What are the performance implications of mutable vs. immutable data types?**

-   **Immutable data types (tuples):**
    
    -   Potentially faster for lookups and certain operations due to simpler internal structure (no mutability overhead).
    -   May require more memory when creating new objects due to copying (for deep immutability).
    -   Useful for performance-critical data that shouldn't be modified.
    
-   **Mutable data types (lists):**
    
    -   More efficient for modifying data in-place, avoiding creation of new objects.
    -   Can be slower for lookups and operations that heavily rely on immutability assumptions.
    -   Suitable for data that needs frequent updates or manipulation.
    

**5. How do you compare `tuple` and `list` comprehension for creating tuples and lists?**

-   **Use cases:**
    
    -   `tuple` comprehension: Primarily for creating concise, unmodifiable sequences.
    -   `list` comprehension: More versatile for creating modifiable lists, often with conditional expressions.
    
-   **Readability:**
    
    -   Both can be very readable in specific contexts. Choose the one that best conveys your intent and the immutability requirement.
    
-   **Performance:**
    -   Generally,  `tuple` comprehension might be slightly faster due to immutability, but the difference is often negligible in most practical scenarios.

## Dictionaries
Dictionaries are mutable, unordered collections of key-value pairs enclosed in curly braces `{}`. They allow you to store diverse data types associated with unique keys, offering flexibility for representing complex relationships. Dictionaries fall under the **mutable** category, meaning you can add, remove, or modify key-value pairs after creating the dictionary
**Purpose:**
- Organize and represent data with meaningful associations between keys and values.
- Implement data structures like hash tables for efficient lookups and access.
- Model real-world entities with attributes and properties (e.g., user profiles, inventory items).
    

### **Different Ways to Initialize Dictionaries**

1.  **Empty Dictionary:**
    ```python
    empty_dict = {}
    ```
2.  **Dictionary with Items:**
    ```python
    student_info = {"name": "Alice", "age": 25, "major": "Computer Science"}
    ```
3.  **Using  `dict()`  Constructor:**
    ```python
    new_dict = dict(name="Bob", age=30, skills=["Python", "Java"])
    
    ```

### Copy Dictionaries (Deep and Shallow)    

1. **Shallow Copy**
	-   Using the `copy()` method or `dict(original_dict)` constructor creates a shallow copy.
	-   Modifying a value in either dictionary will affect the other:
	```python
	original_dict = {"name": "Alice", "age": 30} 
	shallow_copy = original_dict.copy() 
	original_dict["age"] = 35  # Modify value in original dictionary 
	print(shallow_copy["age"]) # Output: 35 (value changed due to shallow copy)
	``` 
2. **Deep Copy**
	-   Using the `copy.deepcopy()` function from the `copy` module creates a deep copy.
	-   Modifications in one dictionary won't affect the other:
	```python
	original_dict = {"name": "Bob", "address": {"city": "New York"}} 
	deep_copy = copy.deepcopy(original_dict)
	```
	
### Built-in Dictionary Methods/Functions

1.  **`len(dict)`:** Returns the number of key-value pairs in the dictionary.
2.  **`dict.keys()`:** Returns a view of all dictionary keys.
3.  **`dict.values()`:** Returns a view of all dictionary values.
4.  **`dict.items()`:** Returns a view of all key-value pairs as tuples.
5.  **`in`:** Checks if a key exists in the dictionary.
6.  **`dict.get(key, default)`:** Returns the value for a key, or a default value if not found.
7.  **`dict.setdefault(key, default)`:** Returns the value for a key, or sets it to the default value if not found.
8.  **`dict.update(other)`:** Updates the dictionary with key-value pairs from another dictionary.
9.  **`dict.pop(key, default)`:** Removes and returns the value for a key, or a default value if not found.
10.  **`dict.clear()`:** Removes all key-value pairs from the dictionary.

### Packing and Unpacking Dictionaries

-   **Packing:** Creating a dictionary from existing variables:
    ```python
    first_name = "Alice"
    last_name = "Smith"
    address = "123 Main St"
    person = {"first_name": first_name, "last_name": last_name, "address": address}  
    ```
    
-   **Unpacking:** Assigning dictionary values to variables:
    ```python
    person = {"name": "Bob", "age": 30, "city": "New York"}
    name, age, city = person["name"], person["age"], person["city"]
    
    ```

### Nested Dictionaries

-   Store complex data structures with hierarchical relationships:
    ```python
    employees = {
        "Alice": {"department": "Engineering", "salary": 80000},
        "Bob": {"department": "Marketing", "salary": 75000},
    } 
    ```
-   Access nested values using nested keys:
    ```python
    alice_salary = employees["Alice"]["salary"]
    ```
### Accessing Dictionary Items
1.  **By Key:**
This is the most straightforward method, where you directly use the key enclosed in square brackets (`[]`) to retrieve the corresponding value. If the key doesn't exist, a `KeyError` is raised.
	```python
	person = {"name": "Alice", "age": 30, "city": "New York"}
	name = person["name"]  # Accessing the value associated with the "name" key
	print(name)  # Output: Alice
	```
2. **`get()` Method:**
This method provides a safer approach by allowing you to specify a default value to return if the key is not found. It avoids `KeyError` exceptions, making your code more robust.
	```python
	occupation = person.get("occupation", "N/A")  # Gets the "occupation" value or "N/A" if not found
	print(occupation)  # Output: N/A
	```
3. **Looping:**
Dictionaries are iterable, meaning you can loop through their elements using `for` loops. You can loop through keys, values, or key-value pairs depending on your needs.

### Questions related to Dictionaries
1.  **How do dictionaries ensure uniqueness of keys?**
**Answer:** Dictionaries rely on hash values calculated from keys for efficient lookups. Since hash values depend on the key's content,  **only immutable data types (strings, numbers, tuples) can be used as keys to guarantee unique and consistent hashing.** Using mutable data types as keys could lead to unpredictable behavior due to changing hash values.

2.  **What are the differences between shallow and deep copying dictionaries?**
**Answer:**  **Shallow copying** creates a new dictionary that references the same objects as the original for its values. Changes made in one dictionary reflect in the other.  **Deep copying** creates a completely independent copy where both keys and values are copied, and modifications are isolated. For nested dictionaries, deep copying is essential to avoid unintended changes.

3.  **How do you iterate through key-value pairs in a dictionary?**
**Answer:** Use the `for key, value in dictionary.items():` loop to iterate through both keys and values simultaneously. Alternatively, loop through `keys()` or `values()` separately if needed.

4.  **What are some common use cases for dictionaries in Python?**
**Answer:** Dictionaries are versatile for representing real-world entities with attributes (e.g., user profiles, inventory items), implementing hash tables for efficient lookups, storing configuration data, and modeling complex relationships between data elements.

5.  **How do you check if a specific key exists in a dictionary?**
**Answer:** The `in` operator provides a straightforward way to check key presence. You can also use the `get(key, default)` method with a default value to avoid `KeyError` exceptions for non-existent keys.