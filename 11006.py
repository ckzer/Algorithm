t = int(input())
x = 0
while x < t:
    x += 1
    n, m = map(int, input().split())
    k = m * 2 - n
    print(k, m - k)
