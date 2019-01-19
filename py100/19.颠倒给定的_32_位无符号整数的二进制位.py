c=bin(int(input("输入整数（0~4294967296）")))
b_list=list(c)
del b_list[0],b_list[0]
b_list.reverse()
print(b_list)