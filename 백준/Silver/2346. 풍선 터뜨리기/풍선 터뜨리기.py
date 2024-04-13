input = __import__('sys').stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
dq = deque([(idx+1, val) for idx, val in enumerate(arr)])
res = []
while dq:
    idx, move = dq.popleft()
    res.append(idx)
    if not dq:
        break
    if move > 0:
        dq.rotate(-(move-1))
    else:
        dq.rotate(-move)

print(*res)