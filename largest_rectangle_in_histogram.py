#BRUTE FORCE 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        for i in range(len(heights)):
            height=heights[i]
            r=i+1
            while r< len(heights) and heights[r]>=height:
                r+=1

            l=i
            while l>=0 and heights[l]>=height:
                l-=1

            r-=1
            l+=1
            maxArea=max(maxArea,height*(r-l+1))
        return maxArea

#STACK
