n, m = input().split()
k = n * int(n)
if len(k) > int(m):
    print(k[0 : int(m)])
else:
    print(k)
