a=float(input("Birinchi sonni kiriting a = "))
b=float(input("Ikkinchi  sonni kiriting b = "))
c=float(input("Uchinchi  sonni kiriting c = "))
def ShiftRight(a,b,c):
    t=c
    c=b
    b=a
    a=t
    print(a,b,c)
ShiftRight(a,b,c)
