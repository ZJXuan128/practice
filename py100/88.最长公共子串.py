st1=input("输入第一个串：")                #动态规划，转化为二维数组解决
st2=input("输入第二个串：")
stl1 = len(st1)
stl2 = len(st2)
record = [[0 for i in range(stl2+1)] for j in range(stl1+1)]#创建一个字符串长度加一的二维数组，首行首列均为0
maxnum=0#子串最大长度
p=0#子串终止位置
for i in range(stl1):
    for j in range(stl2):
        if st1[i]==st2[j]:
            record[i+1][j+1]=record[i][j]+1 #对角线长度对应子串长度，每个元素相同对应数组值位左上角数值加一,连续增加子串长度
        if record[i+1][j+1]>maxnum:
            maxnum=record[i+1][j+1]#记录最大子串长
            p=i+1   #记录子串终止位置
print(st1[p-maxnum:p])#末位置减去长度等于初位置
