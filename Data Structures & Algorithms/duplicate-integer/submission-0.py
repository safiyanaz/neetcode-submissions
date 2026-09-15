class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        temp = nums[0]
        for i in nums:
            ans = False
            if i+1 == temp:
                ans = True
                break 
            temp = i+1

        return ans 

            