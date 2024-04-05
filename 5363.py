n = int(input())
for i in range(n):
    li = list(map(str, input().split()))
    print(" ".join(li[2:] + li[:2]))
# print(*li[2:], *li[:2])
