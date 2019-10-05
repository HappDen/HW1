import math
a = int(input())
b = int(input())
c = int(input())
if b > a and b > c:
    d = math.sqrt(b**2-a**2)
elif a > b and a > c:
    d = math.sqrt(a**2-b**2)
else:
    d = math.sqrt(a**2+b**2)
if d == c:
    print("YES")
else:
   print("NO")
