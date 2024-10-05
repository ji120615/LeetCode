class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        s1 = Counter(s1)
        freq = Counter(s2[0 : l1 - 1])
        for i in range(l1 - 1, l2):
            freq[s2[i]] += 1

            if freq == s1:
                return True
        
            freq[s2[i - (l1 - 1)]] -= 1
        
        return False