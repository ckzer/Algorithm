input = __import__("sys").stdin.readline
n = int(input())
num = 0
for i in range(n):
    num += int(input())
print(num - n + 1)
