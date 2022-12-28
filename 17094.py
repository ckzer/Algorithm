num = int(input())
s = input()
num_cnt, str_cnt = 0, 0
for i in range(num):
    if s[i] == '2':
        num_cnt += 1
    else:
        str_cnt += 1
if num_cnt > str_cnt:
    print(2)
elif num_cnt < str_cnt:
    print('e')
else:
    print('yee')
