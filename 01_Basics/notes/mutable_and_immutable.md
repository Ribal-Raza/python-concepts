# Mutable vs. Immutable in Python: Memory & References

## 1. The Core Concept: Variables are References

In many programming languages, variables are thought of as "containers" or "buckets" that hold values.
In Python, this model is incorrect.

*   **Variables are Tags**: A variable is just a name (a reference) attached to an object in memory.
*   **Objects live in Memory**: The data (numbers, strings, lists) lives in specific memory addresses. The variable points to that address.

## 2. Immutable Objects (The "Statues")

**Definition**: An object whose internal state cannot be changed after it is created.

**Common Immutable Types**:

*   Integers (`int`)
*   Floats (`float`)
*   Strings (`str`)
*   Tuples (`tuple`)
*   Booleans (`bool`)

### How Modification Works (The Illusion)

When you "modify" an immutable variable, you are actually creating a **new** object and moving the reference.

**Example**:
```python
x = 10
x = 15
```
1.  Python creates object `10` at address `A`. `x` points to `A`.
2.  Python creates object `15` at address `B`. `x` moves to point to `B`.
3.  Object `10` is left behind (and eventually garbage collected).

### The "Shared Reference" Proof:

```python
a = 10
b = a      # b points to the same object (10) as a
a = 15     # a moves to new object (15)

print(b)   # Output: 10 (b is still pointing to the old object)
```

## 3. Mutable Objects (The "Briefcases")

**Definition**: An object whose internal contents can be modified in place, without changing its memory address.

**Common Mutable Types**:

*   Lists (`list`)
*   Dictionaries (`dict`)
*   Sets (`set`)

### How Modification Works (In-Place)

When you modify a mutable object, the memory address stays the same. The data inside changes.

### The "Shared Reference" Trap:
This is a common source of bugs.

```python
list_1 = [1, 2, 3]
list_2 = list_1      # list_2 points to the SAME list object as list_1

list_1.append(4)     # We modify the object IN PLACE

print(list_2)        # Output: [1, 2, 3, 4]
                     # list_2 changed because it points to the same object!
```

## 4. Summary Table

| Feature | Immutable | Mutable |
|---|---|---|
| **Examples** | `int`, `str`, `tuple` | `list`, `dict`, `set` |
| **Modification** | Creates a **NEW** object. | Modifies the **EXISTING** object. |
| **Memory Address** | Changes on assignment. | Stays the same on modification. |
| **Copying** | `b = a` is safe (independent). | `b = a` creates a link (dependent). |

## 5. Verifying with `id()`

You can verify this behavior using Python's built-in `id()` function, which returns the memory address of an object.

### Immutable Check
```python
s = "Hello"
print(id(s))  # e.g., 140234
s = s + " World"
print(id(s))  # e.g., 140560 (Different Address -> New Object)
```

### Mutable Check
```python
l = [1, 2]
print(id(l))  # e.g., 250112
l.append(3)
print(id(l))  # e.g., 250112 (Same Address -> Same Object)
```
