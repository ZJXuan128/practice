a=input("输入a值")
n=input("输入项数")
s=0
for i in range (0,int(n)):
    s+=int(a*(i+1))
print(s)