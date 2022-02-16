a = float(input('a = '))
n = int(input('n = '))
kup = 1
if n>0 :       
    for i in range(1,n+1):
        kup*=a
        print(a,'ning',i,'- darajasi',kup)
else:
    print('n>0 bo\'lishi kerak')
