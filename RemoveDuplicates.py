def remove_duplicate_elements(nums):
    
    if not nums:
        return 0
    p = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[p-1]:
            nums[p] = nums[i]
            p +=1
    return p
            
t = int(input())
for i in range(t):
    length = int(input())
    nums = list(map(int, input().split()))
    print(remove_duplicate_elements(nums))
    
    