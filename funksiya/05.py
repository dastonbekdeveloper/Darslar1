print("1-to'g'ri to'rtburchakning uchi koordinatalarini kiriting:")
a=int(input("x1 => "))
b=int(input("y1 => "))
c=int(input("x2 => "))
d=int(input("y2 => "))
print("\n2-to'g'ri to'rtburchakning uchi koordinatalarini kiriting:")
m=int(input("x1 => "))
n=int(input("y1 => "))
o=int(input("x2 => "))
p=int(input("y2 => "))
import math
def RectPS(a,b,c,d):
    print(math.fabs(c-a)*math.fabs(d-b))
    print(2*(math.fabs(c-a)+math.fabs(d-b)))
RectPS(a,b,c,d)
RectPS(m,n,o,p)