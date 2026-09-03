class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) +1
        
        sorted=[]
        for num,count in count.items():
            sorted.append([count,num])
        sorted.sort()

        res=[]
        while len(res)< k:
            res.append(sorted.pop()[1])
        
        return res

