a, b = map(int, input().split())
sum = 0
math = [0]
for i in range(50):
    for j in range(i):
        math.append(i)
for i in range(a, b+1):
    sum += math[i]
print(sum)
