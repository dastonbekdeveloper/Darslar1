from math import*
n = float(input(" N>0  qilib  N  ni kirit: N= "))
while ceil(n)>n or n<0:
  n = float(input("\n\n XATO KIRITDINGIZ!  \nN>0  qilib  qayta N  ni kiriting: N= "))

x = float(input(" X haqiqiy sonni kiriting ni kirit: X= "))
summa = 1

n = int(n)

for i in range(1, n+1):
  summa = summa + (((-1)**i)*(x**(2*i)))/(factorial(2*i))

print(" natijasi: =  ", summa)

print("  COS(X) =  ", cos(x))
