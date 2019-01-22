
import math
print("2\n3")
for i in range (2,100):
    for j in range (2,int(math.sqrt(i)+1)):
        if(i%j==0):
            break
        if(j==int(math.sqrt(i))):
            print(i)