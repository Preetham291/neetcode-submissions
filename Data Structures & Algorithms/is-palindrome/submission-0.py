class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=[i.lower() for i in s if i.isalnum()]
        left=0
        right=len(c)-1
        while left<right:
            if c[left]!=c[right]:
                return False
            right-=1
            left+=1
        return True
        
