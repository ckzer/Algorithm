t = int(input())
for i in range(t):
    a1, a2, a3, a4, a5, a6 = map(int, input().split())
    b1, b2, b3, b4, b5, b6, b7 = map(int, input().split())
    sum1 = (a1 * 1) + (a2 * 2) + (a3 * 3) + (a4 * 3) + (a5 * 4) + (a6 * 10)
    sum2 = (b1 * 1) + (b2 * 2) + (b3 * 2) + (b4 * 2) + (b5 * 3) + (b6 * 5) + (
        b7 * 10)
    if sum1 > sum2:
        print('Battle ', i + 1, ': ', 'Good triumphs over Evil', sep='')
    elif sum1 < sum2:
        print('Battle ',
              i + 1,
              ': ',
              'Evil eradicates all trace of Good',
              sep='')
    else:
        print('Battle ', i + 1, ': ', 'No victor on this battle field', sep='')
"""
t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = a[0] * 1 + a[1] * 2 + a[2] * 3 + a[3] * 3 + a[4] * 4 + a[5] * 10
    sum_b = b[0] * 1 + b[1] * 2 + b[2] * 2 + b[3] * 2 + b[4] * 3 + b[
        5] * 5 + b[6] * 10
    if (sum_a > sum_b):
        print("Battle {}: Good triumphs over Evil".format(i + 1))
    elif (sum_a < sum_b):
        print("Battle {}: Evil eradicates all trace of Good".format(i + 1))
    else:
        print("Battle {}: No victor on this battle field".format(i + 1))
"""