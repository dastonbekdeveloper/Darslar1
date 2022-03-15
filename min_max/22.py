n=int(input("n="))
a=int(input("a="))
b=int(input("a="))
if a>b:
    min1=a
    min2=b
else:
    min1=b
    min2=a
for i in range(2,n):
    a=int(input("a="))
    if min1>=a and min2>=a:
        min2=min1
        min1=a
    elif min1<=a and min2>=a:
        min2=a
print(min1)
print(min2)
