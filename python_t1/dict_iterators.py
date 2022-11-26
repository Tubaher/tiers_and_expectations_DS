# We have different ways to iterate trough a dict
example_dict = {
    "a": "apple",
    "b": "banana",
    "c": "Cifrut",
    "d": "Django",
    "e": "Elixir",
}

# dict.keys() to iterate across the dict keys
for key in example_dict.keys():
    print(key)

# dict.values() to iterate across the dict values
for value in example_dict.values():
    print(value)

# dict.items() to iterate across the dict (key,value)
for key, value in example_dict.items():
    print(f"key: {key}, value: {value}")
