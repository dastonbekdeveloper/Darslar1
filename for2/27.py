n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i+j+1)%2,end='')
    print()
