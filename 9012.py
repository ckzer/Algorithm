t = int(input())

for i in range(t):
    tmp = 1
    left = right = 0
    case = input()
    for j in case:
        if j == '(':
            left += 1
        else:
            right += 1
        if left < right:
            tmp = 0
            break
    if tmp == 0:
        print('NO')
    elif left == right:
        print('YES')
    else:
        print('NO')