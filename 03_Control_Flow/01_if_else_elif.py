"""
Demonstration of conditional statements with clear explanations and organized code.
"""

# -------------------------------
# Checking for an item in a list
# -------------------------------

mylist = [1, 2, "apple", True, (34, "Fine"), 4.7]

if 2 in mylist:
    print("2 is present in the list!")  # Informative output

# ------------------------------
# Checking the type of an element
# ------------------------------

if isinstance(mylist[4], tuple):  # Reliable type check using isinstance
    print("The list contains a tuple.")
else:
    print("The list does not contain a tuple.")

# -------------------------------
# Evaluating list length with elif
# -------------------------------

if len(mylist) == 5:
    print("The list has the perfect length of 5.")
elif 1 <= len(mylist) <= 5:  # Combine conditions for clarity
    print("The list has less than five items.")
elif 5 <= len(mylist) <= 10:
    print("The list has more than five items.")
else:
    print("The list should only have between 1 to 10 items.")

# -----------------------
# Nested conditional logic
# -----------------------

mydict = {
    "name": "Raza",
    "age": 24,
    "hobbies": ["gardening", "music", "coding", "travel"],
    "isAdult": True,
}

if "hobbies" in mydict:
    print("===== Hobbies found =====")
    if "coding" in mydict["hobbies"] or "music" in mydict["hobbies"]:  # Corrected logic
        print("Coding + Music = Perfect combo!")
    elif "rock" in mydict["hobbies"]:
        print("Roses are red")
    else:
        print("Well done on having diverse hobbies!")
else:
    print("Consider exploring some hobbies!")
