s_list=list(input("输入需要排序的字符串："))
s_list.sort()
st=''
for i in range(0,len(s_list)):
    st+=str(s_list[i])
print(st)