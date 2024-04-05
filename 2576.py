a = []
for i in range(7):
    a.append(int(input()))
cnt = 100
sum = 0
for i in range(7):
    if a[i] % 2 == 1:
        sum += a[i]
        if cnt > a[i]:
            cnt = a[i]
if sum == 0:
    print(-1)
else:
    print(sum, cnt, sep="\n")
"""다른버전
n = list(int(input()) for _ in range(7))
odd = []
sum = 0
for i in range(len(n)):
    if n[i] % 2 == 1:
        odd.append(n[i])
        sum += n[i]
if sum == 0: print(-1)
else:
    print(sum, min(odd), sep='\n')
"""
