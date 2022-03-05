n = int(input())
s= 0
while n!=0 :
    b=n%10
    s = s*10+b
    n//=10
print(f'sonni teskarisi : {s}')
