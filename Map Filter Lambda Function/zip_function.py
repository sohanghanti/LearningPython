# The zip() function returns an iterator of tuples based on the iterable object.
# If no parameters are passed, zip() returns an empty iterator
# If a single iterable is passed, zip() returns an iterator of 1-tuples.
# Meaning, the number of elements in each tuple is 1.
# If multiple iterables are passed, ith tuple contains ith
# Suppose, two iterables are passed; one iterable containing 3 and other containing 5 elements.
# Then, the returned iterator has 3 tuples. It’s because iterator stops when shortest iterable is exhaused.


name = ["Manjeet", "Nikhil", "Shambhavi"]
roll_no = [4, 1, 3]
marks = [40, 50, 60]

mapped = zip(name, roll_no, marks)

print(list(mapped))

# Output:
# [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60)]
