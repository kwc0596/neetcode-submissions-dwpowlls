class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #we are iterating left to right in asteroids. 
        #based off of the problem, we only need to consider collisions when
        #there is a positive asteroid in the stack before the negative asteroid.
        #if there are no positive asteroids to the left of the negative one, it never
        #needs to worry about collision because negative asteroids won't collide,
        #and asteroids to the right of it are going the opposite direction.

        #create a stack
        stack = []

        #iterate through the loop (for) 
        for a in asteroids: 
            #check for collisions by checking to see if there a is < 0 and the stack value is > 0
            #also need to check if there's a value in the stack.
            while stack and a < 0 and stack[-1] > 0: 
                #conditionals to compare a to stack. 
                diff = a + stack[-1]
                if abs(a) < abs(stack[-1]): 
                    a = 0
                elif abs(a) > abs(stack[-1]): 
                    stack.pop()
                    
                else: 
                    a = 0
                    stack.pop()
            if a: 
                stack.append(a)
        return stack