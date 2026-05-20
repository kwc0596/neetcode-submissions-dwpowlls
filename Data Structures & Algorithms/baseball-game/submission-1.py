class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # + symbol records a new score that is the sum of the previous two scores

        # D symbol records a new score that is double of the previous score

        # C symbol invalidates the previous score, removing it from the record.

        #return the sum of all the scores on the record.

       

        stack = []

        for i in range(len(operations)): 
            if operations[i] == "+": 
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif operations[i] == "D": 
                stack.append(int(stack[-1]) * 2)
            elif operations[i] == "C": 
                stack.pop()
            else: 
                stack.append(int(operations[i]))
        return sum(stack)

