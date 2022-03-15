n=int(input("N sonini kiriting: N => "))
a=int(input("1-sonini kiriting: n => "))
b=int(input("2-sonini kiriting: n => "))
c=int(input("3-sonini kiriting: n => "))
max1=0
max2=0
max3=0
if a>b and a>c and b>c:
    max1=a
    max2=b
    max3=c
if a>=b and a>=c and c>=b:
    max1=a
    max2=c
    max3=b
if b>a and b>c and a>c:
    max1=b
    max2=a
    max3=c
if b>=a and b>=c and c>=a:
    max1=b
    max2=c
    max3=a
if c>a and c>b and a>b:
    max1=c
    max2=a
    max3=b
if c>=a and c>=b and b>=a:
    max1=c
    max2=b
    max3=a
for i in range(4,n+1):
    d=int(input(f"{i}-sonni kiriting: n => "))    
    if max1<=d:
        max3=max2
        max2=max1
        max1=d
    if max2<d and max1>d:
        max1=max1;
        max3=max2;
        max2=d;
    if max3<=d and max2>d:
        max1=max1;
        max2=max2;
        max3=d;
print(f"Eng maksimum son: max1 = {max1};")
print(f"Undan keyingi eng maksimum son: max2={max2}.")
print(f"Undan ham keyingi eng maksimum son: max3={max3}.")
