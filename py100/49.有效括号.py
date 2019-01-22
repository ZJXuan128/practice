st=input("输入一串括号：")
lens=len(st)
o=0
if(len(st)%2!=0):
    print("无效")
else:
    for i in range(0,int(lens/2)):
        st=st.replace("()","").replace("[]","").replace("{}","")
    if(len(st)>0):
        print("无效")
    else:print("有效")