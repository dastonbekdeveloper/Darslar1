n=int(input("N sonini kiriting: N => "))
j=0
ozgaruvchi=0
yigindi=0
for i in range(1,n+1):
    d=int(input(f"{i}-sonni kiriting: n => "))   
    if d%2==0:
        j=j+1
        if ozgaruvchi==1:
            yigindi=yigindi+1
        ozgaruvchi=1
    else:
        ozgaruvchi=0
if j>0:
    print(f"To'plamda {j} ta juft son bor")
    print(f"To'plamda {yigindi} ta juft sonlar ketma-ketligi bor")
else:
    print("To'plamda juft sonlar mavjud emas")
