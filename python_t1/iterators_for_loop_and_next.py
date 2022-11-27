# to use a for loop we need to provide a sequence.
# a sequence could be a string, a list, a tuple, and many other objects
fruits = ["apple", "banana", "orange", "lemon", "coconut"]

for fruit in fruits:
    print(f"This is a {fruit}")

# we can also add a else block in a for loop that will be executed once
# the loop is over normally without a break on it
# this can be useful when searching for an item
for fruit in fruits:
    if fruit == "lemon":
        print("Yes, we have lemon!")
        break
else:
    print("The fruit was not on stock")

for fruit in fruits:
    if fruit == "grapes":
        print("Yes, we have grapes!")
        break
else:
    print("The fruit was not on stock")

# To use next, we need an iterator first. Then, we can use iter()
fruits_iterator = iter(fruits)
print(f"Next item on the fruits iterator: {next(fruits_iterator)}")
print(f"Next item on the fruits iterator: {next(fruits_iterator)}")
