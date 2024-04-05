a = input()
joi, ioi = 0, 0
for i in range(len(a)):
    if a[i : i + 3] == "JOI":
        joi += 1
    if a[i : i + 3] == "IOI":
        ioi += 1
print(joi)
print(ioi)
