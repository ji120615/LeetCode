# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr.next:
            a = ptr.val
            b = ptr.next.val

            node = ListNode(gcd(a, b), ptr.next)
            ptr.next = node

            ptr = ptr.next.next
        
        return head