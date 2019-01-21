a=0;b=0;c=0
list_0=['x','y','z']
for a in range (0,3):
    for b in range (0,3):
        if(a!=b):
            for c in range (0,3):
                if(c!=a and c!=b):
                    if(list_0[a]!='x'and list_0[c]!='x'and list_0[c]!='z'):
                        print("aVS%s\tbVS%s\tcVS%s"%(list_0[a],list_0[b],list_0[c]))