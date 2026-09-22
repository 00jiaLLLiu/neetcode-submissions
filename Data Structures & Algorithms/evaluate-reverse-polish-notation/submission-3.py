class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for c in tokens:
            if c in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if c =='+':
                    res = a +b
                elif c =='-':
                    res =a -b
                elif c =='*':
                    res = a *b
                elif c=='/':
                    res = int(a/b)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[0]
                

