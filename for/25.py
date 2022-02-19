from math import*
n = float(input("N>0 qilib kiriting.  N= "))
while ceil(n) > n or n<0:
  n = float(input(" \n XATOLIK YUZ BERDI! \n N>0 qilib kiriting.  N= "))

x = float(input("\n Raxmat N ni tug'ri kiritdingiz. \n\n Endi |x| < 1 qilib haqiqiy son x ni kiriting:  x ="))
while abs(x) >=1:
  x = float(input("\nXATOLIK YUZ BERDI!  \n\n Endi |x| < 1 qilib haqiqiy son x ni kiriting:  x ="))

print("Raxmat  n ni ham  x ni ham  to'gri kiritdingiz")

n = int(n)

summa = 0
for i in range(1 , n+1):
  summa += (((-1)**(i-1))*(x**i))/i

print("NATIJA: = " , summa)
