class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        heap_ct = []
        for num,count in count.items():
            heapq.heappush(heap_ct,(count,num))

            if len(heap_ct) > k:
                heapq.heappop(heap_ct)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap_ct)[1])

        return res