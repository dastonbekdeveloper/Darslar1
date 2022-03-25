a=float(input("Istalgan haqiqiy son kiriting a = "))
if a<0:
    def Ishora(a):
        return (a/a)*(-1)
if a>0:
    def Ishora(a):
        return (a/a)    
if a==0:
    def Ishora(a):
        return (a*0)        
print(Ishora(a))
