a=int(input("Istalgan 1-butun sonni kiriting a => "))
b=int(input("Istalgan 2-butun sonni kiriitng: b => "))
if b>a:
    for x in range(a,b+1):
        print(x)
    else:
        print(f"Jami elementlar soni: {b-a+1} ta.")
        print("Sikl tugadi!")
else:
    print("Diqqat! Masala shartiga ko'ra a soni b sonidan kichik bo'lsin!")   
