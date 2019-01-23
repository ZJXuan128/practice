s =0;total = 0
for i in range (0,9):
		if(i == 1 ):
			total = 4
		elif(i ==2):
			total = total*7
		else:total *= 8;	
		print("0~7组成%d位数，有：%d个"%(i,total))
		s+=total
print("总计为：%d" % s)