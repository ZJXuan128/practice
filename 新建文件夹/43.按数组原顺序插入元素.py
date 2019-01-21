st=input("输入一组排好序的数据：")         #也可使用list.insert(index,obj)添加列表元素，判断添加位置即可
s_list=str.split(st)
for i in range(0,len(s_list)):
    s_list[i]=int(s_list[i])
for j in range(0,len(s_list)):
    if(j<len(s_list)and s_list[j]==s_list[j+1]):
        continue
    elif(s_list[j]<s_list[j+1]):
        s_list.append(int(input("输入一个数：")))
        s_list.sort()
        print(s_list)
    elif(s_list[j]>s_list[j+1]):
        s_list.append(int(input("输入一个数：")))
        s_list.sort(reverse=True)
        print(s_list)