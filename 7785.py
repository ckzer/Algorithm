n = int(input())
log = {}
for i in range(n):
    a, b = input().split()
    log[a] = b

log_list = list(log.keys())
cnt = []
for i in range(len(log_list)):
    if log[log_list[i]] == 'enter':
        cnt.append(log_list[i])

cnt = sorted(cnt, reverse=True)
print('\n'.join(cnt))