
def check_even(num):
    if num % 2 == 0:
        return num


list1 = [0, 1, 10, 3, 4, 5, 6, 7, 8, 8, 10, 4]
even = filter(check_even, list1)
print(list(even))

even = map(check_even, list1)
print(list(even))


def multiply(num):
    return num * 8


mul = map(multiply, list1)
print(list(mul))

fil = filter(multiply, list1)
print(list(fil))


