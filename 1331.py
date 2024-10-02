class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [table[e] for e in arr]