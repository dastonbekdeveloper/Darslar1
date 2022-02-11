d = int(input("d = "))
m = int(input("m = "))
y = int(input("y = "))

q = int(input("qo'shiladigan kun => "))

d += q

if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    kabisa = True
else:
    kabisa = False

while d != 0:
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        kabisa = True
    else:
        kabisa = False

    if m == 2:
        if d > (28 + kabisa):
            m += 1
            d -= (28 + kabisa)
        else:
            q = d
            d = 0
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            m += 1
            d -= 30
        else:
            q = d
            d = 0
    else:
        if d > 31:
            m += 1
            if m > 12:
                m = 1
                y += 1
            d -= 31
        else:
            q = d
            d = 0
print(q, m, y, sep="/")
