class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            val = tokens.pop()
            if val not in "+-*/":
                return int(val)
            
            right = dfs()
            left = dfs()

            if val == '+':
                res = left + right
            elif val =='-':
                res = left - right
            elif val =='*':
                res = left * right
            elif val=='/':
                res = int(left/right)
            return res
        return dfs()