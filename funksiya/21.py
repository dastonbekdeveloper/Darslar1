a=int(input("A sonni kiriting: A => "))
b=int(input("B sonni kiriting: B => "))
def SumRange(a,b):
    s=0
    for i in range(a,b):
        s=s+i
    print(s)
SumRange(a,b)
