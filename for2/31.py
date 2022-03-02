# for 31

n = int(input("n = "))

for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i,2*i):
        print(j,end='')
    for j in range(2*i-2,i-1,-1):
        print(j,end='')
    print()

