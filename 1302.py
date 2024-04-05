n = int(input())
li = dict()
li1 = list()
for i in range(n):
    tmp = input()
    if tmp in list(li.keys()):
        li[tmp] += 1
    else:
        li[tmp] = 1
maxim = max(list(li.values()))
name = list(li.keys())
for i in name:
    if li[i] == maxim:
        li1.append(i)
li1.sort()
print(li1[0])

n = int(input())
for i in range(n):
    a = input()
    a_c = a.count("g") + a.count("G")
    b_c = a.count("b") + a.count("B")
    if a_c > b_c:
        print(f"{a} is GOOD")
    elif a_c < b_c:
        print(f"{a} is A BADDY")
    else:
        print(f"{a} is NEUTRAL")
