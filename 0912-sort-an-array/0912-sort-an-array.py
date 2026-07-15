import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        heapq.heapify(nums)
        sorted_nums = [heapq.heappop(nums) for _ in range(n)]

        return sorted_nums