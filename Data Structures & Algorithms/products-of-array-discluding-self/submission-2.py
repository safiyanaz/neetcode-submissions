class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l=[0]* n
        for j in range(n):
            ans = 1
            for i in range(n):
                if i == j:
                    continue 
                ans = nums[i] * ans
            l[j] = ans


        return l