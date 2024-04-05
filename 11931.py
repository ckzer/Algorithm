input = __import__("sys").stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = sorted(a, reverse=True)
for i in range(n):
    print(a[i])
