num = 49
count = 0
if num % 2 != 0: num = num - 1; count = count + 1
n = num // 2
count = count + 1
while n != 0:
    print(n)
    if n % 2 == 0:
        n = n // 2
        count = count + 1
    else:
        n = n - 1
        count = count + 1

print(count)
