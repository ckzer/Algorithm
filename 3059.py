t = int(input())
for i in range(t):
    li1 = []
    sum = 0
    for _ in range(26):
        li1.append(0)
    s = input()
    for j in range(len(s)):
        li1[ord(s[j]) - 65] = 1
    for k in range(len(li1)):
        if li1[k] == 0:
            sum += k + 65
    print(sum)