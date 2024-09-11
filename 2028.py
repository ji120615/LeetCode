class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l = len(rolls)

        a = mean * (l + n) - sum(rolls)

        ans = []
        if a < 1 * n or a > 6 * n:
            return ans

        # for i in range(n):
        #     b = a - (n - i - 1)
        #     if b > 6:
        #         b = 6
        #     ans.append(b)
        #     a -= b

        c = a // n
        d = a % n
        ans = [c] * (n - d) + [c + 1] * d

        return ans