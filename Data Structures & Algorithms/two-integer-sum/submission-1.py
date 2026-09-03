class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos={}
        for index, num in enumerate(nums):  #loop with index
            diff = target - num
            if diff in pos:
                return [pos[diff],index]
            pos[num] = index
        