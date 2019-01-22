
n=int(input("输入"))
n_list=[]
for i in range (0,n):
    n_list.append(i+1)
for i in range (0,len(n_list)):
    if(n_list[i]%15==0):
        print("FizzBuzz")
    elif(n_list[i]%3==0):
        print("Fizz")
    elif(n_list[i]%5==0):
        print("Buzz")
    else:
        print(n_list[i])