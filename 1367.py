# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        target = ""
        while head:
            target += str(head.val)
            head = head.next

        def traverse(node, path):
            if node == None:
                if target in path:
                    return True
                return False

            path += str(node.val)

            return traverse(node.left, path) or traverse(node.right, path)

        return traverse(root, "")