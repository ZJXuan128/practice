def prime(n):
    l = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                l.append(i)
                break    
    return l


while 1:
    s = input("输入一个正整数:")
    if s.isdigit() and int(s) > 0:					#当输入的S是数字且为正数，非整取整，继续执行
        print(s, "=", " * ".join([str(x) for x in prime(int(s))]))		#str()使列表元素规整，利用循环语句循环执行素数函数
    else:
        break