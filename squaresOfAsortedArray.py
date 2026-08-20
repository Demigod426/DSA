# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             nums[i]=nums[i]**2
#         for j in range(len(nums)):
#             for k in range(j+1,len(nums)):
#                 if nums[j]>nums[k]:
#                     nums[j],nums[k]=nums[k],nums[j]
#         return nums

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        l,r=0,len(nums)-1
        
        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                result.append(nums[l]*nums[l])
                l+=1
            else:
                result.append(nums[r]*nums[r])
                r-=1
        return result[::-1]  