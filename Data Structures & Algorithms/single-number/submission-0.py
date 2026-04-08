class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for n in nums: 
            hashMap[n] = hashMap.get(n, 0) + 1
        for key, value in hashMap.items():
            if value == 1:
                return key

        