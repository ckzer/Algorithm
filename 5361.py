t = int(input())
for i in range(t):
    a, b, c, d, e = map(int, input().split())
    sum = 0
    sum += (a * 350.34) + (b * 230.90) + (c * 190.55) + (d * 125.30) + (e * 180.90)
    print("${0:.2f}".format(sum))
