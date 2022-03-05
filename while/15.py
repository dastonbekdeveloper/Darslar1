s =float(input())
p = float(input())
i=0
yigindi =s
while s!=0 :
    yigindi+=s*p/100
    i+=1
    print(yigindi)
    if yigindi ==2*s :
        break
print(i)
