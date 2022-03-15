n=int(input("N sonini kiriting: N => "))
a=int(input("1-sonini kiriting: n => "))
b=int(input("2-sonini kiriting: n => "))
y=0
j=2
x=a*b
for i in range(3,n+1):
    d=int(input(f"{i}-sonni kiriting: n => "))
    y=b*d    
    if x>=y:
        x=y
        b=d
        j=i
    else:
        b=d
print(f"Qo'shni tartib raqami {j-1}- va {j}-sonlar ko'paytmasi minimum! Uning qiymati {x} ga teng")
