n=int(input("10 lik sanoq sistemasida son kiriting="))
a=int(input("qaysi sanoq sistemasiga o'tkazish kerak="))
s=0
while n!=0:
    s=s*10+n%a+1
    n=n//a
d=0
m=s
while m!=0:
    d=d*10+m%10-1
    m=m//10
print(d)
