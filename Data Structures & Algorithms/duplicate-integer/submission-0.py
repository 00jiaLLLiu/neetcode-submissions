from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)
        for k,v in res.items():
            if v > 1:
                return True
        return False







