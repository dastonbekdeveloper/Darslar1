a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if abs(a-b)<abs(a-c):
    print(b,abs(a-b))
if abs(a-b)>abs(a-c):
    print(c,abs(a-c))
