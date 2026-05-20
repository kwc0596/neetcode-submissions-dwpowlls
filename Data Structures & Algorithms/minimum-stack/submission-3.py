class MinStack:

    def __init__(self):
        self.stack = [] #initialize the stack
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val) 
        #append val
        #we want to set up the current minimum in our minstack and so this function will hold the logic to do that.
        if self.minStack: 

            minVal = min(self.minStack[-1], val)
            self.minStack.append(minVal)
        else: 
            minVal = self.stack[-1]
            self.minStack.append(minVal)
        

    def pop(self) -> None:
        self.stack.pop() #pop the stack
        self.minStack.pop() #pop the minStack

        

    def top(self) -> int:
        return self.stack[-1]



    def getMin(self) -> int:
        return self.minStack[-1]
