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

#Using HASHMAP
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        res=0
        for num in nums:
            if not mp[num]:
                mp[num]=mp[num-1]+mp[num+1]+1
                mp[num-mp[num-1]]=mp[num]
                mp[num+mp[num+1]]=mp[num]
                res=max(res,mp[num])
        return res