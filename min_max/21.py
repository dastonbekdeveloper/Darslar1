n=int(input("N sonini kiriting: N => "))
b=int(input("1-sonini kiriting: n => "))
min=b
max=b
s=0
for i in range(2,n+1):
    a=int(input(f"{i}-sonni kiriting: n => "))    
    if min>a:
        min=a    
    if max<a:
        max=a
    s=s+a
orta=(s-min-max+b)/(n-2)
print(f"Eng kichik element {min} ga teng.")
print(f"Eng katta element {max} ga teng.")
print(f"To'plam elementlari o'rta arifmetigi {orta} ga teng.")
