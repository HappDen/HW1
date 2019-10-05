a = int(input())
b = int(input())
c = int(input())
import math
if a > b and a > c:
    d = math.sqrt(a**2-b**2)
else:
    d = math.sqrt(a**2+b**2)
if d == c:
    print("YES")
else:
   print("NO")
