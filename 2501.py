class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # nums = sorted(set(nums))
        # visited = set()

        # M = 1
        # for num in nums:
        #     if num in visited:
        #         continue

        #     streak = 1
        #     temp = num * num
        #     while (temp <= 10 ** 5):
        #         if temp in nums:
        #             visited.add(temp)
        #             streak += 1
        #             temp *= temp
        #         else:
        #             break
        
        #     M = max(M, streak)
    
        # return M if M != 1 else -1

        nums.sort()
        dp = dict()

        M = -1
        for num in nums:
            sqrt = num ** (1 / 2)
            
            if sqrt in dp and sqrt ** 2 == num:
                dp[num] = dp[sqrt] + 1
                M = max(M, dp[num])
            else:
                dp[num] = 1
        
        return M