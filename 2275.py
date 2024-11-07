class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
            M = 0
            
            # print(2 ** 24 > 10 ** 7)
            for i in range(24):
                count = 0
                for candidate in candidates:
                    if candidate & (1 << i):
                        count += 1
                M = max(M, count)
            
            return M