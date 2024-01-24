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