for i in range(1,5):
    for j in range (1,5):
        if(i!=j):
            for t in range (1,5):
                if(t!=j and t!= i):
                    print(i*100+j*10+t)