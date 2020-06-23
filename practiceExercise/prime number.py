def prime_number(num):
    l1 = []
    for j in range(3, num+1):
        for i in range(2, j+1):
            if j % i == 0:
                # print("not prime number ", j)
                break
            else:
                if i == j-1:
                    l1.append(j)
    print(l1)


prime_number(100)


def prime_number2(num):
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0:
            print("not prime number ", num)
            cnt = cnt + 1
            break
        else:
            if i == num-1:
                print("prime number ", num)
                break

prime_number2(99)

