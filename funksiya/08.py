a=int(input("Istalgan son kiriting N => "))
r=int(input("Ushbu sonning oxirigi 1 < = R < = 9 oraliqdagi qo'shmoqchi bo'lgan raqam kiriting: => "))
if a>0 and 1<=r<=9:
    def AddRightDigit(x):
        while x>0:
            print(a,end=(""))
            print(r)
            break
    AddRightDigit(a)
else:
    print("a > 0 va 1 < = R < = 9 shartga amal qiling!")
