def rectangle(l, b):
    print('*' * l)
    for breadth in range(0, b-2):
        print('*' + ' ' * (l-2) + '*')
    print('*' * l)


rectangle(20, 5)



