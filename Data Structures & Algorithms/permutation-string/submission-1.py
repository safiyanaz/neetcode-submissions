class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        for i in range(len(s2)):

            
            sorS2 = "".join(sorted(s2[i:i+1]))
            sorS1 = "".join(sorted(s1))
            if sorS1 == sorS2 and len(sorS1) == len(sorS2):
                return True
        
        return False