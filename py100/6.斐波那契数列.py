Fibo_list=[0,1]
for i in range(2,100):
    Fibo_list.append(Fibo_list[i-1]+Fibo_list[i-2])
print(Fibo_list)