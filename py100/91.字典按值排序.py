d={"ok":1,"no":2} 
#对字典按值排序，用元组列表的形式返回 
d2 = sorted(d.items(), key=lambda d:d[1],reverse = True) #
print (d1,'\n',d2)
