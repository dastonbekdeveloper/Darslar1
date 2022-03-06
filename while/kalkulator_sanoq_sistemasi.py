a=int(input("qaysi sanoq sistemasida son kiritmoqchisiz="))
b=int(input(f"{a}lik sanoq sistemasida sonni kiritng="))
k=int(input("qasyi sanoq sistemasiga o'tkazmoqchisiz = "))
if a==10:
    s=0
    while b!=0:
        s=s*10+b%k+1
        b=b//k
    d=0
    m=s
    while m!=0:
        d=d*10+m%10-1
        m=m//10
    print(d)
else:
    bb=b
    s=0
    for i in range(0,b):
        s=s+(bb%10)*(a**i)
        bb=bb//10
        if bb==0:
            break
    #10 dan k ga otish kerak
    d=0
    while s!=0:
        d=d*10+s%k+1
        s=s//k
    m=d
    d=0
    while m!=0:
        d=d*10+m%10-1
        m=m//10
    print(d)
