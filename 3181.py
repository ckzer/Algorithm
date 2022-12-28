a = input().split()
li1 = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
r = a[0][0]

for i in range(1, len(a)):
    if a[i] in li1:
        continue
    r += a[i][0]
print(r.upper())