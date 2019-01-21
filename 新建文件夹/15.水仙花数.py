for i in range (100,1000):
    g=i%10
    s=(i-g)%100/10
    b=int(i/100)
    if(i==b*b*b+s*s*s+g*g*g):
        print(i)