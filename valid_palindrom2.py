#BRUTE FORCE
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True

        for i in range(len(s)):
            newS=s[:i]+s[i+1:]
            if newS==newS[::-1]:
                return True
        return False

#TWO POINTER
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipl=s[l+1:r+1]
                skipr=s[l:r]
                return skipl==skipl[::-1]or skipr==skipr[::-1]
            l,r=l+1,r-1
        return True

#TWO POINTER OPTIMAL
