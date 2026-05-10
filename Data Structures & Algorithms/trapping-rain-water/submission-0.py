class Solution:
    def trap(self, height: List[int]) -> int:
        #Area will still be length x width. width of each bar is 1. But I also think that
        #we will calculate the max value and then subtract based off of the smaller bars that are within.

        #for example, based off of the problem to the left, the max height is 3 for two bars. so the area within
        #those two bars is likely the largest. But there are also technically three containers that take up space,
        #that we will need to account for. 

        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r] 
        res = 0

        while l < r: 
            if leftMax < rightMax: 
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
