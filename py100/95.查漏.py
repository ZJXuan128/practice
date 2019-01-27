n=int(input("输入n的值："))
nums=[i for i in range (0,n)]
n=input("输入列表：")
n_list=n.split()
n_list.sort()
n_list=[int(i)for i in n_list]
for i in range (0,len(nums)):
    if nums [i] not in n_list:
        print(nums[i])
