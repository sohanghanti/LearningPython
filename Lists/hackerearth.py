str1 = 'aabcccabba'

def string_minimization(str1):
    global new
    r = int(len(str1) / 2)
    left = str1[:r]
    right = str1[r:]

    print(left)
    print(right)
    for i in range(len(left)):
        if left[0] == right[-1]:
            right = right.rstrip()
            left = left.lstrip()
            new = right + left
    return new


out_ = string_minimization(str1)
print(out_)