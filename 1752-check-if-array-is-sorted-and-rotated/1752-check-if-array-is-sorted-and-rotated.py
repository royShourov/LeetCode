class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        breaks = 0
        for i in range(n):
            next = (i + 1) % n
            if nums[i] > nums[next]:
                breaks += 1
        
        if breaks > 1:
            return False 
        
        return True 
