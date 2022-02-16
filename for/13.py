n = int(input('N= '))
sum= 0
for i in range(11,11+n):
    sum+=i/10*(-1)**(i-1)
print(sum)
