t = int(input())
for i in range(t):
    a, b = map(str, input().split())
    li1 = sorted(list(a))
    li2 = sorted(list(b))

    if li1 == li2:
        print(a + ' & ' + b + " are anagrams.")
    else:
        print(a + ' & ' + b + " are NOT anagrams.")
