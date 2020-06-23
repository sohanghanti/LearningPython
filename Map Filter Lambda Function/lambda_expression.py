# lambda is anonymous function
# it is used when you have implement the things only once so no need to create a function for the implementation
# e.g. convert the square function below in lambda expression:


# def square(num):
#     return num ** 2
#
# def sqaure(num): return num**2

var = lambda num: num ** 2


sum = lambda num1, num2: num1 + num2


print(sum(1, 2))

mul = lambda num: num * 2
print(mul(5))
