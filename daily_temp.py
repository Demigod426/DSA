#using stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                p=stack.pop()
                res[p]=i-p
            stack.append(i)
        return res

# TC:O(n), SC:O(n)