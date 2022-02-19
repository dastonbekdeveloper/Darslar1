from math import*
n = int(input(" N ni kirit: N= "))
x = float(input(" X ni kirit: X= "))
summa = 0
for i in range(0, n):
  summa += (((-1)**i)*(x**(2*i+1)))/(factorial(2*i+1))

print(summa)

print(sin(x))
