a = list(map(int, input().split()))
check = 1
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        check = 0
        break
if check == 1:
    print("Good")
else:
    print("Bad")
