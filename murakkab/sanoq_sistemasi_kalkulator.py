# Sanoq sistemalari kalkulyatori:

# Xohlagan sanoqdan -> 10lik
# 10lik so'ralgan sanoq sistemasiga

# 2lik 0 1
# 4lik 0 1 2 3
# 8lik 0 1 2 3 4 5 6 7
# 10lik sanoq sistemasi 0 1 2 3 4 5 6 7 8 9

print("2-10lik sanoq sistemasigacha kiriting")

n = int(input('n = '))
kirish = int(input('Kirish sanoq sistemasi = '))
chiqish = int(input("Chiqish sanoq sistemasi = "))

# Kiritilgan sanoq sistemasi to'g'rimi tekshirish

kirish_n = n
while kirish_n > 0:
    if kirish_n%10 >= kirish:
        kirish_n = int(input('n = '))
        n = kirish_n
        continue
    kirish_n //= 10

daraja = 0
onlik = 0

# 10lik sanoq sistemasiga o'tkazish

while n>0:
    oxiri = n%10
    onlik += oxiri * kirish ** daraja
    n //= 10
    daraja += 1
    
# Onlikdan chiquvchi sanoq sistemasiga o'tkazish

natija = 0
S = 1
while onlik>0:
    qoldiq = onlik % chiqish
    natija += qoldiq * S
    S *= 10
    onlik//=chiqish
    
print(natija)
