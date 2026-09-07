class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] ==target:
                    return [i+1,j+1]
        return []   # BRUTE FORCE TC:O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l<r:
            total=numbers[l]+numbers[l]
            if total==target:
                return [l+1,r+1]
            elif total<target:
                l+=1
            else:
                r-=1