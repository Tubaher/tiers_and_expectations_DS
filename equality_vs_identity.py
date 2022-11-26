list_1 = [1, 2, 3]
list_2 = list_1
a = [3, 4]
b = [3, 4]

# equality
print(list_1 == list_2)  # Evaluate that list_1 and list_2 match with the same content
print(a == b)  # Evaluate that a and b match with the same content

# identity
print(list_1 is list_2)  # Evaluate if they are the same object -> true
print(a is b)  # Evaluate if they are the same object -> false

# a way to see that they are referring to the same object is by watching their id
print(f"Id for list 1: {id(list_1)}")
print(f"Id for list 2: {id(list_2)}")
print(f"Id for a: {id(a)}")
print(f"Id for b: {id(b)}")

# also, if we add an element to list_1 it will be reflected win list_2 since they are
# 'pointing' to the same element
list_1.append(4)
print(f"list_1: {list_1}")
print(f"list_2: {list_2}")
