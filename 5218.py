t = int(input())
for i in range(t):
    li1 = []
    x, y = input().split()
    for j in range(len(x)):
        if ord(x[j]) <= ord(y[j]):
            li1.append(ord(y[j]) - ord(x[j]))
        else:
            li1.append(ord(y[j]) + 26 - ord(x[j]))
    print("Distances: {}".format(" ".join(map(str, li1))))
