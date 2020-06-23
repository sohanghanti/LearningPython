from practiceExercise.interviewMocha_Practice import print_integers

lists = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(lists)-1):
    for j in range(i+1, len(lists)-1):
        if lists[i] + lists[j] == 5:
            print(lists[i], lists[j])


print_integers.print_int()
