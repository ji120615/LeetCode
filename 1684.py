class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(map(str, allowed))
        l = len(words)

        for word in words:
            for c in word:
                if c not in allowed:
                    l -= 1
                    break
        
        return l