def kopaytirish(x,y):
    z=0
    while(y>=1):
        z=z+x
        y=y-1
    return z
def bolish(x,y):
    z=0
    while(x>=y):
        x=x-y
        z+=1
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
y=str(bolish(kopaytirish(c,1000000),d))
while len(y)<7:
    y="0"+y
if sgn2+sgn1==2 or sgn2+sgn1==-2:
    y = y
else:
    y = "-" + y
dr=6
print(y[:len(y)-dr],y[len(y)-dr:],sep=".")
