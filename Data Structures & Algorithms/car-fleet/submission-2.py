class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #if a car and the car behind it arrive at the position at the same time, they can become a part of a car fleet.
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)
