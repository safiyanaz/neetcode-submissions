class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(1, len(numbers)): 
                if numbers[i] + numbers[j] == target: 
                    if numbers[i] < numbers[j] and numbers[i] != numbers[j]:
                        return [i+1,j+1]