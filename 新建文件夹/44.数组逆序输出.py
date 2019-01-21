st=input("输入一组数据：")
s_list=str.split(st)
for i in range(0,len(s_list)):
    s_list[i]=int(s_list[i])
s_list.sort(reverse=True)
print(s_list)
