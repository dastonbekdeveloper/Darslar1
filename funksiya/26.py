a=int(input("istalgan son kiriting: x => "))
def isPower5(a):
    # l=0
    for i in (0,a+1):
        if i**5==a:
            print(f"{a} soni 5 ning {i}-darajasi.")
        else:
            print("Bu son 5 ning darajasi emas.")
