n=int(input("To'plamning elementlar sonini kiriting: n => "))
a=int(input("To'plamga tegishli 1-sonni kiriting: a => "))
max = a
min = a
l=1
j=1
for i in range(2,n+1):
    b=int(input(f"To'plamga tegishli {i}-sonni kiriting: p => "))
    if max<b:
        max=b
        j=i
    if min>b:
        min=b
        l=i
if l<j:  
    print(f"\nEkstremal(min) element tartibi: {l}.")
else:
    print(f"\nEkstremal(max) element tartibi: {j}.")
