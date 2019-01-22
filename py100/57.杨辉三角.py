n=int(input("输入需要得到的层数："))
tr_list=[]
#建立列表
for i in range (0,n):
    tr_list.append([0,0,0,0,0,0,0,0,0,0])
#列表赋值
for j in range (0,n):
    for k in range(0,n):
        if(j==k and k==0):
            tr_list[j][k]=1
        elif(j>k):
            tr_list[j][k]=(tr_list[j-1][k]+tr_list[j-1][k-1])
#循环输出
for i in range (1,10):
    for j in range (0,10):
        if(i>=j and tr_list[i][j]!=0):
            print("%d\t"%(tr_list[i][j]),end='')
    print()