st=input("输入明文：")
s_list=list(st)
for i in range (0,4):
    s_list[i]=(int(s_list[i])+5)%10
s_list[0],s_list[3]=s_list[3],s_list[0]
s_list[1],s_list[2]=s_list[2],s_list[1]
print(s_list)
