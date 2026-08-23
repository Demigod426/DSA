class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev=[]
        for i in range(len(s)-1,-1,-1):
            rev.append(s[i])
        for i in range(len(s)):
            s[i]=rev[i]    # TC: O(n) SC:O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l,r=l+1,r-1  # TC: O(n) SC:O(n)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack=[]
        for i in s:
            stack.append(i)
        j=0
        while stack:
            s[j]=stack.pop()
            j+=1    # TC: O(n) SC:O(n)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def rev(l,r):
            if l<r:
                s[l],s[r]=s[r],s[l]
                rev(l+1,r-1)
        rev(0,len(s)-1)   # TC: O(n) SC:O(n)   