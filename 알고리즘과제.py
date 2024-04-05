def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, (a % b)
    return a


def lcm(a, b):  # 최소공배수
    return a * b / gcd(a, b)


p, q = map(int, input().split())
sum = 0
while p > 0:
    egypt_deno = q // p  # egypt_deno= []값의 정수값
    if float(egypt_deno) != float(q / p):
        egypt_deno += 1
    lcm_num = (
        int(lcm(egypt_deno, q)) if egypt_deno > q else int(lcm(q, egypt_deno))
    )  # 최소공배수 찾기
    p, q = int((lcm_num / q) * p - (lcm_num / egypt_deno)), int(lcm_num)
    sum += 1
print(sum)
