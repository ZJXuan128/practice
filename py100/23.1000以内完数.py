import math
m=0
for i in range (4,1000):
    for j in range (2,int(math.sqrt(i)+1)):
        if(i%j==0):
            m+=(j+int(i/j))
    m+=1
    if(m==i):
        print(i)
    m=0