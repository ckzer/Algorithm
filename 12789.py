n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(n):
        if j + 1 == i:
            check = j
