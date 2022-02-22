n = int(n)
summa = 0
for i in range(1, n+1):
  summa += i**n
  print(i, ")  ", i, " ning ", n, " - darajasi ",i**n, " \n      Yig'indi: ", summa, " \n")
  n -= 1

print("Natija: = ", summa)
