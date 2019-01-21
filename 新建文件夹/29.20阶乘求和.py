def fact(n):
    if(n==1):
        return 1;
    return fact(n-1)*n
s=0
for i in range (1,21):
    s+=fact(i)
print(s)
