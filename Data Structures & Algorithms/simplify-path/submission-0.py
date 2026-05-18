class Solution:
    def simplifyPath(self, path: str) -> str:
        #"..." or "...." would be treated as valid driectory or file names. 

        #path must start with a single slash which we can do later. 

        #Directories within the path must be separated by exactly one slash '/'

        #Path cannot end with a slash. 

        #path must not have any single or double periods 

        #can treat this with a stack implementation because if ".." sits on top of a file value we know that 
        #we can pop that file from the stack. 

        cur = "" #create empty str to iterate through path
        stack = []

        for c in path + "/" : 
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "." and cur != "": 
                    stack.append(cur)
                cur = ""
            else: 
                cur += c
        return "/" + "/".join(stack)
