for _ in range(10):
    dump=int(input())
    li=list(map(int, input().split()))
    for i in range(dump):
        max_li, min_li=max(li), min(li)
        li[li.index(max_li)] -= 1
        li[li.index(min_li)] += 1
    print(f"#{_+1} {max(li)-min(li)}")