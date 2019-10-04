    
import math
a = int(input())
b = int(input())
c = int(input())
discr = b**2 - 4*a*c
if (a and b) ==0 :
    print(" ")
else:
    if discr >= 0:
        if a == 0:
            x1 = (c/b)
            print("x1:-%.2f" % x1)
        else:
            x1 = (-b + math.sqrt(discr))/ (2*a)
            x2 = (-b - math.sqrt(discr))/ (2*a) 
            print("x1=%.2f \nx2=%.2f" % (x1, x2))

    elif discr == 0:
        x = -b / (2*a)
        print("x = %.2f" % x)
    else:
        print(" ")
