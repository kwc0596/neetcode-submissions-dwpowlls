from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        #two sentences are similar if they have the same length
        #sentence1[i] and sentence2[i] are similar according to the similarPairs array. 

        #convert similarPairs to a dictionary? for each sub index inside of the array they can be assigned to the same values?
        #and the key will be the index?

        #first thing we will do is check to see if both sentences have the same length
        #if they do not, we can immediately return false. That is the base case
        #we can also check to see if the word is the exact same in case there are no similar pairs. 
        
        #
        i = 0
        if len(sentence1) != len(sentence2): 
            return False


        hashMap = defaultdict(set)

        for word1, word2 in similarPairs:
            hashMap[word1].add(word2)
            hashMap[word2].add(word1)
        
        for i in range(len(sentence1)): 
            word1 = sentence1[i]
            word2 = sentence2[i]

            if word1 == word2 or word1 in hashMap[word2]:
                continue
            else: 
                return False
        return True


        

    