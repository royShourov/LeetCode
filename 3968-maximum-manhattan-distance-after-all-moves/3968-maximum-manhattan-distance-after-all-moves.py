class Solution:
    def maxDistance(self, moves: str) -> int:
        dx = dy = wild = 0

        for ch in moves:
            if ch == 'R':
                dx += 1
            elif ch == 'L':
                dx -= 1
            elif ch == 'U':
                dy += 1
            elif ch == 'D':
                dy -= 1
            else:  
                wild += 1

        return abs(dx) + abs(dy) + wild