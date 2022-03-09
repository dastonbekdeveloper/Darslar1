n=int(input("n="))
a=int(input("a="))
min=a
index=0
for i in range(1,n):
    a=int(input("a="))
    if a<min:
        index=i+1
        min=a
print("min=",min,"index=",index)
