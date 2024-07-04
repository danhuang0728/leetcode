class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                continue
            i += 1
        return len(nums),nums
            

sol = Solution()
nums =[-1,0,0,0,0,3,3]
print(sol.removeDuplicates(nums))
