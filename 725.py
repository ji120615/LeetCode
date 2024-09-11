# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ptr = head
        l = 0
        while ptr:
            l += 1
            ptr = ptr.next
        
        a = l // k
        b = l % k

        parts = []
        for i in range(k):
            ptr = head

            if ptr == None:
                parts.append(None)
                continue
            
            if i < b:
                for j in range(a):
                    ptr = ptr.next
            else:
                for j in range(a - 1):
                    ptr = ptr.next

            temp = ptr.next
            ptr.next = None
            parts.append(head)
            head = temp

        return parts