def ref(n):                             #先入后出，堆栈
    if(n<=1):
        m=input()
        list_r.append(m)
    else:
        m=input()
        ref(n-1)
        list_r.append(m)
n=5
list_r=[]
print("输入五个字符：")
ref(n)
print(list_r)