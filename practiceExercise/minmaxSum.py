arr = [7, 69, 2, 221, 8974, 8974]

print(max(arr))
print(len(arr))
print(arr.count(max(arr)))
print("result:", len(arr) - arr.count(max(arr)))


def minMaxSum(arr):
    s1, s2 = 0, 0
    arr.sort()
    for i in range(len(arr)-1):
        s1 = s1 + arr[i]
        print(s1)
    print("%%%%%%%%%%%%%%%%%%%%5")
    for j in range(1, len(arr)):
        s2 = s2 + arr[j]
        print(s2)

    print(s1, s2)


minMaxSum(arr)