str1 = 'the quick brown fox jumps over the lazy dog'

list1 = str1.split(" ")

list1 = [len(x) for x in list1 if x != 'the']

print(list1)

sen = 'mathematics'
list1 = {x for x in sen if 'aeiou'.count(x) > 0}

print(list1)


list1 = [x for x in sen if 'aeiou'.count(x) == 0]
print("".join((list1)))