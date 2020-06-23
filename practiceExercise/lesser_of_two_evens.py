def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a, b))
    else:
        print(max(a, b))


lesser_of_two_evens(2, 4)
