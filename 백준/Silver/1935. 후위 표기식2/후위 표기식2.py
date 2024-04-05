class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if not self.items:
            return 1
        return 0

    def top(self):
        return self.items[-1]

s=Stack()
n=int(input())
sentence=input()
cnt=[0]*27
for i in range(n):
    cnt[i]=int(input())
for i in sentence:
    if i=='*':
        a=s.pop()
        b=s.pop()
        s.push(a*b)
    elif i=='+':
        a=s.pop()
        b=s.pop()
        s.push(a+b)
    elif i=='-':
        a=s.pop()
        b=s.pop()
        s.push(b-a)
    elif i=='/':
        a=s.pop()
        b=s.pop()
        s.push(b/a)
    else:
        s.push(cnt[ord(i)-ord('A')])
print("%.2f" %s.top())