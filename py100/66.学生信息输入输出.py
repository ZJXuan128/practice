def input_():
    list_h=[]
    for i in range(0,5):
        st=input("分别输入五名学生的信息（姓名，学号，班级；空格分隔）")
        list_g=st.split( )
        list_h.append(list_g)
    return list_h

def output_(list_h):
    for i in range (0,5):
        for j in range(0,len(list_h[i])):
            print(" ",list_h[i][j],end='')
        print("")
list_h=input_()
output_(list_h)