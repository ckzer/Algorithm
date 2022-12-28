h, m, s = map(int, input().split())
q = int(input())
for i in range(q):
    sum=(h*3600)+(m*60)+s
    h_cnt, m_cnt=0,0
    t, c=map(int, input().split())
    if t==1:
        h_cnt+=c//3600
        c-=h_cnt*3600
        m_cnt+=c//60
        c-=m_cnt*60
        h+=h_cnt
        m+=m_cnt
        s+=c
    elif t==2: