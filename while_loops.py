spam = 0
while spam < 5:
    print("hello")
    spam = spam + 1

##############################################################
cnt = 1
print("Enter the password: ")
pwd = input()

while pwd != 'Welcome1@3':
    while cnt != 5:
        print("Please enter the correct password")
        pwd = input()
        cnt = cnt + 1
        print(cnt)
    break


