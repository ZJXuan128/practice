def summation(n):
    s=0    
    if(n%2==0):
        for i in range (2,n+1,2):
            s+=(1/i)
    else:
        for j in range(1,n+1,2):
            s+=(1/j)
    return s
n=int(input("输入n值"))
s=summation(n)
print(s)