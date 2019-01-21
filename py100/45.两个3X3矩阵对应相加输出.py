print(("输入第一个3X3矩阵"))
s2_list=[]
s4_list=[]
s5_list=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    str=input()
    s1_list=str.split(' ')
    for j in range (0,3):
        s1_list[j]=int(s1_list[j])
    s2_list.append(s1_list)
print(("输入第二个3X3矩阵"))
for i in range (0,3):
    str=input()
    s3_list=str.split(' ')
    for j in range (0,3):
        s3_list[j]=int(s3_list[j])
    s4_list.append(s3_list)
for k in range(0,3):
    for t in range(0,3):
        s5_list[k][t]=s4_list[k][t]+s2_list[k][t]
    print(s5_list[k])