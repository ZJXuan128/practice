nums=[1,2,3,4,1,2,3]
while 1:
    for i in range (1,len(nums)):
        if nums[0]==nums[i]:
           del nums[0]
           del nums[i-1]
           break
    if len(nums)==1:
            print(nums[0])
            break