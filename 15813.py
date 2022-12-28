n = int(input())
name = input()
cnt = 0
for i in range(n):
    cnt += ord(name[i]) - 64
print(cnt)