class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            output.append(1)
        for i in range(len(nums)):
            if i == 0:
                prefix = 1
            else:
                k = i - 1
                prefix *= nums[k]
            output[i] *= prefix
        postfix = 1
        for j in range(len(nums)-1, -1,-1):
            output[j] *= postfix
            postfix *= nums[j]
        return output
            