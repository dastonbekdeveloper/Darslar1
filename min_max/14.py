b=int(input("B sonini kiriting: b => "))
c=int(input("C sonini kiriting: c => "))
max=0
u=1
j=0
for i in range(1,11):
    a=int(input(f"{i}-sonni kiriting: n => "))
    if a>b and a<c and u==1:
        max=a
        j=i
        u=0
    if max<a and a>b and a<c:
        max=a
        j=i
if j>0:
     print(f"\nTo'plamdagi {b} da katta va {c} dan kichik eng katta son {max} ga va uning tartib raqami {j} ga teng.")
else:
    print(f"\nTo'plamdagi {b} da katta va {c} dan kichik son mavjud emas. {j}{j}.")
