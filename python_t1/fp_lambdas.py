# Example of a lambda expression in python
add_2 = lambda x: x + 2
print(add_2(2))

# It can be used with maps and filters
a = [1, 2, 3, 4]
a_by_2 = list(map(lambda x: x * 2, a))
print(a_by_2)

a_to_2 = list(filter(lambda x: x % 2 == 0, a))
print(a_to_2)
