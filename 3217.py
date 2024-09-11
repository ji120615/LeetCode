# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        prev = ListNode()
        ptr = prev

        curr = head
        while curr:
            if curr.val in nums:
                prev.next = None
            else:
                prev.next = curr
                prev = curr
            curr = curr.next
        
        return ptr.next