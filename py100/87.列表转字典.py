key=input("输入各个键：")
list_k=key.split()
value=input("输入对应值：")
list_v=value.split()
for i in range (0,len(list_v)):
    list_v[i]=int(list_v[i])
s=dict(zip(list_k,list_v))
print(s)
