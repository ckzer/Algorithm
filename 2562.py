li = []
for i in range(9):
    li.append(int(input()))
for i in range(9):
    if max(li) == li[i]:
        a = i
        break
print(max(li))
print(a)
