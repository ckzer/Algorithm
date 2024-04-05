while True:
    a = input()
    if a == "#":
        break
    x = -1
    for i in range(len(a)):
        if a[i] in ["a", "e", "i", "o", "u"]:
            x = i
            break
    if x != -1:
        print(a[x:] + a[:x] + "ay")
    else:
        print(a + "ay")
