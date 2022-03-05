n = int(input())
b = int
s=1
while n !=0 :
    b=n%10
    n//=10
    if b%2==1 :
        s=2
        print('toq raqamlar bor')
        break
if s==1:
    print('toq raqamlar yoq')
