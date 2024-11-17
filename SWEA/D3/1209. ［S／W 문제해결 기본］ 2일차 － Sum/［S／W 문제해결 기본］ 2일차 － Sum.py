for _ in range(10):
    max_cnt=0
    t=int(input())
    li=[list(map(int, input().split())) for _ in range(100)]
    for row in li:  # 행
        max_cnt=max(max_cnt, sum(row))

    for i in range(100):
        column_sum=sum(li[row][i] for row in range(100))
        max_cnt=max(max_cnt, column_sum)

    diag1_sum=sum(li[i][i] for i in range(100))
    max_cnt=max(max_cnt, diag1_sum)

    diag2_sum=sum(li[99-i][i] for i in range(100))
    max_cnt=max(max_cnt, diag2_sum)

    print(f"#{t} {max_cnt}")