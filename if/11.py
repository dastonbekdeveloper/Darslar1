a=int(input('a='))
b=int(input('b='))
if a!=b:
    a=b=max(a,b)
else:
    a=b=0
print(a,b)
