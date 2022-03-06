a=int(input('"a="'))
a1=1
a2=1
a3=0
k=2
while a!=a3:
    k+=1
    a3=a1+a2
    a1=a2
    a2=a3
print(k)
