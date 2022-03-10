n=int(input("To'plamning elementlar sonini kiriting: n => "))
maxtoq=0
u=1
j=0
for i in range(1,n+1):
    b=int(input(f"To'plamga tegishli {i}-sonni kiriting: p => "))
    if b%2==1 and u==1:
        maxtoq=b
        j=i
        u=0
    if maxtoq<b and b%2==1:
        maxtoq=b
        j=i
if j>0:
     print(f"\nTo'plamdagi eng katta toq son: {maxtoq} va bu sonning tartib raqami {j} ga teng.")
else:
    print(f"\nTo'plamda toq sonlar mavjud emas. {j}.")
