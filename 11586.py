n = int(input())
mir = list(list(input()) for i in range(n))
k = int(input())
if k == 1:
    for i in range(n):
        for j in range(n):
            print(mir[i][j], end='')
        print()
elif k == 2:
    for i in range(len(mir)):
        for j in range(len(mir[i]) - 1, -1, -1):
            print(mir[i][j], end='')
        print()

else:
    for i in range(n - 1, -1, -1):
        for j in range(n):
            print(mir[i][j], end='')
        print()