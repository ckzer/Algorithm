a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
if a == b == c == 60:
    print("Equilateral")
elif sum == 180:
    if a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
