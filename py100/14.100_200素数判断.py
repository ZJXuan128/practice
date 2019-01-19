import math
t=0
for i in range (101,200):
    m=0
    for j in range (2,int(math.sqrt(i)+1)):
        if(i%j==0):
            m=-1
            break
    if(j==int(math.sqrt(i)) and m!=-1):
        t+=1
        print(i)
print(t)