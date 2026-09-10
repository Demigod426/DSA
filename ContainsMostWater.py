class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        l=0
        r=len(heights)-1
        while l<r:
            length=min(heights[l],heights[r])
            breadth=r-l
            area=length*breadth
            maxwater=max(area,maxwater)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return maxwater


    