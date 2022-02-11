a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b>c or c>b>a:
    print(b)
if b>a>c or c>a>b:
    print(a)
if b>c>a or a>c>b:
    print(c)
