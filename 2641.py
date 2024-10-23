# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        TOTALS = []

        q = deque([root])
        while q:
            total = 0
            for i in range(len(q)):
                curr = q.popleft()
                total += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            TOTALS.append(total)
        
        q = deque([root])
        depth = 0
        root.val = 0
        while q:
            depth += 1
            for i in range(len(q)):
                curr = q.popleft()

                total = 0
                if curr.left:
                    total += curr.left.val
                if curr.right:
                    total += curr.right.val
                
                if curr.left:
                    curr.left.val = TOTALS[depth] - total
                    q.append(curr.left)
                if curr.right:
                    curr.right.val = TOTALS[depth] - total
                    q.append(curr.right)

        return root