c=bin(abs(int(input("输入一个整数:"))))
t=len(c)
b_list=list(c)
n=0
for i in range (2,t):
    if(int(b_list[i])==1):
        n+=1
print(n)