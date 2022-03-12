n = int(input("n = "))
a = int(input("a = "))
i=1
while i<n:
    b = int(input("b = "))
    while a!=b:
        if a>b:
            a%=b
        else:
            b%=a 

        if a==0:
            a=b
        if b==0:
            b=a
    i+=1
print(a)
