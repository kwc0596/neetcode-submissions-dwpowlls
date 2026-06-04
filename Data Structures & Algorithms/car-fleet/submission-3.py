class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        #get paired values of our two arrays using zip. 

        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]: 

            stack.append((target - p) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 

                stack.pop() 

        return len(stack)
            
            
            

        #Instantiate our stack. 
        #append the value to stack based off of time to get to the destination. 
        #value that we get is determined from target - p / speed
        #if the stack value is equal or greater than 2 and the stack value at the top is smaller than the stack value
        #at the bottom, then we know they will intersect before stack at the bottom reaches the target. 
        #we can compare this result to the bottom of the stack and pop if the top value is less than. 

        #we can return the length of the stack which equals car fleets. 