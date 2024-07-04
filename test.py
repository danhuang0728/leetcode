nums = [1]
target = 0
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target :
            return i
        if i == (len(nums)-1):
            if target > nums[i]:
                return i+1
        if nums[i] < target and target < nums[i+1]:
            return i+1
        if target < nums[0]:
            return 0
print(searchInsert(nums,target)) 