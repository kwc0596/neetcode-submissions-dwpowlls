class Solution:
    def decodeString(self, s: str) -> str:
        #I think based off of the value pulled outside of the bracket you can then determine how often the inside bracket
        #will be displayed. based off of that number you can append the value k times to the stack. 

        #is a stack used for the problem invertly? we iterate from right to left? 

        stack = []

        for i in range(len(s)): 
            if s[i] != "]": 
                stack.append(s[i])
            
            else:
                k = ""
                while stack and stack[-1] != "[":
                    k = stack.pop() + k
                stack.pop() #pop one more time to pop the open bracket
                n = ""
                while stack and stack[-1].isdigit(): 
                    n = stack.pop() + n
                stack.append(int(n) * k)
        return "".join(stack)

            #there are two cases to check for. if we reach a closing bracket
            #when it isn't a closing bracket. then we want to use a while loop inside to append the value inside
            #the bracket until we arrive at the open bracket itself. 


            #once this is satisfied, we want to set up another inner loop that iterates until we get the total integer
            #value. 
            #once this is done, we can multiply the new integer by the number value. 

            #we then append this to our stack. 
            #but the problem wants us to return a string value so we can do return "".join(stack)
