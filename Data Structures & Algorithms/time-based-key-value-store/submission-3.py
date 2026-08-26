class TimeMap:

    def __init__(self):
        #initializes the object of the data structure . It is a key-value based store... so we use a dictionary
        self.store = {} #this is it

    def set(self, key: str, value: str, timestamp: int) -> None:

        #stores the key with the value at the given time timestamp
        #first need to check if the key already exists. 
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp]) #we append since we are adding additional values to the key, not replacing. 

        

    def get(self, key: str, timestamp: int) -> str:
        res = "" #we want to store the string result to find the max
        values = self.store.get(key, []) # i still don't understand this code logic

        l, r = 0, len(values) - 1 #need to set up our bounds

        while l <= r: #binary search

            mid = (l + r) // 2 #mid point

            if values[mid][1] <= timestamp: #values[mid][1] takes existing timestamp to compare
                res = values[mid][0] #replaces res string value with "value" passed
                l = mid + 1 #searches to the right to find potential higher max
            else: 
                r = mid - 1 #searches to the left 
        return res #returns string
        
