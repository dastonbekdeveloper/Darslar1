n=int(input("N sonini kiriting: N => "))
b=int(input("1-sonini kiriting: n => "))
max=b
j=1
k=1
for i in range(2,n+1):
    b=int(input(f"{i}-sonni kiriting: n => "))
    if max<b:
        max=b
        j=i
    if max<=b:
        max=b
        k=i
print(f"\nEng katta element {max} ga teng !")
if j!=k:
    print(f"Birinchi uchragan eng katta element tartib raqami {j}")
    print(f"Oxirgi uchragan eng katta element tartib raqami {k}")
    print(f"Birinchi va oxirgi uchragan eng katta element orasida {k-j-1} ta element bor")
else:
    print("To'plamda faqat bitta eng katta element mavjud!")
