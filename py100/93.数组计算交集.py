a=input("输入第一个数组，空格分隔：")
a_list=a.split()
b=input("输入第二个数组，空格分隔：")
b_list=b.split()
a_set=set(a_list)
b_set=set(b_list)
c_set=a_set&b_set
print(c_set)