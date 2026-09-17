#Usinf HASHSET
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        maxlength=0
        for num in num_set:
            if (num-1) not in num_set:
                currentnum=num
                currentlength=1
                while (currentnum+1) in num_set:
                    currentnum+=1
                    currentlength+=1
                maxlength=max(maxlength,currentlength)
        return maxlength