class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        table = dict()

        e = 0
        table[-1] = e
        for i in range(len(arr)):
            e ^= arr[i]
            table[i] = e

        answer = []
        for query in queries:
            e = table[query[1]] ^ table[query[0] - 1]
            answer.append(e)
        
        return answer