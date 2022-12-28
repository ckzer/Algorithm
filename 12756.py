a, b = map(int, input().split())
c, d = map(int, input().split())
while 1:
    d -= a
    b -= c
    if d <= 0 and b <= 0:
        print('DRAW')
        break
    elif d <= 0:
        print('PLAYER A')
        break
    elif b <= 0:
        print('PLAYER B')
        break
