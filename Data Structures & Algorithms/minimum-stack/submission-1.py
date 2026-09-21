class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = [] 
        #store the minivalue for current stack, keep the same length as "stack"

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.ministack[-1] if self.ministack else val)
        self.ministack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        mini = self.ministack[-1]
        return mini
