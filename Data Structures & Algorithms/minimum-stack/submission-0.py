class MinStack:

    def __init__(self):
        self.stack = []
        self.min_at_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_at_val:
            self.min_at_val.append(min(val, self.min_at_val[-1]))
        else:
            self.min_at_val.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_at_val.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_at_val[-1]
