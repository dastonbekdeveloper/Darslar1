n=int(input("n="))
a=int(input("a="))
max1=maxn=a
max1tr=maxntr=1
for i in range(2,n+1):
    a=int(input("a="))
    if max1<a:
        max1=a
        max1tr=i
    if maxn<=a:
        maxn=a
        maxntr=i
print("max1=",max1,"tartib raqami=",max1tr)
print("maxn=",maxn,"tartib raqami=",maxntr)
