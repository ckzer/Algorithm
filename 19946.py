n = int(input())
m = 64
while n % 2 == 0:
    n //= 2
    m -= 1
print(m)
