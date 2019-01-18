import math
print("满足条件的数有：")
for i in range (-100,100000):
    x= math.sqrt(i+100)
    y= math.sqrt(i+268)
    if(x==int(x) and y==int(y)):
        print(i)