a = list(map(int, input().split()))
b = int(input())
a.sort()
for i in range(len(a)):
    if a[i] == b:
        check = len(a) - i
if check <= 5:
    print("A+")
elif check <= 15:
    print("A0")
elif check <= 30:
    print("B+")
elif check <= 35:
    print("B0")
elif check <= 45:
    print("C+")
elif check <= 48:
    print("C0")
else:
    print("F")
