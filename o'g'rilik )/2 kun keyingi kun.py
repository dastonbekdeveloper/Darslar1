# 2kun keyingi kunni topuvchi dastur

d = int(input('d = '))
m = int(input('m = '))
y = int(input('y = '))

# Kabisalikni tekshiryabdi
kabisa=False
if y%4==0:
    kabisa = True
if y%100==0 and y%400!=0:
    kabisa = False

# Sana to'g'ri kiritildimi tekshiryabdi
sana=False
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d>=1 and d<=31:
    sana=True
elif m==2 and d>=1 and d<=28+kabisa:
    sana=True
elif (m==4 or m==6 or m==9 or m==11) and d>=1 and d<=30:
    sana=True
    
d = d + 2
   
# Oyni oxirgi kunlari va yangi oyga o'tish sanasini tekshiryabdi
if (m==4 or m==6 or m==9 or m==11) and sana:
    if d>30:
        d = d%30
        m = m + 1
elif m == 2 and sana:
    if d>28+kabisa:
        d = d%(28+kabisa)
        m = 3
elif sana:
    if d>31:
        d = d % 31
        m = m + 1
    if m==13:
        m=1
        y=y+1

if sana:
    print(d,m,y,sep='.')
else:
    print("Xato sana kiritildi")
