class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []

        mx = 0
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))
        
        prefixGcd.sort()

        left = 0
        right = len(prefixGcd) - 1
        sum_of_gcd = 0

        while left < right:
            sum_of_gcd += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return sum_of_gcd
