class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        for i in range(len(s2)):

            temp = s2[i:i+l]
            if temp == s1:
                return True
        
        return False