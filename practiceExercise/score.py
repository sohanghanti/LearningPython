num = 10


def countMoves(num):
    x = 0
    cnt = 0
    print('Target Number is:', num)
    for i in range(1, num):

        if x == num:
            break
        else:
            x = x + 1
            cnt = cnt + 1

        if num < 10:
            print('count, step: ', cnt, x)
            for j in range(cnt, num):
                if x <= num // 2:
                    x = x * 2
                    # print(x)
                    cnt = cnt + 1
                    print('count, step: ', cnt, x)

        else:
            cnt = countMoves(num // 2)
            if num % 2 == 0:
                x = x * 2
                cnt = cnt + 1
                print('count, step: ', cnt, x)
                return cnt
            else:
                x = x * 2
                cnt = cnt+1
                print('count, step: ', cnt, x)

                x = x + 1
                cnt = cnt + 1
                print('count, step: ', cnt, x)
                return cnt

    return cnt


print('steps:', countMoves(50))
