from math import*
n = float(input(" N > 0 qilib  N ni kiriting:  N = "))
while ceil(n) > n or n < 0:
  n = float(input(" \n XATOLIK YUZ BERDI!\n N > 0 qilib  qayta  N ni kiriting:  N =  "))

x = float(input(" \n Raxmat  N ni to'g'ri kiritdingiz\n\n Endi esa  x ni |x| < 1  shartga mos qilib kiriting. X = "))
while abs(x) >= 1:
  x = float(input(" \n XATOLIK YUZ BERDI!\n X ni qayta  |x| < 1  shartga mos qilib kiriting. X = "))

print("\n\n Raxmat  X ni ham Y ni ham to'g'ri kiritdingiz.")

n = int(n)

summa = x
maxraj = 1

for i in range(1,n+1):
  maxraj *= 2*i
  summa += ((2*i-1)*(x**(2*i+1)))/(maxraj*(2*i+1))
  print(i, ")  ", summa)

print("\nNATIJA: = ", summa)
