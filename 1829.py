class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        product = 0
        for num in nums:
            product ^= num

        bitmask = (1 << maximumBit) - 1
        
        ans = []
        for i in range(len(nums)):
            ans.append(product ^ bitmask)
            product ^= nums[len(nums) - 1 - i]
        
        return ans