class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0]* len(temperatures)
        stack =[]   # (temperature,index)

        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackTemp, stackId = stack.pop()
                res[stackId] = i - stackId
            stack.append((t,i))

        return res