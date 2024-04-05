while True:
    cnt = 0
    a = input()
    if a == "#":
        break
    for i in range(len(a)):
        if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
            cnt += 1
        elif a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U":
            cnt += 1
    print(cnt)
