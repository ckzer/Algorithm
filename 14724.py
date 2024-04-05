n = int(input())
club = {
    "PROBRAIN": 0,
    "GROW": 0,
    "ARGOS": 0,
    "ADMIN": 0,
    "ANT": 0,
    "MOTION": 0,
    "SPG": 0,
    "COMON": 0,
    "ALMIGHTY": 0,
}
cnt_key = list(club.keys())
cnt = list()
for i in cnt_key:
    cnt = map(int, input().split())
    club[i] = max(cnt)

tmp = 0
tmp_cnt = 0
for i in range(9):
    if club[cnt_key[i]] > tmp:
        tmp = club[cnt_key[i]]
        tmp_cnt = i
print(cnt_key[tmp_cnt])
