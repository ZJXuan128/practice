s_list=[]
print("输入10个数：")
for i in range(0,10):
    n=int(input())
    s_list.append(n)
s_list.sort(reverse=False)
print(s_list)