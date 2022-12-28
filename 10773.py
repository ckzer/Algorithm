k = int(input())
money = []
sum = 0
for i in range(k):
    num = int(input())
    if num == 0:
        money.pop()
    else:
        money.append(num)
for i in range(len(money)):
    sum += money[i]
print(sum)