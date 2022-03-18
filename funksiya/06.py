a=int(input("Birinchi sonni kiriting a => "))
b=int(input("Ikkinchi sonni kiriting b => "))
c=int(input("Uchinchi sonni kiriting c => "))
def DigitCountSum(x):
    l=0
    s=0
    while x>0:
        l=l+1
        s=s+x%10
        x=x//10
    print(l)
    print(s)
DigitCountSum(a)
DigitCountSum(b)
DigitCountSum(c)
