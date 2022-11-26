# it basically give a iterator key to each element in a data collection
list_a = ["Ana", "Diego", "Jessy", "Oscar"]

# If we use a for loop to iterate across the list. We can do:
for name in list_a:
    print(name)

# However, if we would like to save the reference of one name,
# so we can access it later on. We can do:

for idx, name in enumerate(list_a):
    print(f"name : {name}, at position {idx}")

# Enumerate just returns an enumerate object, and when it is transformed
# to a list it looks like a list of tuples with (index, item) elements
print(enumerate(list_a))
print(list(enumerate(list_a)))
