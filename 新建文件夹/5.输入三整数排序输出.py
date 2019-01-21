while(1):
    x,y,z=map(int,input("请输入三个整数(使用空格分隔数值)：").split())                #由小到大输出
    if(x>y):
        x,y=y,x
    if(x>z):
        x,z=z,x
    if(y>z):
        y,z=z,y
    print(x,y,z)