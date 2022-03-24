x=int(input("Istalgan 1-sonni kiriting: x => "))
y=int(input("Istalgan 2-sonni kiriting: y => "))
c=int(input("Istalgan 3-sonni kiriting: c => "))
d=int(input("Istalgan 4-sonni kiriting: d => "))
def Minmax(x):
    if x>y:
        print(f"({x}) => (",y,")")
        print(f"({y}) => (",x,")")
    else:
        print(f"({x}) => (",x,")")
        print(f"({y}) => (",y,")")
Minmax(x) 
