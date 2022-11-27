# When it comes to generators, they are like functions that
# instead of returning a value and deleting the function data from the memory
# they yield a value and save the state of the function as follows


def infinite_sequence():
    """generates a infinite sequence of numbers"""
    itr = 0
    while True:
        yield itr
        itr += 1


# we call a yielded value by using next() or a for loop

infinite_sequence_gen = infinite_sequence()
print(f"next: {next(infinite_sequence_gen)}")
print(f"next: {next(infinite_sequence_gen)}")

# with a for loop

count = 0
for num in infinite_sequence_gen:
    print(num)
    if count == 10:
        break
    count += 1

# If you watch the console output the generator does not re-start from zero
# in the for loop. this is because once it is called, it saves the function state
# including the local variables and scoped available data.

# Also, we can generate generator expressions which are like list comprehensions

example_list = (x for x in range(5))
print(type(example_list))

# Also, yield is a expression, so it can be assigned to a variable. This is useful
# when we use send(), throw(), or close() methods with the iterator. With send()
# we can return a value to variable holding the yield value and continue with
# the saved state function


def infinite_sequence_with_send():
    """generates a infinite sequence of numbers"""
    itr = 0
    while True:
        i = yield itr
        if i is not None:
            itr = i
        itr += 1


infinite_sequence_with_send_gen = infinite_sequence_with_send()
for num in infinite_sequence_with_send_gen:
    print(f"num = {num}")
    if num % 2 == 0:
        infinite_sequence_with_send_gen.send(num * 2)

    if num > 100:
        infinite_sequence_with_send_gen.close()  # this close and re-start the generator
        break

# throw() Could be used to throw an exception, it is useful if you are trying to catch and handle errors
