class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        l = len(nums)

        dp1 = [1] * l
        dp2 = [1] * l

        for i in range(l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)

        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if nums[i] > nums[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)

        M = 0
        for i in range(l):
            if dp1[i] == 1 or dp2[i] == 1:
                continue
            M = max(M, dp1[i] + dp2[i])

        return l - (M - 1)