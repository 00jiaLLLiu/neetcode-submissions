#sort
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            new = stones.pop()-stones.pop()
            if new > 0:
                stones.append(new)
        
        return stones[0] if stones else 0