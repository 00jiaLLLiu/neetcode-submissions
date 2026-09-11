class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0,len(numbers)-1):
            dif = target - numbers[i]
            l,r = i+1, len(numbers)-1
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid] == dif:
                    return [i+1,mid+1]
                if numbers[mid] > dif:
                    r = mid-1
                if numbers[mid] < dif:
                    l = mid+1
        return []
        