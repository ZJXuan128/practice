n=int(input("输入n的值："))
n_list=list(range(0,n+1))
t=0
m=0
while(len(n_list)>2):
     for i in range (1,len(n_list)):
         t=(i+t)%3
         if(t==0):
             n_list[i]=0
     print(n_list)
     for j in range(1,len(n_list)):
         if(n_list[j]!=0):
             m+=1
             c=n_list[j]
     if(m==2):
         print(c)
         break