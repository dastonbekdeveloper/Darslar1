a=float(input())
i=1000
s=0
while i>0:
   s=s+round(a,4)
   i=i-1
b=float(input())
z=0
while s>=b:
    s=round(s,4)-b
    z=round(z,4)+0.001
print(z)
