a=int(input("Nuqtaning absissasini kiriting: x => "))
b=int(input("Nutaning ordinatasini kiriting: y => "))
def Quater(a,b):
    if a>0 and b>0:
        print("Birinchi chorak")
    elif a<0 and b>0:
        print("Ikkinchi chorak")
    elif a<0 and b<0:
        print("Uchinchi chorak")
    elif a>0 and b<0:
        print("To'rtinchi chorak")
    elif a==0 and b==0:
        print("Nuqta koordinatalar boshida joylashgan")
Quater(a,b)
