class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        M = max(nums)

        count = 0
        answer = 0
        for num in nums:
            if num == M:
                count += 1
            elif count != 0:
                answer = max(answer, count)
                count = 0
        answer = max(answer, count)

        return answer