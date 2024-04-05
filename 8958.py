t = int(input())
for _ in range(t):
    cnt, sum = 0, 0
    a = tuple(input())
    for i in range(len(a)):
        if a[i] == "O":
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
