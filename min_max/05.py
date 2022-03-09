n=int(input("n="))
m=int(input("m="))
v=int(input("v="))
min=m/v
minm=m
minv=v
for i in range(1,n):
    m=int(input("m="))
    v=int(input("v="))
    if min>m/v:
        min=m/v
        minm=m
        minv=v
print("min=",min,"minm=",minm,"minv",minv)
