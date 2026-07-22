class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zeros = nums.count(0)

        if zeros == 0:
            return 0
        
        zeros_at_end = nums[-zeros:].count(0)
    
        return zeros - zeros_at_end