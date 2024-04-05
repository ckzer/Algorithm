n = int(input())
sum1 = 0
sum0 = 0
for i in range(n):
    k = int(input())
    if k == 1:
        sum1 += 1
    else:
        sum0 += 1
if sum1 > sum0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
