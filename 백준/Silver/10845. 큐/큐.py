input=__import__('sys').stdin.readline
from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
    def pop(self):
        return self.q.popleft() if self.q else -1
    def size(self):
        return len(self.q)
    def empty(self):
        return 0 if self.q else 1
    def front(self):
        return self.q[0] if self.q else -1
    def back(self):
        return self.q[-1] if self.q else -1

q = Queue()
n=int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        q.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(q.pop())
    elif cmd[0] == 'size':
        print(q.size())
    elif cmd[0] == 'empty':
        print(q.empty())
    elif cmd[0] == 'front':
        print(q.front())
    elif cmd[0] == 'back':
        print(q.back())