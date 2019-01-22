k=int(input("输入K值："))
st=input("输入一组数据：")
s_list=str.split(st)
k%=(len(s_list))
s1list=s_list[0:k]
del s_list[0:k]
ss_list=s_list+s1list
print(ss_list)
