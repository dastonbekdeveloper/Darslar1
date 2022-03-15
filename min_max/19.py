n=int(input("N sonini kiriting: N => "))
b=int(input("1-sonini kiriting: n => "))
min=b
s=1
k=1
for i in range(2,n+1):
    a=int(input(f"{i}-sonni kiriting: n => "))
    if min==a:
        s=s+1     
    if min>a:
        min=a
        s=1
print(f"Eng kichik element {min} ga teng.")
print(f"To'plamda {s} ta eng kichik son bor.")
