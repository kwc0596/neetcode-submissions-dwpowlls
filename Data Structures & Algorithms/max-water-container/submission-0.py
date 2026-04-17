class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #you want the difference in heights[i] - heights[j] to be high, but also 
        #the maximum a container could store would be the two containers there height plus the height of every container
        #in between. so we dont necessarily want to look for the largest height. but we want to find the largest
        #sum in the array that can also hold the water. the largest water will go up is based off the container that is shorter. 
        

        #So setting up this algorithm, it is better to use two pointers. We are trying to calculate the maximum area
        #that water can contain. area would be l * width and each of these bars are 1 unit apart. so that would 
        #be the width. So width in this case is bar[r] - bar[l] and then length is just the height. But another
        #thing to consider is that even if one bar is higher than the other, the height is determined by the lower of the
        #two bars to hold the water. So we want to set the pointers at the furthest distance obviously to increase the maximum
        #width, and then we will increment or decrement based off of the two bar's height comparison. 

        res = 0 

        l, r = 0, len(heights) - 1

        while l < r: 
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] < heights[r]: 
                l += 1
            elif heights[l] > heights[r]: 
                r -= 1
            else: 
                r -= 1
        return res 

