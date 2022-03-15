n=int(input("N sonini kiriting: N => "))
b=int(input("1-sonini kiriting: n => "))
max=b
j=1
for i in range(2,n+1):
    b=int(input(f"{i}-sonni kiriting: n => "))
    if max<=b:
        max=b
        j=i
print(f"\nTo'plamdagi oxirgi uchragan eng katta element qiymati {max} ga teng uning tartib raqami {j} ga teng.")
print(f"Ushbu elementdan so'ng yana {n-j} ta element bor.")
