n=int(input("To'plamning elementlar sonini kiriting: n => "))
min=0
u=1
j=0
for i in range(1,n+1):
    b=int(input(f"To'plamga tegishli {i}-sonni kiriting: p => "))
    if b>0 and u==1:
        min=b
        j=i
        u=0
    if min>b and b>0:
        min=b
        j=i
if j>0:
     print(f"\nTo'plamdagi eng kichik butun musbat son: {min} va bu sonning tartib raqami {j} ga teng.")
else:
    print(f"\nTo'plamda musbat sonlar mavjud emas. {j}.")
