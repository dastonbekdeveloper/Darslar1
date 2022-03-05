n = int(input())
a1,a2 =1,1
i=3
while n>i :
    c=a1+a2
    a1=a2
    a2=c
    i+=1
    print(c)
    if c>n :
        print(f"n dan katta fibonachi son : {c}")
        break
