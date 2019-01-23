st=input("输入要查重的字符串：")
for i in range (0,len(st)):
    for j in range (i,len(st)):
        if(st[i]!=st[j]):
            print(j+1)
            t=1
            break
    if(t!=0):
        break
if(t==0):
    print(-1)