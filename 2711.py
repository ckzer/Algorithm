t = int(input())
for _ in range(t):
    a, b = input().split()
    print(b[:int(a)-1]+b[int(a):])
