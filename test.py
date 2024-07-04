nums = [4,1,2,4]
target = 8
def twoSum(self,nums, target):
    hash_table={}
    for i in range(0,len(nums)):
        hash_table[nums[i]] = i
    for i in range(0,len(nums)):
        if target - nums[i] in hash_table:
            if hash_table[target - nums[i]] != i:
                return [i,hash_table[target - nums[i]]]
    return[0,0]
    
print(twoSum(0,nums,target))