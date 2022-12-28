t = int(input())
while t:
    t -= 1
    a_cnt, b_cnt = 0, 0
    n = int(input())
    while n:
        n -= 1
        a, b = map(str, input().split())
        if a == b:
            continue
        else:
            if a == 'R':
                if b == 'P':
                    b_cnt += 1
                else:
                    a_cnt += 1
            elif a == 'P':
                if b == 'R':
                    a_cnt += 1
                else:
                    b_cnt += 1
            else:
                if b == 'R':
                    b_cnt += 1
                else:
                    a_cnt += 1
    if a_cnt > b_cnt:
        print('Player 1')
    elif a_cnt == b_cnt:
        print('TIE')
    else:
        print('Player 2')
