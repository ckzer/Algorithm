n = int(input())
t = list(int(input()) for _ in range(n))
chapter = 0
time = 30
for i in range(n):
    time -= t[i]
    if time > 0:
        chapter += 1
    elif time == 0:
        chapter += 1
        time = 30
    else:
        if abs(time) <= t[i] / 2:
            chapter += 1
            time = 30
        time = 30
print(chapter)
