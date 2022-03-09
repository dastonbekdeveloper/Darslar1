n=int(input("n="))
a=int(input("a="))
b=int(input("b="))
min=2*(a+b)
mina=a
minb=b
for i in range(1,n):
    a=int(input("a="))
    b=int(input("b="))
    if 2*(a+b)<min:
        min=2*(a+b)
        mina=a
        minb=b
print("min=",min,"mina=",mina,"minb=",minb)
