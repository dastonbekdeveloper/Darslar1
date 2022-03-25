a=float(input("A haqiqiy sonni kiriting: A => "))
b=float(input("B haqiqiy sonni kiriting: B => "))
print("\n1-ayirish; 2-ko'paytirish; 3-bo'lish; 4-qo'shish.")
c=int(input("Amalni bildiruvchi sonni kiriting: a => "))
def Calc(A,B,Op):
    if c==1:
        print(a-b)
    elif c==2:
        print(a*b)
    elif c==3:
        print(a/b)
    elif c==4:
        print(a+b)
    else:
        print("Amalni 1 dan 4 oraliqda tanlang!")
Calc(a,b,c)
