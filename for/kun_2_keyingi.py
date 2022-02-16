d=int(input("d="))
m=int(input("m="))
yil=int(input("yil="))
kabisa=False
if yil%4==0:
    kabisa = True
if yil%100==0 and yil%400!=0:
    kabisa = False
    
d=d+2

if m==4 or m==6 or m==9 or m==11:
    if d==31:
        d=1
        m=m+1
    elif d==32:
        d=2
        m=m+1
elif m==2:
    if d ==28 + kabisa:
        d=2
        m=3
    elif d==29+kabisa:
        d=1
        m=3
    elif d==30:
        d=2
        m=3
    
else:
    if d==32:
        d=1
        m=m+1
    elif d==33:
        d=2
        m=m+1
    if m>12:
        m=1
print(d,m,yil,sep='/')
