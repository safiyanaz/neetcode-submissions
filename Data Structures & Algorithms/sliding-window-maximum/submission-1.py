class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxInW = []
        window = []


        for i in range(k):
            window.append(nums[i])

        maxInW.append(max(window))

        for i in range(k, len(nums)):
            window.pop(0)
            window.append(nums[i])
            maxInW.append(max(window))


        return maxInW