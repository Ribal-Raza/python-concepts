"""Demonstrating different ways to declare and manipulate tuples."""

# Tuples are ordered and immutable collections of items, enclosed in parentheses ().

# Declare tuples
usernames = ("Sami", "Jay", "Mike", "Ash", "Morris")
other_usernames = tuple(("Sid", "Kim"))
another = usernames

# Display the declared tuples
print("Usernames Tuple:", usernames)
print("Other Usernames Tuple:", other_usernames)
print("Another Tuple (Referencing 'usernames'):", another)

# Convert a list to a tuple
mylist = [1, 2, 3, 4]
mytuple = tuple(mylist)
print("Tuple Converted from List:", mytuple)

# Declare a tuple without using parentheses
mytuple2 = 2, 4, 7, 0, 2, 0, 1
print("Another Tuple Declared without Parentheses:", mytuple2)

# Concatenate two tuples
new_tuple = mytuple + mytuple2
print("Concatenated Tuple:", new_tuple)

# Sorting tuples
sorted_tuple = sorted(new_tuple)
print("Sorted Tuple:", sorted_tuple)

descending_sorted_tuple = sorted(new_tuple, reverse=True)
print("Sorted Tuple in Descending Order:", descending_sorted_tuple)

# Other tuple methods
count_of_zero = mytuple2.count(0)
print("Count of 0 in 'mytuple2':", count_of_zero)

index_of_7 = mytuple2.index(7)
print("Index of the first occurrence of 7 in 'mytuple2':", index_of_7)

is_mike_present = "Mike" in usernames
print("Is 'Mike' present in 'usernames'?", is_mike_present)

tuple_length = len(usernames)
print("Length of 'usernames' tuple:", tuple_length)
