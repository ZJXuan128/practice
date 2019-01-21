import math
n=int(input("输入n值（n>2)："))
t=1
if(n<=2):
    print("输入正确的数值!")
else:
    for i in range(2,n):
        for j in range (2,int(math.sqrt(i)+1)):
            if(i%j==0):
                break
            if(j==int(math.sqrt(i))):
                t+=1
    print(t)