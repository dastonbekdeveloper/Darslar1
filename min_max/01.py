n=int(input("n="))
max=int(input())
min=max
for i in range(1,n):
    a=int(input())
    if a>max:
        max=a
    if a<min:
        min=a
print("max=",max,"min=",min)
