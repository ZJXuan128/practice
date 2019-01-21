print(("输入3X3矩阵"))
s2_list=[]
t=0
for i in range (0,3):
    str=input()
    s1_list=str.split(' ')
    for j in range (0,3):
        s1_list[j]=int(s1_list[j])
    s2_list.append(s1_list)
    t+=s2_list[i][i]
print(s2_list,t)