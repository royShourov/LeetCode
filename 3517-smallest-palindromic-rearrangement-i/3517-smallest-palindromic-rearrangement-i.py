class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        middle = ""
        for ch in map(chr, range(ord('a'), ord('z') + 1)):
            if freq[ch] % 2 == 1:
                middle = ch
            left.append(ch * (freq[ch] // 2))

        left = "".join(left)
        return left + middle + left[::-1]