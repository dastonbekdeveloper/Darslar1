n=int(input("N sonini kiriting: N => "))
b=int(input("1-sonini kiriting: n => "))
min=b
j=1
for i in range(2,n+1):
    b=int(input(f"{i}-sonni kiriting: n => "))
    if min>b:
        min=b
        j=i
print(f"\nTo'plamdagi eng kichik element qiymati {min} ga teng uning tartib raqami {j} ga teng.")
print(f"Ushbu elementgacha {j-1} ta element bor.")
