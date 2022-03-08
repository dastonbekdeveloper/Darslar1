# c**2 = b**2 + a**2 Powered by Nurgeldi
from math import sqrt
sana = 0
n=int(input("n="))
for c in range(1,n+1):
    for b in range(1,c):
        sana+=1
        a = sqrt(c*c - b*b)
        if a % 1 == 0 and b>a:
            print(c,b,int(a))
print(sana)
