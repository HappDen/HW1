a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b: 
        a %= b
    else:
        b %= a
b = a + b
print('NOD:%s' %b)