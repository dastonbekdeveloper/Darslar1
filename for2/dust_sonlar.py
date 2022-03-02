n=int(input("n="))
s=0
for i in range(1,n+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    d=0
    for k in range(1,s):
        if s%k==0:
            d+=k
    if d==i and s!=i:
        print(i,s)
        #i niki s
        #s niki d
