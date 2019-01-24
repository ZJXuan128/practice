for i in range (10,100):
    four=809*i
    three=9*i
    two=8*i
    if(int(four/1000)!=0and int(three/100)!=0and int(two/10)!=0):
        print(i,four)
        break
