n=int(input("n="))
for i in range(1,n):
    for k in range(i,n+1):
        print(" ",end='')
    for j in range(1,2*i):
        print("*",end=' ')
    print()
