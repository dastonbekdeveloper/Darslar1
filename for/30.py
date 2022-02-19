from math import*
n = float(input(" N>0  qilib  N  ni kirit: N= "))
while ceil(n) > n or n < 0:
  n = float(input("\n\n XATO KIRITDINGIZ!  \nN>0  qilib  qayta N  ni kiriting: N= "))

a = float(input(" A haqiqiy sonni kiriting ni kirit: A= "))
b = float(input(" B haqiqiy sonni kiriting ni kirit: B= "))

n = int(n)

c = (b-a)/n
print(" natijasi: =  ", 1-sin(a))
for i in range(n):
  a += c
  print(" natijasi: =  ", 1-sin(a))
