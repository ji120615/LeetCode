# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for j in range(m)]

        r = 0
        c = -1

        # state = "right"
        # while head:
        #     matrix[r][c] = head.val
        #     head = head.next

        #     if state == "right":
        #         if c + 1 == n or matrix[r][c + 1] != -1:
        #             state = "down"
        #             r += 1
        #         else:
        #             c += 1
        #     elif state == "down":
        #         if r + 1 == m or matrix[r + 1][c] != -1:
        #             state = "left"
        #             c -= 1
        #         else:
        #             r += 1
        #     elif state == "left":
        #         if c - 1 == -1 or matrix[r][c - 1] != -1:
        #             state = "up"
        #             r -= 1
        #         else:
        #             c -= 1
        #     else:
        #         if r - 1 == -1 or matrix[r - 1][c] != -1:
        #             state = "right"
        #             c += 1
        #         else:
        #             r -= 1

        m -= 1
        while head:
            for i in range(n):
                if not head:
                    break
                c += 1
                matrix[r][c] = head.val
                head = head.next
            n -= 1

            for i in range(m):
                if not head:
                    break
                r += 1
                matrix[r][c] = head.val
                head = head.next
            m -= 1

            for i in range(n):
                if not head:
                    break
                c -= 1
                matrix[r][c] = head.val
                head = head.next
            n -= 1

            for i in range(m):
                if not head:
                    break
                r -= 1
                matrix[r][c] = head.val
                head = head.next
            m -= 1

        return matrix