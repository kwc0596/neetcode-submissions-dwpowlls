class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # I am thinking a hashmap would be good but maybe a little unnecessary in this context. 

        #iterate through original array. 
        #place original values in new array. and then place new values afterwards. 

        ans = nums * 2

        return ans