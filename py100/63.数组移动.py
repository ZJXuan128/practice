k=int(input("输入K值："))
st=input("输入一组数据：")
s_list=str.split(st)
k%=(len(s_list))
for i in range (0,k):
    t=s_list[0]
    del s_list[0]
    s_list.append(t)
print(s_list)

