t=input()
for i in range(len(t)):
    if t[i]==t[i].upper():
        print(t[i].lower(), end='')
    else:
        print(t[i].upper(), end='')