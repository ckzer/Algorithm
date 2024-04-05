n = int(input())
sum1 = sum2 = 0
a = list(map(int, input().split()))
for i in range(n):
    sum1 += (a[i] // 30) * 10 + 10
    sum2 += (a[i] // 60) * 15 + 15
if sum1 < sum2:
    print("Y", sum1)
elif sum1 > sum2:
    print("M", sum2)
else:
    print("Y M", sum1)
