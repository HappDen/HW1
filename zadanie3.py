a = int(input())
b = int(input())
c = int(input())
import math
if (a or b or c) < 10 :
    d = math.sqrt(a**2+b**2)
else:
    d = math.sqrt(a**2-b**2)
if d == c:
    print("YES")
else:
   print("NO")