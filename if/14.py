a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if c<a and c<b:
    print(c,max(a,b))
if a<c and a<b:
    print(a,max(c,b))
if b<c and b<a:
    print(b,max(a,c))
