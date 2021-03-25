def fibbonacci(num):
    f = 0
    s = 1
    print(f)
    print(s)
    for i in range(0, num):
        s = f + s
        f = s - f
        print(s)


fibbonacci(10)

temp = 5
for i in range(temp):
    print(i)