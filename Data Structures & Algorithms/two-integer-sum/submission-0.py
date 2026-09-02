class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idmap={}
        for index, num in enumerate(nums):
            idmap[num]=index
        
        for i,n in enumerate(nums):
            diff=target-n
            if diff in idmap and idmap[diff]!= i:
                return [i, idmap[diff]]
        return []