a, b, c = map(int, input().split())
sum1 = int(a * b / c)
sum2 = int(a / b * c)
if sum1 > sum2:
    print(sum1)
else:
    print(sum2)
