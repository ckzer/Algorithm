a, b = map(int, input().split())
n = int(input())
sum = list(range(n))
sum_1 = abs(b-a)
for i in range(n):
    num = int(input())
    calc = abs(num-b)
    sum.append(calc)

for j in range(n):
    if sum[j] > sum[j+1]:
        low = sum[j+1]+1
    else:
        low = sum[j]+1
if low > sum_1:
    print(sum_1)
else:
    print(low)
