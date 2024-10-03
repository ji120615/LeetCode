class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        l = len(nums)

        # total = 0
        # for num in nums:
        #     total = (total + num) % p
        # TARGET = total % p

        TARGET = sum(nums) % p

        if TARGET == 0:
            return 0

        table = {0: -1}
        ps = 0
        m = l
        for i in range(l):
            ps = (ps + nums[i]) % p

            target = (p - (TARGET - ps)) % p

            if target in table:
                m = min(m, i - table[target])

            table[ps] = i

        return -1 if m == l else m