a=int(input("Istalgan son kiriting N => "))
r=int(input("Ushbu sonning oxirigi 1 < = R < = 9 oraliqdagi qo'shmoqchi bo'lgan raqam kiriting: => "))
if a>0 and 1<=r<=9:
    def AddLeftDigit(x):
        while x>0:
            print(r,end=(""))
            print(a)
            break
    AddLeftDigit(a)
else:
    print("a > 0 va 1 < = R < = 9 shartga amal qiling!")
