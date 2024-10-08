class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        for c in s:
            if c == '[':
                stack += 1
            else:
                if stack:
                    stack -= 1

        return stack // 2 + stack % 2