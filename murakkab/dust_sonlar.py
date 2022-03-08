# Do'st sonlar

n = int(input("n = "))

for i in range(1,n+1):
    S = 0
    for j in range(1,i):
        if i%j==0:
            S+=j
    if S>i:
        S1 = 0
        for j in range(1,S):
            if S%j==0:
                S1+=j

        if S1==i:
            print(i,S)
