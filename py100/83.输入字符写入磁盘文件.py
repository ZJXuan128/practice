a_list=[]
while 1:
    s=input("输入字符串：")
    if s=='#':
        break
    a_list.append(s+'\n')

fp=open('file.txt','w')
fp.writelines(a_list)
fp.close()
fp=open('file.txt','r')
str=fp.read()
fp.close()
print("输出文本文件内容：")
print(str)