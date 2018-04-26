import math
x=float(input("Введите х:"))
y=float(input("Введите у:"))
x1 = -10
x2 = 16
y1 = -9
y2 = 21
k = 5
yc = 0
xc = 0
r =  5
b = 0
if (y<k*x+b):
    if((x-xc)**2+(y-yc)**2<r**2):
        if (x1<x<x2) and (y1<y<y2):
            print ("Область 4")
        else:
            if(y<y2):
                print("Область 5")
            else:
                print("Область 6")
    else:
        if(x1<x<x2) and (y1<y<y2):
            print("Область 7")
        else:
            print("Область 8")
else:
    if((x-xc)**2+(y-yc)**2<r**2):
        if(x1<x<x2) and (y1<y<y2):
            print("Область 3")
        else:
            print("Область 2")
    else:
         print ("Область 1")
print("Конец")


