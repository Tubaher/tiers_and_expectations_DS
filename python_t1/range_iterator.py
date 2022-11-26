# range() is not an iterator by itself. It is a method that generate a range objects which
# generates a list of numbers

test = range(6)
print(f"Range object: {test}")

# We cannot use next() on a range object directly because it is not an iterable
# Then, if we would like to iter trough the range object we need to use iter()

range_iter = iter(test)
print(f"Next item in range : {next(range_iter)}")

# range method has start, stop, and step argument

test_range_step = range(1, 10, 2)
test_iter_step = iter(range(1, 10, 2))
print(f"Next item in range 1 : {next(test_iter_step)}")
print(f"Next item in range 2 : {next(test_iter_step)}")

# Also, we can access some properties

print(f"range start: {test_range_step.start}")
print(f"range stop: {test_range_step.stop}")
print(f"range step: {test_range_step.step}")
