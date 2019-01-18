for i in range (1,10):
    print("%d\t"%i,end='')
print("\n")
for t in range (0,67):
    print("-",end='')
print("\n")
for i in range(1,10):
    for j in range(1,10):
        if(i>=j):
            print("%d\t"%(i*j),end='')
    print("")