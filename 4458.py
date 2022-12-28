n = int(input())
for i in range(n):
    m = input()
    print(m[0].upper()+m[1:])

'''
4번째 줄 부분을 저런 출력 말고
m=input()
m[0]=m[0].upper()
print(m)
으로 하면 오류나는지 모르겠음
'''
