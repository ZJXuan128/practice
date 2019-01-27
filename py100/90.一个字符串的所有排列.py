def arrange(st):
    if(len(st)<=1):
        return st
    s_list=[]
    for i in range (len(st)):               #不断选出一个元素，在回归时从尾部组成的前端不断添加
        for j in arrange(st[0:i]+st[i+1:]):
            s_list.append(st[i]+j)
    return s_list


st=input("输入字符串")
s_list=arrange(st)
print(s_list)
