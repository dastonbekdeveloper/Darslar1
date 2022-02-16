a=float(input('a = '))
n = int(input('n = '))
kup = 1
if n>0 :
    for i in range(1,n+1):
        kup*=a
    print(a,'ning',n,'- darajasi',kup)
else:
    print('Musbat daraja kirishingiz kerak edi! n>0')
