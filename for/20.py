n = int(input('n = '))
fac=1
sum=0
if n>0 : 
    for i in range(1,n+1):
        fac*=i      
        sum+=fac
    print('Yig\'indi:',sum)
else:
    print('n>0 bo\'lishi kerak')
