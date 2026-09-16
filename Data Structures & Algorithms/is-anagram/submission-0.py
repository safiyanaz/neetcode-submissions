class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)

        for i in s: 
            if (i not in t): 
                return False
        return True 
