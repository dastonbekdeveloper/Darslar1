# for 29

n = int(input('n = '))

for i in range(n):
    
    for j in range(n-i):
        print(' ',end='')
    
    for j in range(i+1):
        if j==0:
            C = 1
        else:
            C = C * (i+1-j) // j
        print(C,end=' ')
    print()
