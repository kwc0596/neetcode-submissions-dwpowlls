class TimeMap:

    def __init__(self):
        #We want to use a dictionary because we're using key-value data structure that can store multiple values.
        #that means values will hold multiple values under one key meaning that the values will be in an array
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #we need to set the keys and values inside of our dictionary. 
        if key not in self.dictionary: 
            self.dictionary[key] = []
        self.dictionary[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        #I forgot the order in what happens. 
        #set our lower and upper bounds? 
        #we need to first store an empty string. We are returning the value such that set was called previously. 
        #in other cases where we have looked for the minimum value, we are looking for the max. 
        res = ""
        #I am only writing this down because I remember but we also need to set up a variable that has all the existing values so that we can do binary search to get the max value possible. Still don't understand really why
#we use binary search though. 
        values = self.dictionary.get(key, []) #variable that holds the dictionary and gets the key and value pair parameter
        l, r = 0, len(values) - 1

        while l <= r: 
            m = (l + r) // 2

            if values[m][1] <= timestamp: 
                res = values[m][0]
                l = m + 1
            else: 
                r = m - 1
        return res

        
