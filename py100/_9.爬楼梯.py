def fact(n):                #阶乘递归
    if n==1:
        return 1
    return n*fact(n-1)
def C(n,m):                 #排列函数
    if(m==0 or n==m):
        return 1
    else:
        s=int(fact(n)/(fact(n-m)*fact(m)))
        return s
while(1):
    n=int(input("请输入楼梯阶数："))
    w=0
    if(n%2==0):
        for i in range (0,int(n/2+1)):
             w+=C(int(n/2+i),int(n/2-i))
    else:
        for i in range (0,int((n+1)/2)):
            w+=C(int((n+1)/2)+i,int((n-1)/2)-i)
    print("有%d种方法"%w)