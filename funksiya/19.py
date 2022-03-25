a=int(input("1-doiraning radiusini kiriting: R1 => "))
b=int(input("2-doiraning radiusini kiriting: R2 => "))
pi=3.14159
def RingS(a):
    if a>b:
        print(pi*(a**2-b**2))
    elif a<b:
        print(pi*(b**2-a**2))
    else:
        print("Doiraning radiuslari teng bo'lmasin...")
RingS(a)
