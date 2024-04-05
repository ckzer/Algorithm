n = input()
n = n.upper()
li1 = [0] * 26

for i in range(len(n)):
    li1[ord(n[i]) - 65] += 1

cnt = 0

for i in range(26):
    if cnt == 2:
        print("?")
        break
    elif li1[i] == max(li1):
        cnt += 1
        check = i

if cnt < 2:
    print(chr(check + 65))
