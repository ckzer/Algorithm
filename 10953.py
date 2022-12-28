'''
t = int(input())
for i in range(t):
    a, b = map(int, input().split(','))
    print(a+b)
'''
t = int(input())
while t:
    t -= 1
    a, b = map(int, input().split(','))
    print(a+b)
