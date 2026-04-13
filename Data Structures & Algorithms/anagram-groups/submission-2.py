from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Okay so anagrams, I immediately think of hashMaps. HashMaps because anagrams check for frequency of characters
        #in a string. we're sacrificing space for time efficiency. 

        #We can iterate through the entire array. and check every single string. 

        #So how can we add all the anagrams together. 

        #create an empty array and append the hashMap. 

        #base case would be if the strs array is empty. we just return an empty array back. 

        #set up an if condtion to check if the "string" already exists in the hashMap. 

        res = defaultdict(list) #mapping character count to list of Anagrams. #using tuples which is why we defaultdict

        for s in strs: #iterate through the list of strings
            count = [0] * 26 # a - z #create an array that holds the index of the 26 alphabetical characters.

            for c in s: #iterate through each string to go over each character.
                count[ord(c) - ord("a")] += 1 # each character we are going to get the ord value and subtract "a" because
                # "a" equals 0. so we know what character this will be

            res[tuple(count)].append(s)
        return list(res.values()) 
