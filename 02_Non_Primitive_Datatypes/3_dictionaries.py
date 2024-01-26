# Dictionaries holds data/items in key-value pairs, value can be of any data type

# Different ways to create dictionaries
user = {
    "name": "Raza",
    "age": 24,
}

user2 = dict(name="Ahmar", age=26)

print(user)
print(user2)
print(type(user))
print(len(user))

# Access items
print(user["name"])
print(user.get("age"))

# list all keys, values
print(user.keys())
print(user.values())

# items (key-value pairs) as tuples
print(user.items())

# membership checking
print("age" in user)
print("loginstatus" in user)

# change/add values in dicts
user["name"] = "Korg"
print(user)

user.update({"loginstatus": True})
print(user)

# remove items
print(user.pop("loginstatus"))
print(user)

user["isadult"] = True
print(user)

print(user.popitem())  # pop item removes last item and returns it in tuple form
print(user)

# clear and delete
user["isadult"] = True
print(user)

del user["isadult"]
print(user)

user2.clear()
print(user2)

del user2  # deletes whole dict

# copy dict
user2 = user  # user2 has reference to user, change in user2 will cause change in user
user2["name"] = "Raza"
print(user2)
print(user)

user3 = user.copy() 
print(user2)

user4 = dict(user)
print(user4)

# nested dicts
visitor1 = {"name": "1visit", "age": 23}
print(visitor1)

visitor2 = dict(visitor1)
visitor2["name"] = "2visit"
print(visitor2)

visitors = {"visitor1": visitor1, "visitor2": visitor2}

print(visitors)

print(visitors["visitor1"]["name"])
