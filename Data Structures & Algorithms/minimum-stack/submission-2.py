class MinStack:
        #we actually need to create two stack arrays. One stack that holds all the values in the array.
        #the second stack to hold the minimum value of integers generated since then.
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        #for stack, we just need to append the value. 
        #for minStack, we need to determine what the min value is and then append. 

        self.stack.append(val)
        if self.minStack: 
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
