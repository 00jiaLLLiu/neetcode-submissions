class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res =[0]* n

        for i in range(n-2,-1,-1):
            j = i+1
            while j<n and temperatures[j] <= temperatures[i]:
                if res[j]==0: # j后面也没warmer day 不找了，j指向最后端
                    j=n
                    break
                j += res[j]   # 跳跃查找
            if j<n:
                res[i]= j-i
        return res

    