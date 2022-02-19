from math import*
n = float(input("n  butun  ( n>0)  qilib kiriting. \n>>> "))
while ceil(n)>n or n<0 :
  n = float(input("\n\nXATO KIRITDINGIZ!! \nILTIMOS QAYTA KIRITING!!! \n\nn  butun  ( n>0)  qilib kiriting. \n>>> "))

n = int(n)
summa = 1

print (">>> SUMMANI  boshlang'ich qiymati  SUMMA = 1   qilib olingan. \n Biz shu birga qo'shib ketishimiz kerak.\n")

for i in range(1,n+1):
  print(i,")   1/(", i , "!)=" , 1/(factorial(i)) , " \n" )

  print("    "+str(summa) + " +  1/(", i, "!) = " + str(summa) + " + " + str(1 /(factorial(i))) + " = " + str(summa + 1/(factorial(i))) + " \n")
  summa += 1/(factorial(i))


print("SUMMA = ",summa)
