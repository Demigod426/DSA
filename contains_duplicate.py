class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False  # TC: O(n) and SC: O(n)

# for in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             return True
# return False         TC: O(n^2) and SC: O(1)