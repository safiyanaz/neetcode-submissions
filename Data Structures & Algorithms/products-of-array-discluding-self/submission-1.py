class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[0]* (len(nums))
        for j in range(len(nums)):
            ans = 1
            for i in range(len(nums)):
                if i == j:
                    continue 
                ans = nums[i] * ans
            l[j] = ans


        return l