class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #returning a new array 'result' where result[i] is the # of days after the ith day before a warmer 
        #temperature appears on a future day. Otherwise set result[i] to 0 intead. 

        # by default we can set result value to 0. 

        result = [0] * len(temperatures)

        stack = []
        #why do we use a stack. this problem checks to see relationship between a value and consecutive values 
        #next to it, that is why a stack is useful.

        for i, t in enumerate(temperatures): 
            while stack and t > stack[-1][0]: 
                stackT, stackI = stack.pop()
                result[stackI] = (i - stackI)
            stack.append((t, i))
        return result