s1, s2 = map(int, input().split())
check = True
for i in range(s1):
    sample1, sample2 = map(int, input().split())
    if sample1 != sample2:
        check = False
        print("Wrong Answer")
        break
if check == True:
    for i in range(s2):
        system1, system2 = map(int, input().split())
        if system1 != system2:
            check = False
            print("Why Wrong!!!")
            break
if check == True:
    print("Accepted")
