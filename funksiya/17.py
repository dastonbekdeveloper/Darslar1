a=int(input("Kvadrat tenglamaning A koeffitsiyentini ( A!=0 ) ni kiriting A => "))
b=int(input("Kvadrat tenglamaning B koeffitsiyentini kiriting B => "))
c=int(input("Kvadrat tenglamaning ozod hadini kiriting C => "))
if a!=0:
    D=b**2-4*a*c
    def KvadratTIS(a,b,c):
        if D>0:
            print("Kvadrat tenglama 2 ta ildizga ega.")
        elif D<0:
            print("Kvadrat tenglama ildizga ega emas.")
        else:
            print("Kvadrat tenglama 1 ta ildizga ega.")
    KvadratTIS(a,b,c) 
else:
    print("Masala shartiga e'tibor bering. A1=0.")
