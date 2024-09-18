class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        # nums.sort(key=lambda x: x * 10, reverse=True)

        return ''.join(nums) if nums[0] != '0' else '0'