while True:
    b = []
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        break
    b.append(a[2]-a[1])
    b.append(a[3]-a[0])
    print(' '.join(map(str, b)))
