n=int(input("n="))
a=int(input("a="))
b=int(input("b="))
min=a*b
mina=a
minb=b
for i in range(1,n):
    a=int(input("a="))
    b=int(input("b="))
    if a*b<min:
        min=a*b
        mina=a
        minb=b
print("min=",min,"mina=",mina,"minb=",minb)
