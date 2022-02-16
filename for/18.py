a = float(input('a = '))
n = int(input('n = '))
kup = 1
sum = 0
if n>0 :       
    for i in range(1,n+1):
        kup*=a
        print(a,'ning',i,'- darajasi',kup)
        sum+=kup*(-1)**(i+1)
    print('Yig\'indisi:',sum)
else:
    print('n>0 bo\'lishi kerak')
