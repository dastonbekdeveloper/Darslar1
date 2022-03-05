n = int(input())
a1=1
a2 =1
i=1
while i<n :
    c = a1+a2
    a1=a2
    a2=c
    i+=1
    if n>c and n*2//3<c :
        print(c)
    if c>n and n*3//2>c :
        print(c)
