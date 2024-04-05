"""
n = int(input())
sum = 0
for i in range(n+1):
    for j in range(i, n+1):
        sum += i+j
print(sum)    # 주석 test
"""
n = int(input())
sum = 0
x, y = 0, 0
while not (x == n and y == n):
    if x > y:
        y += 1
    else:
        x += 1
        y = 0
    sum += x + y
print(sum)
