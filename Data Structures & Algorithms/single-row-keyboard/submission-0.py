class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        #So we are always starting at index 0 

        # I think we want to use a hashMap here for sure. We would store the index 

        #We can iterate through 'keyboard' and store the character inside of the dictionary with its index.

        #We keep variable that stores our current sum. 
        #we iterate through word and each traverse, we add the journey to sum. 
        #return sum. 

        #we also need to start at index 0. 

        hashMap = {}

        for i in range(len(keyboard)): 
            char = keyboard[i]
            hashMap[char] = i

        total_time = 0
        #index j is the destination point
        i, j = 0, 1
        
        current_position = 0
        for char in word: 
            target_position = hashMap[char] #Get index of the char
            total_time += abs(current_position - target_position)
            current_position = target_position
        return total_time