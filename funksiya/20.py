a=int(input("To'g'ri burchakli uchburchakning 1-katetini kiriting: a => "))
b=int(input("To'g'ri burchakli uchburchakning 2-katetini kiriting: b => "))
import math
c=math.sqrt(a**2+b**2)
if a>0 and b>0:
    def TriangleP(a):
        print(a+b+c)
else:
    print("Katetlar musbat bo'lsin...")
TriangleP(a)
