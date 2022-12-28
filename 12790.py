t = int(input())
for _ in range(t):
    a = tuple(map(int, input().split()))
    hp = a[0]+a[4]
    mp = a[1]+a[5]
    power = a[2]+a[6]
    defence = a[3]+a[7]
    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if power < 0:
        power = 0
    print(hp+(5*mp)+(2*power)+(2*defence))
