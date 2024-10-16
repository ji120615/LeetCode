class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []

        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        answer = []
        while pq:
            count, letter = heapq.heappop(pq)
            count = -count

            if len(answer) >= 2 and answer[-1] == letter and answer[-2] == letter:
                if not pq:
                    break

                nCount, nLetter = heapq.heappop(pq)
                nCount = -nCount
                
                answer.append(nLetter)
                nCount -= 1
                if nCount > 0:
                    heapq.heappush(pq, (-nCount, nLetter))

                heapq.heappush(pq, (-count, letter))
            else:
                answer.append(letter)
                count -= 1
                if count > 0:
                    heapq.heappush(pq, (-count, letter))

        return "".join(answer)