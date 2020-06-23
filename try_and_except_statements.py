def divideBy(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print("you are trying to divide by zero")


print(divideBy(12))
print(divideBy(2))
print(divideBy(0))
print(divideBy(3))


def ask_for_int():
    number = ''
    try:
        number = int(input("Enter the number :"))
    except:
        print('This is not number')


ask_for_int()
