class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        closing = 0
        for c in s:
            if c == '(':
                opening += 1
            else:
                if opening:
                    opening -= 1
                else:
                    closing += 1
            
        return opening + closing