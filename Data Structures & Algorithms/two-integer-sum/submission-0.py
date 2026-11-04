class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in nums and nums.index(looking_for) != i:
                j = nums.index(looking_for)
                if j > i:
                    return [i , j]
                else:
                    return [j, i]
            i += 1    
