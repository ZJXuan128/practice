def move0(nums):
    for i in range(0,len(nums)):
        if(nums[i]==0):
            del nums[i]
            nums.append(0)
    return nums
n=input("输入数组，空格分隔：")
nums=n.split()
for i in range(0,len(nums)):
    nums[i]=int(nums[i])
nums=move0(nums)
print(nums)