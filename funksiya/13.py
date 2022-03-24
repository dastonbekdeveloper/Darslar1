a=float(input("Birinchi sonni kiriting a = "))
b=float(input("Ikkinchi  sonni kiriting b = "))
c=float(input("Uchinchi  sonni kiriting c = "))
def Sortlnc(a,b,c):
    """Ushbu funksiya kiritilgan sonlarni o'sish tartibida joylashtirib chiqaradi"""
    if a>b>c:
        print(f"Max: {a}, Middle: {b}, Min: {c}.")
    if a>c>b:
        print(f"Max: {a}, Middle: {c}, Min: {b}.")
    if b>a>c:
        print(f"Max: {b}, Middle: {a}, Min: {c}.") 
    if b>c>a:
        print(f"Max: {b}, Middle: {c}, Min: {a}.")
    if c>a>b:
        print(f"Max: {c}, Middle: {a}, Min: {b}.")
    if c>b>a:
        print(f"Max: {c}, Middle: {b}, Min: {a}.")
Sortlnc(a,b,c)
