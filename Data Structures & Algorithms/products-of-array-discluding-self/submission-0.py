class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        ans = 1
        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j:
                    ans = nums[i] * ans
            l.append(ans)
            ans = 1

        return l