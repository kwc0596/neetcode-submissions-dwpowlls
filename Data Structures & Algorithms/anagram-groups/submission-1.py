from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHashMap = defaultdict(list)
        result = []
        #Sort array by lowest to highest # of character? 
        for s in strs: 
            sorted_s = tuple(sorted(s))
            anagramHashMap[sorted_s].append(s)

        for value in anagramHashMap.values():
            #will take hashmap and append value to result array
            result.append(value)
        
        #return array with asorted anagrams
        return result

        #Iterate through array. Enter characters into hashmap
        #If they match previous str then it is anagram

        #time complexity of O(log* n ) 

