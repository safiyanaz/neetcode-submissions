class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleS = "".join(filter(str.isalnum, s)).lower()
        if cleS == cleS[::-1]:
            return True
        else: 
            return False 