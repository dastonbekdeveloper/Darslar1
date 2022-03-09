a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
a_sana=0
while a>=c:
    a=a-c
    a_sana+=1
b_sana=0
while b>=c:
    b=b-c
    b_sana+=1
print(a_sana*b_sana)
