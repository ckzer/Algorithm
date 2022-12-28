n, m = map(int, input().split())
a, b = set(), set()
for i in range(n):
    a.add(input())  # 듣도 못한 사람 a set에 입력
for i in range(m):
    b.add(input())  # 보도 못한 사람 b set에 입력
# 리스트를 이용해 a와 b의 교집합을 구한 뒤 sorted 함수를 이용하여 c라는 임시 리스트에 저장
c = sorted(list(a & b))
print(len(c))
for i in range(len(c)):  # c리스트 출력
    print(c[i])
