n=int(input("n="))
a=int(input("a="))
min1=minn=a
min1tr=minntr=1
for i in range(2,n+1):
    a=int(input("a="))
    if min1>a:
        min1=a
        min1tr=i
    if minn>=a:
        minn=a
        minntr=i
print("min1=",min1,"tartib raqami=",min1tr)
print("minn=",minn,"tartib raqami=",minntr)
