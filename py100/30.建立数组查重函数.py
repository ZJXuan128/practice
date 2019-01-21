def search(s_list):
    for i in range (0,len(s_list)):
        for j in range (i+1,len(s_list)):
            if(s_list[i]==s_list[j]):
                return True
    return False
s_list=list(input("输入一组数据"))
a=search(s_list)
print(a)