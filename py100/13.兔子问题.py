#兔子问题是斐波那契数列
a1=1;a2=1
for i in range (0,10):
    print("%d %d "%(a1,a2),end='')
    a1+=a2
    a2+=a1
print()