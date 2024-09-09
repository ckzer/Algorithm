check=False
a=[int(input()) for _ in range(9)]
total_sum = sum(a)-100

for i in range(8):
    for j in range(i+1, 9):
        if a[i]+a[j]==total_sum:
            result=[a[k] for k in range(9) if k!=i and k!=j]
            result.sort()
            for li in result:
                print(li)
            check=True
            break
    if check==True:
        break