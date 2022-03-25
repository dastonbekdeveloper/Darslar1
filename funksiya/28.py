n=int(input("n > 1 son kiriting: n => "))
def IsPrime(n):
    l=0
    if n>1:
        for x in range(2,n):
            if(n%x)==0:
                l=1
            else:
                pass
        if l==0:
            print("Siz kiritgan son tub!")
        elif l==1:
            print("Siz kiritgan son tub emas. Ya'ni murakkab son!")
    else:
        print("n > 1 shartiga e'tibor bering!")
IsPrime(n
