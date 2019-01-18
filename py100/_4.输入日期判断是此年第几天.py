y=int(input("输入年份："))
t=0
f=0
if(y%4==0 and y%100!=0):
    t=1
if(y%400==0):
    t=1
m=int(input("输入月份："))
d=int(input("输入日期："))
m_list=[31,28,31,30,31,30,31,31,30,31,30,31]
if(t==1):
    m_list[1]=29
for i in range(0,m-1):
    f+=m_list[i]
print("第%d天"%(f+d))