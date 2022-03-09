n=int(input("n="))
a=int(input("a="))
max_bir=a
min_oxirgi=a
index_oxirgi_min=1
index_bir_max=1
for i in range(1,n):
    a=int(input("a="))
    if a>max_bir:
        max_bir=a
        index_bir_max=i+1
    if a<=min_oxirgi:
        min_oxirgi=a
        index_oxirgi_min=i+1
print("max_bir=",max_bir,"min_oxirigi=",min_oxirgi)
print("index_oxirigi_min=",index_oxirgi_min,"index_bir_max=",index_bir_max)
