class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        l = len(nums)
        nums.sort()
        
        count = 0
        for (i, num) in enumerate(nums):
            left = lower - num
            right = upper - num

            count += bisect_right(nums, right, i + 1) - bisect_left(nums, left, i + 1)
        
        return count