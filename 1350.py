n = int(input())
m = list(map(int, input().split()))
k = int(input())
cnt = 0
for i in range(n):
    if m[i] == 0:
        continue
    elif m[i] % k == 0:
        cnt += m[i] // k
    elif m[i] > k:
        cnt += m[i] // k + 1
    elif m[i] < k:
        cnt += 1
print(cnt * k)
