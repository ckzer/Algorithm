input = __import__('sys').stdin.readline
from collections import deque

n, k = map(int, input().split())
queue = deque([n])
time = [0 for _ in range(100001)]
while queue:
    v = queue.popleft()
    if v == k:
        print(time[v])
        break
    for next_step in (v-1, v+1, v*2):
        if 0 <= next_step <= 100000 and not time[next_step]:
            time[next_step] = time[v] + 1
            queue.append(next_step)