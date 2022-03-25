a=int(input("istalgan K sonini kiriting: K => "))
b=int(input("istalgan N sonini kiriting: N => "))
def isPowerN(a,b):
    l=0
    while b**l<a:
        l=l+1
    if b**l==a:
        print(f"{a} soni {b} ning {l} darajasi.")
    else:
        print(f"Ushbu son {b} ning darajasi emas.")
isPowerN(a,b)
