n=int(input("n="))
a=int(input("a="))
min_birinchi=a
max_oxirgi=a
for i in range(1,n):
    a=int(input("a="))
    if min_birinchi>a:
        min_birinchi=a
    if max_oxirgi<=a:
        max_oxirgi=a
print("min_birinchi=",min_birinchi,"max_oxirigi=",max_oxirgi)
