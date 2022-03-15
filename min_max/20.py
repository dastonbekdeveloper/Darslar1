n=int(input("N sonini kiriting: N => "))
b=int(input("1-sonini kiriting: n => "))
min=b
max=b
l=1
k=1
for i in range(2,n+1):
    a=int(input(f"{i}-sonni kiriting: n => "))
    if min==a:
        k=k+1     
    if min>a:
        min=a
        k=1
    if max==a:
        l=l+1     
    if max<a:
        max=a
        l=1
print(f"Eng kichik element {min} ga teng.")
print(f"Eng katta element {max} ga teng.")
print(f"To'plamda {k+l} ta ekstremal son bor.")
