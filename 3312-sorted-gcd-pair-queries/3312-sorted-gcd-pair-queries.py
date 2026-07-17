from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        divisible = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            for multiple in range(d, max_val + 1, d):
                divisible[d] += freq[multiple]

        exact = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            cnt = divisible[d]
            total_pairs = cnt * (cnt - 1) // 2

            multiple = 2 * d
            while multiple <= max_val:
                total_pairs -= exact[multiple]
                multiple += d

            exact[d] = total_pairs

        prefix = []
        running = 0
        for d in range(1, max_val + 1):
            running += exact[d]
            prefix.append(running)

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q) + 1)

        return ans