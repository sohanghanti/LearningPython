def reverseString(str1):
    print(str1[::-1])


reverseString('sohanghanti')

###################################################
def reversal(str1):
    print("".join(reversed(str1)))
reversal("Sohan")


################################################
str1 = "Sohan"
for i in range(len(str1)-1, -1, -1):
    print(str1[i])


###################################################+
str2 = "ghanti"
str3 = ''
for i in str2:
    str3 = i + str3
print(str3)
