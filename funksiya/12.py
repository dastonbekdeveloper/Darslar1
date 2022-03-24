a=float(input("Birinchi sonni kiriting a = "))
b=float(input("Ikkinchi  sonni kiriting b = "))
c=float(input("Uchinchi  sonni kiriting c = "))
def Sortlnc(a,b,c):
    """Ushbu funksiya kiritilgan sonlarni o'sish tartibida joylashtirib chiqaradi"""
    if a>b>c:
        print(f"Min: {c}, Middle: {b}, Max: {a}.")
    if a>c>b:
        print(f"Min: {b}, Middle: {c}, Max: {a}.")
    if b>a>c:
        print(f"Min: {c}, Middle: {a}, Max: {b}.") 
    if b>c>a:
        print(f"Min: {a}, Middle: {c}, Max: {b}.")
    if c>a>b:
        print(f"Min: {b}, Middle: {a}, Max: {c}.")
    if c>b>a:
        print(f"Min: {a}, Middle: {b}, Max: {c}.")
Sortlnc(a,b,c)
