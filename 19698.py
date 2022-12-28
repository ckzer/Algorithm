n, w, h, l = map(int, input().split())
w_num = w // l
h_num = h // l
num = w_num * h_num
if n >= num:
    print(num)
else:
    print(n)