# shortest way to create a new list, set, dict etc.

lst = [1, 4, 2, 6, 9, 3, 0]

# create a new list of even numbers
lst1 = [num for num in lst if num % 2 == 0]
# create a dict of states and capitals
states = ['mah', 'kar', 'guj']
caps = ['mum', 'ban', 'gan']

dict_cap = {key: value for (key, value) in zip(states, caps)}

# zip function
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2, 6]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = list(zip(name, roll_no, marks))
print(mapped)


lst = [1, 4, 2, 6, 9, 3, 0]

print(lst[-1:0])
print(lst[2:-2])




