n = int(input())
name = {}
for i in range(n):
    s = input()
    if s[0] in name:
        name[s[0]] += 1
    else:
        name[s[0]] = 1
ans = []
for i in name.keys():
    if name[i] >= 5:
        ans.append(i)
if len(ans) == 0:
    print("PREDAJA")
else:
    ans.sort()
    print(''.join(ans))