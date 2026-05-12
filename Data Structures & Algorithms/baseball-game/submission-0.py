class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #if this is treated as a stack, we can create an empty array. we will append each integer value and then
        #also hold the sum if + is given in the list of operations. 

        #iterate through the list and if the string is an integer, append the value to the new list. 
        #if it is an operation like + append a score of the last two integers in the new list. 
        #if it is a D, append the previous score multiplied by 2. 
        #if it is a C, pop the previous score.
        #while doing that keep a current sum value that keeps track of the current sum. 

        res = []

        cnt = 0

        i = 0
        j = 0
        while i < len(operations):
            if operations[i].lstrip('-').isdigit():
                res.append(int(operations[i]))
                cnt += res[j]
                j += 1
            elif operations[i] == '+': 
                res.append((int(res[j - 1]) + int(res[j - 2])))
                cnt += ((res[-1]))
                j += 1
            elif operations[i] == 'D':
                res.append((int(res[-1]) * 2))
                cnt += ((res[j])) 
                j += 1
            else: 
                cnt -= ((res[-1]))
                res.pop()
                j -= 1
            i += 1
        return cnt
