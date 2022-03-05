n = int(input())
s = 0
i=0
while n!=0 :
    s+=n%10
    n//=10
    i+=1
print(f'raqamlari yigindisi : {s}')
print(f'{i} xonali son')
