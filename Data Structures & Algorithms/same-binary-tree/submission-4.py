# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 or q2:
            for i in range(len(q1)):
                node1 = q1.popleft()
                node2 = q2.popleft()
                if node1 is None and node2 is None:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                q1.append(node1.left)
                q2.append(node2.left)
                q1.append(node1.right)
                q2.append(node2.right)

        return len(q1) == len(q2)

                # if node1 and node2:
                #     if node1.val != node2.val:
                #         return False
                # if not node1 and node2:
                #     return False
                # if not node2 and node1:
                #     return False
                # if node1.left and node2.left:
                #     q1.append(node1.left)
                #     q2.append(node2.left)
                # if node1.right and node2.right:
                #     q1.append(node1.right)
                #     q2.append(node2.right)
        # return True