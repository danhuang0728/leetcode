List = [3,2,2,3]
val = 3
def removeElement( nums, val):
    i = 0 
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
            continue
        i += 1
    return nums
print(removeElement(List,val))