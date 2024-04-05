mbti = input()
cnt = ""
if mbti[0] == "E":
    cnt += "I"
else:
    cnt += "E"
if mbti[1] == "S":
    cnt += "N"
else:
    cnt += "S"
if mbti[2] == "F":
    cnt += "T"
else:
    cnt += "F"
if mbti[3] == "J":
    cnt += "P"
else:
    cnt += "J"
print(cnt)
