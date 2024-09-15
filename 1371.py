class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        VOWEL = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        mask = 0
        M = 0
        table = {0: -1}
        
        for i, c in enumerate(s):
            if c in VOWEL:
                mask ^= (1 << VOWEL[c])

            if mask in table:
                M = max(M, i - table[mask])
            else:
                table[mask] = i
        
        return M