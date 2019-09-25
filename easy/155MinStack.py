class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min=None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min==None or self.min>x:
            self.min=x

    def pop(self) -> None:
        temp=self.stack.pop()
        if len(self.stack)>0:
            if temp==self.min:
                self.min=min(self.stack)
        else:
            self.min=None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()