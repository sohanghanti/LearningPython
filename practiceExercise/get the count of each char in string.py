str1 = 'aassdeeeffgfhnccccccngjhhhh'

letter = ''
cnt = 0
for i in range(0, len(str1)):
    if letter == '':
        letter = str1[i]
        cnt = cnt + 1
        if i == len(str1)-1:
            print(letter + str(cnt))
    elif letter == str1[i]:
        cnt = cnt + 1
        if i == len(str1)-1:
            print(letter + str(cnt))
    else:
        print(letter + str(cnt))
        cnt = 0
        letter = str1[i]
        cnt = cnt + 1
        if i == len(str1)-1:
            print(letter + str(cnt))
