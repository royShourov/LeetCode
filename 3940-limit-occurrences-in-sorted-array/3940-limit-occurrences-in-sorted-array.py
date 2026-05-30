class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        cnt = 0
        prev = None

        for num in nums:
            if num == prev:
                cnt += 1
            else:
                prev = num
                cnt = 1

            if cnt <= k:
                ans.append(num)
        
        return ans