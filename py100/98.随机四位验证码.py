import random
temp=''
for i in range (4):
    n=random.randrange(0,3)
    if n==0:
        num=random.randrange(65,91)
        temp+=chr(num)
    elif n==1:
        num=random.randrange(97,123)
        temp+=chr(num)
    elif n==2:
        m=random.randrange(0,10)
        temp+=str(m)
print(temp)