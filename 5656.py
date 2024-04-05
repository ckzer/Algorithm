cnt = 0
while True:
    t = list(input().split())
    if t[1] == "E":
        break
    cnt += 1
    if t[1] == ">":
        print("Case {}: ".format(cnt) + str(int(t[0]) > int(t[2])).lower())
    elif t[1] == ">=":
        print("Case {}: ".format(cnt) + str(int(t[0]) >= int(t[2])).lower())
    elif t[1] == "<":
        print("Case {}: ".format(cnt) + str(int(t[0]) < int(t[2])).lower())
    elif t[1] == "<=":
        print("Case {}: ".format(cnt) + str(int(t[0]) <= int(t[2])).lower())
    elif t[1] == "==":
        print("Case {}: ".format(cnt) + str(int(t[0]) == int(t[2])).lower())
    elif t[1] == "!=":
        print("Case {}: ".format(cnt) + str(int(t[0]) != int(t[2])).lower())
