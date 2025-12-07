# Object Types / Data Types

- **Number**: Represents numeric data. `1234`, `3.1415`, `3+4j`, `0b111`, `Decimal()`, `Fraction()`
- **String**: An immutable sequence of characters. `'spam'`, `"Bob's"`, `b'a'`, `u'spm'`
- **List**: An ordered, mutable sequence of objects. `[1, [2, 'three'], 4.5]`, `list(range(10))`
- **Tuple**: An ordered, immutable sequence of objects. `(1, 'spam', 4, 'U')`, `tuple('spam')`, `namedtuple`
- **Dictionary**: An unordered mapping of unique keys to values. `{'food': 'yum', 'age': 35}`
- **Set**: An unordered collection of unique and immutable objects. `set('abc')`, `{'a', 'b', 'c'}`
- **File**: Represents a file on the computer for reading or writing. `open('myfile.txt', 'r')`
- **Boolean**: Represents logical values, either True or False. `True`, `False`
- **None**: A special object representing the absence of a value. `None`
- **Functions**: A block of reusable code that performs a specific action. `def my_func(x): return x * 2`
- **Modules**: A file containing Python code, used to organize and reuse code. `import math`
- **Classes**: A blueprint for creating objects, enabling object-oriented programming. `class MyClass: def __init__(self, name): self.name = name`

## Advanced Types

- **Decorators**: A function that takes another function and extends its behavior without explicitly modifying it. `@my_decorator`
- **Generators**: A simple way to create iterators using functions and the `yield` keyword. `def my_gen(): yield 1`
- **Iterators**: An object that enables iteration over a container. `iter([1, 2, 3])`
- **Metaprogramming**: The ability of a program to examine, and modify its own structure and behavior. `type('MyClass', (), {})`