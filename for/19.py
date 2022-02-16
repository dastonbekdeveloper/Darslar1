n = int(input('n = '))
fac=1
if n>0 : 
    for i in range(2,n+1):
        fac*=i      
    print(str(n)+'! =',fac)
else:
    print('n>0 bo\'lishi kerak')
