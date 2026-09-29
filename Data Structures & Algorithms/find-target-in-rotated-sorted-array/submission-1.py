class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<r: 
            m = (l+r)//2
            if nums[m]> nums[r]:
                l= m+1 
            else: 
                r = m

        
        pivot = l

        left = pivot 
        right = len(nums)-1

        while left< right: 
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                left = mid +1
            else: 
                right = mid 
        return -1

        