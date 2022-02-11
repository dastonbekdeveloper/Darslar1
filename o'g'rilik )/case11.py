y=input('c=')
k1=int(input('k1='))
k2=int(input('k2='))
k=0
if y=='s':
    k=0
if y=='q':
    k=1
if y=='j':
    k=2
if y=='g':
    k=3
if k1==0:
    k1=1
elif k1==1:
    k1=-1
if k2==0:
    k2=1
elif k2==1:
    k2=-1
k=(k+k1+k2)%4
if k==0:
    print("Shimol")
if k==1:
    print("Sharq")
if k==2:
    print("Janub")
if k==3:
    print("G'arb")
#Bir kun keyingi sana
d=int(input()) 
m=int(input())
y=int(input())
d=d+1
if y%4==0:
    kabisa=True
if y%100==0 and y%400!=0: 
    kabisa = False;
if m==4 or m==6 or m==9or m==11: 
    if d>30: 
        d=1 
        m+=1
elif m==2: 
    if d>28+kabisa: 
        d=1 
        m+=1
else: 
    if d>31: 
        d=1 
        m+=1
    if m>12: 
        m=1 
        y+=1
print(d,m,y, sep=",")
