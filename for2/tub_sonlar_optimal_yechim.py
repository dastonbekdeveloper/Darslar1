n = int(input("n = "))

sana=0
print(2)
for i in range(3,n*n+1,2):
    bool=True
    for j in range(3,int(i**(1/2))+1,2):
        if i%j == 0 :
            bool=False
            break
    if bool:
        sana+=1
        print(i)
    if sana==n-1:
        break
