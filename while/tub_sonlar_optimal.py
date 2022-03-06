from math import sqrt

n = int(input('n = '))
print(2,end=' ')
sanagich = 0
for i in range(3,n+1,2):
    S=0
    for j in range(3,int(sqrt(i))+1,2):
        sanagich+=1
        if i%10==5:
            S+=1
            break
        if i%j==0:
            S+=1
            break
    if S==0:
        print(i,end=' ')
print("\nSanagich =",sanagich)
