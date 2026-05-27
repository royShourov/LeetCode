class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_last = {}
        upper_first = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower_last[ch] = i
            else:
                c = ch.lower()
                if c not in upper_first:
                    upper_first[c] = i
        
        cnt = 0
        for c in lower_last:
            if c in upper_first and lower_last[c] < upper_first[c]:
                cnt += 1
        
        return cnt