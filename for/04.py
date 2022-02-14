a=float(input("1 kg konfetning narxini kiriting a => "))
if a>0:
    for x in range(1,11):
        print(f"{x} kilogramm konfetning narxi {a*x} so'm turadi.")
else:
    print("Konfetning narxi manfiy bo'lishi mumkin emas!")
