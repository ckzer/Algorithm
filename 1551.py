n, k = map(int, input().split())
li = list(map(int, input().split(',')))
for i in range(k):
    for j in range(len(li) - 1):
        li[j] = li[j + 1] - li[j]
    li.pop()
print(*li, sep=',')  # 여기서 li 변수 앞에 *은 무슨 의미인가?
