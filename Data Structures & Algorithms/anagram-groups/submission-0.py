from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHashMap = defaultdict(list)
        result = []

        for s in strs: 
            sorted_s = tuple(sorted(s))
            anagramHashMap[sorted_s].append(s)

        for value in anagramHashMap.values():
            result.append(value)
        return result

        #Sort array by lowest to highest # of character? 

        #Iterate through array. Enter characters into hashmap
        #If they match previous str then it is anagram

