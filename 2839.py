n = int(input())
sum = 0
while n >= 3:
    if n % 5 == 0:
        five = n // 5
        sum += five
        n = 0
        break
    else:
        n -= 3
        sum += 1
print(-1 if n != 0 else sum)
