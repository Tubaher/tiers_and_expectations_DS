# Thw walrus operator allows us to bind an expression to a variable for its immediate use

fruits = ["apple", "banana", "orange", "grapes"]

for fruit in fruits:
    print(f"fruit: {fruit} in {fruits}")

# we can reduce the code above by using the expression assignment in the for loop

for fruit in (fruits := ["apple", "banana", "orange", "grapes"]):
    print(f"fruit: {fruit} in {fruits}")
    # even when we do not initialize a variable called fruit, with the walrus operator
    # we can assign the assign the list to the fruits variable and used it immediately
