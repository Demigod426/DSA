class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        for j in range(len(nums)):
            for k in range(j+1,len(nums)):
                if nums[j]>nums[k]:
                    nums[j],nums[k]=nums[k],nums[j]
        return nums