a=float(input("1 kg konfetning narxini kiriting a => "))
if a>0:
    for x in range(1,11):
        print(f"{x/10} kilogramm konfetning narxi {a*x/10} so'm turadi.")
else:
    print("Konfetning narxi manfiy bo'lishi mumkin emas!")
