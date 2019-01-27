a=input("输入第一个串：")
b=input("输入第二个串：")
al=len(a)
bl=len(b)
s=[[i for i in range (0,al+1)]for j in range (0,bl+1)]
for i in range (0,bl+1):
    s[i][0]=i
for i in range (0,bl):
    for j in range(0,al):
        if(a[j]==b[i]):
            substitution=s[i][j]
        else:
            substitution=s[i][j]+1
        deletion=s[i][j+1]+1
        insertion=s[i+1][j]+1
        s[i+1][j+1]=min(substitution,deletion,insertion)
print(s[bl][al])