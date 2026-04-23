class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #this is a two pointer approach. 
        #we want to start from opposite ends as that will give us the maximum potential area. 

        #maximum height of area is based off of the lowest of 2 containers. 

        l, r = 0, len(heights) - 1

        res = 0

        #so we will use a while loop to check the area of our left and right pointer. 
        #area would be our length * width. width is calculated based off of pointer separation and
        #our length is calculated based off of min(heights[l], heights[r]) . width would be r - l + 1?
        #after we get our area, we will then check to see which of the two heights is smaller. based
        #off of that condition, we will then shift out pointer based off of which container is smaller. 
        # this will continue until there are no more containers. 
        #we will also do a comparison to store our maximum area in res and then return res. 


        while l < r: 
            width = r - l 
            height = min(heights[l], heights[r])
            area = width * height
            res = max(res, area)
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1
        return res