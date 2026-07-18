class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest = max(nums)
        smallest = min(nums)

        while largest % smallest != 0:
            largest, smallest = smallest, largest % smallest
        
        return smallest