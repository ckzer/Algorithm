n, m = map(int, input().split())
li=dict()
for i in range(n):
    a, b=input().split()
    li[a]=b
for i in range(m):
    a=input()
    print(li[a])