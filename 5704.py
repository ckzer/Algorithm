while True:
    a = input()
    if a == '*':
        break
    d = {}
    for i in range(26):
        d[chr(97 + i)] = 0

    for i in range(len(a)):
        if ord('a') <= ord(a[i]) <= ord('z'):
            d[a[i]] = 1

    d_key = list(d.keys())
    flag = True
    for i in range(len(d_key)):
        if d[d_key[i]] == 0:
            flag = False
            break

    print('Y' if flag == True else 'N')
