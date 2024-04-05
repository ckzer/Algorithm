while True:
    n = input()
    if n == "EOI":
        break
    n = n.lower()

    flag = False
    for i in range(len(n)):
        if n[i : i + 4] == "nemo":
            flag = True
            break
    print("Found" if flag == True else "Missing")
