class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        n = len(matrix)
        for i in range(n):
            row = matrix[i]
            cnt = row.count(1)
            ans.append(cnt)
        return ans