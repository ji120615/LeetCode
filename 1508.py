class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = list()

        for i in range(n):
            subarray_sum = 0
            for j in range(i, n):
                subarray_sum += nums[j]
                subarray_sums.append(subarray_sum)
        
        subarray_sums.sort()

        return sum(subarray_sums[left - 1 : right]) % (10 ** 9 + 7)