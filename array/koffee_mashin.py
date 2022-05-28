def tarkibi(a):
    if a==1:
        print("suv: 100ml")
        print("sut: 50ml")
        print("coffe miqdori: 75 gram")
        print("puli: 2500 so'm")
    elif a==2:
        print("suv: 100ml")
        print("sut: 100ml")
        print("coffe miqdori: 25 gram")
        print("puli: 2000 so'm")
    elif a==3:
        print("suv: 100ml")
        print("sut: 150ml")
        print("coffe miqdori: 50 gram")
        print("puli: 3000 so'm")
dict_1={
        "baza":{
            "espresso":200,
            "lattle":200,
            "copuchino":200,
            "suv":1000,
            "sut":500,
            "shakar":5
        },
        "bazadagi_pullar":{
            "1000-somliklar":5,
            "2000-somliklar":5,
            "5000-somliklar":5,
            "10000-somliklar":5
        },
        "narxlari":{
            "kofe_e_75":1500,
            "kofe_l_25":500,
            "kofe_k_50":1000,
            "suv_100":500,
            "sut_100":1000
        }
    }
while True:
    s=int(input("dasturni ishga tushirmoqchimisiz? \n yes -> 1 \n no -> 2 \n"))
    if s==1:
        d=int(input("Nima hohlaysiz?\n 1->espresso \n 2-> lattle \n 3 -> copuchino \n"))
        tarkibi(d)
        b=int(input("sotib olmoqchimisiz? \n 1-> yes \n 2-> no\n"))
        if d==1:
            if dict_1["baza"]["espresso"]>=75 and dict_1["baza"]["suv"]>=100 and dict_1["baza"]["sut"]>=50:
                dict_1["baza"]["espresso"]-=75;dict_1["baza"]["suv"]-=100;dict_1["baza"]["sut"]-=50
                sum=2500
            else:
                print("kechirasiz bazada espressoga yetadigan mahsulot qolmabdi")
                break
        if d==2:
            if dict_1["baza"]["lattle"]>=25 and dict_1["baza"]["suv"]>=100 and dict_1["baza"]["sut"]>=100:
                sum=2000
                dict_1["baza"]["lattle"]-=25;dict_1["baza"]["suv"]-=100;dict_1["baza"]["sut"]-=50
            else:
                print("kechirasiz bazada lattlega yetadigan mahsulot qolmabdi")
                break
        if d==3:
            if dict_1["baza"]["copuchino"]>=50 and dict_1["baza"]["suv"]>=100 and dict_1["baza"]["sut"]>=100:
                sum=3000
                dict_1["baza"]["copuchino"]-=50;dict_1["baza"]["suv"]-=100;dict_1["baza"]["sut"]-=50
            else:
                print("kechirasiz bazada copuchinoga yetadigan mahsulot qolmabdi")
                break
        if b==1:
            s=0
            while True:
                print("pulni kiritingiz mumkin")
                ming_1=int(input("1 ming somligingiz qancha ->"))
                ming_2=int(input("2 ming somligingiz qancha ->"))
                ming_5=int(input("5 ming somligingiz qancha ->"))
                ming_10=int(input("10 ming somligingiz qancha ->"))
                s=s+ming_1*1000+ming_2*2000+ming_5*5000+ming_10*10000
                if s<sum:
                    buyruq=int(input("pulingiz yetmadi yana pul kiritmoqchimisiz?\n 1->yes \n 2->no"))
                    if buyruq==1:
                        continue
                    elif buyruq==2:
                        print("sizga pulingiz qaytib berildi")
                        break
                else:
                    s=s-sum
                    break
        elif b==2:
            break
        sum=0
        i=0
        while True:
            if s<10000:
                print(f"sizga {i} ta 10000likka qaytdi")
                dict_1["bazadagi_pullar"]["10000-somliklar"]+=ming_10-i
                break
            s=s-10000
            i+=1
        sum=0
        i=0
        while True:
            if s<5000:
                print(f"sizga {i} ta 5000likka qaytdi")
                dict_1["bazadagi_pullar"]["5000-somliklar"]+=ming_5-i
                break
            s=s-5000
            i+=1
        sum=0
        i=0
        while True:
            if s<2000:
                print(f"sizga {i} ta 2000likka qaytdi")
                dict_1["bazadagi_pullar"]["2000-somliklar"]+=ming_2-i
                break
            s=s-2000
            i+=1
        sum=0
        i=0
        while True:
            if s<1000:
                print(f"sizga {i} ta 1000likka qaytdi")
                dict_1["bazadagi_pullar"]["1000-somliklar"]+=ming_1-i
                break
            s=s-1000
            i+=1
        if s==500:
            sh=int(input("kechirasi bizda 500 somlik yo'q edi \n500 som pulingiz qoldi bir oz shakar hohlaysizmi? \n 1-> yes \n 2-> no \n"))
            print("mahsulotingiz tayyor boldi olishingiz mumkin")
            if sh==1:
                dict_1["baza"]["shakar"]-=1
            else:
                break
        else:
            print("mahsulotingiz tayyor boldi olishingiz mumkin")
    else:
        break
print("dasturdan foydalanganingiz uchun raxmat")
print(dict_1["bazadagi_pullar"])
