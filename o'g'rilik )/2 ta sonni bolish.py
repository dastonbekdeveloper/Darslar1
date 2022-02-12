def kopaytirish(x,y):
    z=0
    while(y>=1):
        z=z+x
        y=y-1
    return z
a= input('a=').split(".")
b= input('b=').split('.')
sgn1=1
sgn2=1
if(a[0][0]!='-'):
    c=int(a[0]+a[1])
else:
    c = -int(a[0] + a[1])
    sgn1=-1
if(b[0][0]!='-'):
    d=int(b[0]+b[1])
else:
    d=-int(b[0]+b[1])
    sgn2=-1
y = str(kopaytirish(c, d))
while len(y)<len(a[1]+b[1])+1:
    y="0"+y
if sgn2+sgn1==2 or sgn2+sgn1==-2:
    y= y
else:
    y = "-" + y
dr=int(len(y)-len(a[1]+b[1]))
print(y[:dr],y[dr:],sep=".")
