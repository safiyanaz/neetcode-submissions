class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums = Counter(nums)
        result = [key for key, count in countnums.most_common(k)]
        return result 