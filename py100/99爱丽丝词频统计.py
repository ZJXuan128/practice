def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

fp=open("alice.txt",'r')
st=fp.read()
fp.close()
list_s=st.split()
dic_n=all_list(list_s)
dic_m = sorted(dic_n.items(), key=lambda dic_n:dic_n[1],reverse = True)
for i in range(0,10):
    print(dic_m[i])
