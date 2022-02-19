from math import*
n = int(input(" N ni kirit: N= "))
x = float(input(" X ni kirit: X= "))
summa = 1
for i in range(1,n+1):
  summa += ((x**i)/(factorial(i)))
print(summa)
