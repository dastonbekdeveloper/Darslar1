n=int(input())
a=0
b=0
for i in range(1,n+1):
    s=0
    for j in range(1,i+1):
       if i%j==0:
           s+=1
    if s==2:
        d=0
        for k in range(1,n-i+1):
            if (n-i)%k==0:
                d+=1
        if d==2:
            print(i,n-i)
            break
