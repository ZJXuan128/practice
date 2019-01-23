nums=input("输入数组")
n_list=nums.split()
target=int(input("输入目标值:"))
t=0
for i in range(0,len(n_list)):
    for j in range(0,len(n_list)):
        if(n_list[i]!=n_list[j]and int(n_list[i])+int(n_list[j])==target):
            print("%d+%d=%d"%(int(n_list[i]),int(n_list[j]),target))
            t+=1
    if(t!=0):
        break