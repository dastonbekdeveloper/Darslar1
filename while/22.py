n = int(input())
son = bool
i=2
while i<n :
    if n%i==0 :
        print('tub son emas')
        son=False
        break
    i+=1
    if n%i!=0 :
        son = 1
if son :
     print('tub son')
