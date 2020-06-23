def fibbonacci(num):
    f = 0
    s = 1
    print(f)
    print(s)
    for i in range(num-2):
        s = f + s
        f = s - f
        print(s)


fibbonacci(10)