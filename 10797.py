a = int(input())
n1, n2, n3, n4, n5 = map(int, input().split())
cnt = 0
if a == n1:
    cnt += 1
if a == n2:
    cnt += 1
if a == n3:
    cnt += 1
if a == n4:
    cnt += 1
if a == n5:
    cnt += 1

print(cnt)
